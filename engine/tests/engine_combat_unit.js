const {chromium}=require('playwright');
// 전투 부품 단위 시험: 범위 피해 · 느려짐 · 기절 · 치유 · 피해 고치기 신호 · 몬스터 돌아가기
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:920,height:400}});const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.goto('http://localhost:8765/engine/play.html?'+Date.now());await p.waitForTimeout(1500);
console.log(await p.evaluate(async()=>{const C=await import('./src/combat.js');const g=__E.game,s=g.scenes.top,h=s.hero,w=s.world;g.loop.stop();const R={};
 const ms=w.tagged('monster').filter(e=>e.camp===0),m=ms[0];
 // 범위 피해
 const hp0=ms.map(e=>e.get('health').hp);R.blast=C.blast(w,h,m.x,m.y,80,5)===ms.length&&ms.every((e,i)=>e.get('health').hp===hp0[i]-5);
 // 피해 고치기 신호(2배)
 const off=g.signals.on('combat:before',ev=>{ev.amount*=2});const a=m.get('health').hp;C.hit(w,h,m,4);off();R.before=a-m.get('health').hp===8;
 // 느려짐: 같은 시간에 간 거리 비교
 h.x=m.x-120;h.y=m.y;g.loop.tick(30);const b1=m.get('brain').state;const x0=m.x;g.loop.tick(10);const d1=Math.abs(m.x-x0);m.get('status').slow=.5;m.get('status').slowT=5;const x1=m.x;h.x-=300;g.loop.tick(1);const x2=m.x;g.loop.tick(10);const d2=Math.abs(m.x-x2);R.chase=b1;R.slow=d2>0&&d2<d1*.7;R.d=[+d1.toFixed(1),+d2.toFixed(1)];
 // 기절: 움직이지 않고 공격하지 않음
 m.get('status').stun=1;const x3=m.x;g.loop.tick(30);R.stun=Math.abs(m.x-x3)<.01;
 // 돌아가기: 영웅이 멀리 가면 집으로 돌아가 체력 회복
 h.x=s.home[0];h.y=s.home[1];g.loop.tick(600);R.back=ms.map(e=>e.get('brain').state+':'+(e.get('health').hp===e.get('health').max));
 // 치유
 const hh=h.get('health');hh.hp=100;R.heal=C.heal(w,h,50)===50&&hh.hp===150;
 R.err=g.errors;return JSON.stringify(R)}));console.log('ERR',errs);await b.close()})();
