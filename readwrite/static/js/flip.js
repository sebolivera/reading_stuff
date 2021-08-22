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
    });
    
});