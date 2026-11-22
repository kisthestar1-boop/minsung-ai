// 새싹 엔진 · parts — 기본 부품 모음. world.define 으로 등록해서 물체에 붙여 쓴다.
export function installParts(world) {
  const A = world.game.assets;
  // 그림: frames {idle:[이름], walk:[이름들], act:[이름]} · h 그릴 높이 · 걷는 거리에 맞춰 장면이 바뀐다
  world.define('sprite', {
    defaults: { frames: { idle: [] }, h: 64, state: 'idle', t: 0, dist: 0, flip: false, stride: 15, bob: 1.1 },
    init(e, c) { for (const k in c.frames) c.frames[k].forEach(n => A.image(n)); },
    update(e, c, dt) { c.t += dt; if (c.lockT > 0) { c.lockT -= dt; if (c.lockT <= 0) c.lock = null; } if (c.flash > 0) c.flash -= dt; },
    draw(e, c, r) { const st = (c.lock && c.frames[c.lock]) ? c.lock : c.state, f = c.frames[st] || c.frames.idle, n = st === 'walk' ? f[Math.floor(c.dist / c.stride) % f.length] : f[0], dy = st === 'idle' ? Math.sin(c.t * 2.2) * c.bob : 0, im = A.image(n), fl = c.face < 0 ? !c.flip : c.flip; r.sprite(im, e.x, e.y, c.h, { flip: fl, dy, alpha: c.alpha }); if (c.flash > 0) { r.ctx.globalCompositeOperation = 'lighter'; r.sprite(im, e.x, e.y, c.h, { flip: fl, dy, alpha: .55 }); r.ctx.globalCompositeOperation = 'source-over'; } }
  });
  // 그림자: 발밑의 부드러운 타원 — 캐릭터가 땅에 붙어 보이게 한다
  world.define('shadow', {
    defaults: { rx: 14, ry: 5, a: .24 },
    draw(e, c, r) { const x = r.ctx; x.save(); x.globalAlpha = c.a; x.fillStyle = '#2a2018'; x.beginPath(); x.ellipse(e.x, e.y + 1, c.rx, c.ry, 0, 0, 7); x.fill(); x.restore(); }
  });
  // 이동: vx,vy(−1~1) 방향으로 speed 만큼. 세계 밖으로 나가지 않는다.
  world.define('mover', {
    defaults: { speed: 100, vx: 0, vy: 0, mul: 1 },
    update(e, c, dt, w) { const st = e.get('status'); c.mul = st ? (st.stun > 0 ? 0 : 1 - st.slow) : 1; const m = Math.hypot(c.vx, c.vy), s = e.get('sprite'); if (m > .12 && c.mul > 0) { const v = c.speed * c.mul * dt; e.x = Math.max(20, Math.min(w.w - 20, e.x + c.vx * v)); e.y = Math.max(w.h * .1, Math.min(w.h * .95, e.y + c.vy * v * .85)); if (s) { s.state = 'walk'; s.dist += v * m; if (Math.abs(c.vx) > .12) s.flip = c.vx < 0; } } else if (s) s.state = 'idle'; }
  });
  // 조종: 입력(조이스틱·키보드)을 이동 부품에 전달
  world.define('player', {
    defaults: { off: false },
    update(e, c, dt, w) { const m = e.get('mover'), a = w.game.input.axis; if (m && !c.off) { m.vx = a.x; m.vy = a.y; } }
  });
  // 따라다니기: target 물체 뒤를 부드럽게 따라간다 (정령·동료)
  world.define('follow', {
    defaults: { target: null, ox: -30, oy: 0, lag: 4, float: 0 },
    update(e, c, dt) { const t = c.target; if (!t || t.dead) return; const s = t.get('sprite'), dir = s && s.flip ? -1 : 1, tx = t.x + c.ox * dir, ty = t.y + c.oy, k = Math.min(1, dt * c.lag); e.x += (tx - e.x) * k; e.y += (ty - e.y) * k; const me = e.get('sprite'); if (me) { me.flip = s ? s.flip : false; if (c.float) me.dyBase = c.float; } }
  });
  // 체력과 체력 막대
  world.define('health', {
    defaults: { hp: 100, max: 100, bar: true, col: '#ff7a7a', h: 50, down: false, hitT: 0, lastHit: null, keep: false, regen: 0 },
    update(e, c, dt) { if (c.hitT > 0) c.hitT -= dt; if (c.regen && !c.down && c.hp < c.max) c.hp = Math.min(c.max, c.hp + c.regen * dt); },
    draw(e, c, r) { if (!c.bar || c.hp >= c.max || c.down) return; const x = r.ctx, k = Math.max(0, c.hp / c.max); x.fillStyle = 'rgba(0,0,0,.4)'; r.rr(e.x - 14, e.y - c.h - 8, 28, 4, 2); x.fill(); x.fillStyle = c.col; r.rr(e.x - 14, e.y - c.h - 8, 28 * k, 4, 2); x.fill(); }
  });
  // 이름표
  world.define('label', {
    defaults: { text: '', h: 60, col: '#ffe07a', bg: 'rgba(50,32,10,.78)' },
    draw(e, c, r) { const x = r.ctx; x.font = '900 9px system-ui'; const tw = x.measureText(c.text).width + 10; x.fillStyle = c.bg; r.rr(e.x - tw / 2, e.y - c.h - 20, tw, 14, 7); x.fill(); r.text(c.text, e.x, e.y - c.h - 10, { s: 9, a: 'center', c: c.col }); }
  });
}
