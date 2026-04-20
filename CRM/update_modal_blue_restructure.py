import os

filepath = r'd:\\AIDesign\\lixi\\stuff2\\CRM\\invoice.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Remove old modal blocks
start_marker = '    <!-- Add Invoice Modal'
end_marker = '</body>'
start_idx = content.find(start_marker)
if start_idx != -1:
    end_idx = content.find(end_marker, start_idx)
    if end_idx != -1:
        content = content[:start_idx] + content[end_idx:]

modal_html = """
    <!-- Add Invoice Modal (Restructured Blue POS Theme) -->
    <div x-show="isOpen" style="display: none;" class="fixed inset-0 z-50 flex items-center justify-center p-2 sm:p-4" role="dialog" aria-modal="true">
        <div x-show="isOpen" x-transition.opacity.duration.300ms class="absolute inset-0 bg-slate-900/40 backdrop-blur-sm" @click="isOpen = false"></div>
        
        <div x-show="isOpen" x-transition:enter="transition ease-out duration-300" x-transition:enter-start="opacity-0 scale-95" x-transition:enter-end="opacity-100 scale-100" class="relative bg-white w-full max-w-[1550px] h-[98vh] rounded shadow-2xl flex flex-col overflow-hidden text-[12px] text-slate-700 font-medium border-t-4 border-blue-600">
            
            <!-- Modal Header -->
            <div class="px-6 py-3 bg-white border-b border-slate-100 flex items-center justify-between shrink-0">
                <div class="flex items-center gap-3">
                    <div class="w-8 h-8 bg-blue-600 rounded flex items-center justify-center shadow-lg shadow-blue-100">
                        <svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M12 4v16m8-8H4"/></svg>
                    </div>
                    <div>
                        <h3 class="text-lg font-black text-slate-800 uppercase tracking-tight">Phiếu hóa đơn điện tử</h3>
                        <p class="text-[10px] text-blue-500 font-bold uppercase tracking-widest -mt-1">Professional POS System</p>
                    </div>
                </div>
                <button @click="isOpen = false" class="text-slate-400 hover:text-red-500 p-2 transition-all hover:bg-red-50 rounded">
                    <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
                </button>
            </div>

            <!-- Scrollable Content -->
            <div class="flex-1 overflow-y-auto p-4 flex flex-col gap-5 table-scrollbar bg-slate-50/50">
                
                <!-- GROUP 1: THÔNG TIN KẾT NỐI (Single Row) -->
                <div class="bg-white p-3 rounded-lg border border-slate-100 shadow-sm flex flex-col gap-3">
                    <div class="flex items-center gap-2">
                        <div class="w-1 h-4 bg-blue-600 rounded-full"></div>
                        <h4 class="text-[11px] font-black text-blue-800 uppercase tracking-widest">Group 1: Thông tin kết nối</h4>
                    </div>
                    <div class="flex items-end gap-3 overflow-x-auto no-scrollbar pb-1">
                        <div class="flex-1 min-w-[200px]">
                            <label class="block text-[10px] font-black text-slate-400 uppercase mb-1 px-1">Nền tảng TVAN</label>
                            <select x-model="platform" class="w-full h-8 px-3 bg-slate-50 border border-slate-200 rounded outline-none focus:border-blue-500 focus:bg-white text-blue-700 font-bold transition-all shadow-inner">
                                <option value="fpt">Hóa đơn FPT (TVAN)</option>
                                <option value="viettel">Hóa đơn Viettel (Doanh nghiệp)</option>
                                <option value="matbao">Hóa đơn Mắt Bão (Hệ thống)</option>
                            </select>
                        </div>
                        <div class="flex-1 min-w-[150px]">
                            <label class="block text-[10px] font-black text-slate-400 uppercase mb-1 px-1">Nghiệp vụ</label>
                            <select class="w-full h-8 px-3 bg-slate-100 border border-slate-200 rounded outline-none text-slate-500 font-bold opacity-70" disabled>
                                <option>Hóa đơn thường</option>
                            </select>
                        </div>
                        <div class="flex-1 min-w-[150px]">
                            <label class="block text-[10px] font-black text-slate-400 uppercase mb-1 px-1">Ngày hóa đơn</label>
                            <div class="relative">
                                <input type="text" value="27/03/2026" class="w-full h-8 px-3 bg-slate-50 border border-slate-200 rounded outline-none text-slate-600 font-bold">
                                <svg class="w-4 h-4 text-blue-400 absolute right-2 top-2 pointer-events-none" fill="currentColor" viewBox="0 0 24 24"><path d="M19 4h-1V2h-2v2H8V2H6v2H5c-1.11 0-1.99.9-1.99 2L3 20c0 1.1.89 2 2 2h14c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 16H5V10h14v10zm0-12H5V6h14v2zm-7 5h5v5h-5z"/></svg>
                            </div>
                        </div>
                        <div class="flex-1 min-w-[220px]">
                            <label class="block text-[10px] font-black text-slate-400 uppercase mb-1 px-1">Loại HĐ <span class="text-red-500">*</span></label>
                            <div class="h-8 px-3 bg-slate-100 border border-slate-200 rounded flex items-center text-slate-700 font-bold text-[11px]" x-text="platforms[platform].type"></div>
                        </div>
                        <div class="flex-1 min-w-[100px]">
                            <label class="block text-[10px] font-black text-slate-400 uppercase mb-1 px-1">Mẫu số</label>
                            <div class="h-8 px-3 bg-slate-100 border border-slate-200 rounded flex items-center text-slate-700 font-bold text-center justify-center" x-text="platforms[platform].template"></div>
                        </div>
                        <div class="flex-1 min-w-[120px]">
                            <label class="block text-[10px] font-black text-slate-400 uppercase mb-1 px-1">Ký hiệu</label>
                            <div class="h-8 px-3 bg-slate-100 border border-slate-200 rounded flex items-center text-slate-700 font-bold text-center justify-center italic" x-text="platforms[platform].symbol"></div>
                        </div>
                    </div>
                </div>

                <!-- GROUP 2: THÔNG TIN KHÁCH HÀNG -->
                <div class="bg-white p-3 rounded-lg border border-slate-100 shadow-sm flex flex-col gap-3">
                    <div class="flex items-center gap-2">
                        <div class="w-1 h-4 bg-emerald-500 rounded-full"></div>
                        <h4 class="text-[11px] font-black text-emerald-800 uppercase tracking-widest">Group 2: Thông tin khách hàng</h4>
                    </div>
                    <div class="grid grid-cols-4 gap-4">
                        <div class="col-span-2">
                            <label class="block text-[10px] font-black text-slate-400 uppercase mb-1 px-1">Họ tên người mua hàng</label>
                            <div class="flex">
                                <input type="text" placeholder="Nhập tên người mua..." class="flex-1 h-8 px-3 bg-slate-50 border border-slate-200 rounded-l outline-none focus:border-blue-500 focus:bg-white text-slate-800 font-bold transition-all shadow-inner">
                                <button class="bg-blue-600 text-white px-3 h-8 rounded-r hover:bg-blue-700 transition-colors flex items-center shadow-lg shadow-blue-50"><svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-4.35-4.35m1.35-5.65a7 7 0 11-14 0 7 7 0 0114 0z"/></svg></button>
                            </div>
                        </div>
                        <div>
                            <label class="block text-[10px] font-black text-slate-400 uppercase mb-1 px-1">Số điện thoại</label>
                            <input type="text" class="w-full h-8 px-3 bg-slate-50 border border-slate-200 rounded outline-none focus:border-blue-500 focus:bg-white text-slate-800 font-bold transition-all shadow-inner">
                        </div>
                        <div>
                            <label class="block text-[10px] font-black text-slate-400 uppercase mb-1 px-1">Mã số thuế</label>
                            <input type="text" placeholder="MST công ty..." class="w-full h-8 px-3 bg-slate-50 border border-slate-200 rounded outline-none focus:border-blue-500 focus:bg-white text-blue-600 font-black tracking-widest transition-all shadow-inner">
                        </div>

                        <div class="col-span-2">
                            <label class="block text-[10px] font-black text-slate-400 uppercase mb-1 px-1">Tên đơn vị / Công ty</label>
                            <input type="text" class="w-full h-8 px-3 bg-slate-50 border border-slate-200 rounded outline-none focus:border-blue-500 focus:bg-white text-slate-800 font-bold transition-all shadow-inner">
                        </div>
                        <div class="col-span-2">
                            <label class="block text-[10px] font-black text-slate-400 uppercase mb-1 px-1">Địa chỉ</label>
                            <input type="text" class="w-full h-8 px-3 bg-slate-50 border border-slate-200 rounded outline-none focus:border-blue-500 focus:bg-white text-slate-800 font-bold transition-all shadow-inner">
                        </div>

                        <div>
                            <label class="block text-[10px] font-black text-slate-400 uppercase mb-1 px-1">Email</label>
                            <input type="text" class="w-full h-8 px-3 bg-slate-50 border border-slate-200 rounded outline-none focus:border-blue-500 focus:bg-white text-slate-800 font-bold transition-all shadow-inner">
                        </div>
                        <div>
                            <label class="block text-[10px] font-black text-slate-400 uppercase mb-1 px-1">Số Fax</label>
                            <input type="text" class="w-full h-8 px-3 bg-slate-50 border border-slate-200 rounded outline-none focus:border-blue-500 focus:bg-white text-slate-800 font-bold transition-all shadow-inner">
                        </div>
                        <div class="col-span-2 flex items-end gap-3 pb-2">
                            <label class="flex items-center gap-2 cursor-pointer group">
                                <input type="checkbox" class="w-4 h-4 rounded border-slate-300 text-blue-600 focus:ring-blue-500 transition-all shadow-sm">
                                <span class="text-[11px] font-black text-slate-500 uppercase group-hover:text-blue-600 transition-colors">Khách hàng lẻ không lấy MST</span>
                            </label>
                        </div>
                    </div>
                </div>

                <!-- GROUP 3: SẢN PHẨM & DỊCH VỤ -->
                <div class="bg-white p-3 rounded-lg border border-slate-100 shadow-sm flex flex-col gap-3 flex-1 overflow-hidden">
                    <div class="flex items-center justify-between shrink-0">
                        <div class="flex items-center gap-2">
                            <div class="w-1 h-4 bg-blue-600 rounded-full"></div>
                            <h4 class="text-[11px] font-black text-blue-800 uppercase tracking-widest">Group 3: Hàng hóa, dịch vụ</h4>
                        </div>
                        <div class="flex items-center gap-2">
                            <div class="relative group/search">
                                <span class="absolute left-3 top-2 text-slate-300 group-focus-within/search:text-blue-500 transition-colors">
                                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg>
                                </span>
                                <input type="text" placeholder="Tra cứu sản phẩm (F3)..." class="w-80 h-8 pl-10 pr-4 bg-slate-50 border border-slate-200 rounded-full outline-none focus:bg-white focus:border-blue-500 focus:ring-4 focus:ring-blue-500/10 transition-all font-bold text-slate-600">
                            </div>
                            <button class="h-8 px-4 bg-blue-100 text-blue-700 rounded-full font-black text-[10px] uppercase hover:bg-blue-600 hover:text-white transition-all border border-blue-200">Chọn nhanh</button>
                            <button class="h-8 px-4 bg-slate-800 text-white rounded-full font-black text-[10px] uppercase hover:bg-blue-600 transition-all flex items-center gap-2 shadow-lg shadow-slate-100">
                                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v1m6 11h2m-6 0h-2v4m0-11v-3m6 3h2m-3 3h3m-12-1v2m8-7V4m0 0h-3m3 0h3m-9 14v2m0 0h3m-3 0H6m-3-7h3m11 1h1"/></svg> Quét mã
                            </button>
                        </div>
                    </div>

                    <!-- Products Table -->
                    <div class="border border-slate-100 rounded-lg flex-1 flex flex-col table-scrollbar overflow-hidden bg-white shadow-inner">
                        <div class="overflow-auto flex-1 h-full relative">
                            <table class="w-full text-left whitespace-nowrap min-w-[1450px] border-collapse">
                                <thead class="bg-blue-50/50 sticky top-0 z-10 text-[10px] font-black text-blue-800 uppercase tracking-widest border-b border-blue-100">
                                    <tr>
                                        <th class="p-2 text-center border-r border-blue-50 w-8">+</th>
                                        <th class="p-2 text-center border-r border-blue-50 w-10">STT</th>
                                        <th class="p-2 border-r border-blue-50 w-36">Hình thức</th>
                                        <th class="p-2 border-r border-blue-50 w-24">Mã hàng</th>
                                        <th class="p-2 border-r border-blue-50">Hàng hóa, dịch vụ</th>
                                        <th class="p-2 text-center border-r border-blue-50 w-16">ĐVT</th>
                                        <th class="p-2 text-center border-r border-blue-50 w-24">Số lượng</th>
                                        <th class="p-2 text-center border-r border-blue-50 w-28">Đơn giá</th>
                                        <th class="p-2 text-center border-r border-blue-50 w-24">Thuế suất</th>
                                        <th class="p-2 text-center border-r border-blue-50 w-16">Mã TS</th>
                                        <th class="p-2 text-center border-r border-blue-50 w-24">CK (%)</th>
                                        <th class="p-2 text-center border-r border-blue-50 w-28">Tiền CK</th>
                                        <th class="p-2 text-center border-r border-blue-50 w-32">Thành tiền</th>
                                        <th class="p-2 text-center border-r border-blue-50 w-20">VAT</th>
                                        <th class="p-2 text-center w-36">Tổng cộng</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr class="border-b border-slate-100 group h-10 hover:bg-blue-50/20 transition-colors">
                                        <td class="p-1 px-2 text-center border-r border-slate-50">
                                            <button class="text-slate-300 hover:text-red-500 opacity-0 group-hover:opacity-100 transition-all"><svg class="w-4 h-4 mx-auto" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"/></svg></button>
                                        </td>
                                        <td class="p-1 text-center border-r border-slate-50 font-black text-slate-400">01</td>
                                        <td class="p-1 border-r border-slate-50 px-3 text-slate-800">
                                            <select class="w-full bg-transparent border-0 font-bold text-slate-800 outline-none text-[11px] py-1 cursor-pointer focus:text-blue-600">
                                                <option>Bán hàng</option>
                                                <option>Khuyến mãi</option>
                                                <option>Chiết khấu</option>
                                                <option>Ghi chú</option>
                                            </select>
                                        </td>
                                        <td class="p-1 border-r border-slate-50 px-2"><input type="text" value="SP-001" class="w-full bg-transparent border-0 font-bold text-slate-800 outline-none uppercase tracking-tight focus:text-blue-600"></td>
                                        <td class="p-1 border-r border-slate-50 relative px-2">
                                            <div class="flex items-center gap-2">
                                                <input type="text" class="flex-1 bg-transparent border-0 outline-none font-black text-slate-800 focus:text-blue-600" value="Sản phẩm Demo Hệ thống">
                                                <button class="text-slate-300 hover:text-blue-500"><svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg></button>
                                            </div>
                                        </td>
                                        <td class="p-1 border-r border-slate-50 px-1 text-center"><input type="text" value="Cái" class="w-full text-center bg-transparent border-0 outline-none font-bold text-slate-700 focus:text-blue-600"></td>
                                        <td class="p-1 border-r border-slate-50 px-1 text-center"><input type="text" value="1.00" class="w-full text-center bg-transparent border-0 outline-none font-black text-blue-600 italic"></td>
                                        <td class="p-1 border-r border-slate-50 px-1 text-right"><input type="text" value="1,500,000" class="w-full text-right bg-transparent border-0 outline-none font-black text-slate-800 px-2 italic focus:text-blue-600"></td>
                                        <td class="p-1 border-r border-slate-50 text-center">
                                            <select class="bg-transparent border-0 outline-none font-black text-slate-600 text-[11px] cursor-pointer focus:text-blue-600">
                                                <option>10%</option><option>8%</option><option>5%</option><option>0%</option><option>KCT</option>
                                            </select>
                                        </td>
                                        <td class="p-1 border-r border-slate-50 text-center"><input type="text" value="10" class="w-full text-center bg-transparent border-0 outline-none font-bold text-slate-400 px-1"></td>
                                        <td class="p-1 border-r border-slate-50 px-1"><input type="text" value="0" class="w-full text-center bg-transparent border-0 outline-none font-bold text-slate-800 px-1 focus:text-blue-600"></td>
                                        <td class="p-1 border-r border-slate-50 px-1 text-right font-bold text-slate-400 italic">0</td>
                                        <td class="p-1 border-r border-slate-50 text-right px-3 font-black text-slate-600">1,500,000</td>
                                        <td class="p-1 border-r border-slate-50 text-right px-3 font-black text-slate-500 italic opacity-60">150,000</td>
                                        <td class="p-1 text-right px-4 font-black text-blue-700 text-[14px]">1,650,000</td>
                                    </tr>
                                    <!-- Placeholder to prompt interaction -->
                                    <tr class="h-10 bg-slate-50/10 opacity-30">
                                        <td class="p-1 px-4 text-center border-r border-slate-50 font-black text-slate-300">02</td>
                                        <td colspan="4" class="p-1 px-4 text-slate-300 font-black text-[10px] italic">... (Gõ nội dung hoặc F3 để tra cứu sản phẩm nhanh)</td>
                                        <td colspan="10"></td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>

                <!-- FOOTER SUMMARY AREA -->
                <div class="shrink-0 flex flex-col gap-3">
                    <div class="flex gap-10 items-start">
                        <!-- Left: Notes & Sub-discounts -->
                        <div class="flex-1 grid grid-cols-[80px_1fr_100px_160px] gap-x-4 gap-y-2 items-center">
                            <label class="font-black text-slate-400 uppercase text-[10px] px-1">Ghi chú phiếu</label>
                            <input type="text" placeholder="Nhập ghi chú hoặc diễn giải phục vụ quản lý..." class="h-8 px-3 bg-slate-50 border border-slate-200 rounded outline-none focus:border-blue-500 focus:bg-white text-slate-700 font-bold w-full transition-all shadow-inner">
                            
                            <label class="text-right pr-4 font-black text-slate-400 uppercase text-[10px]">Chiết khấu HĐ</label>
                            <div class="flex items-center gap-2">
                                <input type="text" value="0" class="flex-1 h-8 px-3 bg-slate-50 border border-slate-200 rounded outline-none text-right text-slate-700 font-bold focus:border-blue-500 transition-all">
                                <span class="bg-blue-600 text-white px-2 py-1 rounded text-[10px] font-black tracking-tight">%</span>
                            </div>

                            <div class="col-span-2"></div>
                            
                            <label class="text-right pr-4 font-black text-blue-400 uppercase text-[10px]">Tổng CK Thương mại</label>
                            <input type="text" readonly value="0,00" class="h-8 px-3 bg-slate-100 border border-slate-200 rounded outline-none text-right text-blue-600 font-black italic opacity-60 w-full">
                        </div>

                        <!-- Right: Totals (POS Logic Side) -->
                        <div class="w-[520px] bg-white p-4 rounded-xl border border-blue-50 shadow-lg shadow-blue-500/5 grid grid-cols-[100px_130px_100px_130px] gap-x-4 gap-y-3 items-center">
                            <label class="text-slate-400 text-right pr-2 font-black text-[10px] uppercase">Cộng VNĐ</label>
                            <input type="text" value="1,500,000" readonly class="h-8 px-3 bg-slate-50 border border-slate-100 text-right rounded-lg outline-none font-black text-slate-600 shadow-inner italic">
                            
                            <label class="text-blue-600 text-right pr-2 font-black text-[10px] uppercase tracking-tighter">Tổng trước thuế</label>
                            <input type="text" value="1,500,000" readonly class="h-8 px-3 bg-blue-50 border border-blue-100 text-right rounded-lg outline-none font-black text-blue-700 shadow-inner">
                            
                            <label class="text-slate-400 text-right pr-2 font-black text-[10px] uppercase">VAT VNĐ</label>
                            <input type="text" value="150,000" readonly class="h-8 px-3 bg-slate-50 border border-slate-100 text-right rounded-lg outline-none font-bold text-slate-500 opacity-60 shadow-inner italic">
                            
                            <label class="text-slate-400 text-right pr-2 font-black text-[10px] uppercase">Tổng tiền VAT</label>
                            <input type="text" value="150,000" readonly class="h-8 px-3 bg-slate-50 border border-slate-100 text-right rounded-lg outline-none font-bold text-slate-500 opacity-60 shadow-inner italic">

                            <div class="col-span-2"></div>
                            <label class="text-blue-700 text-right pr-3 font-black text-[12px] uppercase tracking-widest leading-tight">Tổng thanh toán</label>
                            <div class="relative">
                                <input type="text" value="1,650,000" readonly class="h-10 px-4 bg-blue-600 border-0 text-right rounded-lg outline-none font-black text-white text-[16px] shadow-lg shadow-blue-200 w-full tracking-tight">
                                <span class="absolute left-3 top-3 text-[10px] text-blue-200 font-black">VND</span>
                            </div>
                        </div>
                    </div>

                    <!-- Bằng chữ area -->
                    <div class="bg-blue-900/5 p-2 px-4 rounded-lg flex items-center gap-4">
                        <div class="flex items-center gap-2 shrink-0">
                            <span class="w-2 h-2 rounded-full bg-blue-600 animate-pulse"></span>
                            <label class="text-blue-900 font-black text-[10px] uppercase tracking-widest">Bằng chữ</label>
                        </div>
                        <input type="text" value="MỘT TRIỆU SÁU TRĂM NĂM MƯƠI NGÀN ĐỒNG CHẴN." readonly class="flex-1 h-6 bg-transparent border-0 outline-none font-black italic text-blue-800 uppercase tracking-tight text-[11px]">
                    </div>
                </div>

            </div>

            <!-- Modal Footer Actions -->
            <div class="px-6 py-4 bg-slate-50 border-t border-slate-100 flex items-center justify-between shrink-0">
                <div class="flex items-center gap-4">
                    <label class="flex items-center gap-2 cursor-pointer group">
                        <input type="checkbox" checked class="w-4 h-4 rounded border-slate-300 text-blue-600 focus:ring-blue-500 transition-all shadow-sm">
                        <span class="text-[11px] font-black text-slate-500 uppercase group-hover:text-blue-600 transition-colors">Gửi CQT tự động ngay khi lưu</span>
                    </label>
                </div>
                <div class="flex items-center gap-3">
                    <button class="h-9 px-8 bg-white border border-slate-300 text-slate-600 font-black text-[11px] uppercase rounded-full shadow-sm hover:bg-slate-50 transition-all active:scale-95">
                        In bản nháp
                    </button>
                    <button class="h-9 px-8 bg-blue-600 text-white font-black text-[11px] uppercase rounded-full flex items-center gap-2 hover:bg-blue-700 shadow-lg shadow-blue-200 transition-all active:scale-95 group">
                        <svg class="w-4 h-4 group-hover:scale-110 transition-transform" fill="currentColor" viewBox="0 0 24 24"><path d="M17 3H5c-1.11 0-2 .9-2 2v14c0 1.1.89 2 2 2h14c1.1 0 2-.9 2-2V7l-4-4zm-5 16c-1.66 0-3-1.34-3-3s1.34-3 3-3 3 1.34 3 3-1.34 3-3 3zm3-10H5V5h10v4z"/></svg>
                        Lưu hóa đơn
                    </button>
                    <button @click="isOpen = false" class="h-9 px-8 bg-white border border-red-200 text-red-500 font-black text-[11px] uppercase rounded-full hover:bg-red-50 transition-all active:scale-95">
                        Hủy & Thoát
                    </button>
                </div>
            </div>
            
        </div>
    </div>
"""

content = content.replace('</body>', f'{modal_html}\n</body>')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
"
