$(document).ready(function(){
    $(function () {
        $('[data-toggle="tooltip"]').tooltip();
        $( '[data-toggle="tooltip"]' ).each(function() {
            $(this).attr('title', $(this).attr('data-bs-original-title'));
            $(this).attr('data-html', "true");
        });
    });
});