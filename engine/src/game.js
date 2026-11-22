// 새싹 엔진 · game — 부품들을 하나로 묶는 본체
import { Signals, Loop, Scenes } from './core.js';
import { Assets } from './assets.js';
import { Input } from './input.js';
import { Renderer, Camera } from './render.js';
export const VERSION = '1.0.0-숲3';
export class Game {
  constructor(canvas, opt = {}) {
    this.signals = new Signals(); this.assets = new Assets(opt.assetBase || '', opt.assetVer || '');
    this.r = new Renderer(canvas, opt.viewH || 540); this.camera = new Camera();
    this.input = new Input(canvas, (x, y) => this.r.toLocal(x, y)); this.scenes = new Scenes(this); this.data = opt.data || {};
    this.loop = new Loop(dt => { this.input.begin(); this.scenes.update(dt); }, () => { this.r.begin(); this.scenes.draw(this.r); });
    this.errors = []; addEventListener('error', e => this.errors.push(e.message));
  }
  start(scene, params) { this.scenes.go(scene, params); this.loop.start(); }
}
