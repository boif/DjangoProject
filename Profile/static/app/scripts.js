document.addEventListener('DOMContentLoaded', function() {
    const postText = document.getElementById('post-text');
    const fileInput = document.getElementById('file-input');
    const createPostBtn = document.getElementById('create-post-btn');

    postText.addEventListener('input', toggleCreatePostBtn);
    fileInput.addEventListener('change', toggleCreatePostBtn);

    function toggleCreatePostBtn() {
        if (postText.value.trim() !== '' || fileInput.value !== '') {
            createPostBtn.style.display = 'inline-block'; // Показываем кнопку, если есть текст или выбран файл
        } else {
            createPostBtn.style.display = 'none'; // Скрываем кнопку, если нет текста и не выбран файл
        }
    }
});
