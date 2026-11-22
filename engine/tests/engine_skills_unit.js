const {chromium}=require('playwright');
// 기술·성장 부품 단위 시험
(async()=>{const b=await chromium.launch();const errs=[];const R={};
const open=async hero=>{const p=await b.newPage({viewport:{width:920,height:400}});p.on('pageerror',e=>errs.push(hero+':'+e.message));await p.goto('http://localhost:8765/engine/play.html?hero='+hero+'&'+Date.now());await p.waitForTimeout(1200);await p.evaluate(()=>__E.game.loop.stop());return p};
let p=await open('c_war');
R.war=await p.evaluate(()=>{const g=__E.game,s=g.scenes.top,h=s.hero,w=s.world,P=s.progress,f=h.get('fighter'),hp=h.get('health'),o={};
 o.why0=P.why('t_atk');o.why1=P.why('t_hp');o.why2=P.why('water');const d0=f.dmg,m0=hp.max;
 P.gain(7/2.6+.01);o.lv2=P.lv===2&&P.points()===1;o.grow=Math.abs(f.dmg/d0-1.15)<.01&&Math.abs(hp.max/m0-1.15)<.01;
 o.learn=P.learn('t_atk')&&P.rank('t_atk')===1&&Math.abs(f.dmg/d0-1.15*1.08)<.01;o.nopts=P.why('t_atk');
 P.lv=12;P.learn('t_hp');P.learn('t_shell');o.excl=P.why('t_regen');P.learn('t_smash');P.learn('t_leech');o.ultWhy=P.why('t_ult')==='';P.learn('t_ult');o.ult=h.get('caster').list.map(k=>k.id).join(',');
 // 방패 밀치기: 주변 적이 맞고 밀려나고 기절
 const ms=w.tagged('monster').filter(e=>e.camp===0);h.x=ms[0].x-30;h.y=ms[0].y;const hp1=ms[0].get('health').hp;o.cast=s.cast('smash');o.hit=ms[0].get('health').hp<hp1;o.stun=ms[0].get('status').stun>0&&ms[0].get('status').kx>0;o.cd=!s.cast('smash');
 // 받는 피해 감소(단단한 껍질 7%)
 const C0=hp.hp;hp.hp=hp.max;g.signals.emit('x');return o});
R.shell=await p.evaluate(async()=>{const C=await import('./src/combat.js');const s=__E.game.scenes.top,h=s.hero,m=s.world.tagged('monster')[5];const a=h.get('health').hp;C.hit(s.world,m,h,100);return a-h.get('health').hp});
R.save=await p.evaluate(()=>JSON.stringify(__E.game.scenes.top.progress.toJSON()));
R.reset=await p.evaluate(()=>{const P=__E.game.scenes.top.progress;P.reset();return P.spent()===0&&P.points()===11&&__E.game.scenes.top.hero.get('caster').list.length===1});await p.close();
p=await open('c_sum');
R.sum=await p.evaluate(()=>{const g=__E.game,s=g.scenes.top,h=s.hero,w=s.world,P=s.progress,o={};const ms=w.tagged('monster').filter(e=>e.camp===0);h.x=ms[0].x-140;h.y=ms[0].y;
 o.cast=s.cast('smash');o.n=w.tagged('summon').length;g.loop.tick(240);o.fought=w.tagged('monster').filter(e=>e.camp===0&&!e.get('health').down).length<3||ms.some(e=>e.get('health').hp<e.get('health').max);
 P.lv=8;P.learn('t_pal');P.learn('t_catch');P.learn('t_slot');g.loop.tick(60*10);o.gone=w.tagged('summon').length;h.get('caster').list[0].t=0;s.cast('smash');o.n3=w.tagged('summon').length;return o});await p.close();
p=await open('c_mag');
R.mag=await p.evaluate(()=>{const g=__E.game,s=g.scenes.top,h=s.hero,w=s.world,P=s.progress,o={};P.lv=6;P.learn('water');P.learn('t_ice');o.skills=h.get('caster').list.map(k=>k.id).join(',');const ms=w.tagged('monster').filter(e=>e.camp===0);h.x=ms[0].x-40;h.y=ms[0].y;const a=ms[0].get('health').hp;o.water=s.cast('water')&&ms[0].get('health').hp<a;o.ice=ms[0].get('status').stun>=.5;return o});await p.close();
p=await open('c_rog');
R.rog=await p.evaluate(()=>{const g=__E.game,s=g.scenes.top,h=s.hero,w=s.world,o={};const ms=w.tagged('monster').filter(e=>e.camp===0),m=ms.sort((a,b)=>a.x-b.x)[0];h.x=m.x-200;h.y=m.y;const a=m.get('health').hp;o.dash=s.cast('smash')&&Math.abs(h.x-m.x)<=21&&m.get('health').hp<a;return o});await p.close();
p=await open('c_arc');
R.arc=await p.evaluate(()=>{const g=__E.game,s=g.scenes.top,h=s.hero,w=s.world,o={};const ms=w.tagged('monster').filter(e=>e.camp===0);h.x=ms[0].x-200;h.y=ms[0].y;h.get('fighter').hold=true;s.cast('smash');g.loop.tick(40);o.volley=ms.filter(e=>e.get('health').hp<e.get('health').max||e.get('health').down).length;return o});
// 실제 손가락으로 기술 버튼 누르기
await p.evaluate(()=>{const g=__E.game;g.scenes.top.hero.get('caster').list[0].t=0;g.loop.start()});await p.waitForTimeout(300);const vp=p.viewportSize();await p.mouse.click(vp.width-56*vp.height/540,vp.height-60*vp.height/540);await p.waitForTimeout(300);R.tap=await p.evaluate(()=>__E.game.scenes.top.hero.get('caster').list[0].t>0);await p.screenshot({path:'shots/e5.jpg',type:'jpeg',quality:82});
console.log(JSON.stringify(R,null,1));console.log('ERR',errs);await b.close()})();
