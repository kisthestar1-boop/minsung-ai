/* ===== 새싹 엔진 · 내용 표 (data.js) =====
   게임 내용은 여기 표에 있고, 움직임·전투·화면은 index.html(엔진)에 있어요.
   새 캐릭터·기술·몬스터는 이 파일에 한 줄을 더하고 그림을 img/ 에 넣으면 돼요. */

/* 영웅 표 — 한 줄이 캐릭터 하나. n 이름, role 설명, hp 체력, dmg 공격, range 사거리, spd 속도, rate 공격 간격(초),
   shot 쏘는 공격, splash 범위, heal 치유, sk 고유 기술 종류, nw 새 그림, w4 걷기 4장 */
const HEROES={c_sum:{n:'소환사',role:'🐾 소환사 · 등불과 정령',hp:350,dmg:18,range:185,spd:64,rate:.82,shot:1,heal:20,hu:1,sk:'bunny',nw:1,w4:1},c_war:{n:'전사',role:'🛡 전사 · 둥근 방패',hp:580,dmg:23,range:40,spd:62,rate:.8,hu:1,sk:'sheep',nw:1},c_arc:{n:'궁수',role:'🏹 궁수 · 먼 거리',hp:320,dmg:22,range:215,spd:70,rate:.66,shot:1,hu:1,sk:'fox',nw:1},c_mag:{n:'마법사',role:'🔮 마법사 · 범위 마법',hp:300,dmg:24,range:195,spd:62,rate:1.05,splash:64,shot:1,hu:1,sk:'owl',nw:1},c_rog:{n:'도적',role:'🗡 도적 · 날쌘 발',hp:360,dmg:23,range:38,spd:86,rate:.5,hu:1,sk:'thief',nw:1},sprout:{n:'새싹',role:'균형 · 지팡이',hp:380,dmg:20,range:38,spd:62,rate:.8},frost:{n:'서리',role:'얼음 마법 · 범위',hp:300,dmg:19,range:190,spd:62,rate:1.05,splash:52,shot:1,hu:1},thief:{n:'도둑 까망',role:'번개 같은 단검',hp:370,dmg:23,range:38,spd:82,rate:.5,hu:1},baker:{n:'제빵사 모모',role:'치유 · 든든한 빵',hp:430,dmg:15,range:40,spd:60,rate:.85,heal:26,hu:1},fox:{n:'여우 궁수',role:'멀리서 쏘기',hp:290,dmg:15,range:205,spd:66,rate:.8,shot:1},sheep:{n:'양 방패병',role:'단단한 방패',hp:600,dmg:15,range:40,spd:56,rate:.9},hedgehog:{n:'고슴도치 검사',role:'빠른 돌격',hp:410,dmg:25,range:38,spd:72,rate:.6},owl:{n:'부엉이 마법사',role:'범위 마법',hp:270,dmg:19,range:195,spd:60,rate:1.15,splash:60,shot:1},bunny:{n:'토끼 치유사',role:'치유 · 지원',hp:330,dmg:15,range:190,spd:64,rate:.85,shot:1,heal:22},frog:{n:'개구리 응원단',role:'아군 강화',hp:400,dmg:16,range:40,spd:60,rate:.85,buff:1},knight:{n:'잎새 기사',role:'⚔ 전사 · 방패',hp:540,dmg:19,range:40,spd:60,rate:.85,hu:1,sj:1,sk:'sheep'},assassin:{n:'그림자 자객',role:'⚔ 암살 · 쌍단검',hp:340,dmg:26,range:38,spd:86,rate:.48,hu:1,sj:1,sk:'thief'},lancer:{n:'토끼 창기사',role:'⚔ 창 · 긴 찌르기',hp:410,dmg:22,range:60,spd:76,rate:.7,hu:1,sj:1,sk:'hedgehog'},bear:{n:'곰 망치 전사',role:'⚔ 묵직한 한 방',hp:660,dmg:30,range:44,spd:52,rate:1.25,hu:1,sj:1,sk:'sheep'},elf:{n:'엘프 명궁',role:'🏹 궁수 · 먼 거리',hp:290,dmg:17,range:220,spd:68,rate:.7,shot:1,hu:1,sj:1,sk:'fox'},raccoon:{n:'너구리 석궁병',role:'🏹 궁수 · 강한 한 발',hp:320,dmg:24,range:195,spd:62,rate:1.05,shot:1,hu:1,sj:1,sk:'fox'},mage:{n:'별빛 마법사',role:'✨ 마법 · 범위',hp:270,dmg:20,range:195,spd:60,rate:1.1,splash:60,shot:1,hu:1,sj:1,sk:'owl'},deer:{n:'사슴 사제',role:'✨ 치유 · 축복',hp:330,dmg:13,range:185,spd:62,rate:.85,shot:1,heal:24,hu:1,sj:1,sk:'bunny'},monk:{n:'판다 무도가',role:'⚔ 격투 · 빠른 주먹',hp:480,dmg:18,range:38,spd:74,rate:.5,hu:1,sj:1,sk:'hedgehog'},wolf:{n:'늑대 광전사',role:'⚔ 쌍도끼 · 돌격',hp:460,dmg:28,range:40,spd:78,rate:.6,hu:1,sj:1,sk:'thief'},turtle:{n:'거북 성기사',role:'⚔ 방패 · 아주 튼튼',hp:720,dmg:17,range:40,spd:48,rate:.95,hu:1,sj:1,sk:'sheep'},gunner:{n:'수달 총잡이',role:'🏹 총 · 가장 먼 거리',hp:280,dmg:28,range:230,spd:64,rate:1.2,shot:1,hu:1,sj:1,sk:'fox'},alch:{n:'두더지 연금술사',role:'✨ 물약 · 범위',hp:310,dmg:18,range:170,spd:60,rate:1,splash:55,shot:1,hu:1,sj:1,sk:'owl'},penguin:{n:'펭귄 얼음 마법사',role:'✨ 얼음 · 범위',hp:280,dmg:19,range:190,spd:60,rate:1.05,splash:50,shot:1,hu:1,sj:1,sk:'frost'},crow:{n:'까마귀 흑마법사',role:'✨ 저주 · 강한 한 발',hp:260,dmg:26,range:205,spd:62,rate:1.25,shot:1,hu:1,sj:1,sk:'owl'},bard:{n:'고양이 음유시인',role:'🎵 응원 · 치유',hp:300,dmg:14,range:180,spd:66,rate:.8,shot:1,heal:18,hu:1,sj:1,sk:'bunny'}};

