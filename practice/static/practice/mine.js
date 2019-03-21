myfunction();
function myfunction(){
	console.log("I am in the function now!");
	var csrftoken = Cookies.get("csrftoken");
	/*$.ajax({
	    type: 'POST',
	    url: "/post",
	    data: {
	        "partner_ref": "PH",
	        "return_field": ["summary", "details"]
	    },
	    success: function(data){

	    },
	    dataType: 'json'
	});*/
	$.ajaxSetup({
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
	});
};