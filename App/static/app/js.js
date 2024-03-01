const themeToggle = document.getElementById('theme-toggle');

// Добавляем обработчик события при клике на кнопку
themeToggle.addEventListener('click', () => {
    // Получаем ссылку на элемент body
    const body = document.body;

    // Переключаем класс тела документа между dark-theme и light-theme
    body.classList.toggle('dark-theme');
    body.classList.toggle('light-theme');
});