/* 영웅 고유 기술 — [아이콘, 이름, 다시 쓰기까지 초] */
const HUS={c_sum:['🏮','정령 부르기',9],c_war:['🛡','방패 밀치기',5],c_arc:['🏹','연속 사격',4],c_mag:['✨','별빛 마법',7],c_rog:['💨','그림자 베기',4],frost:['❄','얼음 폭풍',6],thief:['🗡','그림자 베기',4],baker:['🥖','빵 나눔',6],fox:['🏹','연속 사격',4],sheep:['🛡','방패 밀치기',5],hedgehog:['🌀','가시 회전',4],owl:['☄','별똥별',7],bunny:['🥕','당근 치유',7],frog:['📣','힘내라 응원',12],knight:['🛡','방패 강타',5],assassin:['🗡','그림자 베기',4],lancer:['🌀','회전 창',4],bear:['🔨','대지 강타',5],elf:['🏹','세 발 화살',4],raccoon:['🎯','연발 석궁',4],mage:['☄','별똥별',7],deer:['🔔','축복의 종',7],monk:['👊','회전 발차기',4],wolf:['🪓','쌍도끼 베기',4],turtle:['🛡','빛의 방패',5],gunner:['💥','연발 사격',4],alch:['🧪','폭발 물약',7],penguin:['❄','얼음 폭풍',6],crow:['🔮','보랏빛 불꽃',7],bard:['🎵','응원의 노래',7]};

