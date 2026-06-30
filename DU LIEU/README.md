# HỆ THỐNG THEO DÕI MẠNG XÔNG - ỐP ĐƯỜNG HẦM NHÀ MÁY A LƯỚI

**Dự án:** Nhà máy Thủy điện A Lưới  
**Giai đoạn:** P4 - Năm 2026  
**Hạng mục:** Theo dõi mạng xông - ốp đường hầm ngang nhà máy  
**Phạm vi:** Từ Chạc 3 (Km11+667) đến Chân giếng đứng 2 (Km10+886) — tổng 781m

---

## 1. TỔNG QUAN DỰ ÁN

Ứng dụng web theo dõi và quản lý **151 điểm đo mối hàn** trên đường hầm thép áp lực của nhà máy thủy điện A Lưới. Hệ thống ghi nhận vị trí, loại hình xử lý và lịch sử sửa chữa cho từng điểm theo dọc tuyến hầm, phân chia thành 6 phân đoạn. Dữ liệu được lưu trữ trong một file JSON duy nhất và tự động nhúng vào HTML khi build.

### Mục đích sử dụng
- Theo dõi tình trạng các mối hàn ống thép lót hầm
- Quản lý lịch sử xử lý nứt vật liệu cơ bản
- Lưu trữ thông tin tăng cường mạng xông qua vùng địa chất yếu
- Tra cứu và xuất báo cáo theo từng phân đoạn

---

## 2. CẤU TRÚC DỰ ÁN

```
DU LIEU/
├── DU_LIEU_DUONG_HAM.json            ← NGUỒN DỮ LIỆU DUY NHẤT (chỉ sửa ở đây)
├── DUONG_HAM_LOT_THEP_A_LUOI.html   ← Ứng dụng chạy offline (được build tự động)
├── tai-lieu.json                     ← Metadata 6 tài liệu PDF tham chiếu
├── CAP_NHAT_GITHUB.cmd               ← Script 1 nhấp: build + commit + push
├── CAP_NHAT_DU_LIEU.ps1              ← Build script: nhúng JSON → HTML, đồng bộ website/
├── TAO_DANH_MUC_TAI_LIEU.ps1        ← Tạo lại tai-lieu.json từ danh sách file trong TAI LIEU/
├── SUA_LOI_GIT_CHAY_1_LAN.bat       ← Chạy 1 lần (Admin) nếu git bị Defender chặn
├── README.md                         ← File này
├── TAI LIEU/                         ← Tài liệu kỹ thuật PDF (6 file)
└── website/
    └── index.html                    ← Phiên bản GitHub Pages (đồng bộ tự động từ file chính)
```

---

## 3. KIẾN TRÚC DỮ LIỆU — QUAN TRỌNG

### Nguyên tắc một nguồn sự thật

```
DU_LIEU_DUONG_HAM.json          ← Chỉ sửa dữ liệu ở đây
        │
        │  CAP_NHAT_DU_LIEU.ps1 (tự động chạy qua .cmd)
        ▼
DUONG_HAM_LOT_THEP_A_LUOI.html  ← const RD=[...] được nhúng tự động
        │                           Sửa CSS/HTML/JS trực tiếp ở file này
        │  (copy toàn bộ tự động)
        ▼
website/index.html               ← KHÔNG sửa tay — luôn là bản sao của file chính
        │
        │  CAP_NHAT_GITHUB.cmd
        ▼
GitHub Pages (online)
```

**Quy tắc:**

- Không bao giờ sửa trực tiếp `const RD` bên trong HTML.
- Không bao giờ sửa tay `website/index.html` — file này bị ghi đè hoàn toàn mỗi lần build.
- Mọi thay đổi giao diện (CSS/HTML/JS): sửa trong `DUONG_HAM_LOT_THEP_A_LUOI.html`.
- Mọi thay đổi dữ liệu: sửa trong `DU_LIEU_DUONG_HAM.json`.
- Sau đó nhấp đúp `CAP_NHAT_GITHUB.cmd` — script tự build và đẩy lên.

