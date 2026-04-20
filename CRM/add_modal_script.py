import os

filepath = r'd:\AIDesign\lixi\stuff2\CRM\invoice.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Update Body x-data
new_body = '''<body class="min-h-screen flex flex-col" x-data="{ 
    isOpen: false, 
    platform: 'fpt', 
    platforms: { 
        'fpt': { type: 'Hóa đơn GTGT từ máy tính tiền', template: '1', symbol: 'C26MAA' }, 
        'viettel': { type: 'Hóa đơn doanh nghiệp', template: '2', symbol: 'C26TVH' }, 
        'matbao': { type: 'Hóa đơn điện tử', template: '1', symbol: 'C26TMC' } 
    } 
}">'''
content = content.replace('<body class="min-h-screen flex flex-col">', new_body)

# Update Button @click
new_button = '''<button @click="isOpen = true" class="px-4 py-2 bg-blue-600 border border-blue-600 rounded-lg text-[13px] font-bold text-white hover:bg-blue-700 hover:border-blue-700 transition-colors shadow-sm flex items-center gap-2">'''
content = content.replace('<button class="px-4 py-2 bg-blue-600 border border-blue-600 rounded-lg text-[13px] font-bold text-white hover:bg-blue-700 hover:border-blue-700 transition-colors shadow-sm flex items-center gap-2">', new_button)

