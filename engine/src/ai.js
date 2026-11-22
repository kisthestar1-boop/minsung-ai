// 새싹 엔진 · ai — 몬스터 머리(brain). 대기 → 추격 → 공격 → 제자리로. 판단만 하고, 걷기는 mover, 때리기는 fighter 가 한다.
import { dist, nearestEnemy } from './combat.js';
export function installAI(world) {
  const S = world.game.signals;
  world.define('brain', {
    // aggro 알아채는 거리 · leash 집에서 이만큼 멀어지면 포기 · group 같은 무리는 함께 깨어난다
    defaults: { state: 'idle', hx: null, hy: null, aggro: 150, leash: 330, group: null, target: null, t: 0, wander: 0 },
    init(e, c) { if (c.hx == null) { c.hx = e.x; c.hy = e.y; } },
    update(e, c, dt, w) {
      const m = e.get('mover'), f = e.get('fighter'), h = e.get('health'); if (!m || !f) return; if (h && h.down) { m.vx = m.vy = 0; f.hold = true; return; }
      const home = Math.hypot(e.x - c.hx, (e.y - c.hy) * 1.4); c.t += dt;
      const set = s => { if (c.state !== s) { c.state = s; c.t = 0; S.emit('ai:state', { e, state: s }); } };
      if (c.state === 'idle') { m.vx = m.vy = 0; f.hold = true; const t = (h && h.lastHit && !h.lastHit.dead && h.hitT > 0) ? h.lastHit : nearestEnemy(w, e, Math.max(c.aggro, f.range + 20)); if (t) { c.target = t; set('chase'); if (c.group != null) for (const o of w.with('brain')) { const b = o.get('brain'); if (o !== e && b.group === c.group && b.state === 'idle') { b.target = t; b.state = 'chase'; b.t = 0; } } } return; }
      if (c.state === 'return') { f.hold = true; const dx = c.hx - e.x, dy = c.hy - e.y, d = Math.hypot(dx, dy); if (d < 6) { m.vx = m.vy = 0; if (h) h.hp = h.max; set('idle'); } else { m.vx = dx / d; m.vy = dy / d; if (h) h.hp = Math.min(h.max, h.hp + h.max * .25 * dt); } return; }
      // chase / attack
      let t = c.target; const ok = t && !t.dead && t.has('health') && !t.get('health').down;
      if (!ok || home > c.leash) { c.target = null; f.target = null; set('return'); return; }
      const d = dist(e, t), reach = f.range * .9; f.hold = false; f.target = d <= f.range ? t : null;
      if (d > reach) { const dx = t.x - e.x, dy = t.y - e.y, q = Math.hypot(dx, dy) || 1; m.vx = dx / q; m.vy = dy / q; set('chase'); }
      else { m.vx = m.vy = 0; const sp = e.get('sprite'); if (sp) sp.flip = t.x < e.x; set('attack'); }
    }
  });
}
