
MAX_SLIDE=3
jQuery(document).ready(
	function(){
        $('#screen').mousemove(function(e){
	    $('#status').html( e.pageX +', '+ e.pageY);
    })
    MAX_SLIDE=14
	
	init_slides();	
    arrange_slides();
    stListener();
    goTo(1)

});

function init_slides(){
	current_slide=1;
	var count=1
	for (count; count<15; count+=1){
		if(count==1)
			$('#otherSlides').append('<div id="n_'+count+ '"  class="currentSlide"> <img src="slides/t'+count+ '.png"> </div>')
		else	
			$('#otherSlides').append('<div id="n_'+count+ '"  class="slide"> <img src="slides/t'+count+ '.png"> </div>')
	}
	
	/**for (var count=1; count<12; count+=1){
		$('#otherSlides').append('<div id="n_'+count+ ' "  class="slide"> <img src="slides/s'+count+ '.png"> </div>')	
	}
	for (var count=1; count<6; count+=1){
		$('#otherSlides').append('<div id="n_'+count+ ' "  class="slide"> <img src="slides/f'+count+ '.png"> </div>')	
	}**/
}		
		
function arrange_slides() {
	console.log('arrangeslides')
	$('.slide').each(function(index) {
	    $(this).css('top',196+10+index*166 + 'px');
	    //console.log('arrangeslides_' + index)
	})
} 
		
function goTo(n_slide){
	$('#otherSlides').append($('.currentSlide'))	
	$('.currentSlide').switchClass('currentSlide','slide',0)
/* 			$('#contentbar').empty() */
			
	//slide should be on and curentSlide off now
	arrange_slides();
	$('#n_'+n_slide).switchClass('slide','currentSlide',0); 	
	$('.currentSlide').hide();
		
	$('#contentbar').append($('.currentSlide')); 	
	$('.currentSlide').show('clip',1000);
	current_slide = n_slide; 
}

function stListener(){			
    source = new EventSource('../../getAction')
    source.onmessage = function (event) {
	    //setTimeout(this.send, 825); 
	    if(event.data=='next'){
		    next();
	        console.log(event.data);
 		} else if(event.data=='prev') {
 			prev();
 			console.log(event.data);
 		} else if(event.data=='play') {
     			playVideo();
     			console.log(event.data);
     	}
 		
 		console.log(current_slide); 

	};
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