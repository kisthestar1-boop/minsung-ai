// 새싹 엔진 · render — 화면 맞춤 · 카메라 · 그리기 도우미
export class Renderer {
  constructor(canvas, viewH = 540) { this.cv = canvas; this.ctx = canvas.getContext('2d'); this.H = viewH; this.W = 960; this.scale = 1; this.fit(); addEventListener('resize', () => this.fit()); }
  fit() { const dpr = Math.min(2, window.devicePixelRatio || 1), cw = this.cv.clientWidth || innerWidth, ch = this.cv.clientHeight || innerHeight; this.scale = ch / this.H; this.W = Math.max(640, cw / this.scale); this.cv.width = Math.round(cw * dpr); this.cv.height = Math.round(ch * dpr); this.k = this.scale * dpr; }
  toLocal(cx, cy) { const r = this.cv.getBoundingClientRect(); return { x: (cx - r.left) / this.scale, y: (cy - r.top) / this.scale }; }
  begin() { const c = this.ctx; c.setTransform(this.k, 0, 0, this.k, 0, 0); c.clearRect(0, 0, this.W, this.H); }
  rr(x, y, w, h, r) { const c = this.ctx; c.beginPath(); c.moveTo(x + r, y); c.arcTo(x + w, y, x + w, y + h, r); c.arcTo(x + w, y + h, x, y + h, r); c.arcTo(x, y + h, x, y, r); c.arcTo(x, y, x + w, y, r); c.closePath(); }
  // 발 위치(x,y)를 기준으로 그림을 높이 h 로 그린다
  sprite(im, x, y, h, o = {}) { if (!im || !im.naturalWidth) return; const c = this.ctx, w = im.naturalWidth * h / im.naturalHeight; c.save(); c.translate(x, y + (o.dy || 0)); if (o.flip) c.scale(-1, 1); if (o.alpha != null) c.globalAlpha = o.alpha; c.drawImage(im, -w / 2, -h, w, h); c.restore(); }
  text(t, x, y, o = {}) { const c = this.ctx; c.font = (o.w || 900) + ' ' + (o.s || 13) + 'px system-ui'; c.textAlign = o.a || 'left'; if (o.stroke) { c.lineWidth = o.lw || 3; c.strokeStyle = o.stroke; c.strokeText(t, x, y); } c.fillStyle = o.c || '#fff'; c.fillText(t, x, y); c.textAlign = 'left'; }
}
// 카메라: 세계 좌표 → 화면 좌표. 대상을 부드럽게 따라가고 세계 밖으로 나가지 않는다.
export class Camera {
  constructor() { this.x = 0; this.y = 0; this.zoom = 1; this.bounds = null; this.view = { x: 0, y: 0, w: 960, h: 540 }; }
  follow(tx, ty, dt, snap) { const vw = this.view.w / this.zoom, vh = this.view.h / this.zoom; let x = tx - vw / 2, y = ty - vh / 2; const b = this.bounds; if (b) { x = Math.max(b.x, Math.min(b.x + b.w - vw, x)); y = Math.max(b.y, Math.min(b.y + b.h - vh, y)); } const k = snap ? 1 : Math.min(1, dt * 6); this.x += (x - this.x) * k; this.y += (y - this.y) * k; }
  apply(ctx) { ctx.translate(this.view.x, this.view.y); ctx.scale(this.zoom, this.zoom); ctx.translate(-this.x, -this.y); }
  toScreen(x, y) { return { x: this.view.x + (x - this.x) * this.zoom, y: this.view.y + (y - this.y) * this.zoom }; }
}