# Inject Modal
modal_html = """
    <!-- Add Invoice Modal (Simplified 1-Column with Groups) -->
    <div x-show="isOpen" style="display: none;" class="fixed inset-0 z-50 flex items-center justify-center p-4 sm:p-6" role="dialog" aria-modal="true">
        <!-- Backdrop -->
        <div x-show="isOpen" x-transition.opacity.duration.300ms class="absolute inset-0 bg-slate-900/40 backdrop-blur-sm" @click="isOpen = false"></div>

        <!-- Modal Panel -->
        <div x-show="isOpen" x-transition:enter="transition ease-out duration-300" x-transition:enter-start="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95" x-transition:enter-end="opacity-100 translate-y-0 sm:scale-100" class="relative bg-slate-50 rounded-xl shadow-2xl w-full max-w-6xl max-h-[90vh] flex flex-col overflow-hidden">
            
            <!-- Header -->
            <div class="px-6 py-4 border-b border-slate-200 bg-white flex items-center justify-between shrink-0 shadow-sm z-10">
                <div class="flex items-center gap-4">
                    <h3 class="text-lg font-bold text-slate-800">Thêm hóa đơn mới</h3>
                    <div class="bg-blue-100 text-blue-700 text-xs font-bold px-2 py-0.5 rounded tracking-wide uppercase">Tạo mới</div>
                </div>
                <button @click="isOpen = false" class="text-slate-400 hover:text-red-500 hover:bg-red-50 p-2 rounded-lg transition-colors">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
                </button>
            </div>

            <!-- Scrollable Content -->
            <div class="flex-1 overflow-y-auto p-6 table-scrollbar">
                
                <div class="grid grid-cols-12 gap-6">
                    <!-- Left Column: TVAN & Customer -->
                    <div class="col-span-12 xl:col-span-4 space-y-6">
                        
                        <!-- Group 1: TVAN Configuration -->
                        <div class="bg-white border border-slate-200 rounded-xl shadow-sm overflow-hidden">
                            <div class="px-4 py-3 border-b border-slate-100 bg-slate-50 flex items-center gap-2">
                                <div class="w-2 h-2 rounded-full bg-blue-500"></div>
                                <h4 class="text-[13px] font-bold text-slate-800 uppercase tracking-wide">Cấu hình TVAN</h4>
                            </div>
                            <div class="p-4 space-y-4 bg-white">
                                <div>
                                    <label class="block text-xs font-bold text-slate-500 mb-1.5 uppercase">Nền tảng kết nối</label>
                                    <select x-model="platform" class="w-full px-3 py-2 bg-white border border-slate-300 rounded font-medium text-slate-800 text-[13px] focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 shadow-sm transition-shadow">
                                        <option value="fpt">Hóa đơn FPT</option>
                                        <option value="viettel">Hóa đơn Viettel</option>
                                        <option value="matbao">Hóa đơn Mắt Bão</option>
                                    </select>
                                </div>
                                
                                <div class="p-3 bg-slate-50 border border-slate-200/60 rounded grid grid-cols-2 gap-3">
                                    <div class="col-span-2">
                                        <label class="block text-[10px] font-bold text-slate-400 mb-1 uppercase">Loại hóa đơn</label>
                                        <div class="text-[13px] font-semibold text-slate-700" x-text="platforms[platform].type"></div>
                                    </div>
                                    <div>
                                        <label class="block text-[10px] font-bold text-slate-400 mb-1 uppercase">Mẫu số</label>
                                        <div class="text-[13px] font-semibold text-slate-700" x-text="platforms[platform].template"></div>
                                    </div>
                                    <div>
                                        <label class="block text-[10px] font-bold text-slate-400 mb-1 uppercase">Ký hiệu</label>
                                        <div class="text-[13px] font-semibold text-slate-700" x-text="platforms[platform].symbol"></div>
                                    </div>
                                </div>

                                <div class="grid grid-cols-2 gap-3">
                                    <div>
                                        <label class="block text-xs font-bold text-slate-500 mb-1.5 uppercase">Ngày hóa đơn</label>
                                        <input type="date" value="2026-03-27" class="w-full px-3 py-1.5 bg-white border border-slate-300 rounded text-[13px] focus:outline-none focus:ring-2 focus:ring-blue-500 shadow-sm transition-shadow text-slate-700 font-medium">
                                    </div>
                                    <div>
                                        <label class="block text-xs font-bold text-slate-500 mb-1.5 uppercase">Thanh toán</label>
                                        <select class="w-full px-3 py-1.5 bg-white border border-slate-300 rounded text-[13px] focus:outline-none focus:ring-2 focus:ring-blue-500 shadow-sm transition-shadow text-slate-700 font-medium">
                                            <option>TM/CK</option>
                                            <option>Tiền mặt</option>
                                            <option>Chuyển khoản</option>
                                        </select>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- Group 2: Customer Information -->
                        <div class="bg-white border border-slate-200 rounded-xl shadow-sm overflow-hidden">
                            <div class="px-4 py-3 border-b border-slate-100 bg-slate-50 flex items-center justify-between">
                                <div class="flex items-center gap-2">
                                    <div class="w-2 h-2 rounded-full bg-emerald-500"></div>
                                    <h4 class="text-[13px] font-bold text-slate-800 uppercase tracking-wide">Khách hàng</h4>
                                </div>
                                <button class="text-[11px] font-bold text-emerald-600 hover:text-emerald-700 uppercase flex items-center gap-1">
                                    <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-4.35-4.35m1.35-5.65a7 7 0 11-14 0 7 7 0 0114 0z"/></svg> Tra cứu
                                </button>
                            </div>
                            <div class="p-4 space-y-4 bg-white">
                                <div>
                                    <label class="block text-xs font-bold text-slate-500 mb-1.5">Tên khách hàng / Đơn vị</label>
                                    <input type="text" placeholder="Nhập tên..." class="w-full px-3 py-2 border border-slate-300 rounded text-[13px] focus:outline-none focus:ring-2 focus:ring-emerald-500 shadow-sm transition-shadow placeholder-slate-300">
                                </div>
                                <div>
                                    <label class="block text-xs font-bold text-slate-500 mb-1.5">Mã số thuế</label>
                                    <input type="text" placeholder="Nhập MST..." class="w-full px-3 py-2 border border-slate-300 rounded text-[13px] font-medium focus:outline-none focus:ring-2 focus:ring-emerald-500 shadow-sm transition-shadow placeholder-slate-300">
                                </div>
                                <div class="grid grid-cols-2 gap-3">
                                    <div>
                                        <label class="block text-xs font-bold text-slate-500 mb-1.5">Số điện thoại</label>
                                        <input type="tel" placeholder="09xx..." class="w-full px-3 py-1.5 border border-slate-300 rounded text-[13px] focus:outline-none focus:ring-2 focus:ring-emerald-500 shadow-sm transition-shadow placeholder-slate-300">
                                    </div>
                                    <div>
                                        <label class="block text-xs font-bold text-slate-500 mb-1.5">Email</label>
                                        <input type="email" placeholder="@..." class="w-full px-3 py-1.5 border border-slate-300 rounded text-[13px] focus:outline-none focus:ring-2 focus:ring-emerald-500 shadow-sm transition-shadow placeholder-slate-300">
                                    </div>
                                </div>
                                <div>
                                    <label class="block text-xs font-bold text-slate-500 mb-1.5">Địa chỉ</label>
                                    <input type="text" placeholder="Địa chỉ đầy đủ" class="w-full px-3 py-2 border border-slate-300 rounded text-[13px] focus:outline-none focus:ring-2 focus:ring-emerald-500 shadow-sm transition-shadow placeholder-slate-300">
                                </div>
                            </div>
                        </div>

                    </div>

                    <!-- Right Column: Products & Services Table -->
                    <div class="col-span-12 xl:col-span-8 flex flex-col">
                        <div class="bg-white border border-slate-200 rounded-xl shadow-sm overflow-hidden flex flex-col flex-1 h-full min-h-[500px]">
                            <div class="px-5 py-3 border-b border-slate-200 bg-slate-50 flex items-center justify-between shrink-0">
                                <div class="flex items-center gap-2">
                                    <div class="w-2 h-2 rounded-full bg-amber-500"></div>
                                    <h4 class="text-[13px] font-bold text-slate-800 uppercase tracking-wide">Hàng hóa & Dịch vụ</h4>
                                </div>
                                <button class="text-[11px] font-bold text-blue-600 hover:text-blue-800 flex items-center gap-1 bg-white border border-blue-200 px-3 py-1.5 rounded shadow-sm transition-colors hover:border-blue-300 active:scale-95">
                                    <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"/></svg>
                                    Thêm Dòng
                                </button>
                            </div>
                            
                            <div class="overflow-x-auto table-scrollbar flex-1 relative bg-white">
                                <table class="w-full text-left min-w-[1000px]">
                                    <thead class="bg-slate-50/50 border-b border-slate-200 sticky top-0 z-10 backdrop-blur">
                                        <tr>
                                            <th class="py-3 px-4 font-semibold text-[11px] text-slate-500 uppercase tracking-wider w-[280px]">Sản phẩm</th>
                                            <th class="py-3 px-3 font-semibold text-[11px] text-slate-500 uppercase tracking-wider text-center w-24">Phân loại</th>
                                            <th class="py-3 px-3 font-semibold text-[11px] text-slate-500 uppercase tracking-wider w-20">ĐVT</th>
                                            <th class="py-3 px-3 font-semibold text-[11px] text-slate-500 uppercase tracking-wider text-center w-20">SL</th>
                                            <th class="py-3 px-3 font-semibold text-[11px] text-slate-500 uppercase tracking-wider text-right w-28">Đơn giá</th>
                                            <th class="py-3 px-3 font-semibold text-[11px] text-slate-500 uppercase tracking-wider text-right w-24">C.Khấu</th>
                                            <th class="py-3 px-3 font-semibold text-[11px] text-slate-500 uppercase tracking-wider w-24">Thuế suất</th>
                                            <th class="py-3 px-3 font-semibold text-[11px] text-slate-500 uppercase tracking-wider text-right w-24">Tiền thuế</th>
                                            <th class="py-3 px-4 font-bold text-[11px] text-slate-800 uppercase tracking-wider text-right w-32">Thành tiền</th>
                                        </tr>
                                    </thead>
                                    <tbody class="divide-y divide-slate-100/80">
                                        <!-- Row 1 -->
                                        <tr class="hover:bg-slate-50 transition-colors group">
                                            <td class="py-2.5 px-4 text-sm align-top">
                                                <div class="flex items-start gap-3">
                                                    <div class="w-10 h-10 bg-slate-100 rounded border border-slate-200 shrink-0 overflow-hidden flex items-center justify-center">
                                                        <img src="https://ui-avatars.com/api/?name=SP&background=e2e8f0&color=64748b" class="w-full h-full object-cover">
                                                    </div>
                                                    <div class="flex flex-col w-full gap-1 pt-0.5">
                                                        <input type="text" value="Sản phẩm Demo A" class="font-bold text-[13px] text-slate-800 bg-transparent border-0 p-0 focus:ring-0 placeholder-slate-300 w-full focus:outline-none">
                                                        <input type="text" value="SP-001" class="text-[10px] text-slate-400 font-bold tracking-widest bg-transparent border-0 p-0 m-0 focus:ring-0 placeholder-slate-300 focus:outline-none">
                                                    </div>
                                                </div>
                                            </td>
                                            <td class="py-2.5 px-3 text-center align-top pt-3">
                                                <div class="flex flex-col gap-1.5 items-start pl-2">
                                                    <label class="flex items-center gap-1.5 text-[11px] font-bold text-slate-500 cursor-pointer hover:text-blue-600 transition-colors">
                                                        <input type="checkbox" class="w-3.5 h-3.5 text-blue-600 rounded border-slate-300 focus:ring-blue-500"> Ảo
                                                    </label>
                                                    <label class="flex items-center gap-1.5 text-[11px] font-bold text-slate-500 cursor-pointer hover:text-emerald-600 transition-colors">
                                                        <input type="checkbox" class="w-3.5 h-3.5 text-emerald-500 rounded border-slate-300 focus:ring-emerald-500" checked> Tặng
                                                    </label>
                                                </div>
                                            </td>
                                            <td class="py-2.5 px-3 align-top pt-2.5"><input type="text" value="Hộp" class="w-full px-2 py-1.5 text-[13px] border border-slate-200 rounded focus:border-blue-500 focus:ring-1 focus:ring-blue-500 outline-none transition-shadow bg-white text-slate-700"></td>
                                            <td class="py-2.5 px-3 align-top pt-2.5"><input type="number" value="1" class="w-full px-2 py-1.5 text-[13px] border border-slate-200 rounded text-center focus:border-blue-500 focus:ring-1 focus:ring-blue-500 outline-none transition-shadow bg-white font-bold text-slate-800"></td>
                                            <td class="py-2.5 px-3 align-top pt-2.5"><input type="text" value="2,500,000" class="w-full px-2 py-1.5 text-[13px] border border-slate-200 rounded text-right focus:border-blue-500 focus:ring-1 focus:ring-blue-500 outline-none font-bold text-slate-800 bg-white transition-shadow"></td>
                                            <td class="py-2.5 px-3 align-top pt-2.5"><input type="text" placeholder="0" class="w-full px-2 py-1.5 text-[13px] border border-slate-200 rounded text-right focus:border-blue-500 focus:ring-1 focus:ring-blue-500 outline-none transition-shadow bg-white"></td>
                                            <td class="py-2.5 px-3 align-top pt-2.5">
                                                <select class="w-full px-1.5 py-1.5 text-[13px] border border-slate-200 rounded focus:border-blue-500 focus:ring-1 focus:ring-blue-500 outline-none bg-white font-bold text-slate-700 transition-shadow">
                                                    <option>10%</option>
                                                    <option>8%</option>
                                                    <option>0%</option>
                                                    <option>KCT</option>
                                                </select>
                                            </td>
                                            <td class="py-2.5 px-3 text-right align-top pt-4">
                                                <div class="text-[13px] font-bold text-slate-500">250,000</div>
                                            </td>
                                            <td class="py-2.5 px-4 text-right align-top pt-3.5 relative">
                                                <div class="text-[14px] font-black text-rose-600 tracking-tight">2,750,000</div>
                                                <button class="absolute -right-2 top-3 text-slate-300 hover:text-red-500 opacity-0 group-hover:opacity-100 transition-all focus:opacity-100 p-1">
                                                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"/></svg>
                                                </button>
                                            </td>
                                        </tr>
                                        <!-- Row 2 -->
                                        <tr class="hover:bg-slate-50 transition-colors group opacity-70 hover:opacity-100 focus-within:opacity-100">
                                            <td class="py-2.5 px-4 text-sm align-top">
                                                <div class="flex items-start gap-3">
                                                    <div class="w-10 h-10 bg-slate-50 rounded border border-slate-200 border-dashed shrink-0 flex items-center justify-center text-slate-300">
                                                        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"/></svg>
                                                    </div>
                                                    <div class="flex flex-col w-full gap-1 pt-0.5">
                                                        <input type="text" placeholder="Tìm sản phẩm..." class="font-medium text-[13px] text-slate-800 bg-transparent border-0 p-0 focus:ring-0 placeholder-slate-400 w-full focus:outline-none">
                                                    </div>
                                                </div>
                                            </td>
                                            <td class="py-2.5 px-3 text-center align-top pt-4"><div class="text-[10px] text-slate-300 uppercase font-bold tracking-wider">--</div></td>
                                            <td class="py-2.5 px-3 align-top pt-2.5"></td>
                                            <td class="py-2.5 px-3 align-top pt-2.5"></td>
                                            <td class="py-2.5 px-3 align-top pt-2.5"></td>
                                            <td class="py-2.5 px-3 align-top pt-2.5"></td>
                                            <td class="py-2.5 px-3 align-top pt-2.5"></td>
                                            <td class="py-2.5 px-3 text-right align-top pt-4"></td>
                                            <td class="py-2.5 px-4 text-right align-top pt-3.5 relative"></td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                        </div>
                    </div>
                </div>

            </div>

            <!-- Footer App-like Actions -->
            <div class="p-4 border-t border-slate-200 bg-slate-50 flex items-center justify-between shrink-0 shadow-inner z-10">
                <div class="flex items-center gap-6 px-2">
                    <div class="flex flex-col text-right">
                        <span class="text-[10px] font-bold text-slate-400 uppercase tracking-widest leading-none mb-1">Tổng cộng</span>
                        <span class="text-2xl font-black text-rose-600 leading-none tracking-tight">2,750,000 <span class="text-sm font-bold opacity-80">₫</span></span>
                    </div>
                </div>
                <div class="flex items-center gap-3">
                    <button @click="isOpen = false" class="px-6 py-2.5 border border-slate-300 bg-white rounded-lg font-bold text-[13px] text-slate-600 hover:bg-slate-100 hover:text-slate-800 transition-all shadow-sm">
                        Đóng
                    </button>
                    <button class="px-8 py-2.5 rounded-lg font-bold text-[13px] text-white bg-blue-600 hover:bg-blue-700 shadow-md shadow-blue-500/40 transition-all focus:ring-4 focus:ring-blue-500/20 active:scale-95 flex items-center gap-2">
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg>
                        Lưu Hóa Đơn
                    </button>
                </div>
            </div>

        </div>
    </div>
"""

content = content.replace('</body>', f'{modal_html}\n</body>')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
