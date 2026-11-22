const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:920,height:400},isMobile:true,hasTouch:true,deviceScaleFactor:2});const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.goto('http://localhost:8765/sprout/?'+Date.now());await p.evaluate(()=>localStorage.clear());await p.reload();await p.waitForTimeout(3500);
await p.evaluate(()=>{__G.newRun('village');__G.scene='play';__G.startDuel();__G.duelMode('rpg');__G.tick(30,33)});await p.waitForTimeout(1500);
console.log(await p.evaluate(()=>{__G.startDuel();__G.duelMode('rpg');__G.tick(60,33);const D=__G.DU;return JSON.stringify({wild:D.wild.map(w=>[w.k,Math.round(w.x),Math.round(w.y)]),alive:D.units.filter(u=>u.wild!=null).length})}));
// 영웅을 첫 야생 보스 옆으로
await p.evaluate(()=>{const D=__G.DU,w=D.units.find(u=>u.wild===0),h=D.H[1].u;h.x=w.x-70;h.y=w.y+10;D.units.filter(u=>u.pal).forEach(u=>{u.x=h.x-20;u.y=h.y});__G.cast('smash');__G.tick(50,33)});
await p.screenshot({path:'/tmp/sprout_test_wild1.jpg',type:'jpeg',quality:86});
console.log(await p.evaluate(()=>{const D=__G.DU;let n=0;for(let j=0;j<6;j++){for(let t=0;t<12;t++){const w=D.units.find(u=>u.wild===j&&u.hp>0);if(w){__G6.mcKill(w);w.hp=0;__G.tick(3,33)}D.wild[j].t=60;__G.tick(3,33)}}return JSON.stringify({mc:__G.SV.mc,pity:__G.SV.cpity,pals:__G.SV.pals})}));
await p.evaluate(()=>{__G.DU.capShow=null;__G.DU.cardOpen=1;__G.DU.mcSel='wb5';__G.tick(3,33)});await p.screenshot({path:'/tmp/sprout_test_cards3.jpg',type:'jpeg',quality:86});
console.log('ERR',errs.slice(0,5));await b.close()})();
