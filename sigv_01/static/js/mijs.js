$(document).ready(function(){

	var log = EstadoLoguin();
	var logueado = "false";
	if (log != 3)
	{
		logueado = "true";
	}

	$('#loguin').hide();

	$('#open_close').click(function(){
		$('#loguin').slideToggle();
		if (logueado == "true"){
				$('.control-labe').text("Salir del sistema");
				$('#migrupo').hide();
				$('#btnEntrare').hide();	

				$('#btnCerrar').show();
		}else{
				//$('#usu').show();
				//$('#pas').show();
				//$('#che').show();
				
				$('#btnEntrare').show();
				$('#btnCerrar').hide();
		}
	})

})

$(document).ready(function(){

	
	var altura = $('#minavb').offset().top;
	
	$(window).on('scroll', function(){
		if ($(window).scrollTop() > altura){
			$('#libtn').hide();
			$('#minavb').addClass('menu-fixed');
			
		}else{
			$('#libtn').show();
			$('#minavb').removeClass('menu-fixed');
		}
	});
});

$(document).ready(function(){
 	var log = EstadoLoguin();
	if (log != 3)
	{
 		$('.ir-arriba').hide();
		$('.social').hide();
		$('#footer').hide();
		

 		
	}else{
		$('.ir-arriba').click(function(){
			$('body, html').animate({
				scrollTop: '0px'
			}, 300);
		});
	 
		$(window).scroll(function(){
			if( $(this).scrollTop() > 0 ){
				$('.ir-arriba').slideDown(300);
			} else {
				$('.ir-arriba').slideUp(300);
			}
		});
	}
 
});

$(document).ready(function(){
	var f = new Date();
    $('#lblhora').text(f.getFullYear() + "-" + (f.getMonth() +1) + "-" + f.getDate());
});

$(document).ready(function(){
    //$('#lblhora').text(f.getFullYear() + "-" + (f.getMonth() +1) + "-" + f.getDate());
    $("#btnGenerarNotificacion").click(function(){
    	//tabla = document.getElementById('#mitabla')[0];
    	
    	$('.form-control').value = "jaja";
    	alert("yeah: ");

    });
});



