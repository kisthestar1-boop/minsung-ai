const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const errs=[];const p=await b.newPage({viewport:{width:1280,height:720}});p.on('pageerror',e=>errs.push(e.message));
await p.goto('http://localhost:8765/engine/?'+Date.now());await p.waitForTimeout(1200);await p.evaluate(()=>localStorage.removeItem('sprout_edit'));await p.reload();await p.waitForTimeout(1200);
await p.click('[data-map="coast"]');await p.waitForTimeout(400);await p.click('#list .row[data-t="gate"][data-i="1"]');await p.waitForTimeout(400);
const ins=await p.evaluate(()=>document.querySelector('#insp h2').textContent);
const mk=await p.$('.mk[data-t="gate"][data-i="1"]');const bb=await mk.boundingBox();await p.mouse.move(bb.x+bb.width/2,bb.y+bb.height/2);await p.mouse.down();await p.mouse.move(bb.x+60,bb.y+30,{steps:5});await p.mouse.up();await p.waitForTimeout(500);
await p.evaluate(()=>{const r=document.querySelector('[data-f="glv"]');r.value=9;r.dispatchEvent(new Event('input',{bubbles:true}))});await p.waitForTimeout(500);
const sv=await p.evaluate(()=>JSON.parse(localStorage.getItem('sprout_edit')).maps.coast.gates[1]);await p.screenshot({path:'shots/ed_gate.jpg',type:'jpeg',quality:78});
// 저장한 관문이 엔진에 반영되는지
await p.goto('http://localhost:8765/engine/play.html?map=coast&'+Date.now());await p.waitForTimeout(1500);const eg=await p.evaluate(()=>__E.game.scenes.top.map.gates[1]);
await p.evaluate(()=>localStorage.removeItem('sprout_edit'));
console.log(JSON.stringify({ins,sv,eg}));console.log('ERR',errs);await b.close()})();
