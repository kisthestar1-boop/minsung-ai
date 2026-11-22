// 새싹 엔진 · input — 끌어서 움직이는 조이스틱 + 누르는 버튼 + 키보드
export class Input {
  constructor(canvas, toLocal) { this.axis = { x: 0, y: 0 }; this.stick = null; this.keys = new Set(); this.taps = []; this.buttons = []; this.toLocal = toLocal;
    const P = e => this.toLocal(e.clientX, e.clientY);
    canvas.addEventListener('pointerdown', e => { const p = P(e); const b = this.hit(p.x, p.y); if (b) { this.taps.push(b); return; } this.stick = { id: e.pointerId, ox: p.x, oy: p.y, dx: 0, dy: 0 }; canvas.setPointerCapture && canvas.setPointerCapture(e.pointerId); });
    canvas.addEventListener('pointermove', e => { const s = this.stick; if (!s || s.id !== e.pointerId) return; const p = P(e), dx = p.x - s.ox, dy = p.y - s.oy, d = Math.hypot(dx, dy), m = Math.min(1, d / 44); s.dx = d ? dx / d * m : 0; s.dy = d ? dy / d * m : 0; });
    const up = e => { if (this.stick && this.stick.id === e.pointerId) this.stick = null; };
    canvas.addEventListener('pointerup', up); canvas.addEventListener('pointercancel', up);
    addEventListener('keydown', e => this.keys.add(e.key)); addEventListener('keyup', e => this.keys.delete(e.key)); }
  hit(x, y) { for (let i = this.buttons.length - 1; i >= 0; i--) { const b = this.buttons[i]; if (x >= b.x && x <= b.x + b.w && y >= b.y && y <= b.y + b.h) return b; } return null; }
  // 매 프레임: 버튼 목록을 비우고(그릴 때 다시 등록), 누른 버튼의 동작을 실행한다
  begin() { const t = this.taps; this.taps = []; for (const b of t) b.cb && b.cb(); let x = 0, y = 0; if (this.stick) { x = this.stick.dx; y = this.stick.dy; } const k = this.keys; if (k.has('ArrowLeft') || k.has('a')) x -= 1; if (k.has('ArrowRight') || k.has('d')) x += 1; if (k.has('ArrowUp') || k.has('w')) y -= 1; if (k.has('ArrowDown') || k.has('s')) y += 1; const d = Math.hypot(x, y); if (d > 1) { x /= d; y /= d; } this.axis.x = x; this.axis.y = y; this.buttons = []; }
  button(x, y, w, h, cb) { this.buttons.push({ x, y, w, h, cb }); }
}
