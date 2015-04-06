$.getJSON("/api/rank", function(result){
	var data = result["rank"];
	var len = data.length;

    //display rank
    var rank_holder = "rank_";
    var link_holder = "link_";

    for(var i = 0; i<len; i++){
    	var dict = data[i];
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

    //build table
});

$.getJSON("/api/language", function(result){
	var data = result["languages"];
	//display icons
	var dataLen = data.length;
	var htmlCode = "<div class=\"col-md-12 col-md-offset-1\">";

	for(var i = 0; i < dataLen; ++i){
		var dict = data[i];
		var name = dict['language_name'];
		var imgSrc = dict['language_image_small'];
		if(name == "C++" || name == "C"){
			name = "c&c++";
		}
		else if(name == "C#"){
			name = "csharp"
		}
		else{
			name = name.toLowerCase();
			name = name.replace(" ", "");
		}

		htmlCode += "<div class = \"image\">";
		htmlCode += "<div class=\"col-md-2\" >";
		htmlCode += "<a href=language/" + name + ">";
		htmlCode += "<img width=\"150\" src=\"static/" + imgSrc + "\" class=\"img-rounded\" style=\"margin: 30px\">";
		htmlCode += "</a></div></div>";
		if(i == 4){
			htmlCode += "</div><div class=\"col-md-12 col-md-offset-1\">";
		}

		// var icon_holder = "image_" + name;
		// document.getElementById("image_" + name).innerHTML = htmlCode;
	}
	htmlCode += "</div>";

	document.getElementById("lang_image_icon").innerHTML = htmlCode;
});

