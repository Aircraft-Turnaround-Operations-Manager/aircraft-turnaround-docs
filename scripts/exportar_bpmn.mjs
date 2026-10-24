// Exporta cada diagrama (vista) de um arquivo .bpmn para PNG e SVG, renderizando com o bpmn-js no Chrome sem janela.
//
// Nomes: o primeiro diagrama do arquivo sai com o nome base do .bpmn; os demais, com o nome base mais o id do
// diagrama sem o "D_" (ex.: D_tarefas_em_solo -> 04-bpmn-to-be-tarefas-em-solo.png). Também grava a geometria
// medida de cada vista (formas, linhas e caixas reais dos textos) em <tmp>/bpmn-geo/, que o
// scripts/verificar_bpmn.py confere.
//
// Uso:  npm install --prefix scripts        (uma vez; instala o bpmn-js 18.9.1 em scripts/node_modules)
//       node scripts/exportar_bpmn.mjs especificacao/diagramas/04-bpmn-to-be.bpmn [escala_png]
// Precisa do Google Chrome ou do Microsoft Edge; o caminho pode ser dado em CHROME.
import { spawn } from 'node:child_process';
import { readFileSync, writeFileSync, mkdtempSync, mkdirSync, existsSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join, dirname, basename } from 'node:path';
import { fileURLToPath } from 'node:url';

const [bpmnPath, escala = '2'] = process.argv.slice(2);
if (!bpmnPath) { console.error('uso: node scripts/exportar_bpmn.mjs arquivo.bpmn [escala_png]'); process.exit(1); }
const dist = join(dirname(fileURLToPath(import.meta.url)), 'node_modules/bpmn-js/dist');
if (!existsSync(dist)) { console.error('bpmn-js não encontrado: rode "npm install --prefix scripts"'); process.exit(1); }
const viewerJs = readFileSync(join(dist, 'bpmn-viewer.production.min.js'), 'utf8');
const css = ['diagram-js.css', 'bpmn-js.css'].map(f => readFileSync(join(dist, 'assets', f), 'utf8')).join('\n');
const xml = readFileSync(bpmnPath, 'utf8');
const chrome = [process.env.CHROME, 'C:/Program Files/Google/Chrome/Application/chrome.exe', 'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe',
  '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', '/usr/bin/google-chrome', '/usr/bin/chromium'].find(c => c && existsSync(c));
if (!chrome) { console.error('Chrome/Edge não encontrado; defina CHROME com o caminho do executável'); process.exit(1); }
const port = 9300 + Math.floor(Math.random() * 500);
const proc = spawn(chrome, ['--headless=new', `--remote-debugging-port=${port}`, `--user-data-dir=${mkdtempSync(join(tmpdir(), 'bpmn-chrome-'))}`, '--no-first-run', 'about:blank'], { stdio: 'ignore' });

let ws, seq = 0; const pend = new Map();
const send = (method, params = {}) => new Promise((res, rej) => { const i = ++seq; pend.set(i, { res, rej }); ws.send(JSON.stringify({ id: i, method, params })); });
async function conectar() {
  for (let t = 0; t < 50; t++) {
    try { const l = await (await fetch(`http://127.0.0.1:${port}/json/list`)).json(); const p = l.find(x => x.type === 'page'); if (p) return p.webSocketDebuggerUrl; } catch { }
    await new Promise(r => setTimeout(r, 200));
  }
  throw new Error('o Chrome não respondeu');
}
const avaliar = async (expr) => { const r = await send('Runtime.evaluate', { expression: expr, awaitPromise: true, returnByValue: true }); if (r.exceptionDetails) throw new Error(JSON.stringify(r.exceptionDetails).slice(0, 800)); return r.result.value; };

