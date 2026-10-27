// Mede, no Chrome sem janela, o SVG exportado pelo draw.io: a caixa real de cada texto e o trajeto de cada linha, por célula.
// Usado por scripts/verificar_drawio.py. Uso: node scripts/medir_svg.mjs arquivo.svg saida.json
// Precisa do Google Chrome ou do Microsoft Edge; o caminho pode ser dado em CHROME.
import { spawn } from 'node:child_process';
import { readFileSync, writeFileSync, mkdtempSync, existsSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
const [svgPath, out] = process.argv.slice(2);
const svg = readFileSync(svgPath, 'utf8').replace(/^[\s\S]*?<svg/, '<svg');
const port = 9500 + Math.floor(Math.random() * 400);
const chrome = [process.env.CHROME, 'C:/Program Files/Google/Chrome/Application/chrome.exe', 'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe',
  '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', '/usr/bin/google-chrome', '/usr/bin/chromium'].find(c => c && existsSync(c));
if (!chrome) { console.error('Chrome/Edge não encontrado; defina CHROME com o caminho do executável'); process.exit(1); }
const proc = spawn(chrome, ['--headless=new', `--remote-debugging-port=${port}`, `--user-data-dir=${mkdtempSync(join(tmpdir(), 'med-'))}`, 'about:blank'], { stdio: 'ignore' });
let ws, seq = 0; const pend = new Map();
const send = (m, p = {}) => new Promise((res, rej) => { const i = ++seq; pend.set(i, { res, rej }); ws.send(JSON.stringify({ id: i, method: m, params: p })); });
let u; for (let t = 0; t < 50 && !u; t++) { try { u = (await (await fetch(`http://127.0.0.1:${port}/json/list`)).json()).find(x => x.type === 'page')?.webSocketDebuggerUrl } catch { } await new Promise(r => setTimeout(r, 200)); }
try {
  ws = new WebSocket(u); await new Promise(r => ws.onopen = r);
  ws.onmessage = (m) => { const d = JSON.parse(m.data); if (d.id && pend.has(d.id)) { const p = pend.get(d.id); pend.delete(d.id); d.error ? p.rej(new Error(d.error.message)) : p.res(d.result); } };
  const r = await send('Runtime.evaluate', { returnByValue: true, awaitPromise: true, expression: `(()=>{document.body.innerHTML=${JSON.stringify(svg)};
    const s=document.querySelector('svg');const inv=s.getScreenCTM().inverse();
    const cx=(el)=>{const b=el.getBBox();const m=inv.multiply(el.getScreenCTM());const P=[[b.x,b.y],[b.x+b.width,b.y+b.height]].map(([x,y])=>[m.a*x+m.c*y+m.e,m.b*x+m.d*y+m.f]);
      return [Math.min(P[0][0],P[1][0]),Math.min(P[0][1],P[1][1]),Math.max(P[0][0],P[1][0]),Math.max(P[0][1],P[1][1])].map(n=>Math.round(n*10)/10)};
    const res={};
    s.querySelectorAll('g[data-cell-id]').forEach(g=>{const id=g.dataset.cellId;if(id==='0'||id==='1')return;
      const own=[...g.querySelectorAll('*')].filter(el=>el.closest('g[data-cell-id]')===g);
      const textos=own.filter(el=>el.tagName==='text').map(t=>({t:t.textContent,b:cx(t)}));
      const linhas=own.filter(el=>el.tagName==='path'&&el.getAttribute('fill')==='none').map(p=>p.getAttribute('d'));
      res[id]={textos,linhas};});
    return res;})()` });
  writeFileSync(out, JSON.stringify(r.result.value));
} finally { try { ws?.close(); } catch { } proc.kill(); }
