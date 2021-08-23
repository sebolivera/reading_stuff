$(document).ready(function(){
    $("#dontclick:not(#source)").on("click", function()
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
        $("#ohno").remove();
        $("nav").css("visibility", "hidden");
        $("footer").remove();
        $("body").removeClass("bg-dark");
        $("body").removeClass("bg-light");
        $("html").css("background", "url("+m_image+") no-repeat");
        $("html").css("background-position", "center");
        $("html").css("background-size", "cover");
        $("body").css("background-color", "rgba(38, 0, 0, 0.97)");
        $("html, body").css("height", "100%");
    }).delay( 1000 );
    
});