# Design System - App.vn

> Tài liệu hướng dẫn thiết kế và phong cách giao diện cho toàn bộ hệ thống App.vn

## 🎨 Color Palette

### Primary Colors
```css
--primary-blue: #1B3DA1;        /* Main brand color */
--primary-blue-dark: #0b2060;   /* Darker variant for gradients */
--primary-blue-light: #2563eb;  /* Lighter variant for hover states */
```

### Secondary Colors
```css
--green-success: #8BC34A;       /* Success states, online indicators */
--blue-info: #3b82f6;          /* Info messages, links */
--red-error: #ef4444;          /* Error states, alerts */
--orange-warning: #fb923c;     /* Warning states */
--yellow-attention: #fbbf24;   /* Attention, highlights */
```

### Neutral Colors
```css
--gray-50: #F9FAFB;    /* Lightest background */
--gray-100: #F3F4F6;   /* Light background */
--gray-200: #E5E7EB;   /* Borders, dividers */
--gray-300: #D1D5DB;   /* Disabled states */
--gray-400: #9CA3AF;   /* Placeholder text */
--gray-500: #6B7280;   /* Secondary text */
--gray-600: #4B5563;   /* Body text */
--gray-700: #374151;   /* Headings */
--gray-800: #1F2937;   /* Dark text */
--gray-900: #111827;   /* Darkest text */
```

## 📐 Layout Structure

### Global Sidebar (Dark Blue)
```html
<!-- Width: 64px collapsed, 256px expanded -->
<div class="w-16 sidebar-pro-style text-white flex flex-col">
  <!-- Logo with Mega Menu -->
  <div class="px-3 mb-8 flex items-center h-10 relative group">
    <div onclick="window.location.href='../index.html'"
         class="h-10 w-10 bg-white rounded-lg flex items-center justify-center">
      <img src="../logo.png" alt="App.vn Logo" class="w-7 h-7 object-contain">
    </div>
    <span class="sidebar-text ml-3 font-bold text-xl opacity-0">App.vn</span>
  </div>
  
  <!-- Navigation Items -->
  <nav class="w-full flex-1 flex flex-col gap-2 px-3">
    <!-- Active Item -->
    <a href="#" class="flex items-center h-10 px-2 rounded-lg sidebar-icon-active">
      <i class="fa-solid fa-icon"></i>
      <span class="sidebar-text ml-3 text-sm opacity-0">Menu Item</span>
    </a>
  </nav>
  
  <!-- Toggle Button -->
  <div class="p-4 border-t border-white/10 mt-auto">
    <button onclick="toggleSidebar()">
      <i class="fa-solid fa-chevron-left" id="toggle-icon"></i>
    </button>
  </div>
</div>
```

**Sidebar Gradient:**
```css
.sidebar-pro-style {
    background-color: #1B3DA1;
    background-image:
        radial-gradient(80% 40% at 100% 0%, rgba(255, 255, 255, 0.2) 0%, transparent 100%),
        radial-gradient(60% 40% at 0% 100%, rgba(255, 255, 255, 0.1) 0%, transparent 100%),
        linear-gradient(160deg, #1B3DA1 0%, #0b2060 100%);
}
```

### Secondary Sidebar (White)
```html
<!-- Width: 256px - 320px depending on module -->
<div class="w-64 bg-white border-r border-gray-200 flex flex-col">
  <!-- Search Bar -->
  <div class="p-3 border-b border-gray-100">
    <div class="relative">
      <i class="fa-solid fa-magnifying-glass absolute left-3 top-1/2 -translate-y-1/2 text-gray-400"></i>
      <input type="text" placeholder="Tìm kiếm..."
             class="w-full pl-8 pr-3 py-2 bg-gray-50 border border-gray-200 rounded-lg">
    </div>
  </div>
  
  <!-- Content Area -->
  <div class="flex-1 overflow-y-auto p-4">
    <!-- Filter items, categories, etc. -->
  </div>
</div>
```

