$.getJSON("/api/rank", function(result){
	var data = result["rank"];
	var len = data.length;

    //display rank
    var rank_holder = "rank_";
    var link_holder = "link_";

    for(var i = 0; i<len; i++){
    	var dict = data[i];
		// var id = dict["language_ID"];
		var rankId = dict['rank_ID'];
		var name = dict['language_name'];
		var link = dict['link'];
		
		//display rank
		if(link == "#"){
			document.getElementById(rank_holder + rankId).innerHTML = name;
		}
		else{
			document.getElementById(rank_holder + rankId).innerHTML = "<a href=" + link + " >" + name + "</a>";
		}

	}
});

$.getJSON("/api/language", function(result){
	var data = result["languages"];
	var dataLen = data.length;
	for(var i = 0; i < dataLen; ++i){
		var dict = data[i];
		var name = dict['language_name'];
		var imgSrc = dict['language_image_small'];

		switch(name){
			case "C/C++":
				name = "c&c++";
				break;
			case "Java":
				name = "java";
				break;
			case "PHP":
				name = "php";
				break;
			case "Python":
				name = "python";
				break;
			case "Javascript":
				name = "javascript";
				break;
			default:
				break;
		}
		var htmlCode = "<div class = \"image\">";
		htmlCode += "<div class=\"col-md-2\" >";
		htmlCode += "<a href=language/" + name + ">";
		htmlCode += "<img src=\"static/" + imgSrc + "\" class=\"img-rounded\" style=\"margin: 30px\">";
		htmlCode += "</a></div></div>";

		var icon_holder = "image_" + name;
		document.getElementById("image_" + name).innerHTML = htmlCode;
	}
});

