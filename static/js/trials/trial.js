// $('h3').click(function () {
// console.log("It changed");
// // change text each time u click on it
// $(this).text('Succesful')

// });


// $('input').eq(0).keypress(function () {
// $('h3').css("color","blue");

// });


// $("h3").on("dblclick", function (){
// $(this).css("color", "red")
// });

// $("h3").on("mouseenter", function (){
// $(this).css("color", "red")
// })

// DATEPICKER
var datepickerDateFormat = 'yy-mm-dd';
var displayDateFormat = datepickerDateFormat.replace('yy', 'yyyy');

// $(document).ready(function () {
//
//     var dateFieldValue = $.trim($("#id_start_date", "#id_end_date").val());
//     if (dateFieldValue == '') {
//         $("#id_start_date").val(displayDateFormat);
//         $("#id_end_date").val(displayDateFormat);
//     }
//
//     daymarker.bindElement("#id_start_date", "#id_end_date",
//         {
//             onClose: function () {
//                 $("#id_start_date").trigger('blur');
//                 $("#id_end_date").trigger('blur');
//             }
//         });
//
//     //$("img.ui-datepicker-trigger").addClass("editable");
//
//     $("#id_start_date").click(function () {
//         daymarker.show("#id_start_date");
//         if ($(this).val() == displayDateFormat) {
//             $(this).val('');
//         }
//     });
//
// });

//---------------- //


var leaveBalanceUrl = '{% url "leave:get_leave_balance" %}';
var lang_invalidDate = 'Should be a valid date in yyyy-mm-dd format';
var lang_dateError = 'To date should be after from date';
var lang_details = 'view details';
var lang_BalanceNotSufficient = "Balance not sufficient";
var lang_Duration = "Duration";
var lang_StartDay = "Start Day";
var lang_EndDay = "End Day";

$(document).ready(function () {
    showTimeControls(false, false);
    updateLeaveBalance();

    $('#end_date').change(function () {
        toDateBlur($(this).val());
    });

    $('#applyleave_partialDays').change(function () {
        handlePartialDayChange(true);
    });

    if (trim($("#start_date").val()) == displayDateFormat || trim($("#end_date").val()) == displayDateFormat
        || trim($("#start_date").val()) == '' || trim($("#end_date").val()) == '') {
        showTimeControls(false, false);
    } else if (trim($("#start_date").val()) == trim($("#end_date").val())) {
        showTimeControls(true, false);
    } else {
        showTimeControls(false, true);
    }

    // Bind On change event of time elements
    $('select.timepicker').change(function () {
        fillTotalTime($(this));
    });


});

