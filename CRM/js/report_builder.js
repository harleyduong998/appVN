document.addEventListener('DOMContentLoaded', function () {
    // 1. Elements
    const metricsSelection = document.getElementById('metrics-selection');
    const chartTypeSelection = document.getElementById('chart-type-selection');
    const groupBySelection = document.getElementById('group-by-selection');
    const groupBySection = document.getElementById('group-by-section');
    const previewContent = document.getElementById('preview-content');
    const mixedChartConfig = document.getElementById('mixed-chart-config');
    const mixedMetricsConfig = document.getElementById('mixed-metrics-config');

    // Panels & Modals
    const metricCatalogPanel = document.getElementById('metric-catalog-panel');
    const customMetricModal = document.getElementById('custom-metric-modal');
    const catalogContent = document.getElementById('catalog-content');
    const catalogTitle = document.getElementById('catalog-current-title');
    const catalogBackBtn = document.getElementById('catalog-back-btn');
    const closeCatalogBtnX = document.getElementById('close-metric-catalog-x');

    // Buttons
    const openCatalogBtn = document.getElementById('open-custom-metric-modal');
    const triggerCustomBtn = document.getElementById('trigger-custom-metric-modal');
    const applyMetricsBtn = document.getElementById('apply-selected-metrics');
    
    const closeCustomModalBtn = document.getElementById('close-custom-metric-modal');
    const cancelCustomModalBtn = document.getElementById('cancel-custom-metric');
    const createCustomMetricBtn = document.getElementById('create-custom-metric');

    // Data for Metric Catalog
    const metricData = {
        categories: [
            { id: 'custom_cat', name: 'Chỉ số tùy chỉnh', icon: 'fa-magic', isCustom: true },
            { id: 'customers', name: 'Customers', icon: 'fa-user' },
            { id: 'finance', name: 'Finance and payments', icon: 'fa-university' },
            { id: 'fraud', name: 'Fraud prevention', icon: 'fa-shield-alt' },
            { id: 'inventory', name: 'Inventory', icon: 'fa-store' },
            { id: 'marketing', name: 'Marketing', icon: 'fa-bullhorn' },
            { id: 'orders', name: 'Orders', icon: 'fa-shopping-basket' },
            { id: 'sales', name: 'Sales revenue', icon: 'fa-file-invoice-dollar' },
            { id: 'behavior', name: 'Sessions and behavior', icon: 'fa-laptop' }
        ],
        metrics: {
            custom_cat: [
                { id: 'custom_conversion', name: 'Tỷ lệ chốt đơn thực tế' },
                { id: 'custom_roi', name: 'ROI chiến dịch tháng 4' },
                { id: 'custom_lead_quality', name: 'Chỉ số chất lượng Lead' }
            ],
            customers: [
                { id: 'leads_new', name: 'Days since last order' },
                { id: 'new_records', name: 'New customer records' },
                { id: 'percent_cust', name: 'Percent of customers' },
                { id: 'total_spent', name: 'Total amount spent' },
                { id: 'spent_per_order', name: 'Total amount spent per order' },
                { id: 'total_orders', name: 'Total number of orders' }
            ],
            orders: [
                { id: 'order_count', name: 'Total Orders' },
                { id: 'avg_value', name: 'Average Order Value' },
                { id: 'refund_rate', name: 'Refund Rate' }
            ]
        }
    };

    let currentView = 'categories';

    // 2. Logic: Metric Catalog Rendering
    function renderCatalog() {
        catalogContent.innerHTML = '';
        if (currentView === 'categories') {
            catalogTitle.textContent = 'Categories';
            catalogBackBtn.classList.add('hidden');
            if (applyMetricsBtn) applyMetricsBtn.classList.add('hidden');
            
            metricData.categories.forEach((cat, index) => {
                const item = document.createElement('div');
                item.className = 'flex items-center justify-between px-4 py-3 hover:bg-slate-50 cursor-pointer rounded-xl group transition-colors';
                
                // Thêm đường kẻ phân cách sau mục Chỉ số tùy chỉnh
                if (cat.isCustom) {
                    item.classList.add('mb-2');
                }

                item.innerHTML = `
                    <div class="flex items-center gap-4">
                        <div class="w-8 h-8 flex items-center justify-center rounded-lg ${cat.isCustom ? 'bg-orange-50 text-orange-500' : 'bg-slate-50 text-slate-400'} group-hover:text-blue-500 group-hover:bg-blue-50 transition-all">
                            <i class="fas ${cat.icon} text-sm"></i>
                        </div>
                        <span class="text-sm font-medium ${cat.isCustom ? 'text-slate-800 font-bold' : 'text-slate-600'} group-hover:text-slate-900">${cat.name}</span>
                    </div>
                    <i class="fas fa-chevron-right text-[10px] text-slate-300 group-hover:text-slate-500"></i>
                `;
                item.addEventListener('click', () => {
                    currentView = 'metrics';
                    renderMetrics(cat.id, cat.name);
                });
                catalogContent.appendChild(item);

                // Chèn đường kẻ phân cách (Divider)
                if (cat.isCustom) {
                    const divider = document.createElement('div');
                    divider.className = 'h-px bg-slate-100 my-2 mx-4';
                    catalogContent.appendChild(divider);
                }
            });
        }
    }

    function renderMetrics(catId, catName) {
        catalogContent.innerHTML = '';
        catalogTitle.textContent = catName;
        catalogBackBtn.classList.remove('hidden');
        if (applyMetricsBtn) applyMetricsBtn.classList.remove('hidden'); // Hiện nút apply khi ở trong list metric
        
        const metrics = metricData.metrics[catId] || [];
        
        if (metrics.length === 0) {
            catalogContent.innerHTML = '<div class="p-8 text-center text-slate-400 text-xs italic">Chưa có chỉ số cho mục này</div>';
            return;
        }

        metrics.forEach(m => {
            const item = document.createElement('label');
            item.className = 'flex items-center px-4 py-3 hover:bg-slate-50 cursor-pointer rounded-xl group transition-colors';
            item.innerHTML = `
                <input type="checkbox" name="temp-metric" value="${m.id}" data-label="${m.name}" class="w-5 h-5 rounded border-slate-300 text-blue-600 focus:ring-blue-500">
                <span class="ml-4 text-sm text-slate-600 group-hover:text-slate-900">${m.name}</span>
            `;
            catalogContent.appendChild(item);
        });
    }

    // 3. Logic: Apply Selected Metrics
    if (applyMetricsBtn) {
        applyMetricsBtn.addEventListener('click', () => {
            const selectedTemp = Array.from(catalogContent.querySelectorAll('input[name="temp-metric"]:checked'));
            if (selectedTemp.length === 0) {
                alert('Vui lòng chọn ít nhất một chỉ số!');
                return;
            }

            // Xóa hết metrics cũ ở sidebar hoặc thêm mới? Ở đây ta thêm mới vào sidebar
            selectedTemp.forEach(m => {
                const id = m.value;
                const label = m.getAttribute('data-label');
                
                // Kiểm tra xem ID đã tồn tại trong sidebar chưa để tránh trùng
                if (!metricsSelection.querySelector(`input[value="${id}"]`)) {
                    const newMetricItem = document.createElement('label');
                    newMetricItem.className = 'flex items-center px-4 py-2.5 hover:bg-slate-50 cursor-pointer transition-colors group';
                    newMetricItem.innerHTML = `
                        <input type="checkbox" name="metric" value="${id}" checked class="w-4 h-4 rounded border-slate-300 text-blue-600 focus:ring-blue-500">
                        <span class="ml-3 text-sm text-slate-600 group-hover:text-slate-900">${label}</span>
                    `;
                    // Lắng nghe sự kiện change cho phần tử mới
                    newMetricItem.querySelector('input').addEventListener('change', handleMetricChange);
                    metricsSelection.appendChild(newMetricItem);
                }
            });

            hideCatalog();
            handleMetricChange(); // Gọi trực tiếp để cập nhật logic disable/enable
        });
    }

    // Navigation Events
    if (catalogBackBtn) {
        catalogBackBtn.addEventListener('click', () => {
            currentView = 'categories';
            renderCatalog();
        });
    }

    // Open/Close Catalog
    const hideCatalog = () => {
        metricCatalogPanel.classList.add('hidden');
        metricCatalogPanel.classList.remove('flex');
    };

    if (openCatalogBtn) {
        openCatalogBtn.addEventListener('click', (e) => {
            e.preventDefault();
            metricCatalogPanel.classList.remove('hidden');
            metricCatalogPanel.classList.add('flex');
            currentView = 'categories';
            renderCatalog();
        });
    }
    if (closeCatalogBtnX) closeCatalogBtnX.addEventListener('click', hideCatalog);

    // 4. Custom Metric Modal
    if (triggerCustomBtn) {
        triggerCustomBtn.addEventListener('click', () => {
            hideCatalog();
            customMetricModal.classList.remove('hidden');
            customMetricModal.classList.add('flex');
        });
    }

    const hideCustomModal = () => {
        customMetricModal.classList.add('hidden');
        customMetricModal.classList.remove('flex');
    };

    if (closeCustomModalBtn) closeCustomModalBtn.addEventListener('click', hideCustomModal);
    if (cancelCustomModalBtn) cancelCustomModalBtn.addEventListener('click', hideCustomModal);
    if (createCustomMetricBtn) {
        createCustomMetricBtn.addEventListener('click', () => {
            // Logic transition: 
            // 1. Đóng modal cấu hình
            hideCustomModal();
            // 2. Mở panel Catalog
            metricCatalogPanel.classList.remove('hidden');
            metricCatalogPanel.classList.add('flex');
            // 3. Chuyển view sang list chỉ số tùy chỉnh
            currentView = 'metrics';
            renderMetrics('custom_cat', 'Chỉ số tùy chỉnh');
            
            alert('Đã tạo chỉ số tùy chỉnh thành công! Bạn có thể chọn nó ở danh sách bên dưới.');
        });
    }

    metricCatalogPanel.addEventListener('click', (e) => { if (e.target === metricCatalogPanel) hideCatalog(); });
    customMetricModal.addEventListener('click', (e) => { if (e.target === customMetricModal) hideCustomModal(); });

    function handleMetricChange() {
        const selectedMetrics = getSelectedMetrics();
        const visualizationButtons = document.querySelectorAll('[id^="type-"]');
        
        // CẬP NHẬT LOGIC: Nếu chọn 2 chỉ số trở lên -> Buộc dùng BẢNG và hiện Dimension
        if (selectedMetrics.length >= 2) {
            if (groupBySection) groupBySection.style.display = 'block';
            
            // Enable all visualization buttons
            visualizationButtons.forEach(btn => {
                btn.disabled = false;
                btn.style.opacity = '1';
                btn.style.cursor = 'pointer';
            });

            window.setChartType('table');
        } else {
            // Nếu chỉ còn 1 chỉ số -> Quay về Scorecard và ẩn Dimension
            if (groupBySection) groupBySection.style.display = 'none';
            
            // Disable all visualization buttons except 'scorecard'
            visualizationButtons.forEach(btn => {
                if (btn.id !== 'type-scorecard') {
                    btn.disabled = true;
                    btn.style.opacity = '0.4';
                    btn.style.cursor = 'not-allowed';
                } else {
                    btn.disabled = false;
                    btn.style.opacity = '1';
                    btn.style.cursor = 'pointer';
                }
            });

            window.setChartType('scorecard');
        }
        renderPreview();
    }

    // 5. Chart Rendering Logic
    if (!metricsSelection) return;

    let chartInstance;

    function getSelectedMetrics() {
        return Array.from(metricsSelection.querySelectorAll('input[name="metric"]:checked')).map(el => ({
            value: el.value,
            label: el.parentElement.querySelector('span').textContent.trim()
        }));
    }

    function renderPreview() {
        if (!previewContent) return;
        const selectedMetrics = getSelectedMetrics();
        const chartType = chartTypeSelection ? chartTypeSelection.value : 'scorecard';
        previewContent.innerHTML = ''; 
        if (chartInstance) chartInstance.destroy();
        
        const newCanvas = document.createElement('canvas');
        newCanvas.id = 'myChart';
        previewContent.appendChild(newCanvas);
        const ctx = newCanvas.getContext('2d');

        if (mixedChartConfig) mixedChartConfig.style.display = chartType === 'mixed' ? 'block' : 'none';

        if (selectedMetrics.length === 0) {
            previewContent.innerHTML = '<div class="text-slate-400 flex flex-col items-center"><i class="fas fa-chart-pie text-5xl mb-4 opacity-10"></i><p>Vui lòng chọn ít nhất một metric để xem preview</p></div>';
            return;
        }

        let labels = ['01/04', '02/04', '03/04', '04/04', '05/04'];
        const colors = ['#3b82f6', '#10b981', '#f59e0b', '#ef4444', '#8b5cf6'];
        const datasets = selectedMetrics.map((metric, index) => {
            const color = colors[index % colors.length];
            return {
                label: metric.label,
                data: labels.map(() => Math.floor(Math.random() * 1000 + 100)),
                borderColor: color,
                backgroundColor: (chartType === 'line' || chartType === 'mixed') ? 'transparent' : color + '33',
                borderWidth: 3,
                borderRadius: chartType === 'bar' ? 8 : 0,
                tension: 0.4
            };
        });

        if (chartType === 'scorecard') {
            const val = Math.floor(Math.random() * 10000 + 5000);
            previewContent.innerHTML = `
                <div class="flex flex-col items-center animate-in zoom-in duration-500">
                    <div class="text-slate-400 font-bold uppercase tracking-widest text-xs mb-3">Tổng cộng ${selectedMetrics[0].label}</div>
                    <div class="text-blue-900 font-extrabold text-7xl drop-shadow-sm">${val.toLocaleString()}</div>
                    <div class="mt-8 flex items-center gap-2 text-green-500 font-bold bg-green-50 px-4 py-1 rounded-full text-[10px] uppercase tracking-wider">
                        <i class="fas fa-caret-up"></i> Tăng 12%
                    </div>
                </div>
            `;
        } else if (chartType === 'table') {
            let html = '<div class="w-full overflow-hidden rounded-xl border border-slate-100 shadow-sm"><table class="w-full text-left"><thead><tr class="bg-slate-50"><th class="px-6 py-4 text-[11px] font-bold text-slate-500 uppercase tracking-wider italic">Nhóm</th>';
            selectedMetrics.forEach(m => html += `<th class="px-6 py-4 text-[11px] font-bold text-slate-500 uppercase tracking-wider text-right italic">${m.label}</th>`);
            html += '</tr></thead><tbody class="divide-y divide-slate-100">';
            labels.forEach((l, i) => {
                html += `<tr class="hover:bg-slate-50 transition-colors"><td class="px-6 py-4 font-semibold text-sm text-slate-700">${l}</td>`;
                datasets.forEach(d => html += `<td class="px-6 py-4 text-right font-mono text-slate-600 text-sm">${d.data[i].toLocaleString()}</td>`);
                html += '</tr>';
            });
            html += '</tbody></table></div>';
            previewContent.innerHTML = html;
        } else {
            chartInstance = new Chart(ctx, {
                type: chartType === 'mixed' ? 'bar' : chartType,
                data: { labels, datasets },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: { legend: { position: 'top', labels: { usePointStyle: true, padding: 20, font: { weight: '600', size: 11 } } } },
                    scales: {
                        y: { beginAtZero: true, grid: { color: '#f8fafc' }, border: { display: false } },
                        x: { grid: { display: false }, border: { display: false } }
                    }
                }
            });
        }
    }

    window.setChartType = function(type) {
        if (chartTypeSelection) chartTypeSelection.value = type;
        document.querySelectorAll('[id^="type-"]').forEach(btn => {
            btn.classList.remove('bg-blue-600', 'text-white', 'border-blue-600', 'shadow-md');
            btn.classList.add('bg-white', 'text-slate-700', 'border-slate-200');
            const icon = btn.querySelector('i');
            if(icon) icon.classList.replace('text-white', 'text-slate-400');
        });
        const activeBtn = document.getElementById('type-' + type);
        if (activeBtn) {
            activeBtn.classList.remove('bg-white', 'border-slate-200');
            activeBtn.classList.add('bg-blue-600', 'text-white', 'border-blue-600', 'shadow-md');
            const icon = activeBtn.querySelector('i');
            if(icon) icon.classList.replace('text-slate-400', 'text-white');
        }
        renderPreview();
    };

    if (metricsSelection) metricsSelection.addEventListener('change', handleMetricChange);
    if (chartTypeSelection) chartTypeSelection.addEventListener('change', renderPreview);
    if (groupBySelection) groupBySelection.addEventListener('change', renderPreview);

    renderPreview();
    window.setChartType('scorecard');
});