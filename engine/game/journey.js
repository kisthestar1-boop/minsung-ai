// 새싹 원정대 · 여정 지도 씬 — 모험 위에 겹쳐 띄운다. 가 본 맵은 눌러서 빠른 이동, 못 가 본 맵은 관문으로 먼저 가야 한다.
// 참고한 구조: 중심 지도에서 지역으로 들어가는 허브(마리오64) · 가 본 곳만 빠른 이동(디아블로 웨이포인트) · 지역을 길로 잇기(포켓몬)
const KEY = 'sprout_engine_visited';
export const visited = { get() { try { return JSON.parse(localStorage.getItem(KEY) || '[]'); } catch (e) { return []; } }, add(id) { const v = this.get(); if (!v.includes(id)) { v.push(id); try { localStorage.setItem(KEY, JSON.stringify(v)); } catch (e) {} } return v; } };
export class Journey {
  constructor(game) { this.game = game; }
  enter(p) { this.p = p; this.t = 0; this.seen = p.seen || visited.get(); this.game.data.MAPS.forEach(m => this.game.assets.image(m.bg)); }
  update(dt) { this.t += dt; }
  go(m) { const p = this.p; this.game.signals.emit('travel', { from: p.cur, to: m.id, fast: true }); this.game.scenes.go('adventure', { hero: p.hero, map: m.id, saved: p.saved }); }
  draw(r) {
    const x = r.ctx, g = this.game, M = g.data.MAPS, n = M.length, a = Math.min(1, this.t / .25), cw = Math.min(210, (r.W - 60) / n - 16), ch = cw * .56, tot = n * cw + (n - 1) * 26, x0 = r.W / 2 - tot / 2, y0 = r.H / 2 - ch / 2 - 6;
    x.save(); x.globalAlpha = a; x.fillStyle = 'rgba(16,22,18,.86)'; x.fillRect(0, 0, r.W, r.H);
    r.text('🧭 여정 지도', r.W / 2, 54, { s: 22, a: 'center', c: '#ffe9a8' }); r.text('가 본 곳은 눌러서 바로 이동해요 · 처음 가는 곳은 맵 끝의 관문으로 가요', r.W / 2, 80, { s: 12, a: 'center', c: '#cfe8d8' });
    M.forEach((m, i) => { const cx = x0 + i * (cw + 26), cur = m.id === this.p.cur, seen = this.seen.includes(m.id) || cur;
      if (i < n - 1) { x.strokeStyle = '#ffd84d'; x.lineWidth = 3; x.setLineDash([6, 6]); x.beginPath(); x.moveTo(cx + cw + 3, y0 + ch / 2); x.lineTo(cx + cw + 23, y0 + ch / 2); x.stroke(); x.setLineDash([]); }
      const im = g.assets.image(m.bg); x.save(); r.rr(cx, y0, cw, ch, 12); x.clip(); if (im.naturalWidth) x.drawImage(im, cx, y0, cw, ch); else { x.fillStyle = '#31463a'; x.fillRect(cx, y0, cw, ch); } if (!seen) { x.fillStyle = 'rgba(16,22,18,.72)'; x.fillRect(cx, y0, cw, ch); } x.restore();
      x.lineWidth = cur ? 4 : 2; x.strokeStyle = cur ? '#ffd84d' : seen ? '#9ff0c8' : 'rgba(255,255,255,.3)'; r.rr(cx, y0, cw, ch, 12); x.stroke();
      if (!seen) r.text('🔒', cx + cw / 2, y0 + ch / 2 + 10, { s: 26, a: 'center' });
      r.text(m.n, cx + cw / 2, y0 + ch + 22, { s: 14, a: 'center', c: '#fff' }); r.text(cur ? '📍 지금 여기' : seen ? '눌러서 이동' : '아직 못 가 본 곳', cx + cw / 2, y0 + ch + 40, { s: 11, a: 'center', c: cur ? '#ffd84d' : seen ? '#9ff0c8' : '#9cb4a8' });
      if (seen && !cur) g.input.button(cx, y0, cw, ch + 44, () => this.go(m)); });
    const bw = 120, bx = r.W / 2 - bw / 2, by = r.H - 62; x.fillStyle = 'rgba(255,246,216,.95)'; r.rr(bx, by, bw, 36, 18); x.fill(); r.text('닫기', r.W / 2, by + 24, { s: 14, a: 'center', c: '#5a3d16' }); g.input.button(bx, by, bw, 36, () => g.scenes.pop());
    x.restore();
  }
}
