// 새싹 엔진 · progress — 성장. 경험치·레벨·스킬 트리. 능력치는 "기본값 × 레벨 × 트리"로 매번 다시 계산한다(덧칠하지 않는다).
import { heal } from './combat.js';
import { addSkill, cast } from './skills.js';
export class Progress {
  // D = 내용 표 {HEROES, HUS, TRN, TRJ, TRREC, SKILLDEF, GROW} · hk 영웅 키 · saved = {lv,xp,tr}
  constructor(world, hero, hk, D, saved) { this.w = world; this.e = hero; this.hk = hk; this.D = D; this.G = D.GROW; this.job = D.TRREC[hk]; this.J = D.TRJ[this.job];
    this.lv = 1; this.xp = 0; this.tr = {}; this.kills = 0; this.gold = 0; this.rvCd = 0; if (saved) { this.lv = saved.lv || 1; this.xp = saved.xp || 0; this.tr = Object.assign({}, saved.tr); }
    const S = world.game.signals; this.off = [S.on('combat:before', ev => this.before(ev)), S.on('combat:kill', ev => this.onKill(ev))];
    const c = hero.get('caster'); if (c) c.mods = s => this.mods(s); this.apply(true); }
  destroy() { this.off.forEach(f => f()); }
  toJSON() { return { lv: this.lv, xp: this.xp, tr: Object.assign({}, this.tr) }; }
  // --- 경험치와 레벨
  need(lv = this.lv) { return this.G.a + lv * this.G.b; }
  gain(n) { if (this.lv >= this.G.cap) return; this.xp += n * (this.G.early[this.lv] || 1); let up = 0; while (this.lv < this.G.cap && this.xp >= this.need()) { this.xp -= this.need(); this.lv++; up++; }
    if (up) { this.apply(); const h = this.e.get('health'); if (!h.down) heal(this.w, this.e, h.max * .35); this.w.spawn(this.e.x, this.e.y).add('ring', { r: 46, col: '#ffe07a', life: .6 }); this.w.game.signals.emit('progress:level', { lv: this.lv, pts: this.points() }); } }
  // --- 스킬 트리
  rank(k) { return this.tr[k] || 0; }
  val(k) { return this.D.TRN[k].v * this.rank(k); }          // 단계까지 곱한 값 (예: 8% × 3단계 = 24)
  pct(k) { return this.val(k) / 100; }
  node(k) { return this.J.t.find(q => q[0] === k) || null; }
  spent() { let s = 0; for (const k in this.tr) s += this.tr[k]; return s; }
  points() { return Math.max(0, this.lv - 1 - this.spent()); }
  why(k) { const n = this.D.TRN[k], q = this.node(k), r = this.rank(k); if (!n || !q) return '이 직업의 기술이 아니에요'; if (r >= n.mx) return '최고 단계예요';
    if (q[4] && this.rank(q[4]) > 0) return '옆 기술(' + this.D.TRN[q[4]].n + ')을 골라서 배울 수 없어요'; if (q[3] && !q[3].some(x => this.rank(x) > 0)) return '먼저 배워야 해요: ' + q[3].map(x => this.D.TRN[x].n).join(' 또는 ');
    if (n.lv && this.lv < n.lv) return '영웅 Lv.' + n.lv + '부터 배울 수 있어요'; if (this.points() < 1) return '포인트가 없어요 · 레벨이 오르면 1점씩 생겨요'; return ''; }
  learn(k) { if (this.why(k)) return false; this.tr[k] = this.rank(k) + 1; this.apply(); this.w.game.signals.emit('progress:learn', { k, rank: this.tr[k] }); return true; }
  reset() { this.tr = {}; this.apply(); this.w.game.signals.emit('progress:reset', {}); }
  // 배울 수 있는 것 중 트리 위쪽부터 하나 (자동 시험·추천용)
  suggest() { for (const q of this.J.t) if (!this.why(q[0])) return q[0]; return null; }
  // --- 능력치 다시 계산: 기본값(표) × 레벨 × 트리
  apply(first) { const H = this.D.HEROES[this.hk], e = this.e, g = Math.pow(this.G.grow, this.lv - 1), h = e.get('health'), f = e.get('fighter'), m = e.get('mover'), c = e.get('caster');
    const max = Math.round(H.hp * g * (1 + this.pct('t_hp'))), k = first ? 1 : h.hp / h.max; h.max = max; h.hp = Math.min(max, Math.max(h.down ? 0 : 1, Math.round(max * k)));
    h.regen = max * (.012 + this.pct('t_regen'));
    f.dmg = H.dmg * g * (1 + this.pct('t_atk')); f.range = Math.max(125, H.range * .72) * (1 + this.pct('t_range')); m.speed = H.spd * 2.4 * (1 + this.pct('t_spd'));
    if (c) { c.haste = 1 + this.pct('t_haste'); const U = this.D.HUS[this.hk], SD = this.D.SKILLDEF;
      addSkill(e, { id: 'smash', k: SD[this.hk].k, d: SD[this.hk], cd: U[2], icon: U[0], name: U[1], tag: 'smash' });
      for (const k of ['water', 'rain']) if (this.rank(k)) addSkill(e, { id: k, k: SD[k].k, d: SD[k], cd: SD[k].cd, icon: this.D.TRN[k].i, name: this.D.TRN[k].n, rank: this.rank(k), tag: 'tree' }); else c.list = c.list.filter(s => s.id !== k);
      if (this.rank('t_ult')) addSkill(e, { id: 'ult', k: SD.storm.k, d: SD.storm, cd: SD.storm.cd, icon: '🌟', name: '폭풍', tag: 'ult' }); else c.list = c.list.filter(s => s.id !== 'ult'); } }
  // --- 기술에 붙는 트리 효과
  mods(s) { const me = this; return { extra: s.k === 'summon' && this.rank('t_slot') ? 1 : 0, palMul: 1 + this.pct('t_pal'),
    after(ctx, sk, fn) { if (sk.id === 'water' && me.rank('t_echo')) { const p = ctx.pow; ctx.pow = p * me.D.TRN.t_echo.v / 100; fn(ctx); ctx.pow = p; } } }; }
  // --- 전투에 끼어드는 트리 효과 (피해가 지나가는 한 곳)
  side(e) { const t = e && e.get && e.get('team'); return t ? t.side : 0; }
  before(ev) { const mine = this.side(ev.src) === 1 && !ev.src.dead, R = Math.random;
    if (ev.src === this.e) { if (ev.kind === 'smash') ev.amount *= 1 + this.pct('t_smash'); if (ev.kind === 'ult') ev.amount *= 1 + this.pct('t_ult'); if (ev.magic) { ev.amount *= 1 + this.pct('t_surge'); const st = ev.tgt.get('status'); if (st && this.rank('t_ice')) st.stun = Math.max(st.stun, this.val('t_ice')); } }
    if (mine && this.rank('t_crit') && R() < this.pct('t_crit')) { ev.amount *= 2; ev.crit = true; }
    if (mine && ev.src !== this.e && this.rank('cheer') && ev.src.owner === this.e) ev.amount *= 1 + this.pct('cheer');
    if (ev.tgt === this.e) { if (this.rank('t_dodge') && R() < this.pct('t_dodge')) { ev.cancel = true; ev.note = '피했다!'; return; } ev.amount *= 1 - this.pct('t_shell'); } }
  onKill(ev) { const t = ev.tgt; if (t === this.e || this.side(t) !== -1) return; this.kills++; if (this.rank('t_leech')) heal(this.w, this.e, this.e.get('health').max * this.pct('t_leech')); this.gold += 1 + this.val('t_gold'); this.gain(t.xp || 5); }
  // 쓰러졌을 때: '다시 피는 꽃'이 준비돼 있으면 true (바로 부활)
  tick(dt) { if (this.rvCd > 0) this.rvCd -= dt; }
  tryRevive() { if (!this.rank('t_revive') || this.rvCd > 0) return false; this.rvCd = this.D.TRN.t_revive.v; return true; }
}
