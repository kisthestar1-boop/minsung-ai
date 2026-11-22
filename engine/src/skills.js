// 새싹 엔진 · skills — 기술. 표(SKILLDEF)에 적힌 "동작 종류 + 숫자"를 실행한다. 새 기술은 표에 한 줄, 새 동작은 defineSkill 한 번.
import { hit, heal, enemies, dist } from './combat.js';
const KINDS = new Map();
export const defineSkill = (kind, fn) => KINDS.set(kind, fn);
const ring = (w, x, y, r, col) => w.spawn(x, y).add('ring', { r, col });
const allies = (w, e, r) => w.with('team').filter(o => o.get('team').side === e.get('team').side && o.has('health') && !o.get('health').down && dist(e, o) <= r);
const nearest = (w, e, r) => enemies(w, e).map(o => [dist(e, o), o]).filter(q => q[0] <= r).sort((a, b) => a[0] - b[0]).map(q => q[1]);

// c = { w 세계, e 쓰는 물체, d 표의 숫자, pow 공격력, rank 단계, o 피해 꼬리표 } · 돌려주는 값 = 맞힌 수
defineSkill('summon', c => { const { w, e, d } = c, H = e.get('health'), n = d.n + (c.extra || 0), pm = c.palMul || 1;
  const old = w.tagged('summon').filter(o => o.owner === e && !o.get('health').down); while (old.length + n > 4) old.shift().get('life').t = 0;
  for (let j = 0; j < n; j++) { const oy = (j - (n - 1) / 2) * 26, q = w.spawn(e.x + 18, e.y + oy).tag('summon').add('team', { side: e.get('team').side }).add('shadow', { rx: 8, ry: 3 })
    .add('sprite', { h: 30, frames: { idle: [d.img], walk: [d.img] }, bob: 3 }).add('mover', { speed: 78 * 2.2 }).add('status').add('health', { hp: H.max * d.hp * pm, max: H.max * d.hp * pm, h: 30, col: '#8fd8ff' })
    .add('fighter', { dmg: c.pow * d.dmg * pm, range: 150, rate: .95, shot: 1, col: '#bfefff' }).add('pal', { owner: e, ox: -22 - j * 6, oy }).add('life', { t: d.life }); q.owner = e; ring(w, q.x, q.y, 22, '#dff6ff'); }
  if (d.heal) heal(w, e, H.max * d.heal); return n; });
defineSkill('bash', c => { const { w, e, d } = c; let n = 0; for (const o of nearest(w, e, d.r)) { hit(w, e, o, c.pow * d.mul, c.o); const st = o.get('status'); if (st) { st.kx = Math.sign(o.x - e.x || 1) * (d.knock || 0); if (d.stun) st.stun = Math.max(st.stun, d.stun); } n++; } if (d.heal) heal(w, e, e.get('health').max * d.heal); ring(w, e.x, e.y, d.r, '#fff'); return n; });
defineSkill('volley', c => { const { w, e, d } = c, ts = nearest(w, e, d.r).slice(0, d.n); for (const t of ts) w.spawn(e.x, e.y).add('projectile', { src: e, target: t, dmg: c.pow * d.mul, col: '#ffb46a', speed: 560, o: c.o }); return ts.length; });
defineSkill('nova', c => { const { w, e, d } = c, t = nearest(w, e, d.range)[0], f = e.get('sprite') && e.get('sprite').flip ? -1 : 1, x = t ? t.x : e.x + f * 110, y = t ? t.y : e.y; let n = 0; for (const o of enemies(w, e)) if (Math.hypot(o.x - x, (o.y - y) * 1.4) <= d.r) { hit(w, e, o, c.pow * d.mul, c.o); n++; } ring(w, x, y, d.r, '#ffe07a'); return n; });
defineSkill('dash', c => { const { w, e, d } = c, t = nearest(w, e, d.range)[0], f = e.get('sprite') && e.get('sprite').flip ? -1 : 1; if (!t) { e.x += f * 70; return 0; } e.x = t.x - Math.sign(t.x - e.x || 1) * 20; e.y = t.y; hit(w, e, t, c.pow * d.mul, c.o); if (d.heal) heal(w, e, e.get('health').max * d.heal); ring(w, t.x, t.y, 26, '#c9b6ff'); return 1; });
defineSkill('burst', c => { const { w, e, d } = c, m = d.mul + (d.per || 0) * Math.max(0, c.rank - 1); let n = 0; for (const o of nearest(w, e, d.r)) { hit(w, e, o, c.pow * m, c.o); n++; } ring(w, e.x, e.y, d.r, d.ult ? '#ffe07a' : '#9fd8ff'); return n; });
defineSkill('mend', c => { const { w, e, d } = c, k = d.heal + (d.per || 0) * Math.max(0, c.rank - 1); let n = 0; for (const o of allies(w, e, d.r)) { heal(w, o, o.get('health').max * k); n++; } ring(w, e.x, e.y, d.r, '#9be88a'); return n; });

export function installSkills(world) {
  const S = world.game.signals;
  // 기술 주머니: list = [{id, k(동작), d(숫자), cd, t(남은 대기), icon, name, rank, tag}] · haste 대기 시간 빨라짐
  world.define('caster', {
    defaults: { list: [], haste: 1, mods: null },
    init(e, c) { c.list = c.list.slice(); },
    update(e, c, dt) { for (const s of c.list) if (s.t > 0) s.t = Math.max(0, s.t - dt * c.haste); }
  });
}
export function addSkill(e, s) { const c = e.get('caster'), i = c.list.findIndex(q => q.id === s.id); const n = Object.assign({ t: 0, rank: 1, cd: 5, icon: '✨', name: s.id }, s); if (i >= 0) { n.t = c.list[i].t; c.list[i] = n; } else c.list.push(n); return n; }
export function ready(e, id) { const s = e.get('caster').list.find(q => q.id === id); return !!s && s.t <= 0; }
// 기술 쓰기: 대기 중이거나 쓰러졌거나 기절이면 false
export function cast(world, e, id) {
  const c = e.get('caster'), s = c && c.list.find(q => q.id === id), h = e.get('health'), st = e.get('status'); if (!s || s.t > 0 || (h && h.down) || (st && st.stun > 0)) return false;
  const fn = KINDS.get(s.k); if (!fn) throw new Error('기술 동작 없음: ' + s.k); const f = e.get('fighter'), m = c.mods ? c.mods(s) : {};
  const ctx = { w: world, e, d: s.d, rank: s.rank, pow: (f ? f.dmg * f.mul : 10), o: { kind: s.tag || 'skill', magic: !!s.d.magic }, extra: m.extra || 0, palMul: m.palMul || 1 };
  s.t = s.cd; const sp = e.get('sprite'); if (sp) { sp.lock = 'act'; sp.lockT = .4; } if (f) f.cd = Math.max(f.cd, .3);
  const n = fn(ctx); world.game.signals.emit('skill:cast', { e, skill: s, hits: n }); if (m.after) m.after(ctx, s, fn); return true;
}
