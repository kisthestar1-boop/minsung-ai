const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const errs=[];const p=await b.newPage({viewport:{width:920,height:400},deviceScaleFactor:2});p.on('pageerror',e=>errs.push(e.message));
await p.goto('http://localhost:8765/engine/play.html?'+Date.now());await p.waitForTimeout(1600);const vp=p.viewportSize(),k=vp.height/540;
const W=await p.evaluate(()=>__E.game.r.W);
await p.mouse.click((W-65)*k,28*k);await p.waitForTimeout(700);const a=await p.evaluate(()=>[__E.game.scenes.top.constructor.name,__E.game.scenes.stack.length]);await p.screenshot({path:'shots/jn1.jpg',type:'jpeg',quality:80});
// 못 가 본 맵은 눌러도 이동 안 함
const lock=await p.evaluate(()=>{const g=__E.game;g.input.taps=[];return g.input.buttons.length});
await p.mouse.click(W/2*k,(540-44)*k);await p.waitForTimeout(400);const c=await p.evaluate(()=>__E.game.scenes.top.constructor.name);
// 해안에 다녀온 뒤에는 빠른 이동 가능
await p.evaluate(()=>{const s=__E.game.scenes.top;s.travel(s.gates[0].q)});await p.waitForTimeout(1200);await p.mouse.click((W-65)*k,28*k);await p.waitForTimeout(600);
const d=await p.evaluate(()=>{const g=__E.game,j=g.scenes.top;return {top:j.constructor.name,seen:j.seen,cur:j.p.cur,btns:g.input.buttons.length}});await p.screenshot({path:'shots/jn2.jpg',type:'jpeg',quality:80});
await p.evaluate(()=>{const j=__E.game.scenes.top;j.go(__E.game.data.MAPS[0])});await p.waitForTimeout(900);const e=await p.evaluate(()=>[__E.game.scenes.top.map.id,__E.game.scenes.stack.length,__E.game.errors]);
console.log(JSON.stringify({a,lock,c,d,e}));console.log('ERR',errs);await b.close()})();
