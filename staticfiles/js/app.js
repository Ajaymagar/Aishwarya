console.log('Its working')

let theme = localStorage.getItem('theme')

if(theme == null){
	setTheme('blue')
}else{
	setTheme(theme)
}

let themeDots = document.getElementsByClassName('theme-dot')


for (var i=0; themeDots.length > i; i++){
	themeDots[i].addEventListener('click', function(){
		let mode = this.dataset.mode
		console.log('Option clicked:', mode)
		setTheme(mode)
	})
}

function setTheme(mode){
	if(mode == 'light'){
		document.getElementById('theme-style').href = 'static/css/style.css'
	}

	if(mode == 'blue'){
		document.getElementById('theme-style').href = 'static/css/blue.css'  
	}

	if(mode == 'green'){
		document.getElementById('theme-style').href = 'static/css/green.css'
	}

	if(mode == 'purple'){
		document.getElementById('theme-style').href = 'static/css/purple.css'
	}

	localStorage.setItem('theme', mode)
}


!(function($){
	"use strict";


	$(window).on('load', function() {
		if ($('#preloader').length) {
		  $('#preloader').delay(100).fadeOut('slow', function() {
			$(this).remove();
		  });
		}
	  });
	



	$(window).scroll(function() {
		if ($(this).scrollTop() > 100) {
		  $('.back-to-top').fadeIn('slow');
		} else {
		  $('.back-to-top').fadeOut('slow');
		}
	  });
	
	  $('.back-to-top').click(function() {
		$('html, body').animate({
		  scrollTop: 0
		}, 1500, 'easeInOutExpo');
		return false;
	  });



})(jQuery);

