const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const errs=[];
// 새 엔진: 해안 맵에서 걷고 싸우기 60초
let p=await b.newPage({viewport:{width:920,height:400},deviceScaleFactor:2});p.on('pageerror',e=>errs.push('play:'+e.message));
await p.goto('http://localhost:8765/engine/play.html?map=coast&'+Date.now());await p.waitForTimeout(2000);await p.screenshot({path:'shots/coast_play.jpg',type:'jpeg',quality:80});
console.log(await p.evaluate(()=>{const g=__E.game,s=g.scenes.top,h=s.hero,w=s.world;g.loop.stop();for(let f=0;f<3600;f++){const hp=h.get('health');const ci=s.campLeft.findIndex(n=>n>0);const ms=w.tagged('monster').filter(e=>!e.get('health').down&&e.camp===ci);let t=null,bd=1e9;for(const e of ms){const d=Math.hypot(e.x-h.x,(e.y-h.y)*1.4);if(d<bd){bd=d;t=e}}const r=h.get('fighter').range*.8;g.input.stick=(t&&bd>r&&!hp.down)?{id:9,ox:0,oy:0,dx:(t.x-h.x)/Math.hypot(t.x-h.x,t.y-h.y),dy:(t.y-h.y)/Math.hypot(t.x-h.x,t.y-h.y)}:null;if(t&&bd<r*1.3)s.cast('smash');g.loop.tick(1)}return JSON.stringify({map:s.map.id,bg:s.bg.naturalWidth,...s.stats,lv:s.progress.lv,err:g.errors,fail:g.assets.failed})}));await p.close();
// 편집기: 맵 바꾸기 · 옮기기 · 저장 · 첫 맵은 그대로
p=await b.newPage({viewport:{width:1280,height:720}});p.on('pageerror',e=>errs.push('ed:'+e.message));await p.goto('http://localhost:8765/engine/?'+Date.now());await p.waitForTimeout(1200);
const n0=await p.evaluate(()=>document.querySelectorAll('#list .row').length);await p.click('[data-map="coast"]');await p.waitForTimeout(600);
const r=await p.evaluate(()=>({id:mapId,rows:document.querySelectorAll('#list .row').length,img:document.querySelector('#stage img.map').src.split('/').pop(),first:MP().camps[0].n,world:S.map.camps[0].n}));
await p.screenshot({path:'shots/ed_coast.jpg',type:'jpeg',quality:80});
await p.evaluate(()=>{setPos({t:'camp',i:0},.3,.75);save()});await p.waitForTimeout(500);const sv=await p.evaluate(()=>{const E=JSON.parse(localStorage.getItem('sprout_edit'));return [E.maps.coast.camps[0].fx,E.map.camps[0].fx]});
console.log(JSON.stringify({n0,r,sv}));console.log('ERR',errs);await b.close()})();
