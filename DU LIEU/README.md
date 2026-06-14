# HỆ THỐNG THEO DÕI MẠNG XÔNG - ỐP ĐƯỜNG HẦM NHÀ MÁY A LƯỚI

**Dự án:** Nhà máy Thủy điện A Lưới  
**Giai đoạn:** P4 - Năm 2026  
**Hạng mục:** Theo dõi mạng xông - ốp đường hầm ngang nhà máy  
**Phạm vi:** Từ Chạc 3 (Km11+667) đến Chân giếng đứng 2 (Km10+886)

---

## 1. TỔNG QUAN DỰ ÁN

Ứng dụng web theo dõi và quản lý **151 điểm đo mối hàn** trên đường hầm thép áp lực của nhà máy thủy điện A Lưới. Hệ thống ghi nhận vị trí, loại hình xử lý, và lịch sử sửa chữa cho từng điểm theo dọc tuyến hầm, phân chia thành 6 phân đoạn.

### Mục đích sử dụng
- Theo dõi tình trạng các mối hàn ống thép lót hầm
- Quản lý lịch sử xử lý nứt vật liệu cơ bản
- Lưu trữ thông tin tăng cường mạng xông qua vùng địa chất yếu
- Tra cứu và xuất báo cáo theo từng phân đoạn

---

## 2. CẤU TRÚC DỰ ÁN

```
DU LIEU/
├── DUONG_HAM_LOT_THEP_A_LUOI.html   # Ứng dụng độc lập (offline, 118.8 KB)
├── tai-lieu.json                     # Metadata tài liệu tham chiếu
├── README.md                         # File này
├── TAI LIEU/                         # Tài liệu kỹ thuật PDF
│   ├── 0. QDPD BAN HÀNH LỸ TRÌNH ĐƯỜNG HẦM...pdf
│   ├── 1. QDPD XỬ LÝ NỨT VẬT LIỆU CƠ BẢN PĐ2 NĂM 2021.pdf
│   ├── 2. BVTC XỬ LÝ TẠI VỊ TRÍ KM11-326 VA 368 _ MÓP ỐNG NĂM 2021.pdf
│   ├── 3. BVTK MĂNG XÔNG QUA VÙNG ĐỊA CHẤT ĐỨT GÃY KM11-200 DEN KM11-500 NĂM 2021.pdf
│   ├── 4. QDPD BVTK GIA CUONG MANG XONG NAM 2022.pdf
│   └── 5. BV HOAN CONG 15.2022.XL-AL-KYHC.pdf
└── website/                          # Phiên bản web (deploy GitHub Pages)
    └── index.html                    # Ứng dụng web chính
```

---

## 3. CÁC PHÂN ĐOẠN ĐƯỜNG HẦM

| Phân đoạn | Lý trình | Số điểm | Chiều dày ống | Ghi chú |
|-----------|----------|---------|---------------|---------|
| PĐ 1 | Km11+667 → Km11+500 | 25 | 38 mm | |
| PĐ 2 | Km11+500 → Km11+326 | 11 | 18 mm | |
| PĐ 3 | Km11+326 → Km11+200 | 13 | 20 mm | **Vùng địa chất yếu, đứt gãy cấp IV-V** |
| PĐ 4 | Km11+200 → Km11+000 | 36 | 20 mm | |
| PĐ 5 | Km11+000 → Km10+950 | 46 | 18 mm | |
| PĐ 6 | Km10+950 → Km10+886 | 20 | 22 mm | |
| **Tổng** | | **151** | | |

---

## 4. HỆ THỐNG MÃ HÓA DỮ LIỆU

### 4.1 Loại mối hàn / xử lý

| Mã | Tên đầy đủ | Ý nghĩa |
|----|------------|---------|
| **ĐH** | Đường Hàn | Mối hàn chính trên ống |
| **ĐHĐS** | Đường Hàn Dự Phòng | Mối hàn dự phòng / tăng cường |
| **-CB-** | Cơ Bản | Xử lý nứt vật liệu cơ bản |
| **-TB-** / **(TB)** | Tăng Cường | Mối hàn tăng cường |
| **TAP** | Tạp | Mối hàn tạm thời / thử nghiệm |
| **-MX** | Mạng Xông | Vùng đặt mạng xông tăng cường |

