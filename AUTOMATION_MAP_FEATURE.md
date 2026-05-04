# Automation Map - Tính năng Bản đồ tự động hóa doanh nghiệp

## Tổng quan
Automation Map là modal hiển thị bản đồ toàn bộ các tính năng và mô-đun cần thiết để tự động hóa quy trình bán hàng. Người dùng có thể xem tiến trình hoàn thành, quản lý các mô-đul, thêm/sửa/xóa tính năng.

### Behavior khi onLoad với Business mới
- Khi trang load hoặc người dùng chuyển đổi sang business mới:
  - **Không hiển thị module nào cả** (grid rỗng)
  - **Progress Banner**: 0/0 bước = 0%
  - **Nút "Quản lý module"**: Người dùng phải click để chọn các module cần bật
  - Sau khi chọn module từ "Quản lý module", các module được bật sẽ hiển thị trên grid
  - Tính năng trong mỗi module sẽ được render theo danh sách mặc định hoặc để trống

### Phân loại Module trong "Quản lý Module"
Modal "Quản lý module" hiển thị 2 section:
- **"Module đang sử dụng"**: Các module đã được bật (enabled = true)
  - Hiển thị các module hiện tại đang active trong grid
  - Số lượng = số module bật
  - **Với business mới**: Số lượng = 0 (không có module nào bật)
  - Có toggle để tắt module
  
- **"Module chưa sử dụng"**: Các module chưa được bật (enabled = false)
  - Hiển thị các module có sẵn nhưng chưa bật
  - Số lượng = tổng module có sẵn - số module bật
  - **Với business mới**: Số lượng = tổng module có sẵn (tất cả module)
  - Có toggle để bật module

## Cấu trúc chính

### 1. Header
- Tiêu đề: "Tự động hóa doanh nghiệp với App.vn" (kèm icon robot)
- Nút đóng modal

### 2. Tabs
- **Danh sách thiết lập**: Hiển thị grid các mô-đun với tính năng theo danh mục
- **Timeline triển khai**: Lịch triển khai các mô-đun (chưa có nội dung chi tiết)

### 3. Progress Banner
- Thanh tiến trình (progress bar) hiển thị % hoàn thành
- Hiển thị: "X / Y bước" (ví dụ: 4 / 22 bước)
- Hiển thị phần trăm (%) ở góc phải

