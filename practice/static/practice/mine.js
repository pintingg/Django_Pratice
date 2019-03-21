myfunction();
function myfunction(){
	console.log("I am in the function now!");
	var csrftoken = Cookies.get("csrftoken");
	function csrfSafeMethod(method) {
	    // these HTTP methods do not require CSRF protection
	    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
	}
	$.ajaxSetup({
	    beforeSend: function(xhr, settings) {
	        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
	            xhr.setRequestHeader("X-CSRFToken", csrftoken);
	        }
	    }
	});
	$.ajax({
	    type: 'POST',
	    url: "/post",
	    data: {
	        "a": "0",
	        "b": "2"
	    },
	    success: function(response){
	    	console.log("Received");
	    	console.log(response.data);
	    },
	    dataType: 'json'
	});
	/*$.ajaxSetup({
    	data: {csrfmiddlewaretoken: csrftoken},
	}); 
	$.post({
	    url : "/post",
	    data : {a : "test"},
	    success : function(response){
	    	console.log("Received");
	    	console.log(response.data);
	    },
	    dataType : "json"
	});*/
};