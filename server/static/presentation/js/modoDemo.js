
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

function pullNewSlides(){

total_slides

}		
		
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
 		} else if(event.data=='prev') {
 			prev();
 		} 		

	};
	
	source.addEventListener("change", function( e ) {
		//console.log(e.data);
		console.log(JSON.parse(e.data) );
		rcvFolder=JSON.parse(e.data)
		//TODO load images as DIVS
		path=rcvFolder.path;
		numberslides=rcvFolder.slides;
		$('#otherSlides').empty();		
		for (var j=2; j<=numberslides; j+=1 ){
			$('#otherSlides').append('<div class ="slide" id="n_'+ j +'"> <img src="'+path+'/s'+ j +'.png">  </div>' )
		}
		
		$('#otherSlides').append('<div id="n_1"  class="currentSlide"> <img src="'+path+'/s1.png>  </div>' )
		 //PUT IMAGE N1
   		 arrange_slides();
   		 goTo(1);		 
		 //MAKE NEXT AND PREV WORK
	
		}, false);
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