/* 카드 등급 — [이름, 진한 색, 연한 색] */
const RAR=[['일반','#8d949c','#dfe3e8'],['희귀','#3f86dc','#cfe3fb'],['영웅','#9a55dc','#e6d3fa'],['전설','#e89a20','#ffe6a8']];

/* 강한 야생 몬스터 — [이름, 체력, 공격, 사거리, 속도, 공격 간격, 키, 추가 능력] */
const WB=[['이끼 골렘',420,16,42,34,1.3,96,{}],['꿀단지 아기곰 왕',320,20,40,55,1,92,{}],['번개 구름양',220,18,200,45,1.3,84,{shot:1,splash:50}],['호박 기사',260,24,42,70,.8,84,{}],['수정 여우',200,22,210,80,1,90,{shot:1}],['아기 숲 용',380,26,150,50,1.2,98,{shot:1,splash:60}]];

/* 몬스터별 카드 등급 (0 일반 · 1 희귀 · 2 영웅 · 3 전설) */
const MCR={e0:0,e1:0,m1:0,e3:1,m0:1,m3:1,e2:2,m2:2,wb0:3,wb1:3,wb2:3,wb3:3,wb4:3,wb5:3};

/* 카드 도감 순서 (* 는 정예) */
const MCIDS=['e0','e1','m1','e3','m0','m3','e2','m2','e2*','m0*','wb0','wb1','wb2','wb3','wb4','wb5'];

/* 카드 ★ 단계에 필요한 장수 */
const STARN=[1,3,7,15,30];

