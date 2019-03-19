myfunction();
function myfunction(){
	document.write('Hello World!');
	data = [{'foo':'bar','baz':'jazz'}];
	$.ajax({
	    type: "POST",
	    url:"/post/",
	    data: {
	    'test': 'success',
	    },
	    success: function(){
	      alert('test')
	     },
	    error: function(){
	        alert("Error");
	});
};