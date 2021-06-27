$(document).ready(function()
{
    $('.toast').toast('show');
    $(".close-toast").on("click", function()
    {
        $(this).parent().parent().toast('hide');
    });
});