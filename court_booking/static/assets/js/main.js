/*
	Solid State by HTML5 UP
	html5up.net | @ajlkn
	Free for personal and commercial use under the CCA 3.0 license (html5up.net/license)
*/


$(document).ready(function () {


			$("#men").on("click", function(){
				$("body").toggleClass("is-menu-visible");
				
			  });
		  

				  $("body").on("click", function(event){
					if ($(event.target).closest("#men").length === 0) {
					  $("body").removeClass("is-menu-visible");
					}
				  });
			  
});