/* 기술 표 — i 아이콘, n 이름, mx 최고 단계, v 한 단계마다의 수치, t 설명({v} 자리에 수치), lv 필요 레벨 */
const TRN={
 t_atk:{i:'🗡',n:'날카로운 일격',mx:5,v:8,t:'공격력 +{v}%'},
 t_hp:{i:'💚',n:'튼튼한 몸',mx:5,v:10,t:'체력 +{v}%'},
 t_smash:{i:'💥',n:'필살 숙련',mx:5,v:20,t:'고유 기술(큰 버튼) 피해 +{v}%'},
 t_crit:{i:'🎯',n:'치명타',mx:3,v:8,t:'우리 편 공격이 {v}% 확률로 2배'},
 t_haste:{i:'⚡',n:'연속기',mx:3,v:10,t:'모든 기술 대기 시간 -{v}%'},
 t_leech:{i:'💗',n:'승리의 기운',mx:3,v:3,t:'적을 쓰러뜨릴 때마다 체력 {v}% 회복'},
 t_ult:{i:'🌟',n:'폭풍의 핵',mx:3,lv:10,v:30,t:'폭풍(전직 기술) 피해 +{v}%'},
 water:{i:'💧',n:'물보라',mx:5,v:1,t:'주변 적 모두에게 마법 피해 · {v}단계'},
 t_surge:{i:'🌊',n:'거센 물결',mx:3,v:15,t:'마법·폭풍 피해 +{v}%'},
 t_ice:{i:'❄',n:'얼음 물결',mx:3,v:0.5,t:'마법에 맞은 적이 {v}초 얼어붙음'},
 t_echo:{i:'🔁',n:'메아리',mx:1,v:50,t:'물보라가 한 번 더 터짐 ({v}% 피해)'},
 t_catch:{i:'🃏',n:'포획술',mx:3,v:25,t:'몬스터 카드를 얻을 확률 +{v}%'},
 t_gold:{i:'🪙',n:'전리품',mx:3,v:1,t:'적을 쓰러뜨릴 때마다 금화 +{v}'},
 rain:{i:'🌿',n:'치유의 비',mx:5,v:1,t:'주변 아군 체력 회복 · {v}단계'},
 cheer:{i:'📣',n:'응원의 깃발',mx:5,v:12,t:'주변 아군 공격력 +{v}%'},
 t_shell:{i:'🛡',n:'단단한 껍질',mx:3,v:7,t:'받는 피해 -{v}%'},
 t_regen:{i:'🌱',n:'새싹 재생',mx:3,v:0.6,t:'1초마다 체력 {v}% 회복'},
 t_pal:{i:'🐾',n:'동료 지휘',mx:3,v:15,t:'동료의 공격·체력 +{v}%'},
 t_revive:{i:'🌸',n:'다시 피는 꽃',mx:1,v:60,t:'쓰러지면 {v}초에 한 번 바로 부활'},
 t_range:{i:'🏹',n:'매의 눈',mx:3,v:10,t:'공격이 닿는 거리 +{v}%'},
 t_spd:{i:'👟',n:'바람 걸음',mx:3,v:7,t:'이동 속도 +{v}%'},
 t_dodge:{i:'💨',n:'날쌘 몸',mx:3,v:8,t:'적의 공격을 {v}% 확률로 피함'},
 t_slot:{i:'➕',n:'셋째 동료',mx:1,v:3,t:'동료 칸이 {v}개로 늘어남'}
};
/* 기술 아이콘 그림(skill_icons.webp, 가로 6칸) 순서 */
const ICK=['t_atk','t_hp','t_smash','t_crit','t_haste','t_leech','t_ult','water','t_surge','t_ice','t_echo','t_catch','t_gold','rain','cheer','t_shell','t_regen','t_pal','t_revive','t_range','t_spd','t_dodge','t_slot','lantern'];
/* 단계 r 일 때의 설명과 값 — v 는 한 단계마다 늘어나는 수치 */
function trDesc(k,r){const n=TRN[k],one=(k==='t_revive'||k==='t_echo'||k==='t_slot'),x=one?n.v:Math.round(n.v*r*100)/100;return n.t.replace('{v}',x)}
/* 직업: [기술, 줄, 칸(-1~1), 먼저 배울 것(하나만 있으면 됨), 둘 중 하나] */
const TRJ={
 war:{i:'🛡',n:'전사',col:'#d9603a',lt:'#fde3d6',p:'앞에서 버티고 크게 때려요',t:[['t_atk',0,0],['t_hp',1,-1,['t_atk']],['t_smash',1,1,['t_atk']],['t_shell',2,-1,['t_hp'],'t_regen'],['t_regen',2,0,['t_hp'],'t_shell'],['t_leech',2,1,['t_smash']],['t_revive',3,-.5,['t_shell','t_regen']],['t_ult',3,1,['t_leech']],['cheer',4,0,['t_revive','t_ult']]]},
 arc:{i:'🏹',n:'궁수',col:'#3fa554',lt:'#dcf3df',p:'멀리서 빠르게 쏴요',t:[['t_atk',0,0],['t_range',1,-1,['t_atk']],['t_spd',1,1,['t_atk']],['t_crit',2,-1,['t_range'],'t_haste'],['t_haste',2,0,['t_range'],'t_crit'],['t_gold',2,1,['t_spd']],['t_smash',3,-.5,['t_crit','t_haste']],['t_leech',3,1,['t_gold']],['t_ult',4,0,['t_smash','t_leech']]]},
 mag:{i:'🔮',n:'마법사',col:'#3a8fd9',lt:'#d9ecfc',p:'넓게 터뜨리고 얼려요',t:[['water',0,0],['t_surge',1,-1,['water'],'t_ice'],['t_ice',1,1,['water'],'t_surge'],['t_echo',2,0,['t_surge','t_ice']],['t_haste',3,-1,['t_echo']],['rain',3,1,['t_echo']],['t_smash',4,-1,['t_haste']],['t_hp',4,1,['rain']],['t_ult',5,0,['t_smash','t_hp']]]},
 rog:{i:'🗡',n:'도적',col:'#7a55c9',lt:'#e7defa',p:'빠르게 찌르고 훔쳐요',t:[['t_spd',0,0],['t_crit',1,-1,['t_spd']],['t_gold',1,1,['t_spd']],['t_dodge',2,-1,['t_crit'],'t_leech'],['t_leech',2,0,['t_crit'],'t_dodge'],['t_catch',2,1,['t_gold']],['t_smash',3,-.5,['t_dodge','t_leech']],['t_haste',3,1,['t_catch']],['t_ult',4,0,['t_smash','t_haste']]]},
 sum:{i:'🐾',n:'소환사',col:'#d99a20',lt:'#fbeecb',p:'몬스터 동료와 함께 싸워요',t:[['t_pal',0,0],['t_catch',1,-1,['t_pal']],['rain',1,1,['t_pal']],['t_slot',2,-1,['t_catch']],['cheer',2,1,['rain']],['t_hp',3,-1,['t_slot'],'t_regen'],['t_regen',3,0,['t_slot'],'t_hp'],['t_revive',3,1,['cheer']],['t_ult',4,0,['t_hp','t_regen','t_revive']]]}
};
const TRREC={c_sum:'sum',c_war:'war',c_arc:'arc',c_mag:'mag',c_rog:'rog',sprout:'sum',frost:'mag',thief:'rog',baker:'sum',fox:'arc',sheep:'war',hedgehog:'war',owl:'mag',bunny:'sum',frog:'sum',knight:'war',assassin:'rog',lancer:'war',bear:'war',elf:'arc',raccoon:'arc',mage:'mag',deer:'sum',monk:'war',wolf:'war',turtle:'war',gunner:'arc',alch:'mag',penguin:'mag',crow:'mag',bard:'sum'};

