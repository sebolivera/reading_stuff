$(document).ready(function(){
    $("#dontclick:not(#source), .nothere").on("click", function()
    {
        $(".mirror").removeClass("mirror");
        $("body").addClass("mirror");
        $("#source").addClass("unmirror");
        $("#source:first-child").clone(true).appendTo("#target");
        $("input[type=text]").on("input propertychange", function()
        {
            $("input[type=text]").val($(this).val());
        });
        $("input[type=password]").on("input propertychange", function()
        {
            $("input[type=password]").val($(this).val());
        });
        $(".unmirror").first().removeClass("unmirror");
        $("*").removeClass("text-light").removeClass("text-dark");
        $("#ohno, .nothere, #huh").remove();
        $("nav div *:not(.navbar-brand)").css("visibility", "hidden");
        $("nav").removeClass("bg-primary").removeClass("shadow").css("box-shadow", "none !important").css("background-color", "transparent !important");
        $("footer").remove();
        $("body").removeClass("bg-dark").removeClass("bg-light").css("background-color", "rgba(38, 0, 0, 0.97)");
        $("html").css("background", "url("+m_image+") no-repeat").css("background-position", "center").css("background-size", "cover");
        $("html, body").css("height", "100%");
        $('label').removeClass("bg-light").removeClass("bg-dark").css("background-color", "rgba(38, 0, 0, 0.97)");
        $("*").removeClass("text-soft-dark").removeClass("text-soft-light").removeClass("very-dark").removeClass("very-light").removeClass("card");
        $("h1").html("WHAT HAVE YOU DONE?").addClass("unmirror");
    }).delay( 1000 );
    
});