from __future__ import annotations

import json
import re
import webbrowser
from datetime import datetime
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

ROOT = Path(__file__).resolve().parents[1]
DRAFTS = ROOT / "okos_app" / "drafts"
DRAFTS.mkdir(exist_ok=True)

HTML = r"""<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width">
<title>OKOS 控制台</title><style>
*{box-sizing:border-box}body{margin:0;background:#f5f5f6;color:#151515;font:14px/1.55 "Microsoft YaHei",sans-serif}
aside{position:fixed;inset:0 auto 0 0;width:220px;background:#101114;color:#fff;padding:24px 18px}.logo{font:900 30px Arial;color:#fff}.logo b{background:#ef151f;padding:7px 10px;border-radius:9px;margin-right:8px}.sub{color:#999;margin:14px 0 30px}
nav button{width:100%;border:0;background:transparent;color:#bbb;text-align:left;padding:13px 15px;margin:4px 0;font-weight:700;border-radius:7px;cursor:pointer}nav button.on,nav button:hover{background:#ef151f;color:white}
main{margin-left:220px;padding:28px 36px;max-width:1500px}.top{display:flex;justify-content:space-between;align-items:center;border-bottom:3px solid #ef151f;padding-bottom:18px}h1{margin:0;font-size:25px}h2{font-size:17px;margin:0 0 16px}
.search{width:390px;padding:11px 15px;border:1px solid #ddd;border-radius:7px;background:white}.grid{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin:22px 0}.kpi,.panel{background:#fff;border:1px solid #e5e5e5;border-radius:8px;padding:18px}.kpi strong{font-size:28px;display:block;margin-top:7px}.kpi.red{border-top:4px solid #ef151f}.cols{display:grid;grid-template-columns:1.35fr 1fr;gap:16px}.row{display:flex;justify-content:space-between;padding:13px 0;border-bottom:1px solid #eee}.tag{color:#ef151f;font-weight:800}
button.primary{background:#ef151f;color:white;border:0;border-radius:6px;padding:10px 16px;font-weight:800;cursor:pointer}button.ghost{border:1px solid #ddd;background:#fff;border-radius:6px;padding:8px 12px;cursor:pointer}
label{display:block;font-weight:800;margin:12px 0 6px}input,textarea,select{width:100%;padding:10px;border:1px solid #ddd;border-radius:6px;font:inherit}textarea{min-height:110px}.actions{margin-top:14px;display:flex;gap:9px}.hidden{display:none}.result{padding:12px 0;border-bottom:1px solid #eee}.path{color:#888;font-size:12px}.empty{color:#999;padding:20px 0}
@media(max-width:900px){aside{position:static;width:100%;height:auto;padding:14px 16px}.logo{font-size:22px}.logo b{padding:4px 7px}.sub{display:none}nav{display:grid;grid-template-columns:repeat(4,1fr);margin-top:12px}nav button{text-align:center;padding:9px 4px}main{margin-left:0;padding:18px}.grid{grid-template-columns:1fr 1fr}.cols{grid-template-columns:1fr}.top{gap:12px;flex-wrap:wrap}.search{width:100%}}
@media(max-width:480px){nav button span{display:none}.grid{grid-template-columns:1fr}.kpi{padding:14px}.kpi strong{font-size:23px}}
</style></head><body><aside><div class="logo"><b>OK</b><span>OS</span></div><div class="sub">赛事联盟操作系统</div><nav>
<button class="on" data-page="home">◼　<span>运营总览</span></button><button data-page="search">⌕　<span>知识搜索</span></button><button data-page="new">＋　<span>录入反馈</span></button><button data-page="drafts">✓　<span>Draft 审核</span></button>
</nav></aside><main>
<section id="home"><div class="top"><div><h1>今日运营总览</h1><small>OKOS · 全程高能</small></div><button class="primary" onclick="go('new')">＋ 录入反馈</button></div><div class="grid">
<div class="kpi red">知识文档<strong id="docs">—</strong></div><div class="kpi">待审核 Draft<strong id="pending">—</strong></div><div class="kpi">已确认观察<strong id="observations">—</strong></div><div class="kpi">系统版本<strong id="version">—</strong></div></div>
<div class="cols"><div class="panel"><h2>最新运营观察</h2><div id="latest"></div></div><div class="panel"><h2>快捷操作</h2><div class="row"><span>反馈社群或赛事结果</span><button class="ghost" onclick="go('new')">录入</button></div><div class="row"><span>查找 OKOS 标准</span><button class="ghost" onclick="go('search')">搜索</button></div><div class="row"><span>批准知识写入</span><button class="ghost" onclick="go('drafts')">审核</button></div></div></div></section>
<section id="search" class="hidden"><div class="top"><h1>OKOS 知识搜索</h1><input class="search" id="q" placeholder="输入赛事、社群、奖励等关键词"></div><div class="panel" style="margin-top:20px" id="results"><div class="empty">输入关键词开始搜索</div></div></section>
<section id="new" class="hidden"><div class="top"><h1>录入运营反馈</h1><span class="tag">先 Draft，后批准</span></div><div class="panel" style="margin-top:20px;max-width:760px"><label>标题</label><input id="title" placeholder="例如：7月4日对抗赛反馈"><label>归属模块</label><select id="category"><option>社群运营</option><option>赛事运营</option><option>奖励机制</option><option>产品建议</option></select><label>结果与事实</label><textarea id="content" placeholder="写清发生了什么、反馈如何；不要把推测当事实。"></textarea><div class="actions"><button class="primary" onclick="submitDraft()">提交审核</button></div><div id="notice"></div></div></section>
<section id="drafts" class="hidden"><div class="top"><h1>Draft 审核</h1><span>人工批准门禁</span></div><div class="panel" style="margin-top:20px" id="draftList"></div></section>
</main><script>
const pages=['home','search','new','drafts'];function go(p){pages.forEach(x=>document.getElementById(x).classList.toggle('hidden',x!==p));document.querySelectorAll('nav button').forEach(b=>b.classList.toggle('on',b.dataset.page===p));if(p==='drafts')loadDrafts()}
document.querySelectorAll('nav button').forEach(b=>b.onclick=()=>go(b.dataset.page));
async function api(path,opt){let r=await fetch(path,opt);return r.json()}async function stats(){let d=await api('/api/stats');Object.keys(d).forEach(k=>{let e=document.getElementById(k);if(e)e.textContent=d[k]});document.getElementById('latest').innerHTML=d.latest?.map(x=>`<div class="result"><b>${x}</b></div>`).join('')||'<div class="empty">暂无记录</div>'}
let timer;q.oninput=()=>{clearTimeout(timer);timer=setTimeout(async()=>{let d=await api('/api/search?q='+encodeURIComponent(q.value));results.innerHTML=d.length?d.map(x=>`<div class="result"><b>${x.title}</b><div>${x.snippet}</div><div class="path">${x.path}</div></div>`).join(''):'<div class="empty">没有找到结果</div>'},250)}
async function submitDraft(){let body={title:title.value,category:category.value,content:content.value};if(!body.title||!body.content)return notice.textContent='请填写标题和事实';await api('/api/drafts',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)});notice.innerHTML='<p class="tag">已进入审核队列</p>';title.value='';content.value='';stats()}
async function loadDrafts(){let d=await api('/api/drafts');draftList.innerHTML=d.length?d.map(x=>`<div class="result"><b>${x.title}</b> · ${x.category}<p>${x.content}</p><button class="primary" onclick="approve('${x.id}')">确认写入 OKOS</button></div>`).join(''):'<div class="empty">没有待审核内容</div>'}
async function approve(id){await api('/api/drafts/'+id+'/approve',{method:'POST'});loadDrafts();stats()}stats();
</script></body></html>"""

