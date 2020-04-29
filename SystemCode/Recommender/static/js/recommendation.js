(function () {
    "use strict";

    var page = {
        ready: function () {
            $("#region").change(retrieveCountry);

            $("#courses-btn").click(function () {
                $("#courses-div").show()
            });

            $("#sendChat").click(() => {
                if (!$("#sendChat").prop("disabled")) {
                    sendChat()
                }
            });

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

function scrollTopResp() {
    var div = document.getElementById('chatContent');
    div.scrollTop = div.scrollHeight;
}

function sendChat() {
    var question = $("#question").val();
    if (question == '') return

    //1. append questions
    var content = "<div class='offset-md-10 user-message'>" + question + "</div>";
    $('#chatContent').append(content)

    //generate a random number
    var seqno = new Date().getTime()

    $.ajax({
        url: '/sendChat/',
        data: {
            'enquiry': question,
            'csrfmiddlewaretoken': $('[name="csrfmiddlewaretoken"]').val()
        },
        type: 'POST',
        beforeSend: function () {
            //disable submit button
            $("#sendChat").attr({
                disabled: "disabled"
            })

            //preloading image
            var image = "<img id='loading' src='" + loadingurl + "'/>"
            var content = "<div id='" + seqno + "' class='col-md-2 chat-message'>" + image + "</div>";
            $("#chatContent").append(content)

            //set content bottom
            scrollTopResp()
        },
        success: function (data) {
            //2. append answers
            $("#question").val('')

            //remove disalbe status
            $("#sendChat").removeAttr('disabled')

            //remove image and append result
            $("#loading").remove()
            $("#" + seqno).append(data)

            //set content bottom
            scrollTopResp()
        }
    });
}