/* 모험 지도 — home 시작점, npc 마을 사람, camps 야영지(퀘스트 순서대로), wild 강한 야생 몬스터
   위치는 지도 그림 기준 비율(0~1). fx 가로, row 세로. ks 몬스터 구성, el 정예, m 세기, boss 마지막 보스 */
const RPGMAP={home:[.105,.86],npc:[.145,.8],
 camps:[{n:'밀밭 허수아비',fx:.155,row:.54,ks:['e0','e0','e1'],m:.7},{n:'버섯 숲 빈터',fx:.31,row:.27,ks:['e1','e1','e3'],m:.95},{n:'호숫가 선착장',fx:.385,row:.66,ks:['e0','e3'],el:'e2',m:1.2},{n:'오아시스 유적',fx:.6,row:.82,ks:['e3','e3','m1','m1'],m:1.5},{n:'협곡 붉은 다리',fx:.5,row:.3,ks:['m1','m1'],el:'m0',m:1.8},{n:'유령 늪',skin:'gh_',fx:.8,row:.5,ks:['m2','m3','m3'],m:2.15},{n:'화산 기슭',skin:'lv_',fx:.79,row:.8,ks:['m2','m2','m1'],el:'m0',m:2.5},{n:'눈 덮인 소나무 숲',fx:.72,row:.24,ks:['m3','m3'],el:'e2',m:2.9},{n:'서리의 얼음 성',fx:.855,row:.16,boss:1,ks:[],m:1}],
 wild:[{k:'wb0',fx:.348,row:.335,ci:1},{k:'wb1',fx:.493,row:.87,ci:2},{k:'wb2',fx:.55,row:.43,ci:3},{k:'wb3',fx:.65,row:.53,ci:4},{k:'wb4',fx:.795,row:.52,ci:5},{k:'wb5',fx:.755,row:.65,ci:6}]};
