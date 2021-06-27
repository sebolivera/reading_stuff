$(document).ready(function()
{
    if ($("#ischapter").is(':checked'))
    {
        $(".book-info").show("slide", {direction:"up"});
    }
    $("#ischapter").change(function(e)
    {
        if ($("#ischapter").is(':checked'))
        {
            $(".book-info").show("slide", {direction:"up"});//toggle() was fucking up for some reason
        }
        else
        {
            $(".book-info").hide("slide", {direction:"up"});
        }
    });
    $("form").submit(function(e){
        if ($("#book").val()=='')
        {
            e.preventDefault();
            $(".book-select-error").show();
        }
    });
});