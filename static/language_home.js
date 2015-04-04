$.getJSON("/api/rank", function(result){
	var data = result["rank"];
	// data = JSON.stringify(data);
    // $.each(result, function(key, value){
        // document.write(key+": "+value+"<br />"); 
    //     document.getElementById("placeholder").innerHTML=data.language_ID+" "+data.language_name+" "+data.language_description;
    // });
	document.getElementById("language_0").innerHTML=JSON.stringify(data);
	// document.getElementById("placeholder").innerHTML=JSON.stringify(data);
	var len = data.length;
	// document.getElementById("placeholder").innerHTML=JSON.stringify(first);
	// var dataLen = data.length;
    // $.each(data, function(key, value){
    // var holder = "language_";

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

		//display language icons

		// var description = dict['language_description']
		// if(name == "C/C++"){
		// 	document.getElementById(holder+"C").innerHTML="C";
		// 	document.getElementById(holder+"C++").innerHTML="C++";
		// }
		// else{
		// 	document.getElementById(holder+name).innerHTML=name;
		// }
		// document.getElementById(rank_holder+rank_ID).innerHTML =
    	// document.getElementById(holder+i).innerHTML=JSON.stringify(dict);
	    // document.getElementById(holder+name).innerHTML=id + " " +name+ " " + description;
 
		// var id = dict["language_ID"];
		// var name = dict['language_name'];
		// var description = dict['language_description']
	 //    document.getElementById("placeholder").innerHTML=id + " " +name+ " " + description;
    }

    //build table
});

$.getJSON("/api/language", function(result){
	var data = result["languages"];
	document.getElementById("language_1").innerHTML=JSON.stringify(data);
	//display icons
	var dataLen = data.length;
	for(var i = 0; i < dataLen; ++i){
		var dict = data[i];
		var name = dict['language_name'];
		var imgSrc = dict['language_image_small'];
		// alert(imgSrc);

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
		// alert(htmlCode);
		var icon_holder = "image_" + name;
		// alert(icon_holder);
		document.getElementById("image_" + name).innerHTML = htmlCode;
	}
});