### Main Content Area
```html
<div class="flex-1 flex flex-col bg-white">
  <!-- Header Bar -->
  <div class="h-14 border-b border-gray-200 flex items-center justify-between px-4">
    <!-- Filters, search, actions -->
  </div>
  
  <!-- Content -->
  <div class="flex-1 overflow-auto p-4">
    <!-- Tables, cards, kanban, etc. -->
  </div>
  
  <!-- Footer (Pagination) -->
  <div class="p-4 border-t border-gray-100 flex items-center justify-between">
    <!-- Pagination controls -->
  </div>
</div>
```

## � Hero Section (Standard UI)
Dùng cho phần đầu của các trang quản lý chính, hiển thị tên module, mô tả ngắn và các nút hành động nhanh. Lấy từ [reference-customer.html](reference-customer.html) làm chuẩn.

**Cấu trúc HTML:**
```html
<div class="mx-4 mt-4 p-5 rounded-2xl bg-[#0F2670] bg-gradient-to-r from-[#0F2670] via-[#1B3DA1] to-[#0F2670] relative overflow-hidden group shadow-xl">
    <!-- Status Badge (Optional) -->
    <div class="absolute top-4 right-5 z-10">
        <div class="flex items-center gap-2 px-3 py-1 bg-black/20 backdrop-blur-md rounded-full border border-white/10">
            <span class="w-1.5 h-1.5 rounded-full bg-green-400 animate-pulse shadow-[0_0_8px_rgba(74,222,128,0.8)]"></span>
            <span class="text-[9px] font-bold text-white/90 tracking-widest uppercase">Neural Engine Ready</span>
        </div>
    </div>

    <!-- Content -->
    <div class="relative z-10">
        <h2 class="text-xl font-bold text-white mb-2 flex items-center gap-2">
            [Tên Module]
        </h2>
        <p class="text-xs text-blue-100/70 mb-5 max-w-xl leading-relaxed">
            [Mô tả ngắn gọn về chức năng của module, tối đa 2 dòng để giữ giao diện gọn gàng.]
        </p>

        <!-- Action Buttons -->
        <div class="flex items-center gap-3">
            <button class="flex items-center gap-2 px-4 py-2 bg-white/10 hover:bg-white/15 text-white text-[11px] font-bold rounded-lg border border-white/10 transition-all uppercase tracking-wide">
                <i class="fa-solid fa-rotate text-[10px]"></i> [Action 1]
            </button>
            <button class="flex items-center gap-2 px-4 py-2 bg-white text-[#1B3DA1] text-[11px] font-bold rounded-lg hover:shadow-lg transition-all uppercase tracking-wide">
                <i class="fa-solid fa-wand-magic-sparkles text-[10px]"></i> [AI Action]
            </button>
            <button class="flex items-center gap-2 px-4 py-2 bg-[#FBBF24] hover:bg-[#F59E0B] text-white text-[11px] font-bold rounded-lg transition-all uppercase tracking-wide">
                <i class="fa-solid fa-book-open text-[10px]"></i> [Guide]
            </button>
        </div>
    </div>

    <!-- Abstract Decorations -->
    <div class="absolute top-0 right-0 w-64 h-64 bg-white/5 rounded-full -mr-20 -mt-20 blur-3xl group-hover:bg-white/10 transition-colors"></div>
    <div class="absolute bottom-0 right-10 opacity-10">
        <i class="fa-solid fa-star text-9xl text-white transform rotate-12"></i>
    </div>
</div>
```

