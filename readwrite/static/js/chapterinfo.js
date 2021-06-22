$(document).ready(function()
{
    console.log($("#ischapter").is(':checked'));
    if ($("#ischapter").is(':checked'))
    {
        $(".book-info").toggle("slide", {direction:"up"});
    }
    $("#ischapter").change(function()
    {
        $(".book-info").toggle("slide", {direction:"up"});
    });
    $("form").submit(function(e){
        if ($("#book").val()=='')
        {
            e.preventDefault();
            $(".book-select-error").show();
        }
    });
});