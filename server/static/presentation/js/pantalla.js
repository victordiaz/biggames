
MAX_SLIDE=3
jQuery(document).ready(function(){
        $('#screen').mousemove(function(e){
	    $('#status').html( e.pageX +', '+ e.pageY);
    })
		
    arrange_slides();
    stListener();
    goTo(1)
    MAX_SLIDE=3
});
		
		
function arrange_slides() {
    //console.log('arrangeslide')
	$('.slide').each(function(index) {
	    $(this).css('top',196+10+index*166 + 'px');
	}
)} 
		
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
		goTo(current_slide+1)
}