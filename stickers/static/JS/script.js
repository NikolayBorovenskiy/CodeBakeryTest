$(document).ready(function(){
    //Анимация кнопок редактирования на стекерах tash_list.html
    $('.btn-custom-js').fadeTo('slow', 0.3);
    $('.btn-custom-js').mouseleave(function(event) {
        $(this).fadeTo('slow', 0.3);
    });
    $('.btn-custom-js').mouseenter(function(event) {
        $(this).fadeTo('fast', 1.0);
    });

    //Фича что-бы выезжало меню сортировки
    $('.filter').fadeOut('slow');
    $('.slidet').click(function(event) {
        $('.filter').slideToggle('slow');
        console.log('Привет');
    });
});
