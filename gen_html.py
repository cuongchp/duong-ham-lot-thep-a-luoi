# -*- coding: utf-8 -*-
import json, os

base = r"D:\1. WOKRS\1. THUY DIEN A LƯƠI\2- NHA MAY A LUOI\NAM 2026\3. P4\11. THEO DOI MANG XONG-OP DUONG HAM"
data = json.load(open(os.path.join(base, 'DU_LIEU_DUONG_HAM.json'), encoding='utf-8'))

# Fix section names
for r in data:
    r['phan_doan'] = r['phan_doan'].replace('PĐ5','PĐ 5').replace('PĐ6','PĐ 6')

json_str = json.dumps(data, ensure_ascii=False)

html = """<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Đường Hầm Lót Thép - Nhà Máy Thủy Điện A Lưới</title>
<style>
:root{--bd:#0369a1;--b:#0ea5e9;--bl:#bae6fd;--bxl:#e0f2fe;--bp:#f0f9ff;--w:#fff;--g1:#f1f5f9;--g2:#e2e8f0;--g5:#64748b;--g7:#334155;--g9:#0f172a;--gr:#059669;--or:#d97706;--re:#dc2626;--sh:0 2px 8px rgba(3,105,161,.12);--shl:0 8px 24px rgba(3,105,161,.18);--r:10px}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:'Segoe UI',Arial,sans-serif;background:var(--g1);color:var(--g7);font-size:14px}
.hdr{background:linear-gradient(135deg,#0369a1,#0284c7 60%,#0ea5e9);color:#fff;position:sticky;top:0;z-index:100;box-shadow:var(--shl)}
.hdr-in{max-width:1400px;margin:0 auto;padding:14px 20px;display:flex;align-items:center;gap:16px;flex-wrap:wrap}
.hdr-logo{width:46px;height:46px;background:rgba(255,255,255,.2);border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:22px;flex-shrink:0}
.hdr-t{flex:1;min-width:200px}
.hdr-t h1{font-size:17px;font-weight:700;line-height:1.3}
.hdr-t p{font-size:12px;opacity:.85;margin-top:2px}
.hdr-bdg{background:rgba(255,255,255,.2);border:1px solid rgba(255,255,255,.35);padding:4px 12px;border-radius:20px;font-size:12px;font-weight:600;white-space:nowrap}
.main{max-width:1400px;margin:0 auto;padding:20px 16px}
.tabs{display:flex;gap:6px;flex-wrap:wrap;margin-bottom:20px}
.tab{padding:7px 16px;border-radius:20px;border:2px solid var(--bl);background:#fff;color:var(--bd);font-size:13px;font-weight:600;cursor:pointer;transition:all .2s}
.tab:hover{background:var(--bl)}
.tab.active{background:var(--b);color:#fff;border-color:var(--b);box-shadow:0 2px 8px rgba(14,165,233,.35)}
.tab-mx{border-color:#e9d5ff;color:#6b21a8;background:#faf5ff}
.tab-mx:hover{background:#e9d5ff}
.tab-mx.active{background:#7c3aed;color:#fff;border-color:#7c3aed;box-shadow:0 2px 8px rgba(124,58,237,.4)}
.mx-seg-card{background:#fff;border-radius:8px;padding:12px 14px;border-left:4px solid #7c3aed;box-shadow:var(--sh)}
.mx-seg-card .msn{font-size:22px;font-weight:800;color:#6b21a8}
.mx-seg-card .mst{font-size:11px;font-weight:700;color:#6b21a8;margin-bottom:4px}
.mx-seg-card .mss{font-size:11px;color:var(--g5)}
.lt-chip{padding:5px 12px;background:#faf5ff;border:1px solid #e9d5ff;border-radius:16px;font-size:11px;font-weight:600;color:#6b21a8;cursor:pointer;transition:all .15s}
.lt-chip:hover{background:#7c3aed;color:#fff;border-color:#7c3aed}
.mx-badge{display:inline-block;padding:2px 7px;background:#f3e8ff;color:#6b21a8;border-radius:10px;font-size:10px;font-weight:700;margin-left:4px;border:1px solid #e9d5ff}
.diag-wrap{background:#fff;border-radius:var(--r);padding:18px 20px;margin-bottom:20px;box-shadow:var(--sh)}
.diag-wrap h2{font-size:14px;font-weight:700;color:var(--bd);margin-bottom:14px}
.diag{display:flex;align-items:stretch;overflow-x:auto;padding-bottom:6px;gap:0}
.nd{text-align:center;flex-shrink:0}
.nd-lbl{font-size:11px;color:var(--g5);margin-top:6px;white-space:nowrap}
.nd-km{font-size:10px;color:var(--bd);font-weight:600}
.nd-ic{width:38px;height:38px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:18px;margin:0 auto 4px;border:3px solid var(--bd);background:#fff}
.seg{flex:1;min-width:90px;display:flex;flex-direction:column;align-items:center;cursor:pointer;transition:transform .15s;padding:0 2px}
.seg:hover{transform:translateY(-2px)}
.seg-bar{width:100%;height:36px;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:700;color:#fff}
.seg-info{font-size:10px;color:var(--g5);text-align:center;margin-top:5px;line-height:1.4}
.seg-thick{font-size:11px;font-weight:700;color:var(--bd)}
.sg{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:14px;margin-bottom:20px}
.sc{background:#fff;border-radius:var(--r);padding:16px 18px;box-shadow:var(--sh);border-left:4px solid var(--b);transition:box-shadow .2s;cursor:pointer}
.sc:hover{box-shadow:var(--shl)}
.sc.active{border-left-color:var(--bd);background:var(--bp)}
.sc-hd{display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:8px}
.sc-ti{font-size:13px;font-weight:700;color:var(--bd)}
.sc-bdg{background:var(--bxl);color:var(--bd);font-size:10px;font-weight:700;padding:2px 8px;border-radius:10px}
.sc-n{font-size:28px;font-weight:800;color:var(--bd);line-height:1}
.sc-s{font-size:11px;color:var(--g5);margin-top:4px}
.sc-r{font-size:11px;color:var(--g7);margin-top:6px;padding-top:6px;border-top:1px solid var(--g2)}
.lgd{background:#fff;border-radius:var(--r);padding:16px 20px;margin-bottom:20px;box-shadow:var(--sh)}
.lgd h2{font-size:13px;font-weight:700;color:var(--bd);margin-bottom:10px;cursor:pointer;display:flex;align-items:center;justify-content:space-between}
.lgd-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:10px}
.lgd-item{background:var(--g1);border-radius:8px;padding:10px 14px}
.lgd-item strong{color:var(--bd);font-size:12px}
.lgd-item p{font-size:12px;color:var(--g7);margin-top:3px;line-height:1.5}
.ctrl{display:flex;gap:10px;flex-wrap:wrap;align-items:center;margin-bottom:16px}
.srch{flex:1;min-width:200px;padding:9px 14px 9px 36px;border:2px solid var(--bl);border-radius:24px;font-size:13px;outline:none;transition:border-color .2s;background:#fff url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' fill='%230ea5e9' viewBox='0 0 16 16'%3E%3Cpath d='M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001c.03.04.062.078.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1.007 1.007 0 0 0-.115-.099zm-5.242 1.656a5.5 5.5 0 1 1 0-11 5.5 5.5 0 0 1 0 11z'/%3E%3C/svg%3E") no-repeat 12px center}
.srch:focus{border-color:var(--b)}
.btn{padding:9px 18px;border-radius:24px;border:none;font-size:13px;font-weight:600;cursor:pointer;transition:all .2s;display:flex;align-items:center;gap:6px}
.btn-p{background:var(--b);color:#fff}.btn-p:hover{background:var(--bd)}
.btn-g{background:var(--gr);color:#fff}.btn-g:hover{background:#047857}
.btn-o{background:#fff;color:var(--bd);border:2px solid var(--bl)}.btn-o:hover{background:var(--bxl)}
.rc{font-size:12px;color:var(--g5);white-space:nowrap}
.tw{background:#fff;border-radius:var(--r);box-shadow:var(--sh);overflow:hidden}
.ts{overflow-x:auto}
table{width:100%;border-collapse:collapse;min-width:700px}
thead{background:linear-gradient(135deg,var(--bd),var(--b));color:#fff}
thead th{padding:12px 14px;text-align:left;font-size:12px;font-weight:700;letter-spacing:.3px;white-space:nowrap}
tbody tr{border-bottom:1px solid var(--g2);transition:background .15s}
tbody tr:hover{background:var(--bp)}
tbody tr.exp{background:var(--bxl)}
td{padding:10px 14px;font-size:13px;vertical-align:middle}
.ts-stt{font-weight:700;color:var(--bd);width:50px}
.ts-pd{width:90px}
.ts-lt{font-weight:600;color:var(--g7);white-space:nowrap}
.ts-th{text-align:center}
.tb-bdg{display:inline-block;padding:3px 10px;border-radius:12px;font-weight:700;font-size:12px}
.ts-mt{max-width:280px}
.mt-p{color:var(--g7)}
.mt-m{color:var(--b);font-size:11px;cursor:pointer}
.ts-ac{white-space:nowrap;width:100px}
.ex-row td{padding:0;background:var(--bp)}
.ex-ct{padding:14px 20px 16px}
.ex-ti{font-size:12px;font-weight:700;color:var(--bd);margin-bottom:10px}
.chip-wrap{display:flex;flex-wrap:wrap;gap:6px}
.chip{padding:4px 10px;border-radius:16px;font-size:11px;font-weight:600;background:#fff;border:1px solid var(--bl);color:var(--g7)}
.chip.dh{background:var(--bxl);color:var(--bd);border-color:var(--bl)}
.chip.dhds{background:#dbeafe;color:#1d4ed8;border-color:#bfdbfe}
.chip.cb{background:#dcfce7;color:#166534;border-color:#bbf7d0}
.chip.tb{background:#fef9c3;color:#854d0e;border-color:#fde68a}
.chip.tap{background:#ffe4e6;color:#9f1239;border-color:#fecdd3}
.chip.mx{background:#f3e8ff;color:#6b21a8;border-color:#e9d5ff}
.pd-b{display:inline-block;padding:3px 10px;border-radius:12px;font-size:11px;font-weight:700;white-space:nowrap}
.pd1{background:#dbeafe;color:#1e40af}.pd2{background:#dcfce7;color:#166534}
.pd3{background:#fef3c7;color:#92400e}.pd4{background:#fce7f3;color:#9d174d}
.pd5{background:#ede9fe;color:#5b21b6}.pd6{background:#ccfbf1;color:#134e4a}
.bsm{padding:4px 10px;font-size:11px;border-radius:8px;border:none;cursor:pointer;font-weight:600;transition:all .15s}
.be{background:var(--bxl);color:var(--bd)}.be:hover{background:var(--bl)}
.bx{background:var(--g1);color:var(--g7)}.bx:hover{background:var(--g2)}
.mo-ov{display:none;position:fixed;inset:0;background:rgba(0,0,0,.45);z-index:1000;align-items:center;justify-content:center;padding:16px}
.mo-ov.open{display:flex}
.mo{background:#fff;border-radius:14px;width:100%;max-width:600px;box-shadow:0 20px 60px rgba(0,0,0,.3);max-height:90vh;overflow-y:auto}
.mo-hd{background:linear-gradient(135deg,var(--bd),var(--b));color:#fff;padding:18px 22px;border-radius:14px 14px 0 0;display:flex;align-items:center;justify-content:space-between}
.mo-hd h3{font-size:16px;font-weight:700}
.mo-cl{background:none;border:none;color:#fff;font-size:22px;cursor:pointer;opacity:.8;line-height:1}
.mo-cl:hover{opacity:1}
.mo-bd{padding:22px}
.fr{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-bottom:14px}
.fr1{grid-template-columns:1fr}
.fg label{display:block;font-size:12px;font-weight:700;color:var(--bd);margin-bottom:5px}
.fg input,.fg select,.fg textarea{width:100%;padding:9px 12px;border:2px solid var(--bl);border-radius:8px;font-size:13px;outline:none;transition:border-color .2s;font-family:inherit}
.fg input:focus,.fg select:focus,.fg textarea:focus{border-color:var(--b)}
.fg textarea{min-height:90px;resize:vertical}
.mo-ft{padding:16px 22px;border-top:1px solid var(--g2);display:flex;gap:10px;justify-content:flex-end}
.pag{display:flex;align-items:center;justify-content:center;gap:6px;padding:16px;flex-wrap:wrap}
.pb{width:34px;height:34px;border-radius:8px;border:2px solid var(--bl);background:#fff;color:var(--bd);font-weight:600;font-size:13px;cursor:pointer;transition:all .15s;display:flex;align-items:center;justify-content:center}
.pb:hover{background:var(--bl)}.pb.active{background:var(--b);color:#fff;border-color:var(--b)}.pb:disabled{opacity:.4;cursor:default}
.nf{position:fixed;bottom:20px;right:20px;background:var(--gr);color:#fff;padding:12px 20px;border-radius:10px;font-weight:600;font-size:13px;box-shadow:var(--shl);z-index:2000;display:none}
.nf.show{display:block;animation:fiu .3s}
@keyframes fiu{from{opacity:0;transform:translateY(10px)}to{opacity:1;transform:translateY(0)}}
tfoot td{background:var(--bp);font-weight:700;font-size:12px;color:var(--bd);padding:10px 14px}
.es{text-align:center;padding:40px 20px;color:var(--g5)}
.hl{background:#fef08a;border-radius:3px;padding:0 2px}
@media(max-width:768px){.sg{grid-template-columns:repeat(2,1fr)}.fr{grid-template-columns:1fr}.hdr-bdg{display:none}.ctrl{flex-direction:column;align-items:stretch}.srch{min-width:0}}
@media(max-width:480px){.sg{grid-template-columns:1fr}.tabs{gap:4px}.tab{padding:5px 12px;font-size:12px}.main{padding:12px 10px}}
</style>
</head>
<body>
<header class="hdr">
  <div class="hdr-in">
    <div class="hdr-logo">&#127981;</div>
    <div class="hdr-t">
      <h1>&#128232; ĐƯỜNG HẦM LÓT THÉP &mdash; NHÀ MÁY THỦY ĐIỆN A LƯỚI</h1>
      <p>Theo dõi mạng xông ống &bull; Từ Chạc 3 đến Chân giếng đứng 2 &bull; Ban QLDA NMĐ A Lưới</p>
    </div>
    <div class="hdr-bdg">&#128202; 151 Điểm đo &bull; 6 Phân đoạn</div>
  </div>
</header>

<div class="main">
  <div class="tabs" id="tabs">
    <button class="tab active" onclick="fSec('all',this)">Tất cả</button>
    <button class="tab" onclick="fSec('PĐ 1',this)">Phân đoạn 1</button>
    <button class="tab" onclick="fSec('PĐ 2',this)">Phân đoạn 2</button>
    <button class="tab" onclick="fSec('PĐ 3',this)">Phân đoạn 3</button>
    <button class="tab" onclick="fSec('PĐ 4',this)">Phân đoạn 4</button>
    <button class="tab" onclick="fSec('PĐ 5',this)">Phân đoạn 5</button>
    <button class="tab" onclick="fSec('PĐ 6',this)">Phân đoạn 6</button>
    <button class="tab tab-mx" onclick="fSec('MX',this)">&#128279; Đường hàn MX</button>
  </div>

  <div class="diag-wrap">
    <h2>&#127778; Sơ đồ tổng thể đường hầm <span style="font-size:11px;font-weight:400;color:#64748b">&mdash; nhấn vào phân đoạn để lọc</span></h2>
    <div class="diag">
      <div class="nd">
        <div class="nd-ic">&#9000;</div>
        <div class="nd-lbl">Chạc 3</div>
        <div class="nd-km">Km11+667</div>
      </div>
      <div class="seg" onclick="fSec('PĐ 1',null)">
        <div class="seg-bar" style="background:linear-gradient(90deg,#1e40af,#2563eb);border-radius:4px 0 0 4px;">PĐ 1</div>
        <div class="seg-info"><span class="seg-thick">38 mm</span><br>25 điểm<br><small>667→551</small></div>
      </div>
      <div class="seg" onclick="fSec('PĐ 2',null)">
        <div class="seg-bar" style="background:linear-gradient(90deg,#166534,#16a34a);">PĐ 2</div>
        <div class="seg-info"><span class="seg-thick">18 mm</span><br>11 điểm<br><small>551→492</small></div>
      </div>
      <div class="seg" onclick="fSec('PĐ 3',null)" style="position:relative">
        <div style="position:absolute;top:-22px;left:50%;transform:translateX(-50%);background:#fed7aa;color:#9a3412;font-size:9px;font-weight:700;padding:2px 8px;border-radius:10px;white-space:nowrap;border:1px solid #fdba74">&#9888; Địa chất yếu</div>
        <div class="seg-bar" style="background:linear-gradient(90deg,#92400e,#d97706);">PĐ 3</div>
        <div class="seg-info"><span class="seg-thick">20 mm</span><br>13 điểm<br><small>492→423</small></div>
      </div>
      <div class="seg" onclick="fSec('PĐ 4',null)">
        <div class="seg-bar" style="background:linear-gradient(90deg,#831843,#db2777);">PĐ 4</div>
        <div class="seg-info"><span class="seg-thick">20 mm</span><br>36 điểm<br><small>423→232</small></div>
      </div>
      <div class="seg" onclick="fSec('PĐ 5',null)">
        <div class="seg-bar" style="background:linear-gradient(90deg,#5b21b6,#7c3aed);">PĐ 5</div>
        <div class="seg-info"><span class="seg-thick">18 mm</span><br>46 điểm<br><small>232→987</small></div>
      </div>
      <div class="seg" onclick="fSec('PĐ 6',null)">
        <div class="seg-bar" style="background:linear-gradient(90deg,#134e4a,#0d9488);border-radius:0 4px 4px 0;">PĐ 6</div>
        <div class="seg-info"><span class="seg-thick">22 mm</span><br>20 điểm<br><small>987→886</small></div>
      </div>
      <div class="nd">
        <div class="nd-ic">&#8593;</div>
        <div class="nd-lbl">Chân GĐ2</div>
        <div class="nd-km">Km10+886</div>
      </div>
    </div>
  </div>

  <div class="sg" id="sg"></div>

  <!-- MX PANEL: shown only when MX filter active -->
  <div id="mxPanel" style="display:none;margin-bottom:20px;">
    <div style="background:linear-gradient(135deg,#6b21a8,#7c3aed);border-radius:var(--r);padding:16px 20px;color:#fff;margin-bottom:14px;">
      <div style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:10px;">
        <div>
          <div style="font-size:16px;font-weight:800;">&#128279; THỐNG KÊ ĐƯỜNG HÀN MX (Đã ốp măng xông)</div>
          <div style="font-size:12px;opacity:.85;margin-top:3px;">Các vị trí đường hàn đã được ốp măng xông xử lý khuyết tật</div>
        </div>
        <div id="mxTotalBdg" style="background:rgba(255,255,255,.2);border:1px solid rgba(255,255,255,.4);padding:6px 16px;border-radius:20px;font-size:14px;font-weight:800;"></div>
      </div>
    </div>
    <div id="mxSecGrid" style="display:grid;grid-template-columns:repeat(auto-fill,minmax(180px,1fr));gap:12px;margin-bottom:16px;"></div>
    <div style="background:#fff;border-radius:var(--r);padding:14px 18px;box-shadow:var(--sh);">
      <div style="font-size:13px;font-weight:700;color:#6b21a8;margin-bottom:10px;">&#128203; Danh sách lý trình có đường hàn MX</div>
      <div id="mxLyTrinhList" style="display:flex;flex-wrap:wrap;gap:8px;"></div>
    </div>
  </div>

  <div class="lgd">
    <h2 onclick="tgLgd(this)">&#128218; Hướng dẫn đọc ký hiệu <span id="lgdArr">&#9660;</span></h2>
    <div class="lgd-grid" id="lgdC">
      <div class="lgd-item"><strong>&#128204; Cấu trúc ký hiệu</strong><p><b>Ký tự 1 - Ký tự 2 - Ký tự 3 - Ký tự 4</b><br>Ví dụ: <code>01-CB-0,7m-5h</code></p></div>
      <div class="lgd-item"><strong>1&#65039;&#8419; Ký tự 1: Số thứ tự đường hàn</strong><p>Số 1&ndash;151, tính từ phía sau Chạc 3 đến chân giếng đứng 2</p></div>
      <div class="lgd-item"><strong>2&#65039;&#8419; Ký tự 2: Loại kiểm tra</strong><p><b>CB</b> = Các bon &bull; <b>TB</b> = Tấm bịt nút khoan phụt &bull; <b>Tap</b> = Tấm táp khuyết tật &amp; khoan phụt</p></div>
      <div class="lgd-item"><strong>3&#65039;&#8419; Ký tự 3: Khoảng cách (m)</strong><p>Khoảng cách từ lý trình đường hàn đến thượng lưu.<br>Lý trình thực = Lý trình &minus; ký tự 3</p></div>
      <div class="lgd-item"><strong>4&#65039;&#8419; Ký tự 4: Hướng giờ</strong><p>Theo đồng hồ, nhìn từ Chạc 3 về chân giếng đứng 2 (1h&ndash;12h)</p></div>
      <div class="lgd-item"><strong>&#128279; Ký hiệu khác</strong><p><b>ĐH-XX</b> = Đường hàn số XX &bull; <b>ĐHĐS-XX</b> = Đường hàn đối xứng &bull; <b>MX</b> = Mối xuyên</p></div>
    </div>
  </div>

  <div class="ctrl">
    <input type="text" class="srch" id="srch" placeholder="Tìm theo STT, lý trình, phân đoạn, ký hiệu..." oninput="doSrch()">
    <button class="btn btn-p" onclick="opMo(null)">&#43; Thêm điểm đo</button>
    <button class="btn btn-o" onclick="expCSV()">&#8659; Xuất CSV</button>
    <span class="rc" id="rc"></span>
  </div>

  <div class="tw">
    <div class="ts">
      <table id="tbl">
        <thead><tr>
          <th>STT</th><th>Phân đoạn</th><th>Lý trình</th>
          <th>Dày (mm)</th><th>Mô tả / Ký hiệu</th><th>Ghi chú</th><th>Thao tác</th>
        </tr></thead>
        <tbody id="tb"></tbody>
        <tfoot id="tf"></tfoot>
      </table>
    </div>
    <div class="pag" id="pg"></div>
  </div>
</div>

<div class="mo-ov" id="moOv">
  <div class="mo">
    <div class="mo-hd"><h3 id="moTi">&#43; Thêm điểm đo</h3><button class="mo-cl" onclick="clMo()">&times;</button></div>
    <div class="mo-bd">
      <div class="fr">
        <div class="fg"><label>STT *</label><input type="number" id="fStt" placeholder="VD: 152" min="1"></div>
        <div class="fg"><label>Phân đoạn *</label>
          <select id="fPd">
            <option value="PĐ 1">Phân đoạn 1</option><option value="PĐ 2">Phân đoạn 2</option>
            <option value="PĐ 3">Phân đoạn 3</option><option value="PĐ 4">Phân đoạn 4</option>
            <option value="PĐ 5">Phân đoạn 5</option><option value="PĐ 6">Phân đoạn 6</option>
          </select>
        </div>
      </div>
      <div class="fr">
        <div class="fg"><label>Lý trình *</label><input type="text" id="fLt" placeholder="VD: Km10+880,000"></div>
        <div class="fg"><label>Chiều dày (mm) *</label><input type="number" id="fCd" placeholder="VD: 22" min="1"></div>
      </div>
      <div class="fr fr1">
        <div class="fg"><label>Mô tả hiện trạng (mỗi ký hiệu một dòng)</label>
          <textarea id="fMt" placeholder="ĐH-152&#10;ĐHĐS-152&#10;152-CB-0,5-5h&#10;152-CB-0,5-7h"></textarea></div>
      </div>
      <div class="fr fr1">
        <div class="fg"><label>Ghi chú</label><input type="text" id="fGc" placeholder="Ghi chú (nếu có)"></div>
      </div>
    </div>
    <div class="mo-ft">
      <button class="btn btn-o" onclick="clMo()">Hủy</button>
      <button class="btn btn-g" onclick="svRec()">&#10003; Lưu</button>
    </div>
  </div>
</div>
<div class="nf" id="nf"></div>

<script>
const RD=""" + json_str + """;
let aD=RD.map(r=>({...r,phan_doan:r.phan_doan.replace('PĐ5','PĐ 5').replace('PĐ6','PĐ 6')}));
let fD=[...aD],cS='all',cQ='',cP=1,eI=null;
const PS=20;
const SC={'PĐ 1':'pd1','PĐ 2':'pd2','PĐ 3':'pd3','PĐ 4':'pd4','PĐ 5':'pd5','PĐ 6':'pd6'};
const TC={'38':'#1e40af','20':'#166534','22':'#134e4a','18':'#5b21b6'};
const SI={'PĐ 1':{r:'Km11+667 ÷ Km11+551',n:''},'PĐ 2':{r:'Km11+551 ÷ Km11+492',n:''},'PĐ 3':{r:'Km11+492 ÷ Km11+423',n:'⚠ Địa chất yếu - Đứt gãy IV,V'},'PĐ 4':{r:'Km11+423 ÷ Km11+232',n:'Đoạn dài nhất'},'PĐ 5':{r:'Km11+232 ÷ Km10+987',n:''},'PĐ 6':{r:'Km10+987 ÷ Km10+886',n:'Gần chân giếng đứng 2'}};
function gc(c){if(!c)return '';if(c.startsWith('ĐH')&&!c.startsWith('ĐHĐS'))return 'dh';if(c.startsWith('ĐHĐS'))return 'dhds';if(c.includes('-CB-'))return 'cb';if(c.includes('-TB-')||c.includes('(TB)'))return 'tb';if(c.toLowerCase().includes('tap'))return 'tap';if(c.endsWith('-MX')||c.includes('-MX'))return 'mx';return '';}
function isMX(r){return r.mo_ta_list.some(m=>m.includes('-MX'));}
function rSg(){
  const secs=['PĐ 1','PĐ 2','PĐ 3','PĐ 4','PĐ 5','PĐ 6'];
  const mxAll=aD.filter(r=>isMX(r));
  document.getElementById('sg').innerHTML=secs.map(s=>{
    const rs=aD.filter(r=>r.phan_doan===s),tk=rs.length?rs[0].chieu_day:'-';
    const segs=Math.max(0,rs.length-1);
    const mxC=rs.filter(r=>isMX(r)).length;
    const cb=rs.reduce((a,r)=>a+r.mo_ta_list.filter(m=>m.includes('-CB-')).length,0);
    const tb=rs.reduce((a,r)=>a+r.mo_ta_list.filter(m=>m.includes('-TB-')||m.includes('(TB)')).length,0);
    const tp=rs.reduce((a,r)=>a+r.mo_ta_list.filter(m=>m.toLowerCase().includes('tap')).length,0);
    const inf=SI[s]||{};const ac=(cS===s)?'active':'';
    return `<div class="sc ${ac}" onclick="fSec('${s}',null)">
      <div class="sc-hd"><div class="sc-ti">${s.replace('PĐ','Phân đoạn')}</div><div class="sc-bdg">${tk} mm</div></div>
      <div class="sc-n">${rs.length}</div>
      <div class="sc-s">điểm đo &bull; <b>${segs}</b> đoạn ống</div>
      <div class="sc-r">${inf.r||''}<br>
      <span style="color:#166534">CB:${cb}</span> &bull; <span style="color:#854d0e">TB:${tb}</span> &bull; <span style="color:#9f1239">Tap:${tp}</span>
      ${mxC?`&bull; <span style="color:#6b21a8;font-weight:700;cursor:pointer" onclick="event.stopPropagation();fSec('MX',null)">MX:${mxC}</span>`:''}
      ${inf.n?`<br><span style="color:#d97706;font-weight:600;font-size:10px">${inf.n}</span>`:''}
      </div></div>`;
  }).join('');
}
function rMX(){
  const mxRecs=aD.filter(r=>isMX(r));
  const secs=['PĐ 1','PĐ 2','PĐ 3','PĐ 4','PĐ 5','PĐ 6'];
  document.getElementById('mxTotalBdg').textContent=mxRecs.length+' vị trí MX / '+aD.length+' điểm đo';
  document.getElementById('mxSecGrid').innerHTML=secs.map(s=>{
    const cnt=mxRecs.filter(r=>r.phan_doan===s).length;
    if(!cnt)return `<div class="mx-seg-card" style="opacity:.45"><div class="mst">${s.replace('PĐ','Phân đoạn')}</div><div class="msn">0</div><div class="mss">vị trí MX</div></div>`;
    return `<div class="mx-seg-card"><div class="mst">${s.replace('PĐ','Phân đoạn')}</div><div class="msn">${cnt}</div><div class="mss">vị trí MX</div></div>`;
  }).join('');
  document.getElementById('mxLyTrinhList').innerHTML=mxRecs.map(r=>{
    const mxCodes=r.mo_ta_list.filter(m=>m.includes('-MX'));
    return `<span class="lt-chip" onclick="scrollToRow(${r.stt})" title="${mxCodes.join(', ')}">
      <b>STT ${r.stt}</b> &mdash; ${r.ly_trinh}
      <span class="mx-badge">${mxCodes.length} MX</span>
    </span>`;
  }).join('');
}
function scrollToRow(stt){
  cS='MX';cQ='';cP=1;
  aF();
  setTimeout(()=>{
    const el=document.getElementById('row-'+stt);
    if(el){el.scrollIntoView({behavior:'smooth',block:'center'});el.style.outline='3px solid #7c3aed';setTimeout(()=>el.style.outline='',2000);}
  },200);
}
function fSec(s,btn){
  cS=s;cP=1;
  document.querySelectorAll('.tab').forEach(b=>b.classList.remove('active'));
  if(btn)btn.classList.add('active');
  else{
    const ts=document.querySelectorAll('.tab');
    if(s==='all')ts[0].classList.add('active');
    else if(s==='MX'){ts[ts.length-1].classList.add('active');}
    else{const i=['PĐ 1','PĐ 2','PĐ 3','PĐ 4','PĐ 5','PĐ 6'].indexOf(s)+1;if(ts[i])ts[i].classList.add('active');}
  }
  document.getElementById('mxPanel').style.display=(s==='MX')?'block':'none';
  if(s==='MX')rMX();
  aF();rSg();
}
function doSrch(){cQ=document.getElementById('srch').value.toLowerCase();cP=1;aF();}
function aF(){
  fD=aD.filter(r=>{
    let so;
    if(cS==='all')so=true;
    else if(cS==='MX')so=isMX(r);
    else so=r.phan_doan===cS;
    if(!so)return false;
    if(!cQ)return true;
    return String(r.stt).includes(cQ)||r.ly_trinh.toLowerCase().includes(cQ)||r.phan_doan.toLowerCase().includes(cQ)||r.chieu_day.includes(cQ)||r.mo_ta_list.some(m=>m.toLowerCase().includes(cQ))||(r.ghi_chu&&r.ghi_chu.toLowerCase().includes(cQ));
  });
  rTbl();rPag();
  const label=cS==='MX'?'đường hàn MX':'điểm đo';
  document.getElementById('rc').textContent=fD.length+' / '+aD.length+' '+label;
}
function hl(t){if(!cQ)return t;const re=new RegExp('('+cQ.replace(/[.*+?^${}()|[\\]\\\\]/g,'\\\\$&')+')','gi');return t.replace(re,'<mark class="hl">$1</mark>');}
function rTbl(){
  const tb=document.getElementById('tb'),tf=document.getElementById('tf');
  const st=(cP-1)*PS,pg=fD.slice(st,st+PS);
  if(!pg.length){tb.innerHTML='<tr><td colspan="7"><div class="es"><div>🔍</div>Không tìm thấy dữ liệu</div></td></tr>';tf.innerHTML='';return;}
  tb.innerHTML=pg.map(r=>{
    const pc=SC[r.phan_doan]||'',tc=TC[r.chieu_day]||'#374151';
    const pv=r.mo_ta_list.slice(0,3).join(', ');
    const mo=r.mo_ta_list.length>3?` <span class="mt-m">+${r.mo_ta_list.length-3} nữa...</span>`:'';
    const cb=r.mo_ta_list.filter(m=>m.includes('-CB-')).length;
    const tb2=r.mo_ta_list.filter(m=>m.includes('-TB-')||m.includes('(TB)')).length;
    const tp=r.mo_ta_list.filter(m=>m.toLowerCase().includes('tap')).length;
    const mxC=r.mo_ta_list.filter(m=>m.includes('-MX')).length;
    const oi=aD.findIndex(x=>x.stt===r.stt);
    return `<tr id="row-${r.stt}">
      <td class="ts-stt">${hl(String(r.stt))}</td>
      <td class="ts-pd"><span class="pd-b ${pc}">${r.phan_doan}</span>${mxC?`<br><span class="mx-badge" style="display:inline-block;margin-top:3px">MX</span>`:''}</td>
      <td class="ts-lt">${hl(r.ly_trinh)}</td>
      <td class="ts-th"><span class="tb-bdg" style="background:${tc}22;color:${tc}">${r.chieu_day}</span></td>
      <td class="ts-mt"><span class="mt-p">${hl(pv)}</span>${mo}
        <div style="font-size:10px;color:#64748b;margin-top:3px">
          ${cb?`<span style="color:#166534">CB:${cb}</span> `:''}${tb2?`<span style="color:#854d0e">TB:${tb2}</span> `:''}${tp?`<span style="color:#9f1239">Tap:${tp}</span> `:''}${mxC?`<span style="color:#6b21a8;font-weight:700">MX:${mxC}</span>`:''}
        </div></td>
      <td style="font-size:12px;color:#64748b">${r.ghi_chu||'&mdash;'}</td>
      <td class="ts-ac">
        <button class="bsm bx" onclick="txp(${r.stt})">&#9660; Chi tiết</button>
        <button class="bsm be" onclick="opMo(${oi})" style="margin-top:4px">&#9998; Sửa</button>
      </td>
    </tr>
    <tr class="ex-row" id="ex-${r.stt}" style="display:none"><td colspan="7"><div class="ex-ct">
      <div class="ex-ti">&#128204; Toàn bộ ký hiệu tại ${r.ly_trinh} (STT ${r.stt})</div>
      <div class="chip-wrap">${r.mo_ta_list.map(m=>`<span class="chip ${gc(m)}">${hl(m)}</span>`).join('')}</div>
      ${r.ghi_chu?`<div style="margin-top:10px;font-size:12px;color:#334155"><b>Ghi chú:</b> ${r.ghi_chu}</div>`:''}
    </div></td></tr>`;
  }).join('');
  const tot=fD.length,segsF=Math.max(0,tot-1);
  const cb=fD.reduce((a,r)=>a+r.mo_ta_list.filter(m=>m.includes('-CB-')).length,0);
  const tb3=fD.reduce((a,r)=>a+r.mo_ta_list.filter(m=>m.includes('-TB-')||m.includes('(TB)')).length,0);
  const tp=fD.reduce((a,r)=>a+r.mo_ta_list.filter(m=>m.toLowerCase().includes('tap')).length,0);
  const mxF=fD.filter(r=>isMX(r)).length;
  const mxLink=mxF&&cS!=='MX'?` &mdash; <span style="cursor:pointer;text-decoration:underline;color:#7c3aed" onclick="fSec('MX',null)">Xem tất cả &#8594;</span>`:'';
  tf.innerHTML=`<tr><td colspan="2">&#931; <b>${tot}</b> điểm đo &bull; <b>${segsF}</b> đoạn ống</td><td colspan="2">CB:<b>${cb}</b> &bull; TB:<b>${tb3}</b> &bull; Tap:<b>${tp}</b></td><td colspan="3" style="color:#6b21a8">&#128279; Đường hàn MX: <b>${mxF}</b> vị trí${mxLink}</td></tr>`;
}
function txp(stt){
  const r=document.getElementById('ex-'+stt),mr=document.getElementById('row-'+stt);
  if(!r)return;const h=r.style.display==='none';
  r.style.display=h?'table-row':'none';mr.classList.toggle('exp',h);
  const b=mr.querySelector('.bx');if(b)b.innerHTML=h?'&#9650; Đóng':'&#9660; Chi tiết';
}
function rPag(){
  const tot=Math.ceil(fD.length/PS),pg=document.getElementById('pg');
  if(tot<=1){pg.innerHTML='';return;}
  let h=`<button class="pb" onclick="gP(${cP-1})" ${cP===1?'disabled':''}>&#8249;</button>`;
  for(let i=1;i<=tot;i++){
    if(i===1||i===tot||Math.abs(i-cP)<=2)h+=`<button class="pb ${i===cP?'active':''}" onclick="gP(${i})">${i}</button>`;
    else if(Math.abs(i-cP)===3)h+='<span style="padding:0 4px;color:#64748b">…</span>';
  }
  h+=`<button class="pb" onclick="gP(${cP+1})" ${cP===tot?'disabled':''}>&#8250;</button>`;
  pg.innerHTML=h;
}
function gP(p){const tot=Math.ceil(fD.length/PS);if(p<1||p>tot)return;cP=p;rTbl();rPag();document.getElementById('tbl').scrollIntoView({behavior:'smooth',block:'start'});}
function opMo(idx){
  eI=idx;const mo=document.getElementById('moOv'),ti=document.getElementById('moTi');
  if(idx!==null){const r=aD[idx];ti.textContent='✎ Chỉnh sửa điểm đo STT '+r.stt;
    document.getElementById('fStt').value=r.stt;document.getElementById('fPd').value=r.phan_doan;
    document.getElementById('fLt').value=r.ly_trinh;document.getElementById('fCd').value=r.chieu_day;
    document.getElementById('fMt').value=r.mo_ta_list.join('\\n');document.getElementById('fGc').value=r.ghi_chu||'';
  }else{ti.textContent='+ Thêm điểm đo mới';
    document.getElementById('fStt').value=aD.length+1;document.getElementById('fPd').value='PĐ 6';
    ['fLt','fCd','fMt','fGc'].forEach(id=>document.getElementById(id).value='');
  }
  mo.classList.add('open');
}
function clMo(){document.getElementById('moOv').classList.remove('open');eI=null;}
function svRec(){
  const stt=parseInt(document.getElementById('fStt').value),pd=document.getElementById('fPd').value;
  const lt=document.getElementById('fLt').value.trim(),cd=document.getElementById('fCd').value.trim();
  const mt=document.getElementById('fMt').value.trim(),gc2=document.getElementById('fGc').value.trim();
  if(!stt||!pd||!lt||!cd){alert('Vui lòng điền đầy đủ các trường bắt buộc (*)');return;}
  const rec={stt,phan_doan:pd,ly_trinh:lt,chieu_day:cd,mo_ta_list:mt?mt.split('\\n').filter(x=>x.trim()):[],ghi_chu:gc2};
  if(eI!==null){aD[eI]=rec;shN('✓ Đã cập nhật điểm đo STT '+stt);}
  else{aD.push(rec);aD.sort((a,b)=>a.stt-b.stt);shN('✓ Đã thêm điểm đo STT '+stt);}
  clMo();aF();rSg();svLS();
}
function shN(m){const n=document.getElementById('nf');n.textContent=m;n.classList.add('show');setTimeout(()=>n.classList.remove('show'),3000);}
function tgLgd(h){const c=document.getElementById('lgdC'),a=document.getElementById('lgdArr');const hid=c.style.display==='none';c.style.display=hid?'grid':'none';a.innerHTML=hid?'&#9660;':'&#9658;';}
function expCSV(){
  const rows=[['STT','Phan doan','Ly trinh','Chieu day (mm)','Mo ta','Ghi chu']];
  fD.forEach(r=>rows.push([r.stt,r.phan_doan,r.ly_trinh,r.chieu_day,r.mo_ta_list.join(' | '),r.ghi_chu]));
  const csv=rows.map(r=>r.map(c=>'"'+String(c).replace(/"/g,'""')+'"').join(',')).join('\\r\\n');
  const a2=document.createElement('a');a2.href=URL.createObjectURL(new Blob(['\\uFEFF'+csv],{type:'text/csv;charset=utf-8'}));
  a2.download='DuongHam_ALuoi_'+new Date().toISOString().slice(0,10)+'.csv';a2.click();
  shN('✓ Đã xuất '+fD.length+' bản ghi');
}
function svLS(){try{localStorage.setItem('dhALuoi',JSON.stringify(aD));}catch(e){}}
function ldLS(){try{const d=localStorage.getItem('dhALuoi');if(d){aD=JSON.parse(d);}}catch(e){}}
document.getElementById('moOv').addEventListener('click',function(e){if(e.target===this)clMo();});
ldLS();rSg();aF();
</script>
</body>
</html>"""

out = os.path.join(base, 'DU LIEU', 'DUONG_HAM_LOT_THEP_A_LUOI.html')
with open(out, 'w', encoding='utf-8') as f:
    f.write(html)
print('Created:', out)
print('Size:', os.path.getsize(out), 'bytes')