### Tại sao không đọc JSON trực tiếp từ HTML?

Trình duyệt **chặn `fetch()` khi mở file HTML qua `file://`** (giao thức local). Nếu HTML đọc JSON bằng fetch, nó chỉ hoạt động trên HTTP server (GitHub Pages) — mở offline thì trắng dữ liệu. Giải pháp: script build nhúng toàn bộ JSON thành `const RD=[...]` ngay trong HTML, đảm bảo hoạt động cả offline lẫn online.

### Dữ liệu tài liệu (tai-lieu.json)

`tai-lieu.json` cũng được nhúng vào HTML dưới dạng `DOCS_EMBEDDED` (cùng lý do). Khi mở offline: dùng data nhúng. Khi mở qua HTTP: fetch từ file JSON để lấy bản mới nhất.

---

## 4. CÁC PHÂN ĐOẠN ĐƯỜNG HẦM

| Phân đoạn | Lý trình | Chiều dài | Số điểm | Chiều dày ống | Ghi chú |
| --- | --- | --- | --- | --- | --- |
| PĐ 1 | Km11+667 → Km11+551 | 116m | 25 | 38 mm | |
| PĐ 2 | Km11+551 → Km11+492 | 59m | 11 | 18 mm | |
| PĐ 3 | Km11+492 → Km11+423 | 69m | 13 | 20 mm | ⚠ Địa chất yếu — Đứt gãy IV,V |
| PĐ 4 | Km11+423 → Km11+232 | 191m | 36 | 20 mm | Đoạn dài nhất |
| PĐ 5 | Km11+232 → Km10+987 | 245m | 46 | 18 mm | |
| PĐ 6 | Km10+987 → Km10+886 | 101m | 20 | 22 mm | Gần chân giếng đứng 2 |
| **Tổng** | | **781m** | **151** | | |

---

## 5. HỆ THỐNG MÃ HÓA DỮ LIỆU

### 5.1 Loại mối hàn / xử lý

| Mã | Tên đầy đủ | Ý nghĩa |
|----|------------|---------|
| **ĐH** | Đường Hàn | Mối hàn chính trên ống |
| **ĐHĐS** | Đường Hàn Dự Phòng | Mối hàn dự phòng / tăng cường |
| **-CB-** | Cơ Bản | Xử lý nứt vật liệu cơ bản |
| **-TB-** / **(TB)** | Tăng Cường | Mối hàn tăng cường |
| **TAP** | Tạp | Mối hàn tạm thời / thử nghiệm |
| **-MX** | Mạng Xông | Vùng đặt mạng xông tăng cường |
| **CBCV** | Cán bộ công vụ | Điểm kiểm tra cán bộ — hiển thị riêng trên sơ đồ |

### 5.2 Định dạng mã CB (Cơ Bản)

```
[Vị trí]-CB-[Chiều sâu]m-[Thời gian]h
Ví dụ: 01-CB-0,7m-5h  →  Điểm 01, khoan sâu 0,7m, bơm 5 giờ
        03-CB-2,8m-7h  →  Điểm 03, khoan sâu 2,8m, bơm 7 giờ
```

### 5.3 Màu sắc tick trên sơ đồ (theo số lượng mạng xông)

| Màu | Ý nghĩa |
|-----|---------|
| Xanh lá nhạt | Chưa có mạng xông |
| Vàng | Đã đặt 1 mạng xông |
| Cam | Đã đặt 2 mạng xông |
| Đỏ | Đã đặt 3 mạng xông trở lên |

---

## 6. CẤU TRÚC BẢN GHI DỮ LIỆU (DU_LIEU_DUONG_HAM.json)

Mỗi bản ghi trong file JSON có dạng:

