const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:900,height:400},isMobile:true,hasTouch:true,deviceScaleFactor:2});const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.goto('http://localhost:8765/sprout/?'+Date.now());await p.evaluate(()=>localStorage.clear());await p.reload();await p.waitForTimeout(2500);
const play=(n)=>p.evaluate((n)=>{const D=__G.DU;let k=0;while(k++<n){if(D.pick)__G.duelPick(0);const u=D.H[1].u;if(u){const es=D.units.filter(o=>o.side<0&&o.hp>0);let t=null,bd=1e9;for(const o of es){const d=Math.hypot(o.x-u.x,o.y-u.y);if(d<bd){bd=d;t=o}}if(t&&bd>40){D.stick={ox:1,oy:1,dx:(t.x-u.x)/bd,dy:(t.y-u.y)/bd}}else{D.stick=null;if(t&&!(u.skT.smash>0))__G.cast('smash');else if(t&&D.H[1].sk.water&&!(u.skT.water>0))__G.cast('water')}}__G.tick(1,33)}const u=D.H[1].u;return JSON.stringify({lv:D.H[1].lv,pts:__G6.trPts(),sk:D.H[1].sk,tr:D.H[1].tr,kills:D.kills,mc:__G.SV.mc,pals:__G.SV.pals,pity:__G.SV.cpity,palU:D.units.filter(x=>x.pal).map(x=>x.k+(x.mon?'(M)':'')+Math.round(x.hp)),hp:u&&Math.round(u.hp)+'/'+Math.round(u.hpMax),dmg:u&&Math.round(u.dmg),pick:!!D.pick})},n);
await p.evaluate(()=>{__G.newRun('village');__G.scene='play';__G.startDuel();__G.duelMode('rpg');__G.tick(60,33)});
console.log(await play(900));await p.screenshot({path:'/tmp/sprout_test_a1.jpg',type:'jpeg',quality:80});
// 스킬 배우기
console.log(await p.evaluate(()=>{const r=[];for(const k of ['t_atk','water','t_smash','t_surge','t_ice','rain','t_hp'])r.push(k+':'+__G6.trLearn(k));return r.join(' ')}));
await p.evaluate(()=>{__G.DU.treeOpen=1;__G.DU.trSel='t_ice';__G.tick(2,33)});await p.screenshot({path:'/tmp/sprout_test_tree.jpg',type:'jpeg',quality:85});
await p.evaluate(()=>{__G.DU.treeOpen=0;__G6.mcGive('e2*',300,300);__G6.mcGive('e0');__G6.mcGive('e0');__G6.mcGive('e0');__G6.mcGive('m3');__G.tick(8,33)});await p.screenshot({path:'/tmp/sprout_test_cap.jpg',type:'jpeg',quality:85});
await p.evaluate(()=>{__G.DU.cardOpen=1;__G.DU.mcSel='e2*';__G.tick(2,33)});await p.screenshot({path:'/tmp/sprout_test_cards.jpg',type:'jpeg',quality:85});
await p.evaluate(()=>{__G.DU.mcSel='m2';__G.tick(2,33)});await p.screenshot({path:'/tmp/sprout_test_cards2.jpg',type:'jpeg',quality:85});
await p.evaluate(()=>{__G.DU.cardOpen=0;__G.tick(3,33)});
console.log(await play(1500));await p.screenshot({path:'/tmp/sprout_test_a2.jpg',type:'jpeg',quality:80});
// 저장 후 다시 시작
console.log(await p.evaluate(()=>{__G.startDuel();__G.duelMode('rpg');__G.tick(30,33);const D=__G.DU;return JSON.stringify({lv:D.H[1].lv,tr:D.H[1].tr,sk:D.H[1].sk,pts:__G6.trPts(),pal:D.units.filter(x=>x.pal).map(x=>x.k+(x.mon?'(M)':''))})}));
// 다른 모드
for(const m of ['hero','luck','grow','lol']){console.log(m,await p.evaluate((m)=>{__G.startDuel();__G.duelMode(m);__G.tick(200,33);const D=__G.DU;return JSON.stringify({mode:D.mode,pal:D.units.filter(x=>x.pal).map(x=>x.k+(x.mon?'(M)':'')),n:D.units.length})},m));await p.screenshot({path:'/tmp/sprout_test_m_'+m+'.jpg',type:'jpeg',quality:70})}
console.log('ERR',errs.slice(0,5));await b.close()})();
