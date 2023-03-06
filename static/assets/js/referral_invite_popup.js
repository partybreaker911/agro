$(document).ready(function () {
    // Show the popup when the button is clicked
    $('#invite-referral-btn').on('click', function () {
        $('#referral-invite-popup').show();
    });

    // Submit the form using AJAX
    $('#referral-invite-form').on('submit', function (event) {
        event.preventDefault();
        $.ajax({
            url: "{% url 'referral_invite' %}",
            type: 'POST',
            data: $(this).serialize(),
            success: function () {
                $('#referral-invite-success').show();
                $('#referral-invite-form').hide();
            },
            error: function () {
                $('#referral-invite-error').html('An error occurred. Please try again.').show();
            }
        });
    });

    // Close the popup when the close button is clicked
    $('#close-referral-invite-popup').on('click', function () {
        $('#referral-invite-popup').hide();
    });
});