def markdown_files():
    return [p for p in ROOT.rglob("*.md") if not any(x in p.parts for x in ("site", "docs"))]

def drafts():
    return [json.loads(p.read_text("utf-8")) for p in sorted(DRAFTS.glob("*.json"), reverse=True)]

class Handler(BaseHTTPRequestHandler):
    def reply(self, data, status=200, kind="application/json; charset=utf-8"):
        raw = data.encode("utf-8") if isinstance(data, str) else json.dumps(data, ensure_ascii=False).encode()
        self.send_response(status); self.send_header("Content-Type", kind); self.send_header("Content-Length", len(raw)); self.end_headers(); self.wfile.write(raw)
    def do_GET(self):
        u = urlparse(self.path)
        if u.path == "/": return self.reply(HTML, kind="text/html; charset=utf-8")
        if u.path == "/api/stats":
            obs = (ROOT/"07-community/operations-observations.md").read_text("utf-8")
            version = re.search(r"v\d+\.\d+\.\d+", (ROOT/"README.md").read_text("utf-8"), re.I)
            latest = re.findall(r"### (OBS-[^\n]+)", obs)[:4]
            return self.reply({"docs":len(markdown_files()),"pending":len(drafts()),"observations":len(latest),"version":version.group(0) if version else "—","latest":latest})
        if u.path == "/api/search":
            q=parse_qs(u.query).get("q",[""])[0].strip().lower(); out=[]
            if q:
                for p in markdown_files():
                    text=p.read_text("utf-8",errors="ignore")
                    i=text.lower().find(q)
                    if i>=0: out.append({"title":next((x[2:] for x in text.splitlines() if x.startswith("# ")),p.stem),"snippet":text[max(0,i-55):i+110].replace("\n"," "),"path":str(p.relative_to(ROOT))})
            return self.reply(out[:30])
        if u.path == "/api/drafts": return self.reply(drafts())
        self.reply({"error":"not found"},404)
    def do_POST(self):
        n=int(self.headers.get("Content-Length",0)); data=json.loads(self.rfile.read(n) or b"{}")
        if self.path == "/api/drafts":
            now=datetime.now(); data.update(id=now.strftime("%Y%m%d%H%M%S%f"),created_at=now.isoformat(timespec="seconds"))
            (DRAFTS/f"{data['id']}.json").write_text(json.dumps(data,ensure_ascii=False,indent=2),"utf-8"); return self.reply(data,201)
        m=re.fullmatch(r"/api/drafts/(\d+)/approve",self.path)
        if m:
            p=DRAFTS/f"{m.group(1)}.json"
            if not p.exists(): return self.reply({"error":"not found"},404)
            d=json.loads(p.read_text("utf-8")); target=ROOT/"07-community/operations-observations.md"
            block=f"\n\n### {d['created_at'][:10]}：{d['title']}\n\n**归属：** {d['category']}  \n**状态：** 人工批准写入\n\n{d['content']}\n"
            target.write_text(target.read_text("utf-8").rstrip()+block+"\n","utf-8"); p.unlink(); return self.reply({"ok":True})
        self.reply({"error":"not found"},404)
    def log_message(self, *_): pass

if __name__ == "__main__":
    url="http://127.0.0.1:8765"; print(f"OKOS 控制台：{url}"); webbrowser.open(url); ThreadingHTTPServer(("127.0.0.1",8765),Handler).serve_forever()
