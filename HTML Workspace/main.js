var url = "https://api.thingspeak.com/update?";
var params_on = "api_key=2BYWHU13YYCX9YCA&field1=1";
var params_off = "api_key=2BYWHU13YYCX9YCA&field1=0";
var params_Auto = "api_key=2BYWHU13YYCX9YCA&field2=1";
var params_Manual = "api_key=2BYWHU13YYCX9YCA&field2=0";
var xhr = new XMLHttpRequest();
var i = 0;
function AutoManual(){
    i = i+1;
    if (i>=3){
        i = 0;
    }
    switch(i){
        case 1:{
            document.getElementById("automanual").innerText = "Auto"
            break;
        }
        case 0:{
            document.getElementById("automanual").innerText = "Auto/Manual"
            break;
        }
        case 2:{
            document.getElementById("automanual").innerText = "Manual"
            break;
        }
    }
    console.log(i);

}
function LED_On()
{
    xhr.open("POST",url,true);
    xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhr.send(params_on);
}
function LED_Off()
{
    xhr.open("POST",url,true);
    xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhr.send(params_off);
}

function Auto()
{
    xhr.open("POST",url,true);
    xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhr.send(params_Auto);
}
function Manual()
{
    xhr.open("POST",url,true);
    xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhr.send(params_Manual);
}

function Time() {
    // Creating object of the Date class
    var date = new Date();
    // Get current hour
    var hour = date.getHours();
    // Get current minute
    var minute = date.getMinutes();
    // Get current second
    var second = date.getSeconds();
    // Variable to store AM / PM
    var period = "";
    // Assigning AM / PM according to the current hour
    if (hour >= 12) {
    period = "PM";
    } else {
    period = "AM";
    }
    // Converting the hour in 12-hour format
    if (hour == 0) {
    hour = 12;
    } else {
    if (hour > 12) {
    hour = hour - 12;
    }
    }
    // Updating hour, minute, and second
    // if they are less than 10
    hour = update(hour);
    minute = update(minute);
    second = update(second);
    // Adding time elements to the div
    document.getElementById("digital-clock").innerText = hour + " : " + minute + " : " + second + " " + period;
    // Set Timer to 1 sec (1000 ms)
    setTimeout(Time, 1000);
   }
    // Function to update time elements if they are less than 10
    // Append 0 before time elements if they are less than 10
   function update(t) {
    if (t < 10) {
    return "0" + t;
    }
    else {
    return t;
    }
   }
   Time();