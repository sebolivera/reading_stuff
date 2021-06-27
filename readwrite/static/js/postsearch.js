$(document).ready(function()
{
    
    $("#search").val('');
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

    const search=$("#search");
    const content=$("#post-holder");
    const delay_by_in_ms = 700
    let scheduled_function = false

    let ajax_call = function (path, request_parameters) {
        $.ajax({
            url: search_path,
            type: "POST",
            data: request_parameters,
            headers: {
            'X-CSRFToken': csrftoken
            },
            success: function(response){
                content.promise().then(() => {
                    // replace the HTML contents
                    content.html(response['html_from_view']);
                    // fade-in the div with new contents
                    content.fadeTo('slow', 1);
                    // stop animating the search 
                });
            }
        });
    }
    
    search.on('keyup', function () {

        const request_parameters = {
            search: $(this).val(), // value of user_input: the HTML element with ID user-input
        };

        // start animating the search 
        content.html('<div class="text-center"><div class="spinner-border m-5" role="status"><span class="visually-hidden">Loading...</span></div></div>');

        // if scheduled_function is NOT false, cancel the execution of the function
        if (scheduled_function) {
            clearTimeout(scheduled_function);
        }

        // setTimeout returns the ID of the function to be executed
        scheduled_function = setTimeout(ajax_call, delay_by_in_ms, path, request_parameters);
    });
});