// 새싹 엔진 · core — 신호(Signals) · 게임 루프 · 씬 관리
// 규칙 3 "신호로 말한다": 부품끼리 직접 부르지 않고 신호를 보내고 듣는다.
export class Signals {
  constructor() { this.m = new Map(); }
  on(name, fn) { if (!this.m.has(name)) this.m.set(name, new Set()); this.m.get(name).add(fn); return () => this.off(name, fn); }
  off(name, fn) { const s = this.m.get(name); if (s) s.delete(fn); }
  emit(name, data) { const s = this.m.get(name); if (s) for (const fn of [...s]) fn(data); }
}

// 고정 간격 업데이트(1/60초) + 그리기. tick()은 시험에서 시간을 직접 넘길 때 쓴다.
export class Loop {
  constructor(update, draw, step = 1 / 60) { this.update = update; this.draw = draw; this.step = step; this.acc = 0; this.last = 0; this.running = false; this.time = 0; this.frames = 0; }
  start() { if (this.running) return; this.running = true; this.last = performance.now(); const f = (t) => { if (!this.running) return; let dt = Math.min(0.1, (t - this.last) / 1000); this.last = t; this.advance(dt); this.draw(); requestAnimationFrame(f); }; requestAnimationFrame(f); }
  stop() { this.running = false; }
  advance(dt) { this.acc += dt; let n = 0; while (this.acc >= this.step && n++ < 6) { this.update(this.step); this.acc -= this.step; this.time += this.step; this.frames++; } if (n > 6) this.acc = 0; }
  tick(n = 1) { for (let i = 0; i < n; i++) { this.update(this.step); this.time += this.step; this.frames++; } this.draw(); }
}

// 씬: enter/exit/update/draw 를 가진 화면 단위. 겹쳐 띄우기(push) 지원 — 규칙 4 "씬 단위".
export class Scenes {
  constructor(game) { this.game = game; this.stack = []; this.defs = new Map(); }
  add(name, def) { this.defs.set(name, def); }
  get top() { return this.stack[this.stack.length - 1] || null; }
  _make(name, params) { const D = this.defs.get(name); if (!D) throw new Error('씬 없음: ' + name); const s = typeof D === 'function' ? new D(this.game) : Object.create(D); s.name = name; s.game = this.game; s.enter && s.enter(params || {}); return s; }
  go(name, params) { while (this.stack.length) { const s = this.stack.pop(); s.exit && s.exit(); } this.stack.push(this._make(name, params)); this.game.signals.emit('scene:go', name); }
  push(name, params) { this.stack.push(this._make(name, params)); this.game.signals.emit('scene:push', name); }
  pop() { const s = this.stack.pop(); if (s && s.exit) s.exit(); this.game.signals.emit('scene:pop', s && s.name); }
  update(dt) { const t = this.top; if (t && t.update) t.update(dt); }           // 맨 위 씬만 움직인다(아래는 멈춤)
  draw(r) { for (const s of this.stack) s.draw && s.draw(r); }                   // 아래부터 차례로 그린다
}
