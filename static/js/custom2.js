
function showMessage(message){
     // var template =  "{% include 'alert.html' with message='" + message+ "' %}";
    var  template = "<div class='container container-alert-message'><div class='col-sm-4 col-sm-offset-8'>"+
        "<div class='alert alert-success alert-dismissable' role='alert'>"+
        "<button class='close' type='button' data-dismiss='alert' aria-label='close'>"+
        "<span aria-hidden='true'>&times;</span></button>'"+message+"'</div></div></div>";

     $('body').append(template);
     $('.container-alert-message').fadeIn();
     setTimeout(function () {
         $('.container-alert-message').fadeOut();
     }, 2800)
}

