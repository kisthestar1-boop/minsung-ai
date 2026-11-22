const {chromium}=require('playwright');
// 새 엔진 전투 시험: 자동 조종(가장 가까운 야영지 몬스터에게 걸어가 싸움)으로 90초
(async()=>{const b=await chromium.launch();const errs=[];
for(const hero of (process.argv[2]||'c_sum,c_war,c_arc,c_mag,c_rog').split(',')){const p=await b.newPage({viewport:{width:920,height:400},deviceScaleFactor:1});p.on('pageerror',e=>errs.push(hero+': '+e.message));p.on('console',m=>{if(m.type()==='error')errs.push(hero+': '+m.text())});
await p.goto('http://localhost:8765/engine/play.html?hero='+hero+'&'+Date.now());await p.waitForTimeout(1800);
const out=await p.evaluate(()=>{const g=__E.game,s=g.scenes.top,h=s.hero,w=s.world;g.loop.stop();const log=[];let first=null,firstCamp=null;const ev={};for(const n of ['combat:attack','combat:hit','combat:kill','camp:clear','ai:state'])g.signals.on(n,()=>ev[n]=(ev[n]||0)+1);
 for(let f=0;f<60*90;f++){const hp=h.get('health');const ms=w.tagged('monster').filter(e=>!e.get('health').down&&!e.tags.has('wild')&&e.camp===s.campLeft.findIndex(n=>n>0));let t=null,bd=1e9;for(const e of ms){const d=Math.hypot(e.x-h.x,(e.y-h.y)*1.4);if(d<bd){bd=d;t=e}}
  const r=h.get('fighter').range*.8;g.input.stick=(t&&bd>r&&!hp.down)?{id:9,ox:0,oy:0,dx:(t.x-h.x)/Math.hypot(t.x-h.x,t.y-h.y),dy:(t.y-h.y)/Math.hypot(t.x-h.x,t.y-h.y)}:null;g.loop.tick(1);
  if(first==null&&s.stats.kills>0)first=+(f/60).toFixed(1);if(firstCamp==null&&s.stats.camps>0)firstCamp=+(f/60).toFixed(1);
  if(f%1800===1799)log.push({t:(f+1)/60,...s.stats,hp:Math.round(hp.hp)})}
 return JSON.stringify({v:__E.VERSION,first,firstCamp,log,ev,ents:w.list.length,err:g.errors})});
console.log(hero,out);if(hero==='c_sum')await p.screenshot({path:'shots/e2_end.jpg',type:'jpeg',quality:82});await p.close()}
// 실제 시간으로 싸우는 장면 한 장
const p=await b.newPage({viewport:{width:920,height:400},deviceScaleFactor:2});p.on('pageerror',e=>errs.push(e.message));await p.goto('http://localhost:8765/engine/play.html?'+Date.now());await p.waitForTimeout(1500);
await p.evaluate(()=>{const g=__E.game,s=g.scenes.top,h=s.hero,m=s.world.tagged('monster').find(e=>e.camp===0);h.x=m.x-150;h.y=m.y+20;s.snap=true});await p.waitForTimeout(1300);await p.screenshot({path:'shots/e2_fight.jpg',type:'jpeg',quality:85});
console.log('ERR',errs.slice(0,5));await b.close()})();
