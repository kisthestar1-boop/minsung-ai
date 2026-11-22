// 새싹 원정대 · 모험 씬 (새싹 엔진 1.0 위에서 도는 기준 게임) — 숲 3단계: 지도 · 영웅 · 야영지 전투 · 고유 기술 · 레벨과 스킬 트리
import { World } from '../src/world.js';
import { installParts } from '../src/parts.js';
import { installCombat, heal } from '../src/combat.js';
import { installAI } from '../src/ai.js';
import { installSkills, cast } from '../src/skills.js';
import { Progress } from '../src/progress.js';
const COL = { c_sum: '#9fe8ff', c_arc: '#ffe98a', c_mag: '#d6a8ff' };
export class Adventure {
  constructor(game) { this.game = game; }
  enter(p) {
    const g = this.game, D = g.data, M = this.map = (D.MAPS || []).find(m => m.id === p.map) || D.RPGMAP, hk = this.hk = p.hero || 'c_sum', H = D.HEROES[hk];
    const w = this.world = new World(g); installParts(w); installCombat(w); installAI(w); installSkills(w);
    this.bg = g.assets.image(M.bg || 'bg_world', 'jpg'); w.h = 1500; w.w = 1500 * 2752 / 1536;
    const P = (fx, row) => [w.w * fx, w.h * row];
    this.stats = { kills: 0, camps: 0, deaths: 0 }; this.msg = null; this.campLeft = [];
    // 관문(다른 맵으로 가는 길) — 여정: 큰 맵들이 관문으로 이어진다
    this.gates = (M.gates || []).map(q => { const [x, y] = P(q.fx, q.row); return { x, y, q }; }); this.gateNear = null; this.leaving = null; this.fadeT = .7;
    // 영웅
    const walk = H.w4 ? [1, 2, 4, 5] : [1, 2]; const [hx, hy] = this.home = P(M.home[0], M.home[1]);
    this.hero = w.spawn(hx, hy).tag('hero').add('team', { side: 1 }).add('shadow', { rx: 15 })
      .add('sprite', { h: 96, frames: { idle: [hk + '_h0'], walk: walk.map(i => hk + '_h' + i), act: [hk + '_h3'] } })
      .add('mover', { speed: H.spd * 2.4 }).add('player').add('status')
      .add('health', { hp: H.hp, max: H.hp, col: '#6fd35a', h: 96, keep: true, bar: false }).add('caster')
      .add('fighter', { dmg: H.dmg, range: Math.max(125, H.range * .72), rate: H.rate, shot: H.shot || 0, splash: H.splash || 0, col: COL[hk] || '#ffe98a' });
    if (hk === 'c_sum') w.spawn(hx - 30, hy - 60).tag('spirit').add('sprite', { h: 26, frames: { idle: ['spirit'], walk: ['spirit'] }, bob: 3.5 }).add('follow', { target: this.hero, ox: -34, oy: -64, lag: 5 });
    this.progress = new Progress(w, this.hero, hk, D, p.saved);
    const back = p.from && this.gates.find(q => q.q.to === p.from); if (back) { this.hero.x = back.x + (back.x < w.w / 2 ? 80 : -80); this.hero.y = back.y; }
    this.say('🧭 ' + (M.n || '모험'));
    // 몬스터 한 마리 만들기 (표의 능력치 × 세기)
    const R = D.CAMPRULE, mon = (x, y, img, st, hh, hpM, dmgM, group, extra = {}) => w.spawn(x, y).tag('monster').add('team', { side: -1 }).add('shadow', { rx: hh * .28, ry: hh * .1 })
      .add('sprite', { h: hh, frames: { idle: [img] }, face: -1 }).add('mover', { speed: st.spd * 1.6 }).add('status')
      .add('health', { hp: Math.round(st.hp * hpM), max: Math.round(st.hp * hpM), h: hh })
      .add('fighter', Object.assign({ dmg: st.dmg * dmgM, range: st.range, rate: st.rate, shot: st.shot || 0, splash: st.splash || 0, col: '#ff9a7a', hold: true, cd: .5 }, extra)).add('brain', { group });
    // 야영지
    M.camps.forEach((c, i) => { const [cx, cy] = P(c.fx, c.row), all = c.ks.concat(c.el ? [c.el] : []); this.campLeft[i] = 0;
      all.forEach((k, j) => { const a = j / all.length * 6.283, el = c.el && j === all.length - 1, info = D.MONINFO[k], st = D.MONSTAT[k]; if (!info || !st) return; const hh = (el ? 1.28 : 1) * 40;
        const late = i < R.elFrom ? 0 : 1, e = mon(cx + Math.cos(a) * 34, cy + Math.sin(a) * 22, info[1], st, hh, c.m * R.hp * (el ? R.elHp[late] : 1), c.m * R.dmg * (el ? R.elDmg[late] : 1), 'c' + i); e.camp = i; e.xp = el ? R.elXp : R.xp; e.kind = k; this.campLeft[i]++; if (el) { e.elite = true; e.add('label', { text: '👑 정예', h: hh }); } }); });
    // 강한 야생 몬스터
    (M.wild || []).forEach(q => { const i = +q.k.slice(2), W0 = D.WB[i]; if (!W0) return; const [x, y] = P(q.fx, q.row), hh = W0[6] * .61 * 1.28, c = M.camps[q.ci] || { m: 1 };
      const e = mon(x, y, 'wb_' + i, { hp: W0[1], dmg: W0[2], range: W0[3], spd: W0[4], rate: W0[5], shot: W0[7].shot, splash: W0[7].splash }, hh, c.m * R.wildHp, c.m * R.wildDmg, 'w' + i); e.tag('wild'); e.wild = i; e.xp = R.wildXp; e.add('label', { text: '👑 ' + W0[0], h: hh }); });
    // 신호: 처치 · 야영지 정리 · 영웅 쓰러짐
    const S = g.signals; this.off = [
      S.on('progress:level', ev => this.say('⭐ Lv.' + ev.lv + ' · 스킬 포인트 ' + ev.pts)),
      S.on('combat:kill', ev => { const t = ev.tgt; if (t === this.hero) { if (this.progress.tryRevive()) { const hp = t.get('health'); hp.down = false; hp.hp = hp.max * .5; this.say('🌸 다시 피는 꽃! 바로 부활해요'); return; } this.stats.deaths++; this.revive = 2.2; this.say('쓰러졌어요… 마을에서 다시 일어나요'); return; }
        if (t.tags.has('monster')) { this.stats.kills++; if (t.camp != null && --this.campLeft[t.camp] === 0) { this.stats.camps++; heal(w, this.hero, this.hero.get('health').max * .3); this.say('🏕 ' + M.camps[t.camp].n + ' 정리!'); S.emit('camp:clear', { i: t.camp, camp: M.camps[t.camp] }); } } }),
    ];
    g.camera.zoom = 1.28; g.camera.bounds = { x: 0, y: 0, w: w.w, h: w.h }; this.snap = true;
    S.emit('adventure:ready', this);
  }
  exit() { (this.off || []).forEach(f => f()); this.progress.destroy(); }
  cast(id) { return cast(this.world, this.hero, id); }
  // 관문을 지나 다른 맵으로: 레벨과 스킬 트리를 그대로 들고 간다
  travel(q) { this.leaving = q; }
  say(text) { this.msg = { text, t: 2.4 }; }
  update(dt) {
    const g = this.game, c = g.camera, h = this.hero, hp = h.get('health');
    if (hp.down) { h.get('mover').vx = h.get('mover').vy = 0; h.get('player').off = true; h.get('sprite').alpha = .45; this.revive -= dt; if (this.revive <= 0) { h.x = this.home[0]; h.y = this.home[1]; hp.hp = hp.max; hp.down = false; h.get('sprite').alpha = 1; h.get('player').off = false; this.snap = true; } }
    this.progress.tick(dt); this.world.update(dt); if (this.msg && (this.msg.t -= dt) <= 0) this.msg = null;
    if (this.fadeT > 0) this.fadeT -= dt; this.gateNear = null; for (const q of this.gates) if (Math.hypot(q.x - h.x, (q.y - h.y) * 1.4) < 90) this.gateNear = q;
    if (this.leaving) { const q = this.leaving; g.signals.emit('travel', { from: this.map.id, to: q.to }); g.scenes.go('adventure', { hero: this.hk, map: q.to, from: this.map.id || 'world', saved: this.progress.toJSON() }); return; }
    c.view = { x: 0, y: 0, w: g.r.W, h: g.r.H }; c.follow(h.x, h.y - 30, dt, this.snap); this.snap = false;
  }
  draw(r) {
    const x = r.ctx, w = this.world, c = this.game.camera, hp = this.hero.get('health');
    x.save(); c.apply(x); if (this.bg.naturalWidth) x.drawImage(this.bg, 0, 0, w.w, w.h); else { x.fillStyle = '#9fc98a'; x.fillRect(0, 0, w.w, w.h); } for (const q of this.gates) { const t = performance.now() / 1000, k = .5 + .5 * Math.sin(t * 1.6); x.save(); x.globalAlpha = .35 + k * .2; x.fillStyle = '#fff3b0'; x.beginPath(); x.ellipse(q.x, q.y, 46, 22, 0, 0, 7); x.fill(); x.globalAlpha = .9; x.strokeStyle = '#ffd84d'; x.lineWidth = 3; x.stroke(); x.restore(); r.text('🧳 ' + q.q.n, q.x, q.y - 34, { s: 13, a: 'center', c: '#fff', stroke: 'rgba(40,26,12,.85)' }); }
    w.draw(r); x.restore();
    // 임시 표시(화면 부품 모듈이 생기면 옮긴다): 체력 · 처치 수 · 알림
    x.fillStyle = 'rgba(40,26,12,.72)'; r.rr(10, 10, 250, 52, 14); x.fill(); const P = this.progress; r.text('⚙ 새싹 엔진 · 숲 3단계   Lv.' + P.lv + (P.points() ? '  ✦' + P.points() : ''), 22, 27, { s: 11, c: '#ffe9a8' });
    x.fillStyle = 'rgba(0,0,0,.45)'; r.rr(22, 48, 150, 5, 2.5); x.fill(); x.fillStyle = '#ffd84d'; r.rr(22, 48, 150 * Math.max(.02, Math.min(1, P.xp / P.need())), 5, 2.5); x.fill();
    x.fillStyle = 'rgba(0,0,0,.45)'; r.rr(22, 34, 150, 10, 5); x.fill(); x.fillStyle = '#6fd35a'; r.rr(22, 34, 150 * Math.max(.02, hp.hp / hp.max), 10, 5); x.fill(); r.text('⚔ ' + this.stats.kills + '  🏕 ' + this.stats.camps, 180, 44, { s: 11, c: '#fff' });
    if (this.msg) { const a = Math.min(1, this.msg.t * 2); x.save(); x.globalAlpha = a; x.fillStyle = 'rgba(40,26,12,.8)'; const tw = 260; r.rr(r.W / 2 - tw / 2, 64, tw, 32, 16); x.fill(); r.text(this.msg.text, r.W / 2, 85, { s: 14, a: 'center', c: '#ffe9a8' }); x.restore(); }
    if (this.gateNear) { const q = this.gateNear.q, bw = 250, bh = 40, gx = r.W / 2 - bw / 2, gy = r.H - 64, low = this.progress.lv < (q.lv || 1); x.fillStyle = 'rgba(255,246,216,.95)'; r.rr(gx, gy, bw, bh, 20); x.fill(); x.strokeStyle = '#e2a93c'; x.lineWidth = 3; x.stroke();
      r.text('🧳 ' + q.n + '(으)로 떠나기' + (low ? ' · 권장 Lv.' + q.lv : ''), r.W / 2, gy + 26, { s: 14, a: 'center', c: '#5a3d16' }); this.game.input.button(gx, gy, bw, bh, () => this.travel(q)); }
    if (this.fadeT > 0) { x.fillStyle = 'rgba(16,22,18,' + Math.min(1, this.fadeT / .7) + ')'; x.fillRect(0, 0, r.W, r.H); }
    // 임시 기술 버튼 (화면 부품 모듈이 생기면 옮긴다)
    const L = this.hero.get('caster').list, bx = r.W - 56, by = r.H - 60; L.forEach((k, i) => { const big = !i, rad = big ? 34 : 24, cx = big ? bx : bx - 26 - i * 54, cy = big ? by : by + 14, cd = k.t / k.cd;
      x.fillStyle = cd > 0 ? 'rgba(40,30,20,.6)' : 'rgba(255,246,216,.92)'; x.beginPath(); x.arc(cx, cy, rad, 0, 7); x.fill(); x.lineWidth = 3; x.strokeStyle = cd > 0 ? 'rgba(255,255,255,.35)' : '#e2a93c'; x.stroke();
      if (cd > 0) { x.strokeStyle = '#ffd84d'; x.beginPath(); x.arc(cx, cy, rad, -1.5708, -1.5708 + 6.283 * (1 - cd)); x.stroke(); }
      r.text(k.icon, cx, cy + rad * .3, { s: rad * .85, a: 'center' }); this.game.input.button(cx - rad, cy - rad, rad * 2, rad * 2, () => this.cast(k.id)); });
    const s = this.game.input.stick; if (s) { x.save(); x.globalAlpha = .5; x.strokeStyle = '#fff'; x.lineWidth = 2; x.beginPath(); x.arc(s.ox, s.oy, 40, 0, 7); x.stroke(); x.fillStyle = '#fff6d8'; x.beginPath(); x.arc(s.ox + s.dx * 34, s.oy + s.dy * 34, 15, 0, 7); x.fill(); x.restore(); }
  }
}