// roda dentro da página: abre cada diagrama, mede a geometria e salva o SVG
const naPagina = `(async()=>{const v=new BpmnJS({container:'#c'});const imp=await v.importXML(${JSON.stringify(xml)});
  const out={avisos:imp.warnings.map(w=>w.message),vistas:[]};const vp=()=>document.querySelector('#c .viewport');
  const caixa=(el)=>{const b=el.getBBox();if(!b.width&&!b.height)return null;const m=vp().getScreenCTM().inverse().multiply(el.getScreenCTM());
    const P=[[b.x,b.y],[b.x+b.width,b.y],[b.x,b.y+b.height],[b.x+b.width,b.y+b.height]].map(([x,y])=>[m.a*x+m.c*y+m.e,m.b*x+m.d*y+m.f]);
    const xs=P.map(p=>p[0]),ys=P.map(p=>p[1]);return [Math.min(...xs),Math.min(...ys),Math.max(...xs),Math.max(...ys)].map(n=>Math.round(n*10)/10);};
  for(const d of v.getDefinitions().diagrams){const o=await v.open(d.id);out.avisos.push(...o.warnings.map(w=>d.id+': '+w.message));
    const raiz=v.get('canvas').getRootElement();const geo=[];
    v.get('elementRegistry').forEach((e,gfx)=>{if(!e.businessObject||e===raiz)return;let r=e;while(r.parent)r=r.parent;if(r!==raiz)return;
      const vis=gfx.querySelector('.djs-visual')||gfx;
      geo.push({id:e.id,tipo:e.type,label:!!e.labelTarget,dono:e.labelTarget?e.labelTarget.id:null,pai:e.parent?e.parent.id:null,
        b:e.waypoints?null:[e.x,e.y,e.x+e.width,e.y+e.height],wp:e.waypoints?e.waypoints.map(p=>[p.x,p.y]):null,
        de:e.source?e.source.id:null,para:e.target?e.target.id:null,exp:!!(e.di&&e.di.isExpanded),
        textos:[...vis.querySelectorAll('text tspan')].map(t=>({t:t.textContent,b:caixa(t)})).filter(t=>t.b&&t.t.trim()),
        icones:[...vis.children].filter(c=>c.tagName==='path'&&!e.waypoints).map(caixa).filter(Boolean)});});
    const {svg}=await v.saveSVG();out.vistas.push({id:d.id,svg,geo});}
  return out;})()`;

try {
  ws = new WebSocket(await conectar());
  await new Promise(r => ws.onopen = r);
  ws.onmessage = (m) => { const d = JSON.parse(m.data); if (d.id && pend.has(d.id)) { const p = pend.get(d.id); pend.delete(d.id); d.error ? p.rej(new Error(d.error.message)) : p.res(d.result); } };
  await avaliar(`document.body.innerHTML=${JSON.stringify(`<style>${css}</style><div id="c" style="width:4000px;height:3000px"></div>`)};1`);
  await avaliar(viewerJs + ';1');
  const res = await avaliar(naPagina);
  console.log('avisos do bpmn-js:', res.avisos.length ? res.avisos : 'nenhum');
  const base = bpmnPath.replace(/\.bpmn$/, ''); const geoDir = join(tmpdir(), 'bpmn-geo'); mkdirSync(geoDir, { recursive: true });
  for (const [n, d] of res.vistas.entries()) {
    const saida = n === 0 ? base : `${base}-${d.id.replace(/^D_/, '').replace(/_/g, '-')}`;
    // margem de 20 px em volta (o bpmn-js recorta rente ao desenho)
    const svg = d.svg.replace(/width="([\d.]+)" height="([\d.]+)" viewBox="([-\d.]+) ([-\d.]+) ([\d.]+) ([\d.]+)"/,
      (m, w, h, x, y, vw, vh) => `width="${+w + 40}" height="${+h + 40}" viewBox="${+x - 20} ${+y - 20} ${+vw + 40} ${+vh + 40}"`);
    writeFileSync(saida + '.svg', svg);
    writeFileSync(join(geoDir, basename(saida) + '.json'), JSON.stringify(d.geo));
    const m = svg.match(/width="([\d.]+)" height="([\d.]+)"/); const w = Math.ceil(+m[1]), h = Math.ceil(+m[2]);
    await send('Emulation.setDeviceMetricsOverride', { width: w, height: h, deviceScaleFactor: +escala, mobile: false });
    await avaliar(`document.body.style.margin='0';document.body.style.background='#fff';document.body.innerHTML=${JSON.stringify(svg.replace(/^[\s\S]*?<svg/, '<svg'))};1`);
    const shot = await send('Page.captureScreenshot', { format: 'png', clip: { x: 0, y: 0, width: w, height: h, scale: 1 }, captureBeyondViewport: true });
    writeFileSync(saida + '.png', Buffer.from(shot.data, 'base64'));
    console.log('exportado', saida + '.png/.svg', `(${w} × ${h})`);
  }
  console.log('geometria para o verificador em', geoDir);
} finally { try { ws?.close(); } catch { } proc.kill(); }
