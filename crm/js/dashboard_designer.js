document.addEventListener('DOMContentLoaded', function() {
    const availableReports = document.getElementById('available-reports');
    const canvasGrid = document.getElementById('canvas-grid');
    const addFilterBtn = document.getElementById('add-global-filter');
    const filtersBar = document.getElementById('global-filters-bar');
    const activeFiltersContainer = document.getElementById('active-filters');

    // Global Filter Logic
    addFilterBtn.addEventListener('click', function() {
        const filterType = prompt("Chọn loại bộ lọc (ví dụ: Thời gian, Nguồn, Nhân viên):", "Thời gian");
        if (filterType) {
            filtersBar.style.display = 'flex';
            const filterTag = document.createElement('div');
            filterTag.className = 'bg-blue-50 text-blue-600 px-3 py-1 rounded-full text-xs font-semibold border border-blue-100 flex items-center gap-2 shadow-sm';
            filterTag.innerHTML = `
                <span>${filterType}: <span class="font-bold">Tất cả</span></span>
                <span class="remove-filter cursor-pointer hover:text-blue-800 text-lg">&times;</span>
            `;
            
            filterTag.querySelector('.remove-filter').addEventListener('click', function() {
                filterTag.remove();
                if (activeFiltersContainer.children.length === 0) {
                    filtersBar.style.display = 'none';
                }
            });
            
            activeFiltersContainer.appendChild(filterTag);
        }
    });

    // ... existing sortable code
    new Sortable(canvasGrid, {
        group: 'shared',
        animation: 150,
        ghostClass: 'sortable-ghost',
        onAdd: function (evt) {
            const placeholder = canvasGrid.querySelector('.empty-placeholder');
            if (placeholder) placeholder.remove();

            const item = evt.item;
            const reportName = item.querySelector('.item-text').innerText;
            const reportId = item.getAttribute('data-id');

            item.className = 'canvas-report-card bg-white border border-gray-100 rounded-xl shadow-sm overflow-hidden flex flex-col group';
            item.innerHTML = `
                <div class="bg-gray-50 px-4 py-3 flex justify-between items-center border-b border-gray-100">
                    <span class="font-bold text-gray-700 text-sm whitespace-nowrap overflow-hidden overflow-ellipsis">${reportName}</span>
                    <button class="remove-btn text-gray-300 hover:text-red-500 transition-colors">&times;</button>
                </div>
                <div class="p-4 flex-grow">
                    <div class="h-32 bg-blue-50/50 rounded-lg flex items-center justify-center border border-dashed border-blue-100 mb-3 grayscale group-hover:grayscale-0 transition-all">
                        <i class="fas fa-chart-area text-blue-200 text-3xl"></i>
                    </div>
                    <div class="flex flex-wrap gap-2">
                        <span class="text-[10px] bg-gray-100 text-gray-500 px-2 py-0.5 rounded">Lead</span>
                        <span class="text-[10px] bg-gray-100 text-gray-500 px-2 py-0.5 rounded">Conversion</span>
                        <span class="text-[10px] bg-gray-100 text-gray-500 px-2 py-0.5 rounded">Revenue</span>
                    </div>
                </div>
            `;

            const removeBtn = item.querySelector('.remove-btn');
            removeBtn.addEventListener('click', function() {
                item.remove();
                checkEmpty();
            });
        }
    });

    function checkEmpty() {
        if (canvasGrid.children.length === 0) {
            canvasGrid.innerHTML = `
                <div class="empty-placeholder col-span-2 flex flex-col items-center justify-center h-full text-gray-400 py-20 pointer-events-none">
                    <i class="fas fa-mouse-pointer text-4xl mb-4 opacity-20"></i>
                    <p class="text-sm">Kéo thả báo cáo từ bên phải vào đây để thiết kế dashboard</p>
                </div>
            `;
        }
    }
});
