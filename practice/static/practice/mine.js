myfunction();
function myfunction(){
	document.write('Hello World!');
	data = [{'foo':'bar','baz':'jazz'}];
	$.post( "/post", {
    	javascript_data: data
	});
};