/* 맵 목록 (새 엔진용) — 첫 맵은 위의 RPGMAP 그대로. 새 맵은 여기에 한 덩어리씩 추가 (bg 배경 그림 이름) */
/* gates 관문: 다른 맵으로 가는 길 (to 가는 맵, lv 권장 레벨). 여정 = 큰 맵 여러 개가 관문으로 이어진 것 */
const MAPS=[Object.assign(RPGMAP,{id:'world',n:'새싹 마을 들판',bg:'bg_world',gates:[{fx:.955,row:.62,to:'coast',n:'별빛 해안',lv:6}]}),
 {id:'coast',n:'별빛 해안',bg:'bg_coast',home:[.17,.66],npc:[.2,.7],gates:[{fx:.085,row:.66,to:'world',n:'새싹 마을 들판',lv:1},{fx:.3,row:.33,to:'highland',n:'구름 고원',lv:12}],
  camps:[{n:'조개 모래밭',fx:.29,row:.76,ks:['e0','e1','e1'],m:1},{n:'산호 웅덩이',fx:.43,row:.655,ks:['e1','e3','e3'],m:1.3},{n:'야자수 숲',fx:.565,row:.69,ks:['e3','m1'],el:'e2',m:1.6},{n:'난파선 만',fx:.67,row:.72,ks:['m1','m1','m3'],m:2},{n:'분홍 꽃 들판',fx:.58,row:.49,ks:['m3','m3'],el:'m0',m:2.4},{n:'폭포 아래',fx:.455,row:.47,ks:['m2','m3','m3'],m:2.8},{n:'빛나는 버섯 동굴',fx:.61,row:.345,ks:['m2','m2','m1'],el:'m0',m:3.2},{n:'수정 등대 섬',fx:.82,row:.26,boss:1,ks:[],m:1}],
  wild:[{k:'wb1',fx:.36,row:.62,ci:1},{k:'wb3',fx:.52,row:.56,ci:4},{k:'wb5',fx:.7,row:.42,ci:6}]},
 {id:'highland',n:'구름 고원',bg:'bg_highland',home:[.13,.78],npc:[.17,.83],gates:[{fx:.05,row:.87,to:'coast',n:'별빛 해안',lv:6}],
  camps:[{n:'계단식 차밭',fx:.305,row:.69,ks:['e1','e1','e3'],m:1.6},{n:'흔들다리 앞',fx:.4,row:.66,ks:['e3','m1','m1'],m:2},{n:'민들레 언덕',fx:.46,row:.42,ks:['m1','m3'],el:'e2',m:2.4},{n:'떠 있는 돌 유적',fx:.65,row:.56,ks:['m3','m3','m2'],m:2.9},{n:'김 나는 온천',fx:.705,row:.44,ks:['m2','m2'],el:'m0',m:3.4},{n:'바람 솔숲',fx:.668,row:.25,ks:['m2','m3','m3'],m:3.9},{n:'눈길',fx:.8,row:.24,ks:['m3','m3','m1'],el:'m0',m:4.4},{n:'하늘 신전',fx:.86,row:.16,boss:1,ks:[],m:1}],
  wild:[{k:'wb2',fx:.53,row:.55,ci:3},{k:'wb4',fx:.6,row:.36,ci:5}]}];
