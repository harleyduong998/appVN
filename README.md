# App.vn - Hệ thống quản lý doanh nghiệp

Giao diện dashboard hiện đại cho hệ thống quản lý doanh nghiệp, lấy cảm hứng từ Odoo.

## 📁 Cấu trúc dự án

```
AppVN/
├── index.html          # Trang chủ dashboard (mở file này để chạy)
├── styles.css          # CSS dùng chung
├── script.js           # JS dùng chung
├── DESIGN_SYSTEM.md    # Tài liệu hệ thống thiết kế
├── README.md           # File hướng dẫn này
│
├── modules/            # Các trang module của dashboard (sales, customer, crm, ...)
├── crm/                # App CRM (đang phát triển: Lead, Land, Tour, BeautyService, ...)
├── pages/              # Trang HTML lẻ (ABaSegment, aiModalSegment, automation-modal)
├── reference/          # File mockup tham khảo thiết kế (không phải app chạy)
├── docs/               # Tài liệu (.md)
└── assets/             # Tài nguyên dùng chung
    ├── img/            # Ảnh, logo
    └── icons/          # Icon SVG (trước đây là iconFa/)
```

## 🚀 Cách sử dụng

### Mở trang web:

1. **Cách 1: Mở trực tiếp bằng trình duyệt**
   - Nhấp đúp vào file `index.html`
   - Hoặc kéo thả file `index.html` vào trình duyệt

2. **Cách 2: Sử dụng Live Server (khuyến nghị)**
   - Cài đặt extension "Live Server" trong VS Code
   - Nhấp chuột phải vào `index.html` → "Open with Live Server"

### Điều hướng:

- Click vào bất kỳ module card nào để xem trang chi tiết
- Sử dụng phím mũi tên (←↑→↓) để điều hướng giữa các module
- Nhấn Enter để mở module đang được focus

## ✨ Tính năng

### Giao diện:
- ✅ Header với logo App.vn, thông báo và thông tin người dùng
- ✅ Lời chào cá nhân hóa "Xin chào, Phan Anh! 👋"
- ✅ 15 module cards với icon màu sắc đẹp mắt
- ✅ Responsive design cho mọi thiết bị (Desktop, Tablet, Mobile)

### Hiệu ứng:
- ✅ Hover effects với transform và shadow
- ✅ Ripple effect khi click
- ✅ Smooth animations và transitions
- ✅ Scroll animations khi cuộn trang
- ✅ Loading states khi chuyển trang

### Accessibility:
- ✅ Keyboard navigation (phím mũi tên)
- ✅ Focus states rõ ràng
- ✅ Semantic HTML
- ✅ ARIA labels (có thể mở rộng)

## 🎨 Modules có sẵn

1. **Quản lý bán hàng** - Quản lý đơn hàng và doanh thu
2. **Automation** - Tự động hóa quy trình
3. **Khách hàng** - Quản lý thông tin khách hàng
4. **WorkChatV2** - Hệ thống chat nội bộ
5. **Sản phẩm** - Quản lý kho sản phẩm
6. **CRM** - Quản lý quan hệ khách hàng
7. **Ưu đãi** - Quản lý chương trình khuyến mãi
8. **Loyalty** - Chương trình khách hàng thân thiết
9. **Công tác viên** - Quản lý nhân viên
10. **Combo** - Quản lý combo sản phẩm
11. **Kho hàng** - Quản lý kho và tồn kho
12. **Công thanh toán** - Quản lý thanh toán
13. **Công nợ** - Quản lý công nợ
14. **Hóa đơn điện tử** - Quản lý hóa đơn
15. **Bảo hành** - Quản lý bảo hành sản phẩm

## 🛠️ Tùy chỉnh

### Thay đổi màu sắc:
Mở file `styles.css` và chỉnh sửa các biến CSS trong `:root`:

```css
:root {
    --primary-blue: #1e40af;
    --primary-blue-dark: #1e3a8a;
    /* ... các màu khác */
}
```

### Thêm module mới:
1. Copy một module card trong `index.html`
2. Thay đổi icon, title và link
3. Tạo file HTML mới trong thư mục `modules/`

### Thay đổi thông tin người dùng:
Trong `index.html`, tìm và sửa:

```html
<span class="user-name">Phan Anh</span>
<span class="user-role">Owner</span>
```

## 📱 Responsive Breakpoints

- **Desktop**: > 1024px
- **Tablet**: 768px - 1024px
- **Mobile**: < 768px
- **Small Mobile**: < 480px

## 🌐 Trình duyệt hỗ trợ

- ✅ Chrome/Edge (khuyến nghị)
- ✅ Firefox
- ✅ Safari
- ✅ Opera

## 📝 Ghi chú

- Tất cả các trang module hiện đang là placeholder
- Bạn có thể mở rộng bằng cách thêm nội dung vào các file trong `modules/`
- Design system sử dụng CSS Variables để dễ dàng tùy chỉnh
- JavaScript sử dụng vanilla JS, không cần framework

## 📐 Design System

Tham khảo tài liệu **[DESIGN_SYSTEM.md](DESIGN_SYSTEM.md)** để biết chi tiết về:

- 🎨 **Color Palette** - Bộ màu chuẩn cho toàn hệ thống
- 📐 **Layout Structure** - Cấu trúc sidebar, header, content area
- 🔘 **Components** - Buttons, badges, forms, tables, modals, pagination
- 🎭 **Avatars & Icons** - User avatars, status indicators
- ✨ **Animations** - Hover effects, transitions, fade-in animations
- 🔧 **JavaScript Utilities** - Sidebar toggle, modal control
- 📱 **Responsive Design** - Breakpoints và best practices
- 📦 **Dependencies** - CDN links (Tailwind, Font Awesome, Flatpickr)

Tài liệu này giúp đảm bảo tính nhất quán khi phát triển các module mới.

## 🎯 Phát triển tiếp

Để phát triển thêm, bạn có thể:

1. Thêm backend API (Node.js, Python, PHP...)
2. Tích hợp database (MySQL, PostgreSQL, MongoDB...)
3. Thêm authentication/authorization
4. Xây dựng các trang module chi tiết
5. Thêm biểu đồ và dashboard analytics
6. Tích hợp với các dịch vụ bên thứ ba

---

**Phát triển bởi**: Antigravity AI Assistant  
**Ngày tạo**: 28/01/2026  
**Phiên bản**: 1.0.0