**Quy tắc thiết kế:**
- **Background:** Sử dụng gradient từ `#0F2670` qua `#1B3DA1` về `#0F2670` theo chiều ngang.
- **Bo góc:** `rounded-2xl` (1rem).
- **Padding:** `p-5` để tạo không gian thoáng.
- **Tiêu đề:** `text-xl font-bold text-white`.
- **Nội dung:** `text-xs text-blue-100/70`, giới hạn `max-w-xl`.
- **Nút bấm:** Text in hoa (`uppercase`), font size nhỏ (`text-[11px]`), font weight đậm (`font-bold`).
- **Hiệu ứng:** Thêm lớp trang trí `blur-3xl` và icon mờ ở background để tăng tính thẩm mỹ.

## �🔘 Components

### Buttons

**Primary Button:**
```html
<button class="bg-[#1B3DA1] hover:bg-blue-800 text-white px-4 py-2 rounded-lg text-sm font-semibold shadow-sm transition flex items-center gap-2">
  <i class="fa-solid fa-plus"></i> Thêm mới
</button>
```

**Secondary Button:**
```html
<button class="px-4 py-2 border border-gray-300 rounded-lg text-sm font-semibold text-gray-600 hover:bg-white hover:text-gray-800 transition">
  Hủy bỏ
</button>
```

**Icon Button:**
```html
<button class="w-8 h-8 flex items-center justify-center text-gray-400 hover:bg-gray-100 rounded-lg transition">
  <i class="fa-solid fa-filter"></i>
</button>
```

### Status Badges

```html
<!-- Success/Active -->
<span class="px-2 py-1 rounded bg-green-100 text-green-700 text-[10px] font-bold uppercase">
  Đang bán
</span>

<!-- Warning -->
<span class="px-2 py-1 rounded bg-orange-100 text-orange-600 text-[10px] font-bold uppercase">
  Chờ xử lý
</span>

<!-- Error/Inactive -->
<span class="px-2 py-1 rounded bg-red-100 text-red-600 text-[10px] font-bold uppercase">
  Đã hủy
</span>

<!-- Info -->
<span class="px-2 py-1 rounded bg-blue-100 text-blue-600 text-[10px] font-bold uppercase">
  Mới
</span>
```

### Form Inputs

**Text Input:**
```html
<div>
  <label class="block text-sm font-medium text-gray-700 mb-1">
    Tên trường <span class="text-red-500">*</span>
  </label>
  <input type="text"
         class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 placeholder-gray-400 text-sm"
         placeholder="Nhập nội dung...">
</div>
```

**Select Dropdown:**
```html
<select class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 text-sm bg-white">
  <option>Chọn một tùy chọn</option>
  <option>Option 1</option>
  <option>Option 2</option>
</select>
```

**Toggle Switch:**
```html
<label class="relative inline-flex items-center cursor-pointer">
  <input type="checkbox" checked class="sr-only peer">
  <div class="w-11 h-6 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-blue-300 rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-[#1B3DA1]"></div>
</label>
```

### Data Tables

```html
<table class="w-full text-left border-collapse">
  <thead class="bg-gray-50 sticky top-0 z-10">
    <tr class="text-xs text-gray-500 uppercase font-semibold">
      <th class="p-4 w-10">
        <input type="checkbox" class="rounded border-gray-300 text-[#1B3DA1] focus:ring-[#1B3DA1]">
      </th>
      <th class="p-4">Tên cột</th>
      <th class="p-4 text-right">Thao tác</th>
    </tr>
  </thead>
  <tbody class="divide-y divide-gray-100">
    <tr class="hover:bg-gray-50/50 transition">
      <td class="p-4">
        <input type="checkbox" class="rounded border-gray-300">
      </td>
      <td class="p-4 text-sm text-gray-600">Nội dung</td>
      <td class="p-4 text-right">
        <button class="text-gray-400 hover:text-[#1B3DA1] px-2">
          <i class="fa-solid fa-pen"></i>
        </button>
      </td>
    </tr>
  </tbody>
</table>
```

### Modals

