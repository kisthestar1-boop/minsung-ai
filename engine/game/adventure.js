// 새싹 원정대 · 모험 씬 (새싹 엔진 1.0 위에서 도는 기준 게임) — 숲 2단계: 지도 · 영웅 · 정령 · 야영지 전투 · 강한 몬스터
import { World } from '../src/world.js';
import { installParts } from '../src/parts.js';
import { installCombat, heal } from '../src/combat.js';
import { installAI } from '../src/ai.js';
const COL = { c_sum: '#9fe8ff', c_arc: '#ffe98a', c_mag: '#d6a8ff' };
export class Adventure {
  constructor(game) { this.game = game; }
  enter(p) {
    const g = this.game, D = g.data, M = D.RPGMAP, hk = this.hk = p.hero || 'c_sum', H = D.HEROES[hk];
    const w = this.world = new World(g); installParts(w); installCombat(w); installAI(w);
    this.bg = g.assets.image('bg_world'); w.h = 1500; w.w = 1500 * 2752 / 1536;
    const P = (fx, row) => [w.w * fx, w.h * row];
    this.stats = { kills: 0, camps: 0, deaths: 0 }; this.msg = null; this.campLeft = [];
    // 영웅
    const walk = H.w4 ? [1, 2, 4, 5] : [1, 2]; const [hx, hy] = this.home = P(M.home[0], M.home[1]);
    this.hero = w.spawn(hx, hy).tag('hero').add('team', { side: 1 }).add('shadow', { rx: 15 })
      .add('sprite', { h: 96, frames: { idle: [hk + '_h0'], walk: walk.map(i => hk + '_h' + i), act: [hk + '_h3'] } })
      .add('mover', { speed: H.spd * 2.4 }).add('player').add('status')
      .add('health', { hp: H.hp, max: H.hp, col: '#6fd35a', h: 96, keep: true, bar: false, regen: H.hp * .012 })
      .add('fighter', { dmg: H.dmg, range: Math.max(125, H.range * .72), rate: H.rate, shot: H.shot || 0, splash: H.splash || 0, col: COL[hk] || '#ffe98a' });
    if (hk === 'c_sum') w.spawn(hx - 30, hy - 60).tag('spirit').add('sprite', { h: 26, frames: { idle: ['spirit'], walk: ['spirit'] }, bob: 3.5 }).add('follow', { target: this.hero, ox: -34, oy: -64, lag: 5 });
    // 몬스터 한 마리 만들기 (표의 능력치 × 세기)
    const mon = (x, y, img, st, hh, mul, group, extra = {}) => w.spawn(x, y).tag('monster').add('team', { side: -1 }).add('shadow', { rx: hh * .28, ry: hh * .1 })
      .add('sprite', { h: hh, frames: { idle: [img] }, face: -1 }).add('mover', { speed: st.spd * 1.6 }).add('status')
      .add('health', { hp: Math.round(st.hp * mul), max: Math.round(st.hp * mul), h: hh })
      .add('fighter', Object.assign({ dmg: st.dmg * (.7 + mul * .3), range: st.range, rate: st.rate, shot: st.shot || 0, splash: st.splash || 0, col: '#ff9a7a', hold: true, cd: .5 }, extra)).add('brain', { group });
    // 야영지
    M.camps.forEach((c, i) => { const [cx, cy] = P(c.fx, c.row), all = c.ks.concat(c.el ? [c.el] : []); this.campLeft[i] = 0;
      all.forEach((k, j) => { const a = j / all.length * 6.283, el = c.el && j === all.length - 1, info = D.MONINFO[k], st = D.MONSTAT[k]; if (!info || !st) return; const hh = (el ? 1.28 : 1) * 40;
        const e = mon(cx + Math.cos(a) * 34, cy + Math.sin(a) * 22, info[1], st, hh, c.m * (el ? 2.2 : 1), 'c' + i); e.camp = i; e.xp = st.xp * (el ? 3 : 1); e.kind = k; this.campLeft[i]++; if (el) { e.elite = true; e.add('label', { text: '👑 정예', h: hh }); } }); });
    // 강한 야생 몬스터
    (M.wild || []).forEach(q => { const i = +q.k.slice(2), W0 = D.WB[i]; if (!W0) return; const [x, y] = P(q.fx, q.row), hh = W0[6] * .61 * 1.28, c = M.camps[q.ci] || { m: 1 };
      const e = mon(x, y, 'wb_' + i, { hp: W0[1], dmg: W0[2], range: W0[3], spd: W0[4], rate: W0[5], shot: W0[7].shot, splash: W0[7].splash }, hh, c.m * 2.1, 'w' + i); e.tag('wild'); e.wild = i; e.xp = 40; e.add('label', { text: '👑 ' + W0[0], h: hh }); });
    // 신호: 처치 · 야영지 정리 · 영웅 쓰러짐
    const S = g.signals; this.off = [
      S.on('combat:kill', ev => { const t = ev.tgt; if (t === this.hero) { this.stats.deaths++; this.revive = 2.2; this.say('쓰러졌어요… 마을에서 다시 일어나요'); return; }
        if (t.tags.has('monster')) { this.stats.kills++; if (t.camp != null && --this.campLeft[t.camp] === 0) { this.stats.camps++; heal(w, this.hero, this.hero.get('health').max * .3); this.say('🏕 ' + M.camps[t.camp].n + ' 정리!'); S.emit('camp:clear', { i: t.camp, camp: M.camps[t.camp] }); } } }),
    ];
    g.camera.zoom = 1.28; g.camera.bounds = { x: 0, y: 0, w: w.w, h: w.h }; this.snap = true;
    S.emit('adventure:ready', this);
  }
  exit() { (this.off || []).forEach(f => f()); }
  say(text) { this.msg = { text, t: 2.4 }; }
  update(dt) {
    const g = this.game, c = g.camera, h = this.hero, hp = h.get('health');
    if (hp.down) { h.get('mover').vx = h.get('mover').vy = 0; h.get('player').off = true; h.get('sprite').alpha = .45; this.revive -= dt; if (this.revive <= 0) { h.x = this.home[0]; h.y = this.home[1]; hp.hp = hp.max; hp.down = false; h.get('sprite').alpha = 1; h.get('player').off = false; this.snap = true; } }
    this.world.update(dt); if (this.msg && (this.msg.t -= dt) <= 0) this.msg = null;
    c.view = { x: 0, y: 0, w: g.r.W, h: g.r.H }; c.follow(h.x, h.y - 30, dt, this.snap); this.snap = false;
  }
  draw(r) {
    const x = r.ctx, w = this.world, c = this.game.camera, hp = this.hero.get('health');
    x.save(); c.apply(x); if (this.bg.naturalWidth) x.drawImage(this.bg, 0, 0, w.w, w.h); else { x.fillStyle = '#9fc98a'; x.fillRect(0, 0, w.w, w.h); } w.draw(r); x.restore();
    // 임시 표시(화면 부품 모듈이 생기면 옮긴다): 체력 · 처치 수 · 알림
    x.fillStyle = 'rgba(40,26,12,.72)'; r.rr(10, 10, 230, 44, 14); x.fill(); r.text('⚙ 새싹 엔진 · 숲 2단계 (전투)', 22, 27, { s: 11, c: '#ffe9a8' });
    x.fillStyle = 'rgba(0,0,0,.45)'; r.rr(22, 34, 150, 10, 5); x.fill(); x.fillStyle = '#6fd35a'; r.rr(22, 34, 150 * Math.max(.02, hp.hp / hp.max), 10, 5); x.fill(); r.text('⚔ ' + this.stats.kills + '  🏕 ' + this.stats.camps, 180, 44, { s: 11, c: '#fff' });
    if (this.msg) { const a = Math.min(1, this.msg.t * 2); x.save(); x.globalAlpha = a; x.fillStyle = 'rgba(40,26,12,.8)'; const tw = 260; r.rr(r.W / 2 - tw / 2, 64, tw, 32, 16); x.fill(); r.text(this.msg.text, r.W / 2, 85, { s: 14, a: 'center', c: '#ffe9a8' }); x.restore(); }
    const s = this.game.input.stick; if (s) { x.save(); x.globalAlpha = .5; x.strokeStyle = '#fff'; x.lineWidth = 2; x.beginPath(); x.arc(s.ox, s.oy, 40, 0, 7); x.stroke(); x.fillStyle = '#fff6d8'; x.beginPath(); x.arc(s.ox + s.dx * 34, s.oy + s.dy * 34, 15, 0, 7); x.fill(); x.restore(); }
  }
}
