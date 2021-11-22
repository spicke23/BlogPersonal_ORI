/*
let boton = document.getElementById('boton')

if(boton){
  boton.addEventListener('click', validarFormulario)
}

// Funcion que valida el ingreso de los datos en el formulario de contacto
function validarFormulario (e) {
    
    e.preventDefault()
    //Variables
      let nombre = document.getElementById("nombreUsuario").value
      let apellido = document.getElementById("apellidoUsuario").value
      let correo = document.getElementById("correoUsuario").value
      let clave1 = document.getElementById("clave1Usuario").value
      let clave2 = document.getElementById("clave2Usuario").value

      // Realizamos las validaciones de los Datos
     if (nombre)
       {
         alert('Completar los datos')
       }
       else
       {
        alert('Hemos recibido su mensaje, nuestro equipo se pondrá en contacto con usted.')
       }
    
    }
*/

function Valida(){
    
    //e.preventDefault()
    //Variables

    let nombre = document.getElementById("nombreUsuario").value
    let largoNombre = nombre.length
    let apellido = document.getElementById("apellidoUsuario").value
    let largoApellido = apellido.length
    let correo = document.getElementById("correoUsuario").value
    let largoCorreo = correo.length
    let clave1 = document.getElementById("clave1Usuario").value
    let largoClave1 = clave1.length
    let clave2 = document.getElementById("clave2Usuario").value
    let largoClave2 = clave2.length
    let mensaje1, mensaje2, mensaje3, mensaje4, mensaje5

    if((nombre == null) || (largoNombre < 1)){
        mensaje1 = 'Campo Nombre'
    }
    if((apellido == "") || (largoApellido < 1)){
        mensaje2 = 'Campo Apellido'
    }
    if((correo == "") || (largoCorreo < 1)){
        mensaje3 = 'Campo Correo'
    }
    if((clave1 == "") || (largoClave1 < 1)){
        mensaje4 = 'Campo Clave'
    }
    if((clave2 == "") || (largoClave2 < 1)){
        mensaje5 = 'Campo Repetir Clave'
    }
    mensaje = 'Falta Completar:'+'\n'+mensaje1+'\n'+mensaje2+'\n'+mensaje3+'\n'+mensaje4+'\n'+mensaje5
    alert(mensaje)

    // Validamos Claves
    if(clave1 != clave2){
        alert("Las claves no coinciden")
    }
}