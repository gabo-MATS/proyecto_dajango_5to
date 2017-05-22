var botoncambiarRisa = document.getElementById("cambiar");
botoncambiarRisa.onclick=function(){ 
var texto="waka waka: ";

for(var i = 0; i < 10; i++){
	texto+=i;
}
var risa=document.getElementById("ferrari");
risa.innerHTML = texto;
}
var nombre = document.getElementById("nombre")
var titulo = document.getElementById("titulo")
var btnSaludar = document.getElementById("saludar")

btnSaludar.onclick = function() {
	var txtNombre = nombre.value;
	titulo.innerHTML = "Hola " + txtNombre;
}


////////////////////////////////////
var inAutomatico = document.getElementById("automatico");
var txtAutomatico = document.getElementById("texto-automatico");

inAutomatico.onkeyup=function(){
	txtAutomatico.innerHTML = inAutomatico.value;
}

var btnIr = document.getElementById("ir");
var idpagina = document.getElementById("website");

btnIr.onclick = function() {
	window.location = idpagina.value;
}

/////////////////////////////

var square = document.getElementById("square");
var btnAnimar = document.getElementById("animar");

btnAnimar.onclick = function(){
	square.classList.add("open");
}