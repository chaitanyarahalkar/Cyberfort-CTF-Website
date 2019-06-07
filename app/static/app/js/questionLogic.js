var clock;

    function getTime(){
      var xhttp = new XMLHttpRequest();
      xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
          // document.getElementById("demo").innerHTML = this.responseText;
          clock = $('.countdown-timer').FlipClock(this.responseText, {
            clockFace: 'HourlyCounter',
            countdown: true,
            callbacks: {
              stop: function() {
                 window.location.href= "/logout";
              }
            }
        });
        }
       };
        xhttp.open("GET", "/timer", true);
        xhttp.send();
        setTimeout(getTime,60000);
      }


    $(document).ready(function() {
      getTime();

  });


    function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


  function csrfSafeMethod(method) {
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

    function getHint(id){

      $.ajaxSetup({
              beforeSend: function(xhr, settings) {
            if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
                xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
                }
            }
        });
      $.ajax({
          type: "POST",
          dataType: "json",
          url: "/hint/",
          data: {hintid:id},
          beforeSend: function(xhr, settings) {
            $.ajaxSettings.beforeSend(xhr, settings);
          },
          success: function(result) {
            var selector = "#hint-content";
              $(selector).text(result.hint);
              $("#points").text(result.points + " Points");
          }
      });
  }


$("#username").keyup(function () {
      var username = $(this).val();

      $.ajax({
        url: '/uservalidator/',
        data: {
          'username': username
        },
        dataType: 'json',
        success: function (data) {
          if (data.is_taken) {
            $("#username").removeClass("is-valid").addClass('is-invalid');
          }
          else{
            $("#username").removeClass("is-invalid").addClass('is-valid'); 
          }
        }
      });

    });