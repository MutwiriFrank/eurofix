$(document).ready(function(){
    $('.menu-toggle').click(function(){
        $('nav').toggleClass('active')
    })
    $('nav ul li').click(function(){
        $(this).siblings().removeClass('active')
        $(this).removeClass('active')
        $(this).toggleClass('active')

    })
})

