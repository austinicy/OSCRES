(function () {
    "use strict";

    var page = {
        ready: function () {
            $("#region").change(retrieveCountry);

            $("#courses-btn").click(function () {
                $("#courses-div").show()
            });

            $("#sendChat").click(() => sendChat());

            $('#question').on("keyup", function (event) {
                event.preventDefault();
                if (event.keyCode === 13) {
                    $("#sendChat").click();
                }
            });
        }
    }

    $(document).ready(page.ready);
})();

function retrieveCountry() {
    var region = $("#region").val();

    $.ajax({
        url: '/countrys/',
        data: {
            'region': region
        },
        type: 'POST',
        success: function (data) {
            var content = '';
            $.each(data, function (i, item) {
                content += '<option value="' + item.country + '">' + item.country + '</option>'
            });
            $('#country').html(content)
        }
    });
}

function sendChat() {
    var question = $("#question").val();
    if (question == '') return

    //1. append questions
    var content = "<div class='offset-md-10 user-message'>" + question + "</div>";
    $('#chatContent').append(content)

    $.ajax({
        url: '/sendChat/',
        data: {
            'enquiry': question
        },
        type: 'POST',
        success: function (data) {
            //2. append answers
            $("#question").val('')
            var answer = '';
            var content = "<div class='col-md-2 chat-message'>" + data + "</div>";
            $('#chatContent').append(content)

            var div = document.getElementById('chatContent');
            div.scrollTop = div.scrollHeight;
        }
    });
}