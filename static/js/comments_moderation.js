$(document).ready(function()
{
    const content = $(".main-comments");
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

    let ajax_call = function (path, request_parameters, div_to_destroy_if_sucess) {
        $.ajax({
            url: path,
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
                    div_to_destroy_if_sucess.remove();
                });
            }
        });
    }

    $(".form-moderation").unbind('submit').bind('submit', function(e){//arguably not the best way to do this...
        const request_parameters = {
            id: $(this).attr('id'), // value of user_input: the HTML element with ID user-input
        };
        e.preventDefault();
        if($(this).hasClass('approve'))
        {
            ajax_call(url_approve, request_parameters, $(this).parent().parent());
        }
        else if($(this).hasClass('delete'))
        {
            if (confirm('Are you sure you want to delete this comment?')) {
            // Save it!
                ajax_call(url_delete, request_parameters, $(this).parent().parent());
                //console.log("calling: " + url_delete + " with " + $(this).attr('id'));
            } else {
            // Do nothing!
                console.log('Thing was not saved to the database.');
            }
        }
    });
});