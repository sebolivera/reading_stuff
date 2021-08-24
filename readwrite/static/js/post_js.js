$(document).ready(function()
{
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    const csrftoken = getCookie('csrftoken');

    $(".fav").on("click",function()
    {
        if ($(this).hasClass("add_fav"))
        {
            $(this).removeClass("add_fav").addClass("delete_fav");
            $(this).html($("#star-fill-span").html());
            console.log("unfilled");
            var request_parameters = {id_post : $(this).attr("id")};
            $.ajax({
                url: url_favorites,
                type: "POST",
                data: request_parameters,
                headers: {
                'X-CSRFToken': csrftoken
                },
                success: function(response){
                    $(this).promise().then(() => {
                        $(this).html($("#star-fill-span").html());
                    });
                }
            });
        }
        else if($(this).hasClass("delete_fav"))
        {
            console.log("has delete fav")
            $(this).removeClass("delete_fav").addClass("add_fav");
            $(this).html($("#star-span").html());
            var request_parameters = {id_post : $(this).attr("id")};
            $.ajax({
                url: url_favorites,
                type: "POST",
                data: request_parameters,
                headers: {
                'X-CSRFToken': csrftoken
                },
                success: function(response){
                    $(this).promise().then(() => {
                        $(this).html($("#star-span").html());
                    });
                }
            });
        }
    });
});