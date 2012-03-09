

	
function arrange_slides() {
	//console.log('arrangeslides')
	$('.slide').each(function(index) {
	    $(this).css('top',196+10+index*166 + 'px');
	    //console.log('arrangeslides_' + index)
	})
} 
		
function goTo(n_slide){
	if(n_slide>MAX_SLIDE)
		return;
	$('#otherSlides').append($('.currentSlide'))	
	$('.currentSlide').switchClass('currentSlide','slide',0)
/* 			$('#contentbar').empty() */
			
	//slide should be on and curentSlide off now
	arrange_slides();
	current_slide = n_slide;
	$('#n_'+n_slide).switchClass('slide','currentSlide',0); 	
	$('.currentSlide').hide();
		
	$('#contentbar').append($('.currentSlide')); 	
	$('.currentSlide').show('clip',1000);
	 
}


		
function next() {
	if(current_slide==MAX_SLIDE)
		return
	else
		goTo(current_slide+1)
} 
		
function prev() {
	if(current_slide==1)
		return
	else
		goTo(current_slide-1)
}