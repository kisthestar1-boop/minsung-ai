const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:920,height:400},isMobile:true,hasTouch:true,deviceScaleFactor:2});const errs=[];p.on('pageerror',e=>errs.push(e.message));p.on('console',m=>{if(m.type()==='error')errs.push(m.text())});
await p.goto('http://localhost:8765/engine/play.html?'+Date.now());await p.waitForTimeout(2500);
const st=()=>p.evaluate(()=>{const g=__E.game,s=g.scenes.top,h=s.hero;return JSON.stringify({v:__E.VERSION,scene:s.name,ents:s.world.list.length,hero:[Math.round(h.x),Math.round(h.y)],state:h.get('sprite').state,frames:g.loop.frames,failed:g.assets.failed,err:g.errors})});
console.log(await st());await p.screenshot({path:'shots/e1a.jpg',type:'jpeg',quality:82});
// 실제 손가락으로 끌기
await p.mouse.move(200,250);await p.mouse.down();await p.mouse.move(260,225,{steps:5});await p.waitForTimeout(1500);console.log(await st());await p.screenshot({path:'shots/e1b.jpg',type:'jpeg',quality:82});await p.mouse.up();await p.waitForTimeout(400);console.log(await st());
// 시험용 시간 넘기기: 오른쪽으로 10초 걷기
console.log(await p.evaluate(()=>{const g=__E.game;g.loop.stop();g.input.stick={id:9,ox:0,oy:0,dx:1,dy:-.3};const t0=performance.now();g.loop.tick(600);return JSON.stringify({ms:Math.round(performance.now()-t0),hero:[Math.round(g.scenes.top.hero.x),Math.round(g.scenes.top.hero.y)]})}));
await p.screenshot({path:'shots/e1c.jpg',type:'jpeg',quality:82});console.log('ERR',errs.slice(0,4));await b.close()})();
