var icons = document.getElementsByClassName("icon");
var tabs = document.getElementsByClassName("tab");
var cards = document.getElementsByClassName("card")
var initialX = window.innerWidth;
var initialY = window.innerHeight;
var collapseWidth = 834;

function adaptToSize() {
   if (window.innerWidth <= collapseWidth) {
      bottom();
   } else {
      top();
   }
}

function bottom() {
	document.getElementById('menu').style.bottom = 0;
	document.getElementById('clear-header').style.visibility = "visible";
	document.getElementById('menu').style.backgroundPosition = "bottom center";
	var temp = document.getElementsByClassName("container");
	for (var i = temp.length - 1; i >= 0; i--) {
	  temp[i].style.display = "inline-flex";
	}
	for (var i = 0; i < tabs.length; i++) {
	    tabs[i].style.display = "none";
	    icons[i].style.display = "block";
	}
}

function top() {
	document.getElementById('menu').style.top = 0;
	document.getElementById('clear-header').style.visibility = "hidden";
	document.getElementById('menu').style.backgroundPosition = "top center";
	for (var i = 0; i < icons.length; i++) {
	    icons[i].style.display = "none"
	}
}

window.onresize = function(event) {
   var x = window.innerWidth
   if ((x <= collapseWidth && x < initialX)||(x > collapseWidth && x > initialX)) {
   	document.location.reload(false);
   }
   initialX = x;
};