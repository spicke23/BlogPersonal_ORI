function MuestraVentana() {
    var mensaje = 'BienVenido a tu sitio de comida saludable'
    alert(mensaje)
}

window.onload = MuestraVentana

function generarNuevoColor(){
	var simbolos, color;
	simbolos = "0123456789ABCDEF";
	color = "#";

	for(var i = 0; i < 6; i++){
		color = color + simbolos[Math.floor(Math.random() * 16)];
	}

    let division = document.getElementById('comidas')
	division.style.background = color;
}

/*** Esto es jQuery ***/
$(document).ready(function (){
    $('#button a').click(function(){
        var integer = $(this).attr('rel');
        $('#myslide .cover').animate({left:-705*(parseInt(integer)-1)})
        $('#button a').each(function(){
            $(this).removeClass('active');
            if($(this).hasClass('button'+integer)){
                $(this).addClass('active')}
        });
    });
});
