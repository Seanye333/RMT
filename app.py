import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="来自你的谭小护的爱心波波",
    page_icon="💖",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Hide Streamlit chrome so the full page looks like the standalone site
st.markdown("""
<style>
  #root > div:first-child { padding: 0 !important; }
  .stApp { background: transparent !important; }
  header[data-testid="stHeader"]      { display: none !important; }
  section[data-testid="stSidebar"]    { display: none !important; }
  .block-container                    { padding: 0 !important; max-width: 100% !important; }
  footer                              { display: none !important; }
</style>
""", unsafe_allow_html=True)

HTML = """<!DOCTYPE html>
<html lang="zh">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=Dancing+Script:wght@400;700&family=Lato:wght@300;400&display=swap" rel="stylesheet" />
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    :root {
      --pink:    #f9a8d4;
      --lavender:#c4b5fd;
      --gold:    #fbbf24;
      --surface: rgba(255,255,255,0.06);
      --border:  rgba(255,255,255,0.12);
    }
    html, body {
      min-height: 100vh;
      background: radial-gradient(ellipse at 30% 0%, #2d1b69 0%, #0f0720 60%);
      font-family: 'Lato', sans-serif;
      color: #ede9fe;
      overflow-x: hidden;
    }
    #bg-canvas { position: fixed; inset: 0; pointer-events: none; z-index: 0; }
    #hearts-container { position: fixed; inset: 0; pointer-events: none; z-index: 1; overflow: hidden; }
    .heart {
      position: absolute; bottom: -60px; animation: floatUp linear infinite;
      opacity: 0; user-select: none;
    }
    @keyframes floatUp {
      0%   { transform: translateY(0) rotate(0deg) scale(0.6); opacity: 0; }
      10%  { opacity: 0.7; }
      90%  { opacity: 0.4; }
      100% { transform: translateY(-110vh) rotate(25deg) scale(1.1); opacity: 0; }
    }
    main {
      position: relative; z-index: 2;
      display: flex; flex-direction: column; align-items: center;
      padding: 60px 20px 100px;
    }
    header { text-align: center; margin-bottom: 56px; animation: fadeDown 1.2s ease both; }
    header .pre-title {
      font-family: 'Dancing Script', cursive; font-size: 1.2rem;
      color: var(--pink); letter-spacing: 0.15em; margin-bottom: 12px;
    }
    header h1 {
      font-family: 'Playfair Display', serif;
      font-size: clamp(2.4rem, 6vw, 4.5rem); font-style: italic;
      background: linear-gradient(135deg, var(--pink) 0%, var(--lavender) 50%, var(--gold) 100%);
      -webkit-background-clip: text; -webkit-text-fill-color: transparent;
      background-clip: text; line-height: 1.15;
    }
    header .divider {
      margin: 20px auto; width: 80px; height: 2px;
      background: linear-gradient(90deg, transparent, var(--gold), transparent);
    }
    .letter-card {
      background: var(--surface); border: 1px solid var(--border);
      backdrop-filter: blur(18px); -webkit-backdrop-filter: blur(18px);
      border-radius: 24px; max-width: 680px; width: 100%; padding: 52px 48px;
      box-shadow: 0 0 80px rgba(196,181,253,0.08), 0 8px 32px rgba(0,0,0,0.4);
      animation: fadeUp 1.4s ease 0.3s both;
    }
    .letter-card .salutation {
      font-family: 'Dancing Script', cursive; font-size: 1.7rem;
      color: var(--pink); margin-bottom: 28px;
    }
    .letter-card p {
      font-family: 'Playfair Display', serif; font-size: 1.05rem;
      line-height: 1.9; color: #ede9fe; margin-bottom: 20px;
      opacity: 0; transform: translateY(12px);
      transition: opacity 0.7s ease, transform 0.7s ease;
    }
    .letter-card p.visible { opacity: 1; transform: none; }
    .letter-card .signature {
      font-family: 'Dancing Script', cursive; font-size: 1.5rem;
      color: var(--gold); margin-top: 32px; text-align: right;
    }
    .proposal { margin-top: 64px; text-align: center; animation: fadeUp 1.4s ease 0.8s both; }
    .proposal h2 {
      font-family: 'Dancing Script', cursive;
      font-size: clamp(2rem, 5vw, 3.4rem); color: var(--pink);
      margin-bottom: 8px; text-shadow: 0 0 40px rgba(249,168,212,0.5);
    }
    .proposal .sub { font-size: 0.95rem; color: var(--lavender); margin-bottom: 40px; letter-spacing: 0.05em; }
    .proposal-buttons { display: flex; gap: 20px; justify-content: center; flex-wrap: wrap; }
    .btn {
      font-family: 'Lato', sans-serif; font-size: 1.05rem; font-weight: 400;
      letter-spacing: 0.08em; padding: 16px 44px; border-radius: 50px;
      border: none; cursor: pointer;
      transition: transform 0.25s ease, box-shadow 0.25s ease;
      user-select: none;
    }
    .btn-yes {
      background: linear-gradient(135deg, #f9a8d4, #c084fc);
      color: #1e0a3c; box-shadow: 0 0 24px rgba(249,168,212,0.4);
    }
    .btn-yes:hover { transform: scale(1.07); box-shadow: 0 0 40px rgba(249,168,212,0.7); }
    .btn-no { background: transparent; color: #a78bfa; border: 1.5px solid #a78bfa; }
    .btn-no:hover { transform: scale(0.92); opacity: 0.6; }
    #celebration {
      display: none; position: fixed; inset: 0; z-index: 10;
      background: rgba(15,7,32,0.85); backdrop-filter: blur(8px);
      flex-direction: column; align-items: center; justify-content: center;
      text-align: center; padding: 40px;
    }
    #celebration.show { display: flex; animation: fadeIn 0.6s ease; }
    #celebration h2 {
      font-family: 'Dancing Script', cursive;
      font-size: clamp(2.5rem, 8vw, 5rem);
      background: linear-gradient(135deg, var(--pink), var(--gold));
      -webkit-background-clip: text; -webkit-text-fill-color: transparent;
      background-clip: text; margin-bottom: 20px;
    }
    #celebration p {
      font-family: 'Playfair Display', serif; font-size: 1.2rem;
      color: var(--lavender); max-width: 420px; line-height: 1.8;
    }
    #celebration .big-heart { font-size: 5rem; margin-bottom: 24px; animation: heartbeat 1s ease infinite; }
    @keyframes heartbeat { 0%,100%{transform:scale(1);}50%{transform:scale(1.15);} }
    @keyframes fadeDown { from{opacity:0;transform:translateY(-30px);}to{opacity:1;transform:none;} }
    @keyframes fadeUp   { from{opacity:0;transform:translateY(30px);}to{opacity:1;transform:none;} }
    @keyframes fadeIn   { from{opacity:0;}to{opacity:1;} }
    @media(max-width:520px){ .letter-card{padding:36px 24px;} }
  </style>
</head>
<body>
<canvas id="bg-canvas"></canvas>
<div id="hearts-container"></div>

<main>
  <header>
    <div class="pre-title">✦ 一封来之最帅的谭小护的爱波波 ✦</div>
    <h1>从我心底<br/>到你心里</h1>
    <div class="divider"></div>
  </header>

  <div class="letter-card">
    <div class="salutation">我最亲爱的人，</div>
    <p>生命中有些瞬间，悄悄改变了一切——隔着人群的一个眼神，深夜里共同的笑声，以及某种无声胜有声的沉默。对我而言，你就是所有这些瞬间，凝聚成一个无与伦比的人。</p>
    <p>我无数次尝试用语言表达你对我的意义，却每一次都美丽地词穷。你是我在寒冷清晨渴望的温暖。你是让平凡变得闪光的念想。你，毫无疑问，是我世界里最美好的部分。</p>
    <p>和你在一起，我明白了爱不只存在于宏大的姿态——它也藏在细微之处。你记住那些小事的方式。你的存在让任何地方都变得像家。你让我渴望成为最真实的自己。</p>
    <p>我不愿想象生命中有任何一个章节没有你的身影。所以，我不会那样去想。</p>
    <div class="signature">永远属于你的 💫</div>
  </div>

  <section class="proposal">
    <h2>你愿意成为我的人吗？</h2>
    <p class="sub">永远永远——这是我的请求。</p>
    <div class="proposal-buttons">
      <button class="btn btn-yes" onclick="celebrate()">愿意，永远 ♡</button>
      <button class="btn btn-no" id="noBtn" onclick="runAway()">也许不...</button>
    </div>
  </section>
</main>

<div id="celebration">
  <div class="big-heart">💖</div>
  <h2>你答应了！</h2>
  <p>我的心比任何时候都快乐。我承诺珍惜与你在一起的每一刻——今天、明天，以及此后的每一天。</p>
</div>

<script>
  /* STAR CANVAS */
  (function(){
    const canvas=document.getElementById('bg-canvas'),ctx=canvas.getContext('2d');
    let W,H,stars=[];
    function resize(){W=canvas.width=window.innerWidth;H=canvas.height=window.innerHeight;}
    function mkStar(){return{x:Math.random()*W,y:Math.random()*H,r:Math.random()*1.2+0.2,a:Math.random(),da:(Math.random()*0.004+0.001)*(Math.random()<0.5?1:-1),hue:Math.random()<0.5?280:340};}
    function initStars(n){stars=[];for(let i=0;i<n;i++)stars.push(mkStar());}
    function draw(){
      ctx.clearRect(0,0,W,H);
      stars.forEach(s=>{
        s.a=Math.max(0.05,Math.min(1,s.a+s.da));
        if(s.a<=0.05||s.a>=1)s.da*=-1;
        ctx.beginPath();ctx.arc(s.x,s.y,s.r,0,Math.PI*2);
        ctx.fillStyle=`hsla(${s.hue},80%,85%,${s.a})`;ctx.fill();
      });
      requestAnimationFrame(draw);
    }
    window.addEventListener('resize',()=>{resize();initStars(220);});
    resize();initStars(220);draw();
  })();

  /* FLOATING HEARTS */
  (function(){
    const container=document.getElementById('hearts-container');
    const symbols=['♡','♥','✦','✿','⋆'];
    const colors=['#f9a8d4','#c4b5fd','#fbbf24','#e879f9','#67e8f9'];
    function spawn(){
      const el=document.createElement('span');
      el.className='heart';
      el.textContent=symbols[Math.floor(Math.random()*symbols.length)];
      el.style.left=Math.random()*100+'vw';
      el.style.fontSize=(Math.random()*1.2+0.7)+'rem';
      el.style.color=colors[Math.floor(Math.random()*colors.length)];
      const dur=Math.random()*10+8,delay=Math.random()*6;
      el.style.animationDuration=dur+'s';
      el.style.animationDelay=delay+'s';
      container.appendChild(el);
      setTimeout(()=>el.remove(),(dur+delay)*1000);
    }
    for(let i=0;i<18;i++)spawn();
    setInterval(spawn,900);
  })();

  /* SCROLL-IN PARAGRAPHS */
  (function(){
    const ps=document.querySelectorAll('.letter-card p');
    const io=new IntersectionObserver(entries=>{
      entries.forEach(e=>{if(e.isIntersecting){e.target.classList.add('visible');io.unobserve(e.target);}});
    },{threshold:0.15});
    ps.forEach((p,i)=>{p.style.transitionDelay=(i*0.18)+'s';io.observe(p);});
  })();

  /* NO BUTTON RUNAWAY */
  let noMoves=0;
  function runAway(){
    const btn=document.getElementById('noBtn');
    noMoves++;
    const maxX=window.innerWidth-180,maxY=window.innerHeight-60;
    const rect=btn.getBoundingClientRect();
    let nx,ny;
    do{nx=Math.random()*maxX;ny=Math.random()*maxY;}
    while(Math.abs(nx-rect.left)<100&&Math.abs(ny-rect.top)<60);
    btn.style.position='fixed';btn.style.left=nx+'px';btn.style.top=ny+'px';btn.style.zIndex=5;
    if(noMoves>=5)btn.style.display='none';
  }

  /* CELEBRATION */
  function celebrate(){
    document.getElementById('celebration').classList.add('show');
    launchConfetti();
  }
  function launchConfetti(){
    const canvas=document.createElement('canvas');
    canvas.style.cssText='position:fixed;inset:0;pointer-events:none;z-index:11;';
    document.body.appendChild(canvas);
    const ctx=canvas.getContext('2d');
    canvas.width=window.innerWidth;canvas.height=window.innerHeight;
    const pieces=Array.from({length:160},()=>({
      x:Math.random()*canvas.width,y:Math.random()*canvas.height-canvas.height,
      r:Math.random()*6+3,d:Math.random()*8+2,
      color:['#f9a8d4','#c4b5fd','#fbbf24','#e879f9','#a5f3fc'][Math.floor(Math.random()*5)],
      tilt:Math.random()*10-10,ts:Math.random()*0.1+0.05,ta:0,
    }));
    let frame=0;
    function drop(){
      ctx.clearRect(0,0,canvas.width,canvas.height);
      pieces.forEach(p=>{
        p.ta+=p.ts;p.y+=(Math.cos(p.ta)+p.d)*0.8;p.x+=Math.sin(p.ta)*1.5;
        if(p.y>canvas.height){p.y=-10;p.x=Math.random()*canvas.width;}
        ctx.beginPath();ctx.ellipse(p.x,p.y,p.r,p.r*0.5,p.tilt,0,Math.PI*2);
        ctx.fillStyle=p.color;ctx.fill();
      });
      frame++;if(frame<300)requestAnimationFrame(drop);else canvas.remove();
    }
    drop();
  }
  document.getElementById('celebration').addEventListener('click',function(){this.classList.remove('show');});
</script>
</body>
</html>"""

components.html(HTML, height=1100, scrolling=True)
