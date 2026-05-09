# AI Gợi Ý Tạo Phễu Chăm Sóc

**Module:** CRM > Quản lý Lead  
**File:** `CRM/leadAppVn.html`  
**Phiên bản:** 1.0  
**Cập nhật:** 2026-05-04

---

## Trạng thái hiển thị (UI States)

### 1. Doanh nghiệp CHƯA có phễu

Hiển thị **Empty State (Hero Center)**


Khi doanh nghiệp chưa có phễu nào, hiển thị màn hình gợi ý AI như sau:
<div align="center">

### 💡 Sẵn sàng để tăng tốc doanh thu?

<p>
Bạn chưa có phễu bán hàng nào.<br/>
Hãy để AI phân tích mục tiêu của bạn và tạo quy trình lead chuyên nghiệp chỉ trong vài giây.
</p>

<p>
<button>✨ AI Gợi ý tạo phễu</button>
<button>Tạo thủ công</button>
</p>

</div>


- Ẩn toàn bộ pipeline
- Mục tiêu: ép user tạo phễu đầu tiên

---

### 2. Doanh nghiệp ĐÃ có phễu

#### 2.1. Truy cập `/auto-task/lead` (không có funnelId)

Hiển thị:

- ❌ Không auto select phễu
- ✅ Hiển thị lại **Hero Center (giống trạng thái 1)**

---

#### 2.2. User đã chọn 1 phễu

URL:

Hiển thị:

- ✅ Pipeline Kanban theo phễu
- ✅ Hero chuyển thành **Top Hero (compact)**


---

#### 2.3. Refresh (F5)

- Nếu có `funnelId` trong URL  
→ Load lại đúng phễu đó

- Không quay về empty state ❌

---

#### 2.4. Animation chuyển trạng thái

Yêu cầu:

- Hero center → thu nhỏ lên top
- Fade + scale nhẹ
- Duration: 200–300ms
- Pipeline xuất hiện sau (delay nhẹ)

👉 Tránh jump UI

---

### 3. Thu gọn Hero (Compact Mode)

Khi đã có phễu:
Hiển thị dạng:
[ Top Bar ]
Quản lý Lead thông minh [ AI Kịch bản ] ---------------------------[ Tổng lead] [Hôm nay]....

---

## Trạng thái button "Áp dụng kịch bản này"

| Trạng thái | Điều kiện | CSS |
|---|---|---|
| Disabled | Chưa chọn kịch bản | `opacity-40 cursor-not-allowed` |
| Enabled | Đã chọn 1 kịch bản | `opacity-100 cursor-pointer hover:opacity-90` |

## Modal Tạo Phễu (Sau khi chọn "Áp dụng kịch bản này")

### Trigger
- Click: **"Áp dụng kịch bản này"** trong AI Modal

---

### UI Modal

| Trường | Bắt buộc | Mô tả | Hành vi |
|---|---|---|---|
| Tên phễu | ✅ | Input text | Auto fill từ template |
| Thư mục | — | Dropdown | Trống
| Nhóm phễu | — | Dropdown | Auto fill từ template |
| Tự động tạo task | — | Toggle on/off |
| Chuỗi hành động | —  (khi bật toggle) | Multiple select |

VD trong mockup: 
[TÁI TƯƠNG TÁC & REMARKETING] ← Nhóm phễu
LEAD CHĂM SÓC LẠI ← Tên phễu

---

### Hành vi chi tiết

#### 1. Tên phễu
- Auto fill theo tên kịch bản
- Validate:

Không được để trống

---

#### 2. Toggle "Tự động tạo task"

- Default: OFF
- Khi OFF:
  - Ẩn field "Chuỗi hành động"

- Khi ON:
  - Hiển thị field "Chuỗi hành động"
  - Không bắt buộc chọn chuỗi hành động nào

---

#### 3. Chuỗi hành động (Multiple Select)

Ví dụ option:
- Gọi điện
- Gửi SMS
- Gửi Email
- Nhắc follow-up
- Tạo lịch hẹn

## Logic tính chỉ số (Khi có `funnelId`)

Áp dụng khi:

/auto-task/lead/{funnelId}


---

### 1. Tổng lead


totalLead = count(lead WHERE funnelId = currentFunnelId)


- Bao gồm tất cả trạng thái
- Không bao gồm lead đã bị xóa

---

### 2. Lead hôm nay


leadToday = count(
lead WHERE funnelId = currentFunnelId
AND DATE(createdAt) = today
)


---

### 3. Tỷ lệ chốt (%)


closeRate = (Won (type = WON) / totalLead) * 100


Trong đó:
- `closedWon` = lead ở type WON

⚠️ Nếu `totalLead = 0` → hiển thị `0%`

---

### 4. Thất bại (%)


failRate = (closedLost / totalLead) * 100


Trong đó:
- `closedLost` = lead ở type = LOST

---

### 5. Phản hồi (thời gian trung bình) (Bỏ qua do chưa đo được)


avgResponseTime = AVG(firstResponseAt - createdAt)


- Tính theo giờ (h)
- Chỉ tính các lead đã có phản hồi

---
### 6. Tiềm năng
totalQualifiedLead = count(lead WHERE leadType = QUALIFIED)


