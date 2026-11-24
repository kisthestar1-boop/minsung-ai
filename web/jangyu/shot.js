const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();
for(const s of process.argv.slice(2)){const p=await b.newPage({viewport:{width:1440,height:900}});await p.goto('file://'+process.cwd()+'/'+s+'/index.html',{waitUntil:'networkidle'}).catch(()=>{});await p.waitForTimeout(800);await p.screenshot({path:'/tmp/claude-0/'+s+'.jpg',type:'jpeg',quality:70,fullPage:true});
const m=await b.newPage({viewport:{width:390,height:844},deviceScaleFactor:1});await m.goto('file://'+process.cwd()+'/'+s+'/index.html',{waitUntil:'networkidle'}).catch(()=>{});await m.waitForTimeout(500);await m.screenshot({path:'/tmp/claude-0/'+s+'_m.jpg',type:'jpeg',quality:70});}
await b.close()})()
