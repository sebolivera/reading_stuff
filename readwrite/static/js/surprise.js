// jGravity works best when targeting the body
$(document).ready(function()
{
    $("#please-dont-click").on("click", function()
    {
        $("body").css("overflow", "hidden");
        $(this).throwable({gravity:{x:0,y:10},});
        setTimeout(() =>
            {$(".angry").fadeIn(5000).delay(2000).css("filter", "saturate(255)");
            var audio = document.getElementById("myAudio");
            audio.loop = true;
            audio.play();
            var interval = 200;
            var vol = 0;
            var fadein = setInterval(//didn't use jquery bc im a fucking idiot
                function() {
                  if (vol < 1) {
                    vol += 0.001;
                    audio.volume = vol;
                  }
                  else {
                    clearInterval(fadein);
                  }
                }, interval);
        }, 5000 );
        
        setTimeout(() =>
            {$(".mad-overlay").fadeIn(5000).delay(2000);
        }, 6000 );
            
        setTimeout(() =>
        {$(".take-me-home").fadeIn(5000).delay(2000);
        }, 7000 );

        
        
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

