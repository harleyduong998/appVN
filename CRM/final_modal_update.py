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
    <!-- Add Invoice Modal (Full POS Sync & System Aesthetic) -->
    <div x-show="isOpen" style="display: none;" class="fixed inset-0 z-50 flex items-center justify-center p-2 sm:p-4" role="dialog" aria-modal="true">
        <div x-show="isOpen" x-transition.opacity.duration.300ms class="absolute inset-0 bg-slate-900/60 backdrop-blur-sm" @click="isOpen = false"></div>
        
        <div x-show="isOpen" x-transition:enter="transition ease-out duration-300" x-transition:enter-start="opacity-0 scale-95" x-transition:enter-end="opacity-100 scale-100" class="relative bg-white w-full max-w-[1550px] h-[98vh] rounded shadow-2xl flex flex-col overflow-hidden text-[12px] text-slate-700 font-medium">
            
            <!-- Modal Header -->
            <div class="px-6 py-3 bg-white border-b border-slate-100 flex items-center justify-between shrink-0">
                <h3 class="text-xl font-bold text-[#1e293b]">Phiếu hóa đơn điện tử</h3>
                <button @click="isOpen = false" class="text-slate-400 hover:text-slate-600 p-2 transition-all">
                    <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
                </button>
            </div>

            <!-- Scrollable Content -->
            <div class="flex-1 overflow-y-auto p-4 flex flex-col gap-6 table-scrollbar">
                
                <!-- SECTION: THÔNG TIN -->
                <div class="flex flex-col gap-3">
                    <div class="flex items-center gap-2">
                        <div class="w-1 h-5 bg-[#f97316] rounded-full"></div>
                        <h4 class="text-[13px] font-black text-[#1e293b] uppercase tracking-wider">Thông tin</h4>
                    </div>
                    
                    <div class="grid grid-cols-[1fr_350px] gap-8">
                        <!-- Left Information Grid -->
                        <div class="grid grid-cols-[110px_1fr_110px_1fr] gap-x-4 gap-y-2 items-center">
                            <label class="font-bold text-slate-700">Tên KH</label>
                            <div class="col-span-3 flex">
                                <input type="text" placeholder="Nhập MST, tên KH hoặc mã KH kết thúc bằng ký tự ; để tìm kiếm" class="flex-1 h-8 px-3 bg-[#f1f5f9] border-0 rounded-l outline-none focus:ring-1 focus:ring-blue-100 text-slate-700 font-bold placeholder-slate-300">
                                <button class="bg-[#22c55e] text-white px-3 h-8 rounded-r flex items-center justify-center hover:bg-[#16a34a]"><svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-4.35-4.35m1.35-5.65a7 7 0 11-14 0 7 7 0 0114 0z"/></svg></button>
                            </div>

                            <label class="font-bold text-slate-700">Mã KH</label>
                            <input type="text" class="h-8 px-3 bg-[#f1f5f9] border-0 rounded outline-none font-bold text-slate-400" readonly value="">
                            <label class="text-right pr-2 text-slate-500 font-bold">Số điện thoại</label>
                            <input type="text" class="h-8 px-3 bg-[#f1f5f9] border-0 rounded outline-none text-slate-700 font-bold">

                            <label class="font-bold text-slate-700">Mã sỗ thuế</label>
                            <input type="text" class="h-8 px-3 bg-[#f1f5f9] border-0 rounded outline-none text-slate-700 font-bold">
                            <label class="text-right pr-2 text-slate-500 font-bold">CCCD người mua</label>
                            <input type="text" class="h-8 px-3 bg-[#f1f5f9] border-0 rounded outline-none text-slate-700 font-bold">

                            <label class="font-bold text-slate-700">Địa chỉ</label>
                            <input type="text" class="col-span-3 h-8 px-3 bg-[#f1f5f9] border-0 rounded outline-none text-slate-700 font-bold">

                            <label class="font-bold text-slate-700">Email</label>
                            <input type="text" class="col-span-3 h-8 px-3 bg-[#f1f5f9] border-0 rounded outline-none text-slate-700 font-bold">

                            <label class="whitespace-nowrap font-bold text-slate-700">Họ và tên người ...</label>
                            <input type="text" placeholder="Họ và tên người mua hàng" class="h-8 px-3 bg-[#f1f5f9] border-0 rounded outline-none text-slate-700 font-bold placeholder-slate-300">
                            <div class="flex items-center justify-end pr-2 gap-1"><span class="text-red-600 font-bold">*</span> <label class="font-bold text-slate-700 uppercase text-[11px]">HTTT</label></div>
                            <select class="h-8 px-3 bg-[#f1f5f9] border-0 rounded outline-none text-[#1b3da1] font-bold">
                                <option>TM/CK</option>
                            </select>

                            <label class="font-bold text-slate-700 uppercase text-[11px]">Mã ĐVQHNS</label>
                            <input type="text" placeholder="Mã đơn vị quan hệ ngân sách" class="h-8 px-3 bg-[#f1f5f9] border-0 rounded outline-none text-slate-700 font-bold placeholder-slate-300">
                            <div class="flex items-center gap-2 col-span-2">
                                <label class="font-bold text-slate-700 uppercase text-[11px] whitespace-nowrap">Số hộ chiếu</label>
                                <input type="text" placeholder="Số hộ chiếu/Giấy tờ nhân thân" class="flex-1 h-8 px-3 bg-[#f1f5f9] border-0 rounded outline-none text-slate-700 font-bold placeholder-slate-300">
                            </div>
                        </div>

                        <!-- Right Invoice Config Grid -->
                        <div class="grid grid-cols-[110px_1fr] gap-x-4 gap-y-2 items-center border-l border-slate-50 pl-8">
                            <label class="font-bold text-slate-700">Nghiệp vụ</label>
                            <select class="h-8 px-3 bg-[#f1f5f9] border-0 rounded outline-none text-slate-600 font-bold" disabled>
                                <option>Hóa đơn thường</option>
                            </select>

                            <div class="flex items-center gap-1">
                                <input type="checkbox" class="w-3.5 h-3.5 accent-[#22c55e]" checked>
                                <label class="font-bold text-slate-700">Ngày hoá đơn <span class="text-red-500">*</span></label>
                            </div>
                            <div class="relative w-full">
                                <input type="text" value="27/03/2026" class="w-full h-8 px-3 bg-[#f1f5f9] border-0 rounded outline-none font-bold text-slate-600 pr-8">
                                <svg class="w-4 h-4 text-blue-500 absolute right-3 top-2 pointer-events-none font-bold" fill="currentColor" viewBox="0 0 24 24"><path d="M19 4h-1V2h-2v2H8V2H6v2H5c-1.11 0-1.99.9-1.99 2L3 20c0 1.1.89 2 2 2h14c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 16H5V10h14v10zm0-12H5V6h14v2zm-7 5h5v5h-5z"/></svg>
                            </div>

                            <label class="font-bold text-slate-700 uppercase text-[11px]">Loại HĐ <span class="text-red-500">*</span></label>
                            <select x-model="platform" class="h-8 px-3 bg-[#f1f5f9] border-0 rounded outline-none text-slate-700 font-bold">
                                <option value="fpt">Hóa đơn FPT (GTGT máy tính tiền)</option>
                                <option value="viettel">Hóa đơn Viettel (Doanh nghiệp)</option>
                                <option value="matbao">Hóa đơn Mắt Bão (Điện tử)</option>
                            </select>

                            <label class="font-bold text-slate-700 uppercase text-[11px]">Mẫu số <span class="text-red-500">*</span></label>
                            <div class="h-8 px-3 bg-[#f1f5f9] rounded flex items-center text-slate-700 font-bold" x-text="platforms[platform].template"></div>

                            <label class="font-bold text-slate-700 uppercase text-[11px]">Ký hiệu <span class="text-red-500">*</span></label>
                            <div class="h-8 px-3 bg-[#f1f5f9] rounded flex items-center text-slate-700 font-bold" x-text="platforms[platform].symbol"></div>
                        </div>
                    </div>
                </div>

                <!-- SECTION: SẢN PHẨM -->
                <div class="flex flex-col gap-3 flex-1 overflow-hidden">
                    <div class="flex items-center justify-between shrink-0">
                        <div class="flex items-center gap-2">
                            <div class="w-1 h-5 bg-[#f97316] rounded-full"></div>
                            <h4 class="text-[13px] font-black text-[#1e293b] uppercase tracking-wider">Sản phẩm</h4>
                        </div>
                        <div class="flex items-center gap-2">
                            <div class="relative">
                                <span class="absolute left-3 top-2 text-slate-400">
                                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg>
                                </span>
                                <input type="text" placeholder="Tìm kiếm sản phẩm" class="w-96 h-9 pl-10 pr-4 bg-[#f1f5f9] border-0 rounded-lg outline-none focus:bg-white focus:ring-1 focus:ring-blue-100 transition-all font-bold text-slate-600">
                            </div>
                            <button class="h-9 px-4 bg-[#2563eb] text-white rounded font-bold text-[13px] hover:bg-blue-600 transition-colors">Chọn nhanh</button>
                            <button class="h-9 px-4 bg-[#2563eb] text-white rounded font-bold text-[13px] hover:bg-blue-600 transition-colors flex items-center gap-2">
                                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v1m6 11h2m-6 0h-2v4m0-11v-3m6 3h2m-3 3h3m-12-1v2m8-7V4m0 0h-3m3 0h3m-9 14v2m0 0h3m-3 0H6m-3-7h3m11 1h1"/></svg> Quét barcode
                            </button>
                        </div>
                    </div>

                    <!-- Products Table -->
                    <div class="border border-slate-200 rounded flex-1 flex flex-col table-scrollbar overflow-hidden bg-white">
                        <div class="overflow-auto flex-1 h-full relative">
                            <table class="w-full text-left whitespace-nowrap min-w-[1450px] border-collapse">
                                <thead class="bg-[#eef2fb] sticky top-0 z-10 text-[11px] font-bold text-[#1b3da1] border-b border-slate-200">
                                    <tr>
                                        <th class="p-2 text-center border-r border-slate-200 w-10">+</th>
                                        <th class="p-2 text-center border-r border-slate-200 w-10">STT</th>
                                        <th class="p-2 border-r border-slate-200 w-48">Hình thức</th>
                                        <th class="p-2 border-r border-slate-200 w-24">Mã hàng</th>
                                        <th class="p-2 border-r border-slate-200">Hàng hóa, dịch vụ</th>
                                        <th class="p-2 text-center border-r border-slate-200 w-16">ĐVT</th>
                                        <th class="p-2 text-center border-r border-slate-200 w-20">Số lượng</th>
                                        <th class="p-2 text-center border-r border-slate-200 w-24">Đơn giá</th>
                                        <th class="p-2 text-center border-r border-slate-200 w-24">Thuế suất</th>
                                        <th class="p-2 text-center border-r border-slate-200 w-16">Mã TS</th>
                                        <th class="p-2 text-center border-r border-slate-200 w-24">Chiết khấu(%)</th>
                                        <th class="p-2 text-center border-r border-slate-200 w-24">Tiền CK</th>
                                        <th class="p-2 text-center border-r border-slate-200 w-28">Thành tiền</th>
                                        <th class="p-2 text-center border-r border-slate-200 w-16">VAT</th>
                                        <th class="p-2 text-center w-28">Tổng cộng</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr class="border-b border-slate-100 group h-9">
                                        <td class="p-1 text-center border-r border-slate-100">
                                            <button class="text-slate-300 hover:text-red-500 opacity-0 group-hover:opacity-100 transition-all"><svg class="w-4 h-4 mx-auto" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"/></svg></button>
                                        </td>
                                        <td class="p-1 text-center border-r border-slate-100 font-bold">1</td>
                                        <td class="p-1 border-r border-slate-100 px-3 text-slate-800">Chiết khấu thương mại</td>
                                        <td class="p-1 border-r border-slate-100"><input type="text" value="" class="w-full bg-transparent border-0 px-2 h-7 font-bold text-slate-800 outline-none"></td>
                                        <td class="p-1 border-r border-slate-100 bg-red-50/20 px-2 flex items-center h-8">
                                            <div class="w-0 h-0 border-t-[4px] border-t-red-500 border-l-[4px] border-l-transparent border-r-[4px] border-r-transparent mr-2 self-start mt-1.5"></div>
                                            <input type="text" class="flex-1 w-full bg-transparent border-0 outline-none text-[12px] font-bold text-slate-800" value="">
                                            <button class="text-slate-400 hover:text-blue-500 ml-1"><svg class="w-4 h-4 font-bold" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg></button>
                                        </td>
                                        <td class="p-1 border-r border-slate-100"><input type="text" value="Cái" class="w-full text-center bg-transparent border-0 outline-none font-bold text-slate-800"></td>
                                        <td class="p-1 border-r border-slate-100"><input type="text" value="0,00" class="w-full text-center bg-transparent border-0 outline-none font-bold text-slate-800 italic"></td>
                                        <td class="p-1 border-r border-slate-100"><input type="text" value="0,00000" class="w-full text-right bg-transparent border-0 outline-none font-bold text-slate-800 px-2 italic"></td>
                                        <td class="p-1 border-r border-slate-100 text-center"><select class="w-full bg-transparent border-0 outline-none font-bold text-slate-800 text-[11px]"><option>10%</option><option>8%</option><option>0%</option></select></td>
                                        <td class="p-1 border-r border-slate-100"><input type="text" value="10" class="w-full text-center bg-transparent border-0 outline-none font-bold text-slate-800 px-1"></td>
                                        <td class="p-1 border-r border-slate-100 bg-orange-50"><input type="text" value="" class="w-full text-right bg-transparent border-0 outline-none font-bold text-slate-800 px-1"></td>
                                        <td class="p-1 border-r border-slate-100 bg-[#e86a10]"><input type="text" value="" class="w-full text-right bg-transparent border-0 outline-none font-bold text-white px-1"></td>
                                        <td class="p-1 border-r border-slate-100 text-right px-3 font-bold">0,00</td>
                                        <td class="p-1 border-r border-slate-100 text-right px-3 font-bold">0,00</td>
                                        <td class="p-1 text-right px-3 font-black text-rose-600">0,00</td>
                                    </tr>
                                    <tr class="h-8">
                                        <td colspan="15" class="py-12 bg-slate-50/20 text-center text-slate-400 font-bold uppercase tracking-widest italic opacity-50">
                                            Chưa có sản phẩm
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>

                <!-- SECTION: TỔNG HỢP -->
                <div class="shrink-0 flex flex-col gap-2">
                    <div class="flex gap-10">
                        <!-- Bottom Left: Remarks & CK -->
                        <div class="flex-1 grid grid-cols-[80px_1fr_100px_140px] gap-x-4 gap-y-2 items-center">
                            <label class="font-bold text-slate-500 uppercase text-[11px]">Ghi chú</label>
                            <input type="text" class="h-8 px-3 bg-[#f1f5f9] border-0 rounded outline-none text-slate-700 font-bold w-full">
                            
                            <label class="text-right pr-4 font-bold text-slate-500 uppercase text-[11px]">Chiết khấu</label>
                            <input type="text" value="0" class="h-8 px-3 bg-[#f1f5f9] border-0 rounded outline-none text-right text-slate-700 font-bold">

                            <div class="col-span-2"></div>
                            
                            <label class="text-right pr-4 font-bold text-slate-500 uppercase text-[11px]">Tổng CKTM</label>
                            <input type="text" readonly value="0,00" class="h-8 px-3 bg-[#f1f5f9] border-0 rounded outline-none text-right text-slate-700 font-bold italic opacity-60">
                        </div>

                        <!-- Bottom Right: Sums (Dense POS Grid) -->
                        <div class="w-[500px] grid grid-cols-[90px_120px_90px_120px] gap-x-3 gap-y-2 items-center">
                            <label class="text-red-500 text-right pr-2 font-black text-[11px]">Cộng VNĐ *</label>
                            <input type="text" value="0" readonly class="h-8 px-3 bg-[#f8fafc] border border-slate-100 text-right rounded outline-none font-black text-slate-700">
                            
                            <label class="text-red-500 text-right pr-2 font-black text-[11px]">Tổng tiền *</label>
                            <input type="text" value="0,00" readonly class="h-8 px-3 bg-[#f8fafc] border border-slate-100 text-right rounded outline-none font-black text-slate-700">
                            
                            <label class="text-slate-500 text-right pr-2 font-bold text-[11px] uppercase">VAT VNĐ</label>
                            <input type="text" value="0" readonly class="h-8 px-3 bg-[#f8fafc] border border-slate-100 text-right rounded outline-none font-bold text-slate-700 opacity-60">
                            
                            <label class="text-slate-500 text-right pr-2 font-bold text-[11px] uppercase whitespace-nowrap">Tổng VAT</label>
                            <input type="text" value="0,00" readonly class="h-8 px-3 bg-[#f8fafc] border border-slate-100 text-right rounded outline-none font-bold text-slate-700 opacity-60">

                            <label class="text-red-500 text-right pr-2 font-black text-[11px]">Tổng VNĐ *</label>
                            <input type="text" value="0" readonly class="h-8 px-3 bg-[#f8fafc] border border-slate-100 text-right rounded outline-none font-black text-slate-700">
                            
                            <label class="text-red-500 text-right pr-2 font-black text-[11px]">Tổng cộng *</label>
                            <input type="text" value="0,00" readonly class="h-8 px-3 bg-[#f1f5fb] border border-blue-50 text-right rounded outline-none font-black text-[#1e40af] italic">
                        </div>
                    </div>

                    <!-- Bằng chữ area -->
                    <div class="flex items-center gap-4 mt-2">
                        <label class="text-red-500 font-black whitespace-nowrap w-[100px] text-[11px] uppercase">Bằng chữ *</label>
                        <input type="text" value="Không đồng" class="flex-1 h-8 px-4 bg-[#f8fafc] border border-slate-100 rounded outline-none font-black italic text-slate-500 uppercase tracking-tight">
                    </div>
                </div>

            </div>

            <!-- Modal Footer Actions -->
            <div class="px-6 py-4 bg-white border-t border-slate-50 flex items-center justify-end gap-3 shrink-0">
                <button class="h-9 px-8 bg-[#22c55e] text-white font-black text-[13px] rounded flex items-center gap-2 hover:bg-[#16a34a] shadow-lg shadow-green-100 transition-all active:scale-95">
                    <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24"><path d="M17 3H5c-1.11 0-2 .9-2 2v14c0 1.1.89 2 2 2h14c1.1 0 2-.9 2-2V7l-4-4zm-5 16c-1.66 0-3-1.34-3-3s1.34-3 3-3 3 1.34 3 3-1.34 3-3 3zm3-10H5V5h10v4z"/></svg>
                    Lưu
                </button>
                <button class="h-9 px-8 bg-[#22c55e] text-white font-black text-[13px] rounded flex items-center gap-2 hover:bg-[#16a34a] shadow-lg shadow-green-100 transition-all active:scale-95">
                    <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24"><path d="M12 4.5C7 4.5 2.73 7.61 1 12c1.73 4.39 6 7.5 11 7.5s9.27-3.11 11-7.5c-1.73-4.39-6-7.5-11-7.5zM12 17c-2.76 0-5-2.24-5-5s2.24-5 5-5 5 2.24 5 5-2.24 5-5 5zm0-8c-1.66 0-3 1.34-3 3s1.34 3 3 3 3-1.34 3-3-1.34-3-3-3z"/></svg>
                    Hiển thị
                </button>
                <button @click="isOpen = false" class="h-9 px-8 bg-[#22c55e] text-white font-black text-[13px] rounded flex items-center gap-2 hover:bg-[#16a34a] shadow-lg shadow-green-100 transition-all active:scale-95">
                    <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24"><path d="M10.09 15.59L11.5 17l5-5-5-5-1.41 1.41L12.67 11H3v2h9.67l-2.58 2.59zM19 3H5c-1.11 0-2 .9-2 2v4h2V5h14v14H5v-4H3v4c0 1.1.89 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2z"/></svg>
                    Thoát
                </button>
            </div>
            
        </div>
    </div>
"""

content = content.replace('</body>', f'{modal_html}\n</body>')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
"
