$(document).ready(function() {
    let header = $('#header');
    let scrollPos = $(window).scrollTop();
    let intro = $('#intro');
    let introH = intro.innerHeight();
    const comment_button = document.getElementById("#comment-btn")


    function toggleCommentForm(postId) {
        const form = document.getElementById(`comment-form-${postId}`);
        if (form.style.display === "none") {
            form.style.display = "block";
        } 
    }

    $('#icon').on('click', function(event) {
        event.preventDefault();
        $('#navv_inner').toggleClass('active');
    });

    // Убираем блокировку перехода по ссылкам
    $('.navv__link').on('click', function() {
        // Можно добавить любую дополнительную логику здесь
        // Например, можно закрыть меню после перехода по ссылке
        $('#navv_inner').removeClass('active');
    });
});