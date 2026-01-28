// ===== MODULE CARD INTERACTIONS =====
document.addEventListener('DOMContentLoaded', () => {
    initializeModuleCards();
    initializeAnimations();
    initializeNotifications();
});

// Initialize module card interactions
function initializeModuleCards() {
    const moduleCards = document.querySelectorAll('.module-card');
    
    moduleCards.forEach((card, index) => {
        // Add staggered animation delay
        card.style.animationDelay = `${index * 0.05}s`;
        
        // Add click handler for entire card
        card.addEventListener('click', (e) => {
            // Don't trigger if clicking the link directly
            if (e.target.closest('.module-link')) return;
            
            const link = card.querySelector('.module-link');
            if (link) {
                // Add loading state
                card.classList.add('loading');
                
                // Simulate navigation delay for smooth transition
                setTimeout(() => {
                    window.location.href = link.href;
                }, 300);
            }
        });
        
        // Add ripple effect on click
        card.addEventListener('mousedown', createRipple);
    });
}

// Create ripple effect
function createRipple(event) {
    const card = event.currentTarget;
    const ripple = document.createElement('span');
    const rect = card.getBoundingClientRect();
    const size = Math.max(rect.width, rect.height);
    const x = event.clientX - rect.left - size / 2;
    const y = event.clientY - rect.top - size / 2;
    
    ripple.style.cssText = `
        position: absolute;
        width: ${size}px;
        height: ${size}px;
        border-radius: 50%;
        background: rgba(255, 255, 255, 0.3);
        left: ${x}px;
        top: ${y}px;
        pointer-events: none;
        transform: scale(0);
        animation: ripple 0.6s ease-out;
        z-index: 1;
    `;
    
    card.appendChild(ripple);
    
    ripple.addEventListener('animationend', () => {
        ripple.remove();
    });
}

// Add ripple animation to CSS dynamically
const style = document.createElement('style');
style.textContent = `
    @keyframes ripple {
        to {
            transform: scale(4);
            opacity: 0;
        }
    }
`;
document.head.appendChild(style);

// Initialize scroll animations
function initializeAnimations() {
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);
    
    // Observe module cards for scroll animations
    const cards = document.querySelectorAll('.module-card');
    cards.forEach(card => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';
        card.style.transition = 'opacity 0.6s ease-out, transform 0.6s ease-out';
        observer.observe(card);
    });
}

// Initialize notification interactions
function initializeNotifications() {
    const notificationBtn = document.querySelector('.notification-btn');
    
    if (notificationBtn) {
        notificationBtn.addEventListener('click', (e) => {
            e.stopPropagation();
            showNotificationPanel();
        });
    }
}

// Show notification panel (placeholder)
function showNotificationPanel() {
    // This is a placeholder for future notification functionality
    console.log('Notification panel clicked');
    
    // You can implement a dropdown/modal here
    alert('Bạn không có thông báo mới');
}

// Add keyboard navigation
document.addEventListener('keydown', (e) => {
    const moduleCards = Array.from(document.querySelectorAll('.module-card'));
    const focusedCard = document.activeElement.closest('.module-card');
    
    if (!focusedCard) return;
    
    const currentIndex = moduleCards.indexOf(focusedCard);
    let nextIndex;
    
    switch(e.key) {
        case 'ArrowRight':
            nextIndex = (currentIndex + 1) % moduleCards.length;
            moduleCards[nextIndex].focus();
            e.preventDefault();
            break;
        case 'ArrowLeft':
            nextIndex = (currentIndex - 1 + moduleCards.length) % moduleCards.length;
            moduleCards[nextIndex].focus();
            e.preventDefault();
            break;
        case 'ArrowDown':
            nextIndex = Math.min(currentIndex + 3, moduleCards.length - 1);
            moduleCards[nextIndex].focus();
            e.preventDefault();
            break;
        case 'ArrowUp':
            nextIndex = Math.max(currentIndex - 3, 0);
            moduleCards[nextIndex].focus();
            e.preventDefault();
            break;
        case 'Enter':
            const link = focusedCard.querySelector('.module-link');
            if (link) link.click();
            break;
    }
});

// Make cards focusable for keyboard navigation
document.querySelectorAll('.module-card').forEach(card => {
    card.setAttribute('tabindex', '0');
});

// Add search functionality (optional enhancement)
function addSearchFunctionality() {
    const searchInput = document.createElement('input');
    searchInput.type = 'text';
    searchInput.placeholder = 'Tìm kiếm module...';
    searchInput.className = 'module-search';
    
    searchInput.style.cssText = `
        width: 100%;
        max-width: 400px;
        padding: 12px 16px;
        border: 1px solid var(--gray-300);
        border-radius: var(--radius-lg);
        font-size: 0.875rem;
        margin-bottom: var(--spacing-xl);
        transition: all 0.2s;
    `;
    
    const welcomeSection = document.querySelector('.welcome-section');
    if (welcomeSection) {
        welcomeSection.appendChild(searchInput);
    }
    
    searchInput.addEventListener('input', (e) => {
        const searchTerm = e.target.value.toLowerCase();
        const moduleCards = document.querySelectorAll('.module-card');
        
        moduleCards.forEach(card => {
            const title = card.querySelector('.module-title').textContent.toLowerCase();
            const shouldShow = title.includes(searchTerm);
            
            card.style.display = shouldShow ? 'flex' : 'none';
            
            if (shouldShow) {
                card.style.animation = 'fadeIn 0.3s ease-out';
            }
        });
    });
}

// Uncomment to enable search
// addSearchFunctionality();

// Performance monitoring
if ('PerformanceObserver' in window) {
    const observer = new PerformanceObserver((list) => {
        for (const entry of list.getEntries()) {
            console.log(`${entry.name}: ${entry.duration}ms`);
        }
    });
    
    observer.observe({ entryTypes: ['measure', 'navigation'] });
}

// Add loading state management
window.addEventListener('beforeunload', () => {
    document.body.style.opacity = '0.8';
    document.body.style.pointerEvents = 'none';
});
