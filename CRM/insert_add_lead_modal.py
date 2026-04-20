import re

filepath = r"d:\AIDesign\lixi\stuff2\CRM\CRM_Lead_v2.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. First add onclick="openAddLeadModal()" to the Thêm Lead button.
# The button looks roughly like:
# <button
#                         class="flex items-center gap-2 bg-[#1b3da1] text-white px-3 py-1.5 rounded-md font-medium hover:bg-blue-800 transition shadow-sm">
#                         <svg ... > ... </svg>
#                         Thêm Lead
#                     </button>
button_pattern = re.compile(
    r'(<button\s+)(class="flex items-center gap-2 bg-\[\#1b3da1\] text-white[^>]*>)(.*?Thêm Lead)',
    re.DOTALL
)

if button_pattern.search(content):
    content = button_pattern.sub(r'\g<1>onclick="openAddLeadModal()" \g<2>\g<3>', content)

# 2. Add the Add Lead modal right before </body>
add_lead_modal_html = """

            <!-- Add Lead Modal -->
            <div id="addLeadModal" class="fixed inset-0 z-[100] hidden">
                <!-- Backdrop -->
                <div class="absolute inset-0 bg-slate-900/40 backdrop-blur-sm opacity-0 transition-opacity duration-300" id="addLeadModalBackdrop" onclick="closeAddLeadModal()"></div>

                <!-- Modal Content -->
                <div class="fixed inset-0 flex items-center justify-center p-4 pointer-events-none">
                    <div id="addLeadModalContent" class="bg-white w-full max-w-4xl rounded-2xl shadow-2xl flex flex-col max-h-[90vh] pointer-events-auto transform scale-95 opacity-0 transition-all duration-300 relative">
                        <!-- Header -->
                        <div class="flex items-center justify-between px-6 py-4 border-b border-slate-100 bg-white z-10 shrink-0 rounded-t-2xl">
                            <div class="flex items-center gap-2.5">
                                <div class="w-8 h-8 rounded-lg bg-blue-50 text-blue-600 flex items-center justify-center border border-blue-100">
                                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"></path></svg>
                                </div>
                                <h2 class="text-lg font-bold text-slate-800">Tạo Lead Mới</h2>
                            </div>
                            <button onclick="closeAddLeadModal()" class="w-8 h-8 flex items-center justify-center rounded-full text-slate-400 hover:text-slate-600 hover:bg-slate-50 transition border border-transparent hover:border-slate-200">
                                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
                            </button>
                        </div>

                        <!-- Body (2 columns) -->
                        <div class="flex-1 overflow-y-auto p-6 grid grid-cols-1 md:grid-cols-2 gap-8 custom-scrollbar bg-slate-50/50">
                            <!-- Left Col: Customer Info -->
                            <div class="space-y-4">
                                <h3 class="font-bold text-slate-800 text-[14px] mb-3 flex items-center gap-2">
                                    <svg class="w-4 h-4 text-[#1b3da1]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"></path></svg>
                                    Thông tin cá nhân
                                </h3>
                                <div>
                                    <label class="block text-[13px] font-medium text-slate-700 mb-1.5">Họ và tên <span class="text-red-500">*</span></label>
                                    <input type="text" placeholder="Nhập tên khách hàng" class="w-full px-3 py-2 bg-white border border-slate-200 rounded-md text-[13px] text-slate-800 focus:outline-none focus:ring-1 focus:ring-blue-500 focus:border-blue-500 shadow-sm transition placeholder:text-slate-400" required>
                                </div>
                                <div class="grid grid-cols-2 gap-4">
                                    <div>
                                        <label class="block text-[13px] font-medium text-slate-700 mb-1.5">Số điện thoại <span class="text-red-500">*</span></label>
                                        <input type="tel" placeholder="Nhập SĐT" class="w-full px-3 py-2 bg-white border border-slate-200 rounded-md text-[13px] text-slate-800 focus:outline-none focus:ring-1 focus:ring-blue-500 focus:border-blue-500 shadow-sm transition placeholder:text-slate-400" required>
                                    </div>
                                    <div>
                                        <label class="block text-[13px] font-medium text-slate-700 mb-1.5">Nguồn tài chính</label>
                                        <select class="w-full px-3 py-2 bg-white border border-slate-200 rounded-md text-[13px] text-slate-600 focus:outline-none focus:ring-1 focus:ring-blue-500 focus:border-blue-500 shadow-sm transition outline-none">
                                            <option>Gia đình hỗ trợ</option>
                                            <option>Tự túc</option>
                                            <option>Vay vốn</option>
                                            <option>Chưa rõ</option>
                                        </select>
                                    </div>
                                </div>
                                <div>
                                    <label class="block text-[13px] font-medium text-slate-700 mb-1.5">Email</label>
                                    <input type="email" placeholder="example@email.com" class="w-full px-3 py-2 bg-white border border-slate-200 rounded-md text-[13px] text-slate-800 focus:outline-none focus:ring-1 focus:ring-blue-500 focus:border-blue-500 shadow-sm transition placeholder:text-slate-400">
                                </div>
                                <div class="grid grid-cols-2 gap-4">
                                    <div class="col-span-2">
                                        <label class="block text-[13px] font-medium text-slate-700 mb-1.5">Địa chỉ</label>
                                        <input type="text" placeholder="Thành phố, Quận huyện, Phố..." class="w-full px-3 py-2 bg-white border border-slate-200 rounded-md text-[13px] text-slate-800 focus:outline-none focus:ring-1 focus:ring-blue-500 focus:border-blue-500 shadow-sm transition placeholder:text-slate-400">
                                    </div>
                                </div>
                                <div>
                                    <label class="block text-[13px] font-medium text-slate-700 mb-1.5">Mạng xã hội</label>
                                    <div class="flex gap-2">
                                        <input type="text" placeholder="Link Zalo..." class="w-full px-3 py-2 bg-white border border-slate-200 rounded-md text-[13px] text-slate-800 focus:outline-none focus:ring-1 focus:ring-blue-500 focus:border-blue-500 shadow-sm transition placeholder:text-slate-400">
                                        <input type="text" placeholder="Link Facebook..." class="w-full px-3 py-2 bg-white border border-slate-200 rounded-md text-[13px] text-slate-800 focus:outline-none focus:ring-1 focus:ring-blue-500 focus:border-blue-500 shadow-sm transition placeholder:text-slate-400">
                                    </div>
                                </div>
                                <div>
                                    <label class="block text-[13px] font-medium text-slate-700 mb-1.5">Ghi chú / Nhu cầu chung</label>
                                    <textarea rows="2" placeholder="Sở thích, định hướng, hoặc thông tin đặc biệt..." class="w-full px-3 py-2 bg-white border border-slate-200 rounded-md text-[13px] text-slate-800 focus:outline-none focus:ring-1 focus:ring-blue-500 focus:border-blue-500 shadow-sm transition placeholder:text-slate-400 resize-none"></textarea>
                                </div>
                            </div>

                            <!-- Right Col: System Info -->
                            <div class="space-y-4">
                                <h3 class="font-bold text-slate-800 text-[14px] mb-3 flex items-center gap-2">
                                    <svg class="w-4 h-4 text-emerald-600" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>
                                    Hệ thống & Phân loại
                                </h3>
                                
                                <div class="grid grid-cols-2 gap-4">
                                    <div>
                                        <label class="block text-[13px] font-medium text-slate-700 mb-1.5">Trạng thái (Bước) <span class="text-red-500">*</span></label>
                                        <select class="w-full px-3 py-2 bg-white border border-slate-200 rounded-md text-[13px] text-slate-800 font-medium focus:outline-none focus:ring-1 focus:ring-blue-500 focus:border-blue-500 shadow-sm transition outline-none">
                                            <option value="1">Chưa liên hệ</option>
                                            <option value="2">Đã liên hệ</option>
                                            <option value="3">Thất bại</option>
                                            <option value="4">Thành công</option>
                                        </select>
                                    </div>
                                    <div>
                                        <label class="block text-[13px] font-medium text-slate-700 mb-1.5">Chi nhánh</label>
                                        <select class="w-full px-3 py-2 bg-blue-50/50 border border-blue-100 rounded-md text-[13px] text-blue-600 font-medium focus:outline-none focus:ring-1 focus:ring-blue-500 focus:border-blue-500 shadow-sm transition outline-none">
                                            <option>Hà Nội</option>
                                            <option>Đà Nẵng</option>
                                            <option>Hồ Chí Minh</option>
                                        </select>
                                    </div>
                                </div>
                                <div class="grid grid-cols-2 gap-4">
                                    <div>
                                        <label class="block text-[13px] font-medium text-slate-700 mb-1.5">Phễu</label>
                                        <select class="w-full px-3 py-2 bg-white border border-slate-200 rounded-md text-[13px] text-slate-600 focus:outline-none focus:ring-1 focus:ring-blue-500 focus:border-blue-500 shadow-sm transition outline-none">
                                            <option>Phễu học viên</option>
                                            <option>Phễu khách mời</option>
                                        </select>
                                    </div>
                                    <div>
                                        <label class="block text-[13px] font-medium text-slate-700 mb-1.5">Nguồn lead</label>
                                        <select class="w-full px-3 py-2 bg-white border border-slate-200 rounded-md text-[13px] text-slate-600 focus:outline-none focus:ring-1 focus:ring-blue-500 focus:border-blue-500 shadow-sm transition outline-none">
                                            <option>Nguồn đơn</option>
                                            <option>Facebook Ads</option>
                                            <option>Tự tìm kiếm</option>
                                            <option>Giới thiệu</option>
                                        </select>
                                    </div>
                                </div>
                                
                                <div class="grid grid-cols-2 gap-4">
                                    <div class="col-span-2">
                                        <label class="block text-[13px] font-medium text-slate-700 mb-1.5">Người phụ trách (Owner)</label>
                                        <div class="relative">
                                            <select class="w-full pl-9 pr-3 py-2 bg-white border border-slate-200 rounded-md text-[13px] text-slate-800 font-medium focus:outline-none focus:ring-1 focus:ring-blue-500 focus:border-blue-500 shadow-sm transition appearance-none cursor-pointer">
                                                <option>Nguyễn Văn A</option>
                                                <option>Trần Thị B</option>
                                                <option>Lê Văn C</option>
                                            </select>
                                            <div class="absolute inset-y-0 left-2.5 flex items-center pointer-events-none">
                                                <img src="https://api.dicebear.com/7.x/notionists/svg?seed=A" class="w-5 h-5 rounded-full border border-slate-200" alt="">
                                            </div>
                                            <div class="absolute inset-y-0 right-3 flex items-center pointer-events-none">
                                                <svg class="w-3.5 h-3.5 text-slate-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                
                                <div>
                                    <label class="block text-[13px] font-medium text-slate-700 mb-1.5">Thẻ Tag</label>
                                    <!-- Tag field mockup matching detail styling -->
                                    <div class="w-full py-1.5 px-1.5 border border-slate-200 rounded-md bg-white min-h-[38px] mt-1 flex flex-wrap gap-1.5 shadow-sm">
                                        <!-- Selected tags -->
                                        <span class="px-2 py-[3px] bg-yellow-400 text-yellow-900 rounded-[4px] text-[11px] font-semibold flex items-center gap-1 cursor-pointer hover:bg-yellow-500 transition">
                                            Hot deal Page 1
                                            <svg class="w-3 h-3 hover:text-red-600 transition" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
                                        </span>
                                        <span class="px-2 py-[3px] bg-sky-100 text-sky-700 border border-sky-200 rounded-[4px] text-[11px] font-semibold flex items-center gap-1 cursor-pointer hover:bg-sky-200 transition">
                                            Online
                                            <svg class="w-3 h-3 hover:text-red-500 transition" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
                                        </span>
                                        <!-- Input -->
                                        <input type="text" placeholder="Thêm thẻ tag..." class="outline-none flex-1 min-w-[100px] text-[12px] bg-transparent text-slate-700 ml-1">
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- Footer -->
                        <div class="px-6 py-4 border-t border-slate-100 bg-white flex justify-end gap-3 shrink-0 rounded-b-2xl">
                            <button onclick="closeAddLeadModal()" class="px-4 py-2 border border-slate-200 bg-white hover:bg-slate-50 text-slate-600 font-medium rounded-lg text-[13px] transition shadow-sm">
                                Hủy bỏ
                            </button>
                            <button onclick="saveNewLead()" class="px-5 py-2 bg-[#1b3da1] text-white font-medium rounded-lg text-[13px] hover:bg-blue-800 focus:ring-2 focus:ring-offset-1 focus:ring-blue-600 transition shadow-sm flex items-center gap-2">
                                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
                                Lưu và Tạo mới
                            </button>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Add Lead Modal Script -->
            <script>
                function openAddLeadModal() {
                    const modal = document.getElementById('addLeadModal');
                    const backdrop = document.getElementById('addLeadModalBackdrop');
                    const content = document.getElementById('addLeadModalContent');
                    
                    modal.classList.remove('hidden');
                    // Delay for transition
                    setTimeout(() => {
                        backdrop.classList.remove('opacity-0');
                        content.classList.remove('opacity-0', 'scale-95');
                        content.classList.add('opacity-100', 'scale-100');
                    }, 10);
                }

                function closeAddLeadModal() {
                    const modal = document.getElementById('addLeadModal');
                    const backdrop = document.getElementById('addLeadModalBackdrop');
                    const content = document.getElementById('addLeadModalContent');
                    
                    backdrop.classList.add('opacity-0');
                    content.classList.remove('opacity-100', 'scale-100');
                    content.classList.add('opacity-0', 'scale-95');
                    
                    setTimeout(() => {
                        modal.classList.add('hidden');
                    }, 300);
                }

                function saveNewLead() {
                    alert('Đã lưu thành công Lead mới! (Đây là nội dung giả lập UI)');
                    closeAddLeadModal();
                }
            </script>
"""

content = content.replace("</body>", add_lead_modal_html + "\n</body>")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Insertion complete")