/* 일반 몬스터 이름과 그림 (편집기용) */
const MONINFO={e0:['시든 새싹','sprite_e0'],e1:['가시 덤불','sprite_e1'],e2:['졸린 독버섯','sprite_e2'],e3:['그림자 도깨비불','sprite_e3'],m0:['투덜 진흙이','m_e0'],m1:['따끔 잠자리','m_e1'],m2:['삐죽 부들이','m_e2'],m3:['등불 유령','m_e3']};
/* 일반 몬스터 능력치 (새 엔진용) — hp 체력, dmg 공격, range 사거리, spd 속도, rate 공격 간격(초), shot 쏘는 공격 */
const MONSTAT={e0:{hp:50,dmg:6,range:36,spd:50,rate:1},e1:{hp:40,dmg:8,range:30,spd:95,rate:.9},e2:{hp:150,dmg:7,range:40,spd:35,rate:1.2},e3:{hp:45,dmg:8,range:205,spd:45,rate:1.3,shot:1},m0:{hp:110,dmg:10,range:38,spd:45,rate:1.1},m1:{hp:60,dmg:11,range:34,spd:100,rate:.8},m2:{hp:70,dmg:11,range:210,spd:40,rate:1.4,shot:1},m3:{hp:70,dmg:12,range:205,spd:50,rate:1.3,shot:1}};
/* 기술 동작 표 (새 엔진용) — k 동작 종류, 나머지는 그 동작의 숫자. mul 은 공격력의 몇 배, r 범위, cd 대기(초)
   동작 종류: summon 소환 · bash 주변 밀치기 · volley 여러 발 · nova 먼 곳 폭발 · dash 순간 베기 · burst 내 주변 폭발 · mend 주변 치유 */
const SKILLDEF={c_sum:{k:'summon',n:2,life:13,hp:.3,dmg:.7,heal:.08,img:'spirit'},c_war:{k:'bash',r:84,mul:1.5,knock:150,stun:.6,heal:.12},c_arc:{k:'volley',n:3,r:250,mul:2},c_mag:{k:'nova',range:270,r:118,mul:2.6,magic:1},c_rog:{k:'dash',range:250,mul:3.4,heal:.1},
 water:{k:'burst',r:115,mul:.9,per:.35,cd:6,magic:1},rain:{k:'mend',r:160,heal:.06,per:.03,cd:9},storm:{k:'burst',r:170,mul:3.2,cd:20,magic:1,ult:1}};
/* 야영지 세기 규칙 (새 엔진용) — 표의 능력치에 곱하는 값. m 은 야영지마다의 세기. elFrom 번째 야영지부터 정예가 더 세다 */
const CAMPRULE={hp:1.8,dmg:1.2,elHp:[1.9,3.2],elDmg:[1.25,1.5],elFrom:4,xp:1,elXp:4,wildHp:2.1,wildDmg:1.2,wildXp:4};
/* 성장 규칙 (새 엔진용) — cap 최고 레벨, need 다음 레벨까지 경험치 = a + 레벨×b, grow 레벨마다 공격·체력 배수, early 처음 레벨의 경험치 배수 */
const GROW={cap:40,a:4,b:3,grow:1.15,early:[0,2.6,1.9,1.4],ultLv:10};
/* 편집기(새싹 엔진)에서 고친 내용 덮어쓰기 — 이 기기에 저장된 편집 내용이 있으면 표에 반영 */
(function(){let E=null;try{E=JSON.parse(localStorage.getItem('sprout_edit')||'null')}catch(e){}if(!E||E.v!==1)return;window.__EDIT=E;
 if(E.map){for(const k of ['home','npc','camps','wild','gates'])if(E.map[k])RPGMAP[k]=E.map[k]}
 if(E.maps){for(const M of MAPS){const o=E.maps[M.id];if(o)for(const k of ['home','npc','camps','wild','gates'])if(o[k])M[k]=o[k]}}
 if(E.heroes)for(const k in E.heroes)if(HEROES[k])Object.assign(HEROES[k],E.heroes[k]);
 if(E.trn)for(const k in E.trn)if(TRN[k])Object.assign(TRN[k],E.trn[k]);
 if(E.hus)for(const k in E.hus)if(HUS[k])HUS[k]=E.hus[k];
 if(E.trj)for(const k in E.trj)if(TRJ[k]&&Array.isArray(E.trj[k].t))TRJ[k].t=E.trj[k].t;
 if(E.wb)E.wb.forEach((w,i)=>{if(WB[i]&&w)for(let j=0;j<7;j++)if(w[j]!=null)WB[i][j]=w[j]})})();