```json
{
  "stt": 1,
  "phan_doan": "PĐ 1",
  "ly_trinh": "Km11+667,421",
  "chieu_day": "38",
  "mo_ta_list": [
    "ĐH-01",
    "ĐH-01.1",
    "01-CB-0,7m-5h"
  ],
  "ghi_chu": ""
}
```

| Trường | Kiểu | Mô tả |
| ------ | ---- | ----- |
| `stt` | số | Số thứ tự điểm đo (1–151) |
| `phan_doan` | chuỗi | `"PĐ 1"` đến `"PĐ 6"` |
| `ly_trinh` | chuỗi | Lý trình thực tế tại điểm đo (dạng `Km11+667,421`) |
| `chieu_day` | chuỗi | Chiều dày ống (mm) |
| `mo_ta_list` | mảng chuỗi | Danh sách mã xử lý tại điểm này |
| `ghi_chu` | chuỗi | Ghi chú tự do |

---

## 7. CÁCH THÊM / SỬA DỮ LIỆU

### Thêm hoặc sửa bản ghi đường hàn

1. Mở `DU_LIEU_DUONG_HAM.json` bằng Notepad hoặc VS Code
2. Thêm / sửa bản ghi theo đúng cấu trúc JSON ở mục 6
3. Nhấp đúp `CAP_NHAT_GITHUB.cmd` — script tự build HTML, đồng bộ website/ và push lên GitHub

### Thêm tài liệu PDF mới

1. Copy file PDF vào thư mục `TAI LIEU\`
2. Chạy `TAO_DANH_MUC_TAI_LIEU.ps1` để tự động tạo lại `tai-lieu.json` từ danh sách file
3. Mở `tai-lieu.json`, điền nội dung trường `summary` cho file vừa thêm
4. Mở `DUONG_HAM_LOT_THEP_A_LUOI.html`, tìm `const DOCS_EMBEDDED=`, thêm cùng dữ liệu vào mảng (để offline cũng hoạt động)
5. Nhấp đúp `CAP_NHAT_GITHUB.cmd`

---

## 8. TÍNH NĂNG ỨNG DỤNG

### Bảng dữ liệu

- Phân trang 20 bản ghi/trang, tìm kiếm, lọc theo phân đoạn
- Mở rộng từng hàng để xem đầy đủ thông tin chi tiết
- Thêm/sửa bản ghi (yêu cầu mật khẩu)

### Sơ đồ trực quan tuyến hầm

- Hiển thị toàn tuyến 781m chia 6 phân đoạn, mỗi đoạn rộng theo chiều dài thực tế
- Tick mark từng điểm đo được định vị theo lý trình thực tế (không đều đặn)
- Màu tick theo số mạng xông đã đặt (xanh/vàng/cam/đỏ)
- Tick điểm CBCV có viền riêng để phân biệt
- **Hover vào tick**: hiện popup mờ với thông tin chi tiết — tự đóng sau 250ms khi rời chuột
- **Click vào tick**: ghim popup (nền tối, không tự đóng) cho đến khi nhấn X
- **Số thứ tự hiện trên tick**: khi hover, STT của điểm đo hiện theo chiều dọc ngay trên tick
- **Popup có thể kéo thả** tự do trong màn hình

### Vùng đứt gãy

- 9 vùng đứt gãy bậc IV được đánh dấu màu đỏ trên sơ đồ
- Vị trí theo lý trình thực tế, tọa độ đồng nhất với tick mark
- Rê chuột vào vùng đỏ để xem phạm vi lý trình

### Km-mark

- Các mốc km được hiển thị đúng vị trí theo chiều dài thực tế tuyến hầm

### Thống kê theo phân đoạn

- Đếm số điểm theo từng loại xử lý theo thời gian thực

### Tài liệu tham chiếu

- Liên kết trực tiếp tới 6 bản vẽ kỹ thuật PDF, hoạt động cả offline và online

---

## 9. QUY TRÌNH CẬP NHẬT THƯỜNG NGÀY

```text
Sửa dữ liệu  →  DU_LIEU_DUONG_HAM.json
                        │
              Nhấp đúp CAP_NHAT_GITHUB.cmd
                        │
              ┌─────────▼──────────────────────────┐
              │ Bước 1: Build                       │
              │   CAP_NHAT_DU_LIEU.ps1:             │
              │   - Nhúng JSON → const RD trong HTML│
              │   - Copy toàn bộ HTML → website/    │
              │ Bước 2: Commit                      │
              │   git add + git commit              │
              │ Bước 3: Push                        │
              │   git push → GitHub Pages cập nhật │
              └────────────────────────────────────┘
