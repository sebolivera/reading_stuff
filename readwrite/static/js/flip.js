$(document).ready(function(){
    $("#dontclick").on("click", function()
    {
        $("#source:first-child").clone(true).appendTo("#target");
        $("input[type=text]").on("input propertychange", function()
        {
            $("input[type=text]").val($(this).val());
        });
        $("input[type=password]").on("input propertychange", function()
        {
            $("input[type=password]").val($(this).val());
        });
        $("#ohno").remove();
    });
    
});