var langJson;
var state = document.getElementById("navbarParam").getAttribute("state");

$.ajax({
  url: "/api/language",
  async: false,
  dataType: 'json',
  success: function (response) {
    // do stuff with response.
    langJson = response["languages"];
  }
});

var menuHTML = genLangMenu();

document.getElementById("langMenu").innerHTML = menuHTML;

function genLangMenu(){
	var len = langJson.length;
	var i = 0;
	var retHTML = "";
	var linkPrefix = "";
	if(state == 0)
		linkPrefix += "language/";

	for(i = 0; i<len; i++){
		var dict = langJson[i];
		var langName = dict["language_name"];
		var langAddr;
		if(langName == "C/C++")
			langAddr = "c&c++";
		else
			langAddr = langName.toLowerCase();
		retHTML += "<li><a href="+linkPrefix+langAddr+">"+langName+"</a></li>"
	}
	return retHTML;
}