```

**Lưu ý Windows Defender:** Nếu bước Commit báo lỗi, chạy `SUA_LOI_GIT_CHAY_1_LAN.bat` bằng quyền Administrator một lần là hết.

---

## 10. TÀI LIỆU KỸ THUẬT THAM CHIẾU

| # | Tên tài liệu | Nội dung |
|---|-------------|---------|
| 0 | QDPD Ban hành lý trình đường hầm | Quy định phân đoạn, lý trình chính thức |
| 1 | QDPD Xử lý nứt VL cơ bản PĐ2 - 2021 | Quy trình xử lý nứt phân đoạn 2 |
| 2 | BVTC Xử lý Km11+326 & Km11+368 - móp ống 2021 | Bản vẽ sửa chữa ống bị móp |
| 3 | BVTK Mạng xông qua vùng đứt gãy Km11+200÷500 - 2021 | Thiết kế mạng xông vùng địa chất yếu |
| 4 | QDPD BVTK Gia cường mạng xông - 2022 | Quy định tăng cường mạng xông |
| 5 | BV Hoàn công 15.2022.XL-AL-KYHC | Bản vẽ hoàn công công trình |

---

## 11. THÔNG TIN KỸ THUẬT

- **Nền tảng**: HTML/CSS/JavaScript thuần, không phụ thuộc thư viện ngoài
- **Dữ liệu đường hàn**: Quản lý trong `DU_LIEU_DUONG_HAM.json`, tự động nhúng vào HTML khi build
- **Dữ liệu tài liệu**: Quản lý trong `tai-lieu.json`, nhúng sẵn vào HTML (`DOCS_EMBEDDED`) cho offline
- **Phiên bản web**: GitHub Pages — `website/index.html` là bản copy tự động của file chính
- **Tương thích**: Mọi trình duyệt hiện đại, có responsive mobile
- **Build tool**: PowerShell 5.1 (`CAP_NHAT_DU_LIEU.ps1`)

---

## 12. LỊCH SỬ CẬP NHẬT

| Ngày | Nội dung |
| ---- | -------- |
| 14/06/2026 | **Kiến trúc 1 nguồn**: `website/index.html` giờ là bản copy tự động của file chính — không cần sửa 2 file |
| 14/06/2026 | **Căn chỉnh lý trình**: Sửa flex phân đoạn theo chiều dài thực (116:59:69:191:245:101m), tick mark định vị theo lý trình tuyệt đối, 9 vùng đứt gãy tính lại theo công thức chuẩn |
| 14/06/2026 | **Hover/Pin popup**: Rê chuột = popup mờ tự đóng; Click = ghim popup với nền tối cho đến khi nhấn X |
| 14/06/2026 | **STT trên tick**: Khi hover vào tick, số thứ tự điểm đo hiện theo chiều dọc ngay trên tick |
| 28/05/2026 | Cập nhật dữ liệu lần 3 |
| 23/05/2026 | Thêm 9 vùng đứt gãy bậc IV trên sơ đồ, cập nhật dữ liệu lần 2 |
| 2026 | Thêm popup kéo thả, thông báo mobile, khởi tạo hệ thống |

---

*Dự án: Nhà máy Thủy điện A Lưới | Phòng Kỹ thuật | Năm 2026*
