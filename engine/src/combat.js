// 새싹 엔진 · combat — 전투. 편(team) · 싸움꾼(fighter) · 발사체(projectile) · 상태(status) · 숫자(floater)
// 피해는 모두 hit() 한 곳을 지난다: 'combat:before'(고칠 수 있음) → 체력 감소 → 'combat:hit' → 쓰러지면 'combat:kill'
export const dist = (a, b) => Math.hypot(a.x - b.x, (a.y - b.y) * 1.4);
export const enemies = (w, e) => { const s = e.get('team'); return w.with('team').filter(o => o !== e && s && o.get('team').side !== s.side && o.has('health') && !o.get('health').down); };
export function nearestEnemy(w, e, r) { let best = null, bd = r; for (const o of enemies(w, e)) { const d = dist(e, o); if (d <= bd) { bd = d; best = o; } } return best; }

export function hit(world, src, tgt, amount, o = {}) {
  const h = tgt && tgt.get('health'); if (!h || tgt.dead || h.down) return 0;
  const ev = { src, tgt, amount, kind: o.kind || 'hit', crit: false, cancel: false };
  world.game.signals.emit('combat:before', ev); if (ev.cancel) return 0;
  const n = Math.max(1, Math.round(ev.amount)); h.hp = Math.max(0, h.hp - n); h.hitT = .18; h.lastHit = src;
  const sp = tgt.get('sprite'); if (sp) sp.flash = .12;
  if (!o.quiet) world.spawn(tgt.x + (Math.random() - .5) * 10, tgt.y).add('floater', { text: String(n), up: (h.h || 50) + 6, col: ev.crit ? '#ffd84d' : ((tgt.get('team') || {}).side > 0 ? '#ff8f8f' : '#fff') });
  ev.amount = n; world.game.signals.emit('combat:hit', ev);
  if (h.hp <= 0) { h.down = true; world.game.signals.emit('combat:kill', { src, tgt }); if (!h.keep) tgt.add('fade', { t: .35 }); }
  return n;
}
export function heal(world, tgt, amount) { const h = tgt.get('health'); if (!h || h.down) return 0; const n = Math.min(h.max - h.hp, Math.round(amount)); if (n > 0) { h.hp += n; world.spawn(tgt.x, tgt.y).add('floater', { text: '+' + n, up: (h.h || 50) + 6, col: '#8ff0a8' }); } return n; }
// 범위 피해: 중심에서 r 안의 적 모두
export function blast(world, src, x, y, r, amount, o) { let n = 0; for (const e of enemies(world, src)) if (Math.hypot(e.x - x, (e.y - y) * 1.4) <= r) { hit(world, src, e, amount, o); n++; } return n; }

export function installCombat(world) {
  const S = world.game.signals;
  world.define('team', { defaults: { side: 1 } });
  // 싸움꾼: 사거리 안의 가장 가까운 적을 rate 초마다 공격. shot 이면 발사체, 아니면 바로 타격. hold=true 면 스스로 공격하지 않음
  world.define('fighter', {
    defaults: { dmg: 10, range: 40, rate: 1, cd: 0, shot: 0, splash: 0, target: null, col: '#ffe98a', hold: false, mul: 1, haste: 1, moving: 0 },
    update(e, c, dt, w) {
      c.cd = Math.max(0, c.cd - dt * c.haste); const h = e.get('health'); if (c.hold || (h && h.down)) return; const st = e.get('status'); if (st && st.stun > 0) return;
      let t = c.target; if (!t || t.dead || !t.has('health') || t.get('health').down || dist(e, t) > c.range) t = nearestEnemy(w, e, c.range); c.target = t; if (!t || c.cd > 0) return;
      c.cd = c.rate; const sp = e.get('sprite'); if (sp) { sp.lock = 'act'; sp.lockT = .22; if (Math.abs(t.x - e.x) > 4) sp.flip = t.x < e.x; }
      const amount = c.dmg * c.mul; S.emit('combat:attack', { src: e, tgt: t, amount });
      if (c.shot) w.spawn(e.x, e.y).add('projectile', { src: e, target: t, dmg: amount, splash: c.splash, col: c.col, z: (h ? h.h : 50) * .55 });
      else { hit(w, e, t, amount); if (c.splash) for (const o of enemies(w, e)) if (o !== t && dist(o, t) <= c.splash) hit(w, e, o, amount * .6); }
    }
  });
  // 발사체: 목표를 향해 날아가 닿으면 피해. 목표가 사라지면 마지막 자리까지 날아가고 사라진다
  world.define('projectile', {
    defaults: { src: null, target: null, dmg: 10, speed: 420, splash: 0, col: '#ffe98a', z: 28, tx: 0, ty: 0, life: 3 },
    init(e, c) { if (c.target) { c.tx = c.target.x; c.ty = c.target.y; } },
    update(e, c, dt, w) {
      const t = c.target, alive = t && !t.dead && t.has('health') && !t.get('health').down; if (alive) { c.tx = t.x; c.ty = t.y; }
      const dx = c.tx - e.x, dy = c.ty - e.y, d = Math.hypot(dx, dy), v = c.speed * dt; c.life -= dt;
      if (d <= v + 6 || c.life <= 0) { if (alive) hit(w, c.src, t, c.dmg); if (c.splash && c.src && !c.src.dead) for (const o of enemies(w, c.src)) if (o !== t && Math.hypot(o.x - c.tx, (o.y - c.ty) * 1.4) <= c.splash) hit(w, c.src, o, c.dmg * .6); S.emit('combat:land', { x: c.tx, y: c.ty, splash: c.splash, col: c.col }); e.dead = true; return; }
      e.x += dx / d * v; e.y += dy / d * v;
    },
    draw(e, c, r) { const x = r.ctx, y = e.y - c.z; x.save(); const g = x.createRadialGradient(e.x, y, 0, e.x, y, 9); g.addColorStop(0, '#fff'); g.addColorStop(.35, c.col); g.addColorStop(1, 'rgba(255,255,255,0)'); x.fillStyle = g; x.beginPath(); x.arc(e.x, y, 9, 0, 7); x.fill(); x.restore(); }
  });
  // 상태: 느려짐(slow 0~1, slowT) · 기절(stun 초)
  world.define('status', {
    defaults: { slow: 0, slowT: 0, stun: 0 },
    update(e, c, dt) { if (c.slowT > 0) { c.slowT -= dt; if (c.slowT <= 0) c.slow = 0; } if (c.stun > 0) c.stun -= dt; }
  });
  // 떠오르는 숫자 (차분하게 살짝만 오르고 사라진다)
  world.define('floater', {
    defaults: { text: '', t: 0, life: .7, up: 50, col: '#fff' },
    update(e, c, dt) { c.t += dt; if (c.t >= c.life) e.dead = true; },
    draw(e, c, r) { const k = c.t / c.life; r.ctx.save(); r.ctx.globalAlpha = 1 - k * k; r.text(c.text, e.x, e.y - c.up - k * 12, { s: 12, a: 'center', c: c.col, stroke: 'rgba(30,20,10,.75)' }); r.ctx.restore(); }
  });
  // 쓰러진 물체가 서서히 사라진다
  world.define('fade', {
    defaults: { t: .35, t0: 0 },
    init(e, c) { c.t0 = c.t; },
    update(e, c, dt) { c.t -= dt; const s = e.get('sprite'); if (s) s.alpha = Math.max(0, c.t / c.t0); if (c.t <= 0) e.kill(); }
  });
}