**Full-screen Modal:**
```html
<div id="modal-id" class="fixed inset-0 z-[100] hidden items-center justify-center bg-black/50 backdrop-blur-sm transition-opacity duration-300">
  <div class="bg-white w-full max-w-6xl h-[90vh] rounded-xl shadow-2xl flex flex-col overflow-hidden">
    
    <!-- Header -->
    <div class="px-6 py-4 border-b border-gray-100 flex items-center justify-between shrink-0 bg-gray-50/50">
      <h2 class="text-xl font-bold text-[#1B3DA1] flex items-center gap-2">
        <i class="fa-solid fa-icon"></i> Tiêu đề Modal
      </h2>
      <button onclick="closeModal()" class="w-8 h-8 flex items-center justify-center rounded-full hover:bg-gray-200 text-gray-500 transition">
        <i class="fa-solid fa-xmark text-lg"></i>
      </button>
    </div>
    
    <!-- Body -->
    <div class="flex-1 overflow-y-auto p-6 bg-[#F9FAFB]">
      <!-- Content here -->
    </div>
    
    <!-- Footer -->
    <div class="px-6 py-4 border-t border-gray-100 bg-gray-50 flex items-center justify-end gap-3 shrink-0">
      <button onclick="closeModal()" class="px-5 py-2.5 border border-gray-300 rounded-lg text-sm font-semibold text-gray-600 hover:bg-white transition">
        Hủy bỏ
      </button>
      <button class="px-5 py-2.5 bg-[#1B3DA1] text-white rounded-lg text-sm font-bold hover:bg-blue-800 shadow-md transition flex items-center gap-2">
        <i class="fa-solid fa-save"></i> Lưu lại
      </button>
    </div>
    
  </div>
</div>
```

### Pagination

```html
<div class="p-4 border-t border-gray-100 flex items-center justify-between">
  <span class="text-xs text-gray-500">Hiển thị 1-10 của 1,204 mục</span>
  <div class="flex items-center gap-1">
    <button class="w-8 h-8 rounded border border-gray-200 flex items-center justify-center text-xs text-gray-500 hover:bg-gray-50">
      <<
    </button>
    <button class="w-8 h-8 rounded bg-[#1B3DA1] text-white flex items-center justify-center text-xs font-bold shadow-sm">
      1
    </button>
    <button class="w-8 h-8 rounded border border-gray-200 flex items-center justify-center text-xs text-gray-500 hover:bg-gray-50">
      2
    </button>
    <span class="text-gray-400 text-xs px-1">...</span>
    <button class="w-8 h-8 rounded border border-gray-200 flex items-center justify-center text-xs text-gray-500 hover:bg-gray-50">
      >>
    </button>
  </div>
</div>
```

## 🎭 Avatars & Icons

### User Avatar (Initials)
```html
<div class="w-10 h-10 rounded-full bg-blue-400 border-2 border-white flex items-center justify-center shadow-sm text-white font-bold text-sm">
  HA
</div>
```

### User Avatar (Image)
```html
<img src="https://images.unsplash.com/photo-..." 
     class="w-10 h-10 rounded-full object-cover"
     alt="User Avatar">
```

### Online Status Indicator
```html
<div class="relative">
  <img src="avatar.jpg" class="w-10 h-10 rounded-full">
  <span class="absolute bottom-0 right-0 w-2.5 h-2.5 bg-green-500 border-2 border-white rounded-full"></span>
</div>
```

## 📱 Responsive Breakpoints

```css
/* Mobile First Approach */
sm: 640px   /* Small devices */
md: 768px   /* Tablets */
lg: 1024px  /* Laptops */
xl: 1280px  /* Desktops */
2xl: 1536px /* Large screens */
```

## ✨ Animations & Transitions

### Hover Effects
```css
/* Card Hover */
.card-hover {
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}
.card-hover:hover {
    transform: translateY(-5px);
    box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1);
}

/* Button Hover */
.btn-hover {
    transition: all 0.2s ease-in-out;
}
```

### Fade In Animation
```css
@keyframes fadeIn {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
}

.animate-fade-in-up {
    animation: fadeIn 0.3s ease-out;
}
```