**Logic tính toán Progress:**
- **Tổng bước (Y)**: Tính bằng tổng số tính năng của tất cả các mô-đul (hiện tại: 22)
- **Bước hoàn thành (X)**: Đếm số tính năng được check (có class "completed" hoặc checkbox checked)
- **Công thức %**: `(X / Y) × 100`
- **Cập nhật tự động**: Khi người dùng check/uncheck checkbox hoặc thêm/sửa/xóa tính năng
- **Thanh progress**: Width = `(X / Y) × 100%`
- **Hiển thị**: 
  - Progress fill (xanh #1B3DA1): `style="width: {percent}%"`
  - Progress steps: `"{X} / {Y} bước"`
  - Progress percentage: `"{percent}%"`

### 4. Manage Module Button
- Nút "Quản lý module" để mở modal quản lý danh mục

### 5. Feature Grid
Hiển thị 6 mô-đun chính:

#### a) **Khách hàng** (icon: Users, màu xanh)
- Đồng bộ khách hàng
- Bổ sung định danh khách hàng
- Phân nhóm khách hàng
- Phân nhóm theo RFM

#### b) **Bán hàng** (icon: Shopping Cart, màu lục)
- Cấu hình trạng thái
- Kết nối vận chuyển
- Cấu hình bản in

#### c) **Sản phẩm** (icon: Box, màu cam)
- Đồng bộ sản phẩm
- Quản lý danh mục
- Mapping sàn

#### d) **Loyalty** (icon: Gem, màu tím)
- Thiết lập hạng
- Thiết lập cộng điểm
- Quy trình tự động hóa

#### e) **Ưu đãi** (icon: Tag, màu đỏ)
- Tạo danh sách ưu đãi
- Gắn vào luồng chăm sóc

#### f) **MiniApp** (icon: Mobile Screen, màu xanh lam)
- Dựng Flow MiniApp
- Dựng UI MiniApp
- Xây dựng MiniApp

## Tương tác người dùng - Chi tiết từng Button

### 1. **Nút Đóng Modal (❌)** - Header
- **Vị trí**: Góc phải header
- **Hành động**: Click → Đóng modal "Tự động hóa doanh nghiệp"
- **Logic**:
  - Ẩn overlay (`automation-map-modal-overlay`)
  - Ẩn modal (`automation-map-modal`)
  - Giải phóng tất cả dropdown menu đang mở (nếu có)

### 2. **Tab "Danh sách thiết lập"** - Tabs
- **Vị trí**: Tab đầu tiên (mặc định active)
- **Hành động**: Click → Chuyển sang tab "Danh sách thiết lập"
- **Logic**:
  - Highlight tab này (class `active`)
  - Hiển thị nội dung grid các mô-đul
  - Ẩn tab "Timeline triển khai"

### 3. **Tab "Timeline triển khai"** - Tabs (Triển khai Phrase sau)
- **Vị trí**: Tab thứ hai
- **Hành động**: Click → Chuyển sang tab "Timeline triển khai"
- **Logic**:
  - Highlight tab này (class `active`)
  - Ẩn grid các mô-đul
  - Hiển thị lịch triển khai (placeholder)

### 4. **Nút "Quản lý module"** - Header Action
- **Vị trí**: Bên phải progress banner
- **Hành động**: Click → Mở modal "Quản lý module"
- **Logic**:
  - Hiển thị overlay (`manage-module-modal-overlay`)
  - Hiển thị modal (`manage-module-modal`)
  - Tải danh sách các module từ JS (mmModules)
  - Render các toggle bật/tắt module:
    - **Với business mới**: Module đang sử dụng và chưa sử dụng không có module nào
    - Người dùng click toggle để bật các module
    - Sau khi bật/tắt, cập nhật state của mmModules
    - Khi đóng modal: render lại grid với các module đang bật
    - **Cập nhật Progress Banner**: Tính toán lại tổng bước dựa trên module bật

### 5. **Checkbox Radio Button (☐)** - Mỗi tính năng
- **Vị trí**: Trước tên tính năng (class `.amm-radio`)
- **Hành động**: Click checkbox → Check/uncheck tính năng
- **Logic**:
  - Thêm/bỏ class "checked" hoặc "completed"
  - Đếm lại tổng bước hoàn thành (X) = số `.amm-radio` có class "checked"
  - Cập nhật `#amm-progress-steps`: `"{X} / 22 bước"`
  - Cập nhật `#amm-progress-fill` style: `"width: {(X/22)*100}%"`
  - Cập nhật `#amm-progress-pct` text: `"{Math.round((X/22)*100)}%"`

### 6. **Nút Menu Kebab (⋮)** - Mỗi tính năng
- **Vị trí**: Cuối mỗi dòng tính năng (class `.amm-li-menu-btn`)
- **Hành động**: Click → Toggle hiển thị/ẩn dropdown menu
- **Logic**:
  - Toggle class `open` trên `.amm-li-actions` của item này
  - Đóng tất cả dropdown menu khác (remove class `open` từ tất cả `.amm-li-actions`)
  - Hiển thị 2 nút: "Sửa" và "Xóa"

### 7. **Nút "Sửa"** - Dropdown Menu
- **Vị trí**: Trong dropdown menu mỗi tính năng
- **Hành động**: Click → Mở modal "Sửa tính năng"
- **Logic**:
  - Lấy reference của `<li>` hiện tại
  - Lấy tên tính năng từ `.amm-li-text`
  - Lấy mô tả từ `li.dataset.desc`
  - Lấy nhãn từ `li.dataset.tag`
  - Lấy ngày từ `li.dataset.dateFrom`, `li.dataset.dateTo`
  - Pre-fill form modal: `#ef-name-input`, `#ef-desc-input`, `#ef-date-from`, `#ef-date-to`, highlight tag
  - Hiển thị modal (`edit-feature-modal-overlay`)
  - Lưu reference: `efCurrentLi = li`
  - Đóng dropdown menu

### 8. **Nút "Xóa"** - Dropdown Menu
- **Vị trí**: Trong dropdown menu mỗi tính năng
- **Hành động**: Click → Xác nhận xóa
- **Logic**:
  - Lấy tên tính năng từ `.amm-li-text`
  - Hiển thị `confirm()`: `"Xóa tính năng '{name}'?"`
  - Nếu xác nhận (OK):
    - Xóa `<li>` từ DOM: `li.remove()`
    - Đếm lại tổng bước (Y) từ số lượng `<li>` còn lại (22 - 1 = 21)
    - Đếm lại bước hoàn thành (X)
    - Cập nhật progress banner
  - Nếu hủy (Cancel): không làm gì
  - Đóng dropdown menu

### 9. **Nút "Thêm tính năng" (+)** - Mỗi card module
- **Vị trí**: Góc phải dưới mỗi card module (class `.amm-card-add-btn`)
- **Hành động**: Hover card → Hiện button (opacity 1), Click → Mở modal "Thêm tính năng"
- **Logic**:
  - Lấy tên module từ `.amm-card-title` (Khách hàng, Bán hàng, v.v.)
  - Lưu reference của button: `afCurrentBtn = this`
  - Hiển thị modal (`add-feature-modal-overlay`)
  - Set tiêu đề modal: `#af-modal-title = "Thêm tính năng cho Module: {moduleName}"`
  - Clear các input field
  - Ẩn form tùy chỉnh
  - Reset checkboxes gợi ý
  - Render danh sách tính năng gợi ý từ JS

### 9.5 **Nút "Tạo tính năng tùy chỉnh"** - Modal "Thêm tính năng"
- **Vị trí**: Bên dưới danh sách tính năng gợi ý (button riêng)
- **Hành động**: Click → Mở popup "Tạo tính năng mới"
- **Logic**:
  - Hiển thị popup/modal nhỏ với form nhập:
    - Input: "Tên tính năng" (placeholder: "Nhập tên tính năng...")
    - Textarea: "Mô tả chi tiết" (nếu cần)
    - Buttons: "Thêm" và "Hủy"
  - Khi click "Thêm":
    - Lấy tên tính năng từ input
    - Kiểm tra: không được trống
    - Tạo checkbox mới trong danh sách gợi ý
    - **Tự động tick checkbox này** (checked = true)
    - Thêm vào `afCheckedSuggests` set
    - Đóng popup
    - Form vẫn mở, sẵn sàng thêm tính năng tiếp theo
  - Khi click "Hủy":
    - Đóng popup
    - Không lưu dữ liệu

### 10. **Modal "Thêm tính năng" - Nút "Xác nhận thêm"**
- **Vị trí**: Footer modal add-feature
- **Hành động**: Click → Xác nhận thêm tính năng mới
- **Logic**:
  - Lấy danh sách tính năng được chọn từ `afCheckedSuggests` (set của checkbox đã tick)
  - Kiểm tra: phải có ít nhất 1 tính năng → alert nếu không
  - Lấy module từ `afCurrentBtn.closest('.amm-card')`
  - Lấy danh sách `.amm-list` của module
  - Với mỗi tính năng cần thêm:
    - Tạo `<li>` mới với HTML: radio button + tên + nút kebab + dropdown actions
    - Thêm event listeners cho: checkbox, nút kebab, nút sửa, nút xóa
    - Append `<li>` vào `.amm-list`
    - Tăng tổng bước (Y) lên 1
  - Sau khi thêm tất cả:
    - Cập nhật progress banner: `updateProgress()`
    - Đóng modal
    - Reset state: `afCurrentBtn = null`, `afCheckedSuggests.clear()`

### 11. **Modal "Thêm tính năng" - Nút "Hủy"**
- **Vị trí**: Footer modal add-feature
- **Hành động**: Click → Đóng modal
- **Logic**:
  - Ẩn overlay (`add-feature-modal-overlay`)
  - Reset tất cả state:
    - `afCurrentBtn = null`
    - `afCheckedSuggests.clear()`
    - `afSelectedTag = null`
  - Clear tất cả input
  - Reset checkboxes gợi ý
  - Ẩn form tùy chỉnh (nếu đang mở)

### 12. **Modal "Sửa tính năng" - Nút "Lưu thay đổi"**
- **Vị trí**: Footer modal edit-feature
- **Hành động**: Click → Lưu thay đổi
- **Logic**:
  - Lấy tên mới từ `#ef-name-input`
  - Kiểm tra: tên không được trống → focus input nếu trống
  - Cập nhật `.amm-li-text`: `efCurrentLi.querySelector('.amm-li-text').textContent = newName`
  - Lưu vào data attributes của `efCurrentLi`:
    - `li.dataset.desc = #ef-desc-input.value`
    - `li.dataset.tag = efSelectedTag || ""`
    - `li.dataset.dateFrom = #ef-date-from.value`
    - `li.dataset.dateTo = #ef-date-to.value`
  - Đóng modal
  - Clear state: `efCurrentLi = null`, `efSelectedTag = null`

### 13. **Modal "Sửa tính năng" - Nút "Hủy"**
- **Vị trí**: Footer modal edit-feature
- **Hành động**: Click → Đóng modal
- **Logic**:
  - Ẩn overlay (`edit-feature-modal-overlay`)
  - Không lưu bất kỳ thay đổi nào
  - Clear state: `efCurrentLi = null`, `efSelectedTag = null`
  - Reset form

### 14. **Modal "Thêm Module" - Search Module (Input + Button)**
- **Vị trí**: Trên thư viện module (header của modal add-module)
- **Hành động**: 
  - **Nhập tên module** vào input search
  - **Click nút search (🔍)** → Lọc thư viện module
- **Logic**:
  - Lấy giá trị từ input search (case-insensitive)
  - Lọc danh sách module: `.filter(m => m.name.includes(searchText))`
  - Render lại grid (`#am-lib-grid`) với các module kết quả
  - Nếu không có kết quả: hiển thị "Không tìm thấy module"
  - Nếu input trống: hiển thị tất cả module gợi ý
  - Clear button (❌): xóa text input, hiển thị lại tất cả module

### 15. **Modal "Quản lý module" - Nút "Thêm Module"**
- **Vị trí**: Footer modal manage-module (nếu có)
- **Hành động**: Click → Mở modal "Thêm module"
- **Logic**:
  - Hiển thị modal (`add-module-modal-overlay`)
  - Render thư viện module gợi ý (`#am-lib-grid`)
  - Collapse form "Tạo Module tùy chỉnh"
  - Focus vào input search (tùy chọn)

### 16. **Modal "Quản lý module" - Nút Đóng (❌)**
- **Vị trí**: Header modal manage-module
- **Hành động**: Click → Đóng modal
- **Logic**:
  - Ẩn overlay (`manage-module-modal-overlay`)
  - Ẩn modal (`manage-module-modal`)
  - **Cập nhật grid module chính**: 
    - Xóa tất cả card module hiện tại (hoặc ẩn chúng)
    - Render lại grid với chỉ các module đang bật (enabled = true)
    - Nếu không có module nào bật: grid rỗng
  - **Cập nhật Progress Banner**: 
    - Tính toán lại tổng bước (Y) = tổng tính năng của các module bật
    - Tính toán lại bước hoàn thành (X) = số tính năng checked trong module bật
    - Cập nhật progress % theo công thức: `(X / Y) × 100`
    - Nếu Y = 0 (không có module nào bật): hiển thị "0 / 0 bước" = "0%"

### 17. **Modal "Quản lý module" - Toggle Module (Bật/Tắt)**
- **Vị trí**: Mỗi module item trong modal (nếu có)
- **Hành động**: Click toggle → Bật/tắt module
- **Logic**:
  - Lấy module name
  - Thay đổi state: `mmModules[name].enabled = !mmModules[name].enabled`
  - Cập nhật UI: style, opacity, text, icon
  - Nếu module bị tắt:
    - Loại tính năng của module khỏi tính progress
    - Nếu là business mới: tất cả module bắt đầu ở trạng thái "tắt"
  - Nếu module bị bật:
    - Tính năng của module sẽ được tính vào progress
  - Không cập nhật progress banner trong modal (chỉ cập nhật khi đóng modal)

## Dữ liệu được lưu trữ

Mỗi tính năng có thể chứa:
- **Tên tính năng**: Tên hiển thị
- **Mô tả chi tiết**: Nội dung chi tiết (lưu trong data-desc)
- **Nhãn**: Một trong 3 loại:
  - Cần phát triển mới
  - Có sẵn - cần cấu hình
  - Ưu tiên cao
- **Ngày bắt đầu**: Từ ngày triển khai (data-dateFrom)
- **Ngày kết thúc**: Đến ngày hoàn thành (data-dateTo)
- **Tính toán ngày làm việc**: Tự động tính số ngày làm việc giữa 2 ngày

## Công thức tính Progress

```
Bước hoàn thành (X) = Tổng số checkbox đã check trong tất cả các mô-đul
Tổng bước (Y) = Tổng số tính năng (checkbox) của tất cả các mô-đul
Progress % = (X / Y) × 100
Progress width = (X / Y) × 100%
```

**Ví dụ:**
- Tổng 22 tính năng
- 4 tính năng đã hoàn thành (checked)
- Progress: 4/22 bước = 18%
- Thanh progress: width 18%

## Modal liên quan

1. **Add Feature Modal**: Thêm tính năng mới cho một mô-đul
2. **Edit Feature Modal**: Sửa thông tin chi tiết tính năng
3. **Manage Module Modal**: Quản lý các mô-đul (thêm, xóa, bật/tắt)
4. **Add Module Modal**: Thêm module tùy chỉnh

---

*Cập nhật: 2026-05-04*
