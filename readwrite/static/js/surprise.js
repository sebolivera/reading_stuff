// jGravity works best when targeting the body
$(document).ready(function()
{
    $("#please-dont-click").on("click", function()
    {
        $('#under-const').throwable({ 
            gravity:{x:0,y:10},
        });
    });
});