## 🔧 JavaScript Utilities

### Sidebar Toggle
```javascript
const sidebar = document.getElementById('sidebar');
const toggleIcon = document.getElementById('toggle-icon');
const sidebarTexts = document.querySelectorAll('.sidebar-text');
let isExpanded = false;

function toggleSidebar() {
    isExpanded = !isExpanded;
    
    if (isExpanded) {
        sidebar.classList.remove('w-16');
        sidebar.classList.add('w-64');
        toggleIcon.classList.add('rotate-180');
        
        setTimeout(() => {
            sidebarTexts.forEach(text => {
                text.classList.remove('opacity-0');
            });
        }, 100);
    } else {
        sidebarTexts.forEach(text => {
            text.classList.add('opacity-0');
        });
        sidebar.classList.remove('w-64');
        sidebar.classList.add('w-16');
        toggleIcon.classList.remove('rotate-180');
    }
}
```

### Modal Control
```javascript
function openModal(modalId) {
    const modal = document.getElementById(modalId);
    modal.classList.remove('hidden');
    modal.classList.add('flex');
}

function closeModal(modalId) {
    const modal = document.getElementById(modalId);
    modal.classList.add('hidden');
    modal.classList.remove('flex');
}
```

## 📦 Dependencies

### Required CDN Links
```html
<!-- Tailwind CSS -->
<script src="https://cdn.tailwindcss.com"></script>

<!-- Google Fonts (Inter) -->
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">

<!-- Font Awesome 6.4.0 -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

<!-- Flatpickr (Date Picker) - Optional -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/flatpickr/dist/flatpickr.min.css">
<script src="https://cdn.jsdelivr.net/npm/flatpickr"></script>
```

## 🎯 Best Practices

### 1. Consistency
- Luôn sử dụng cùng một bộ màu sắc từ color palette
- Giữ khoảng cách (spacing) nhất quán: 4px, 8px, 12px, 16px, 24px, 32px
- Sử dụng cùng font size: 10px, 12px, 14px, 16px, 18px, 20px, 24px

### 2. Accessibility
- Đảm bảo contrast ratio tối thiểu 4.5:1 cho text
- Sử dụng semantic HTML tags
- Thêm aria-labels cho icon buttons
- Hỗ trợ keyboard navigation

### 3. Performance
- Sử dụng CSS transforms thay vì position cho animations
- Lazy load images khi có thể
- Minimize số lượng DOM nodes
- Sử dụng CSS variables cho theming

### 4. Mobile Responsiveness
- Test trên nhiều kích thước màn hình
- Sử dụng touch-friendly button sizes (min 44x44px)
- Ẩn/hiện sidebar tự động trên mobile
- Responsive tables với horizontal scroll

## 📋 Module Checklist

Khi tạo module mới, đảm bảo có:

- [ ] Global sidebar với logo và navigation
- [ ] Secondary sidebar (nếu cần) với search và filters
- [ ] Header bar với actions và search
- [ ] Main content area với proper overflow handling
- [ ] Pagination (nếu có danh sách)
- [ ] Modals cho create/edit operations
- [ ] Responsive design cho mobile/tablet
- [ ] Hover states cho interactive elements
- [ ] Loading states (nếu có async operations)
- [ ] Empty states (khi không có data)
- [ ] Error states (khi có lỗi)

## 🔗 Reference Files

Tham khảo các file đã implement:
- `modules/sales.html` - Sales Management (2669 lines)
- `modules/automation.html` - Automation Workflow (2409 lines)
- `modules/customer.html` - Customer Management (653 lines)
- `modules/workchat.html` - WorkChat Messaging (679 lines)
- `modules/product.html` - Product Management (627 lines)
- `modules/crm.html` - CRM Lead Management (1556 lines)

---

**Last Updated:** 2026-01-28  
**Version:** 1.0  
**Maintained by:** App.vn Development Team