### 4.2 Định dạng mã CB (Cơ Bản)

```
[Vị trí]-CB-[Chiều sâu]m-[Thời gian]h
Ví dụ: 01-CB-0,7m-5h  →  Điểm 01, khoan sâu 0,7m, bơm 5 giờ
        03-CB-2,8m-7h  →  Điểm 03, khoan sâu 2,8m, bơm 7 giờ
```

### 4.3 Màu sắc theo dõi mạng xông

| Màu | Ý nghĩa |
|-----|---------|
| Xanh lá nhạt | Chưa có mạng xông |
| Vàng | Đã đặt 1 mạng xông |
| Cam | Đã đặt 2 mạng xông |
| Đỏ | Đã đặt 3 mạng xông |

---

## 5. TÍNH NĂNG ỨNG DỤNG

- **Bảng dữ liệu**: Phân trang 20 bản ghi/trang, tìm kiếm, lọc theo phân đoạn
- **Sơ đồ trực quan**: Hiển thị toàn tuyến hầm với màu trạng thái từng điểm
- **Thống kê theo phân đoạn**: Đếm số điểm theo từng loại xử lý theo thời gian thực
- **Xem chi tiết**: Mở rộng từng hàng để xem đầy đủ thông tin
- **Chỉnh sửa dữ liệu**: Thêm/sửa bản ghi (yêu cầu mật khẩu)
- **Tài liệu tham chiếu**: Liên kết trực tiếp tới 6 bản vẽ kỹ thuật PDF

---

## 6. CÁCH SỬ DỤNG

### Mở offline (không cần internet)
```
Mở trực tiếp file: DUONG_HAM_LOT_THEP_A_LUOI.html bằng trình duyệt
```

### Chạy phiên bản web (local)
```bash
cd website
npx serve -s . -l 3000
# Truy cập: http://localhost:3000
```

### Triển khai lên GitHub Pages
```bash
cd website
git add .
git commit -m "Cập nhật dữ liệu [ngày]"
git push origin main
```

---

## 7. TÀI LIỆU KỸ THUẬT THAM CHIẾU

| # | Tên tài liệu | Nội dung |
|---|-------------|---------|
| 0 | QDPD Ban hành lý trình đường hầm | Quy định phân đoạn, lý trình chính thức |
| 1 | QDPD Xử lý nứt VL cơ bản PĐ2 - 2021 | Quy trình xử lý nứt phân đoạn 2 |
| 2 | BVTC Xử lý Km11+326 & Km11+368 - móp ống 2021 | Bản vẽ sửa chữa ống bị móp |
| 3 | BVTK Mạng xông qua vùng đứt gãy Km11+200÷500 - 2021 | Thiết kế mạng xông vùng địa chất yếu |
| 4 | QDPD BVTK Gia cường mạng xông - 2022 | Quy định tăng cường mạng xông |
| 5 | BV Hoàn công 15.2022.XL-AL-KYHC | Bản vẽ hoàn công công trình |

---

## 8. LỊCH SỬ CẬP NHẬT

| Ngày | Nội dung |
|------|---------|
| 28/05/2026 | Cập nhật dữ liệu lần 3 |
| 23/05/2026 | Cập nhật dữ liệu lần 2 |
| Trước đó | Khởi tạo hệ thống, thêm tính năng kéo popup, thông báo mobile |

---

## 9. THÔNG TIN KỸ THUẬT

- **Nền tảng**: HTML/CSS/JavaScript thuần, không phụ thuộc thư viện ngoài
- **Dữ liệu**: Nhúng trực tiếp trong file HTML (151 bản ghi JSON)
- **Phiên bản web**: GitHub Pages (static site)
- **Tương thích**: Mọi trình duyệt hiện đại, có responsive mobile
- **Quản lý mã nguồn**: Git (nhánh main)

---

*Dự án: Nhà máy Thủy điện A Lưới | Phòng Kỹ thuật | Năm 2026*
