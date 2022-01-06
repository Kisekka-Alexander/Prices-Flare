/**
 * Created by NOBLE on 04/07/2017.
 */


$(document).ready(function(){
    $('.data-picker-ui-hrm').datepicker({
        dateFormat:"yy-mm-dd",
        changeMonth: true,
        changeYear: true,
    });

});

$(document).ready(function(){
    $('#start-time').datetimepicker({
        datepicker:false,
    });

});

$(document).ready(function(){
    $('#end-time').datetimepicker({
        datepicker:false,
        // format:'H:i',
    });

});

$(document).ready(function(){
    $('#id_time').datetimepicker({
        datepicker:false,
        // format:'H:i',
    });

});

$(document).ready(function(){
    $('#id_date').datetimepicker({
        timepicker:false,
        format:'Y-m-d',

    });
});

$(document).ready(function(){
    $('#id_license_expiry_date').datetimepicker({
        timepicker:false,
        format:'Y-m-d',

    });
});


$(document).ready(function(){
    $('#id_date_of_advert').datetimepicker({
        timepicker:false,
        format:'Y-m-d',

    });
});

$(document).ready(function(){
    $('#id_deadline').datetimepicker({
        timepicker:false,
        format:'Y-m-d',

    });
});

$(document).ready(function(){
    $('#id_date_of_application').datetimepicker({
        timepicker:false,
        format:'Y-m-d',

    });
});

$(document).ready(function(){
    $('#id_project_end_date').datetimepicker({
        timepicker:false,
        format:'Y-m-d',

    });
});

$(document).ready(function(){
    $('#id_project_start_date').datetimepicker({
        timepicker:false,
        format:'Y-m-d',

    });
});


$(document).ready(function(){
    $('#search_date').datetimepicker({
        timepicker:false,
        format:'Y-m-d',

    });
});


$(document).ready(function(){
    $('#id_joined_date').datetimepicker({
        timepicker:false,
        format:'Y-m-d',

    });
});


function node() {
    // var employee = window.prompt("Enter your name:");
    var change = document.getElementById("time_in");
    if (change.value == "Punch In") {
        change.value = "Punch Out";
        window.location.href = "{% url 'time_management:time_out' %}"
    }
    else {
        change.value = "Punch In";
    }
}

function noble() {
    var see = document.getElementById("newtracker")
}


$(document).ready(function () {
    $("#id_date").prop('disabled', true);

})

$(document).ready(function () {
    $("#id_time_in").prop('disabled', true);
})

