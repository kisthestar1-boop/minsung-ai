// 새싹 원정대 · 모험 씬 (새싹 엔진 1.0 위에서 도는 기준 게임) — 숲 1단계: 지도 · 영웅 · 정령 · 몬스터 배치 · 카메라
import { World } from '../src/world.js';
import { installParts } from '../src/parts.js';
export class Adventure {
  constructor(game) { this.game = game; }
  enter(p) {
    const g = this.game, D = g.data, M = D.RPGMAP, hk = p.hero || 'c_sum', H = D.HEROES[hk];
    const w = this.world = new World(g); installParts(w);
    this.bg = g.assets.image('bg_world'); w.h = 1500; w.w = 1500 * 2752 / 1536;
    const P = (fx, row) => [w.w * fx, w.h * row];
    // 영웅: 걷기 4장(w4)이 있으면 4장, 없으면 2장
    const walk = H.w4 ? [1, 2, 4, 5] : [1, 2];
    const [hx, hy] = P(M.home[0], M.home[1]);
    this.hero = w.spawn(hx, hy).tag('hero').add('shadow', { rx: 15 }).add('sprite', { h: 96, frames: { idle: [hk + '_h0'], walk: walk.map(i => hk + '_h' + i), act: [hk + '_h3'] } }).add('mover', { speed: H.spd * 2.4 }).add('player').add('health', { hp: H.hp, max: H.hp, col: '#6fd35a', h: 96 });
    if (hk === 'c_sum') w.spawn(hx - 30, hy - 60).tag('spirit').add('sprite', { h: 26, frames: { idle: ['spirit'], walk: ['spirit'] }, bob: 3.5 }).add('follow', { target: this.hero, ox: -34, oy: -64, lag: 5 });
    // 야영지 몬스터
    M.camps.forEach((c, i) => { const [cx, cy] = P(c.fx, c.row); const all = c.ks.concat(c.el ? [c.el] : []);
      all.forEach((k, j) => { const a = j / all.length * 6.283, el = c.el && j === all.length - 1, info = D.MONINFO[k]; if (!info) return; const hh = (el ? 1.28 : 1) * 40;
        const e = w.spawn(cx + Math.cos(a) * 34, cy + Math.sin(a) * 22).tag('monster').add('shadow', { rx: 11 }).add('sprite', { h: hh, frames: { idle: [info[1]] }, flip: false }).add('health', { hp: 50, max: 50, h: hh }); e.camp = i; if (el) e.add('label', { text: '👑 정예', h: hh }); }); });
    // 강한 야생 몬스터
    (M.wild || []).forEach(q => { const i = +q.k.slice(2), W0 = D.WB[i]; if (!W0) return; const [x, y] = P(q.fx, q.row); w.spawn(x, y).tag('wild').add('shadow', { rx: 18, ry: 7 }).add('sprite', { h: W0[6] * .61 * 1.28, frames: { idle: ['wb_' + i] } }).add('label', { text: '👑 ' + W0[0], h: W0[6] * .61 * 1.28 }); });
    g.camera.zoom = 1.28; g.camera.bounds = { x: 0, y: 0, w: w.w, h: w.h }; this.snap = true;
    g.signals.emit('adventure:ready', this);
  }
  update(dt) { this.world.update(dt); const g = this.game, c = g.camera; c.view = { x: 0, y: 0, w: g.r.W, h: g.r.H }; c.follow(this.hero.x, this.hero.y - 30, dt, this.snap); this.snap = false; }
  draw(r) { const x = r.ctx, w = this.world, c = this.game.camera; x.save(); c.apply(x); if (this.bg.naturalWidth) x.drawImage(this.bg, 0, 0, w.w, w.h); else { x.fillStyle = '#9fc98a'; x.fillRect(0, 0, w.w, w.h); } w.draw(r); x.restore();
    r.ctx.fillStyle = 'rgba(40,26,12,.72)'; r.rr(10, 10, 250, 30, 15); r.ctx.fill(); r.text('⚙ 새싹 엔진 1.0 · 숲 1단계 시험 장면', 22, 30, { s: 13, c: '#ffe9a8' });
    const s = this.game.input.stick; if (s) { x.save(); x.globalAlpha = .5; x.strokeStyle = '#fff'; x.lineWidth = 2; x.beginPath(); x.arc(s.ox, s.oy, 40, 0, 7); x.stroke(); x.fillStyle = '#fff6d8'; x.beginPath(); x.arc(s.ox + s.dx * 34, s.oy + s.dy * 34, 15, 0, 7); x.fill(); x.restore(); } }
}
