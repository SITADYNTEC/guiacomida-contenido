// Motor de reels GuiaComida (HTML → cuadros con scripts/frames.py).
// Cada reel define: window.T (cortes, el último es la duración), BG (fondo por escena), anim(t,T)
// y opcional window.W = [[palabra, inicio, fin], ...] para subtítulos palabra por palabra.
const clamp=(x,a=0,b=1)=>Math.max(a,Math.min(b,x));
const ease=x=>{x=clamp(x);return 1-Math.pow(1-x,3)};
const back=x=>{x=clamp(x);const c=1.7;return 1+(c+1)*Math.pow(x-1,3)+c*Math.pow(x-1,2)};
const $=id=>document.getElementById(id);
const pop=(el,lt,d=0.4)=>{if(!el)return;el.style.transform=`scale(${back(lt/d)})`;el.style.opacity=clamp(lt/0.12)};
const rise=(el,lt,dist=60,d=0.4)=>{if(!el)return;el.style.opacity=ease(lt/d);el.style.transform=`translateY(${(1-ease(lt/d))*dist}px)`};
const slam=(el,lt)=>{if(!el)return;const k=clamp(lt/0.18);el.style.opacity=k>0?1:0;el.style.transform=`scale(${1.6-0.6*ease(k)})`};
function sceneIndex(t){const T=window.T;let idx=0;for(let i=0;i<T.length-1;i++)if(t>=T[i])idx=i;return idx}
function subs(t){
  const box=$('subs');if(!box||!window.W)return;
  const W=window.W;let i=-1;W.forEach((w,j)=>{if(t>=w[1]-0.05)i=j});
  if(i<0||t>W[W.length-1][2]+0.6){box.style.opacity=0;return}
  // grupos de hasta 4 palabras, cortando en puntuación
  const groups=[];let g=[];W.forEach((w,j)=>{g.push(j);if(g.length>=4||/[.,?!…]$/.test(w[0])){groups.push(g);g=[]}});if(g.length)groups.push(g);
  const grp=groups.find(gr=>gr.includes(i));
  box.style.opacity=1;
  box.innerHTML=grp.map(j=>`<span class="${j==i?'on':(j<i?'past':'')}">${W[j][0].replace(/[…]/g,'')}</span>`).join(' ');
}
function render(t){
  const T=window.T,N=T.length-1,idx=sceneIndex(t);
  $('stage').style.background=BG[idx];
  for(let i=0;i<N;i++){const s=$('s'+(i+1));if(s)s.style.opacity=i==idx?1:0}
  subs(t);anim(t,T);
}
