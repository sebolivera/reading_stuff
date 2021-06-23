// jGravity works best when targeting the body
$(document).ready(function()
{
    setTimeout(() =>
        {$(".angry").fadeIn(5000).delay(2000).css("filter", "saturate(255)");
    }, 5000 );
        
    $("#please-dont-click").on("click", function()
    {
        // $(".angry").delay(2000).css("transition", "saturate 5s");
        $('.card, .nav-link, .navbar, footer, header').each(function()
        {
            let i = Math.floor(Math.random() * 5000);
            //$(this).throwable({gravity:{x:0,y:10},}).delay(Math.floor(Math.random() * 10000)+1000);
            setTimeout(() =>
            {
                $(this).throwable({gravity:{x:0,y:10},})
            }, i * 2 );
            
        });
    });
});

