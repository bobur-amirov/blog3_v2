$(document).ready(function (){
    $("#createButtun").click(function (){
       let serializedData =
           $("#createCommentForm").serialize();
       $.ajax({
           url: $("createCommentForm").data('url'),
           data: serializedData,
           type: 'post',
           success: function (response){
               $("#commentList").append('<div class="card mb-1">\n' +
                   '                    <div class="card-body">\n' +
                   '                        <p>' + response.comment.text + '</p>\n' +
                   '                    </div>\n' +
                   '                </div>')
           }
       })
        $("#createCommentForm")[0].reset();

    });
});