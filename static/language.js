var langId = document.getElementById("param").getAttribute("langId");

var apiPath = "/api/language/" + langId;
// alert(apiPath);

$.getJSON(apiPath, function(result){
	// alert("yay");
	var data = result["language"];
	var imgSrc = data["language_image_small"];
	document.getElementById("langJson").innerHTML=JSON.stringify(data);
	document.getElementById("iconImg").innerHTML="<img src=../static/" + imgSrc + " alt=\"Responsive image\" class=\"img-rounded img-response-language\" style='padding-bottom:50px'>";
	
});