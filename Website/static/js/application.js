
$(document).ready(function(){
    //connect to the socket server.
    var socket = io.connect('http://' + document.domain + ':' + location.port + '/test');
    var connection = "True"; 
    var state = "Not connected";
    var gesture= "";

    //receive details from server

    socket.on('newnumber', function(msg) {
        console.log("Received number" + msg.number);
        
        $('#gesture').html("hallo");
    });

});