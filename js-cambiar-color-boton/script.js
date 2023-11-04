function enviarFormulario() {
  let formulario = document.getElementById("miFormulario");
  alert("¡Enviaste el formulario!");
  formulario.reset(); // Esto reinicia el formulario después de mostrar el mensaje
}

// function saludarYVerificarEdad() {
//   const nombre = document.getElementById("nombre").value;
//   const edad = parseInt(document.getElementById("edad").value);
//   const boton = document.querySelector(".boton");

//   if (nombre && !isNaN(edad)) {
//       if (edad >= 18) {
//           alert(`Hola, ${nombre}! Eres mayor de edad.`);
//           boton.style.backgroundColor = "blue";
//       } else {
//           alert(`Hola, ${nombre}! Eres menor de edad.`);
//           boton.style.backgroundColor = "yellow";
//       }
//   } else {
//       alert("Por favor, ingresa un nombre válido y una edad numérica.");
//   }
// }

