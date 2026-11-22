// 새싹 엔진 · assets — 그림 불러오기와 보관
export class Assets {
  constructor(base = '', ver = '') { this.base = base; this.ver = ver; this.img = new Map(); this.pending = 0; this.failed = []; }
  url(name) { return this.base + name + (/\.(png|jpg|webp)$/.test(name) ? '' : (name.startsWith('bg_') ? '.jpg' : '.webp')) + (this.ver ? '?v=' + this.ver : ''); }
  image(name) { let im = this.img.get(name); if (im) return im; im = new Image(); this.img.set(name, im); this.pending++; im.onload = () => { this.pending--; }; im.onerror = () => { this.pending--; this.failed.push(name); }; im.src = this.url(name); return im; }
  ready(name) { const im = this.img.get(name); return !!(im && im.naturalWidth); }
  load(names) { names.forEach(n => this.image(n)); return new Promise(res => { const c = () => this.pending <= 0 ? res(this) : setTimeout(c, 30); c(); }); }
}
