$(document).ready(function () {
    $(document).on('submit', '#newsletter_form', function (e) {
        e.preventDefault();
        const name = $('#newsletter_input_name').val();
        const email = $('#newsletter_input_email').val();
        $.ajax({
            type: 'POST',
            url: 'getemail/',
            data: {
                name: name,
                email: email,
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            success: function () {
                cosole.log()
            },
        });
    });
});