// 새싹 엔진 · world — 물체(Entity)와 부품(Component). 규칙 2 "조립식 부품".
// 물체는 부품을 붙여 만든다: e.add('sprite',{...}).add('mover',{...})
let NEXT = 1;
export class Entity {
  constructor(world, x = 0, y = 0) { this.id = NEXT++; this.world = world; this.x = x; this.y = y; this.c = {}; this.tags = new Set(); this.dead = false; }
  add(name, data = {}) { const def = this.world.comps.get(name); if (!def) throw new Error('부품 없음: ' + name); const c = Object.assign({}, def.defaults, data); this.c[name] = c; def.init && def.init(this, c, this.world); return this; }
  get(name) { return this.c[name]; }
  has(name) { return name in this.c; }
  tag(t) { this.tags.add(t); return this; }
  kill() { if (this.dead) return; this.dead = true; this.world.game.signals.emit('entity:dead', this); }
}
export class World {
  constructor(game) { this.game = game; this.list = []; this.comps = new Map(); this.w = 1000; this.h = 1000; }
  // 부품 종류 등록: {defaults, init(e,c,world), update(e,c,dt,world), draw(e,c,r,world)}
  define(name, def) { this.comps.set(name, def); return this; }
  spawn(x, y) { const e = new Entity(this, x, y); this.list.push(e); return e; }
  with(name) { return this.list.filter(e => !e.dead && name in e.c); }
  tagged(t) { return this.list.filter(e => !e.dead && e.tags.has(t)); }
  near(x, y, r, pred) { const out = []; for (const e of this.list) { if (e.dead) continue; const d = Math.hypot(e.x - x, (e.y - y) * 1.4); if (d <= r && (!pred || pred(e))) out.push([d, e]); } return out.sort((a, b) => a[0] - b[0]).map(q => q[1]); }
  update(dt) { for (const e of this.list) { if (e.dead) continue; for (const k in e.c) { const d = this.comps.get(k); d.update && d.update(e, e.c[k], dt, this); } } if (this.list.some(e => e.dead)) this.list = this.list.filter(e => !e.dead); }
  // 발 위치(y)가 위에 있는 것부터 그려서 앞뒤가 자연스럽게 보인다
  draw(r) { const L = this.list.filter(e => !e.dead).sort((a, b) => a.y - b.y); for (const e of L) for (const k in e.c) { const d = this.comps.get(k); d.draw && d.draw(e, e.c[k], r, this); } }
}
