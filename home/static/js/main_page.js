$("index.html").ready(function () {
    setInterval(function() {
        var date = new Date();

        var year = date.getFullYear();
        var day = date.getDate();
        var month = date.getMonth();
        
        var hours = date.getHours();
        var min = date.getMinutes();
        var sec = date.getSeconds();
        
        document.getElementById("time").innerHTML= hours+":"+min+":"+sec;
        document.getElementById("date").innerHTML= year+"/"+ month+"/"+day;
      }, 1000);

    $("#light").on("click",function(){
        $("#site").removeClass("bg-dark");
        $("#site").addClass("bg-info");    
    });

    $("#dark").on("click",function(){
        $("#site").removeClass("bg-info");
        $("#site").addClass("bg-dark");    
    });
});