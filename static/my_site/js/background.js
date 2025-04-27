document.addEventListener('DOMContentLoaded', function() {
    const bg = document.querySelector('.vector-bg');
    
    // Параллакс-эффект при движении мыши
    document.addEventListener('mousemove', (e) => {
        const speed = 0.02;
        const x = (window.innerWidth - e.pageX * speed) / 100;
        const y = (window.innerHeight - e.pageY * speed) / 100;
        bg.style.transform = `translate(${-x}%, ${-y}%)`;
    });
    
    // Пауза анимации при наведении
    bg.addEventListener('mouseenter', () => {
        bg.style.animationPlayState = 'paused';
    });
    
    bg.addEventListener('mouseleave', () => {
        bg.style.animationPlayState = 'running';
    });
});