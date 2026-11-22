const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const errs=[];const p=await b.newPage({viewport:{width:920,height:400},deviceScaleFactor:2});p.on('pageerror',e=>errs.push(e.message));
await p.goto('http://localhost:8765/engine/play.html?'+Date.now());await p.waitForTimeout(1800);
const a=await p.evaluate(()=>{const s=__E.game.scenes.top,q=s.gates[0];s.progress.lv=7;s.progress.learn('t_pal');s.hero.x=q.x-40;s.hero.y=q.y;s.snap=true;return [s.map.id,s.gates.length]});await p.waitForTimeout(700);await p.screenshot({path:'shots/tv1.jpg',type:'jpeg',quality:80});
const vp=p.viewportSize();await p.mouse.click(vp.width/2,vp.height-44*vp.height/540);await p.waitForTimeout(1600);
const c=await p.evaluate(()=>{const s=__E.game.scenes.top;return {map:s.map.id,lv:s.progress.lv,tr:s.progress.tr,nearGate:Math.abs(s.hero.x-s.gates[0].x)<=81,bg:s.bg.naturalWidth,err:__E.game.errors}});await p.screenshot({path:'shots/tv2.jpg',type:'jpeg',quality:80});
// 돌아가기
await p.evaluate(()=>{const s=__E.game.scenes.top;s.travel(s.gates[0].q)});await p.waitForTimeout(1200);const d=await p.evaluate(()=>{const s=__E.game.scenes.top;return [s.map.id,s.progress.lv]});
console.log(JSON.stringify({a,c,d}));console.log('ERR',errs);await b.close()})();
