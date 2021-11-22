function filename(){
    var rutaAbsoluta = self.location.href;   
    var posicionUltimaBarra = rutaAbsoluta.lastIndexOf("/");
    var rutaRelativa = rutaAbsoluta.substring( posicionUltimaBarra + "/".length , rutaAbsoluta.length );
    return rutaRelativa;  
}

function MuestraVentana() {
    var mensaje = 'BienVenido a tu sitio de comida saludable'
    var nombreArchivo = filename()
    if(nombreArchivo == 'index.html'){
        alert(mensaje)
    }
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
$(document).ready(function(){
    $('#tablaUsuarios').DataTable();
});