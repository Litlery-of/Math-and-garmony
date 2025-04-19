document.addEventListener('DOMContentLoaded', function() {
    const slider = document.getElementById('goldenRatioSlider');
    const goldenVersion = document.querySelector('.golden-version');

    slider.addEventListener('input', function(e) {
        const value = e.target.value + '%';
        goldenVersion.style.width = value; // Изменяем видимую область
        goldenVersion.style.clipPath = `inset(0 0 0 ${value})`; // Эффект "перетягивания"
    });
});