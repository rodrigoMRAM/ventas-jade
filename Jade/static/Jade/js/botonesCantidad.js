const btnDecrementar = document.querySelectorAll('.decrementar');
const btnIncrementar = document.querySelectorAll('.incrementar');
const inputCantidad = document.querySelectorAll('.cantidad');



const pastafrolaCantidad = document.querySelector("#Pastafrola");
const chipaCantidad = document.querySelector("#Chipa");
const alfajorMaicena = document.querySelector("#Maicena");
const scon = document.querySelector("#Scon");
const lista = document.querySelector(".lista")
const boton = document.getElementById("boton")
const divsProductos = document.querySelectorAll('div.productos');




let cantidad = 0
var valorFinal = 0
var textFinal = ""

// chipaCantidad.addEventListener('change', (e)=>{
//     descripcion.value += `Chipa X${e.target.value} \n` 
//     })







btnDecrementar.forEach(element => {
    element.addEventListener('click', () => {
        if (element.nextElementSibling.value > 0) {
            // inputCantidad.value = cantidad;
            element.nextElementSibling.value--
            console.log(element.nextElementSibling.value)
            
        }
        if (element.nextElementSibling.value === 0) {
            element.disabled = true;
        }
    });    
});

let total = document.getElementById("id_total")
let descripcion = document.getElementById("id_descripcion");
btnIncrementar.forEach(element => {
    element.addEventListener('click', () => {
        total.value = 0
        descripcion.value = ""
        textFinal = "";
        valorFinal = 0;        
        cantidad++;
        console.log(element.previousElementSibling.value)
        element.previousElementSibling.value++
        if (cantidad > 1) {
            element.disabled = false;
        }
        incrementarProducto()
        
        
    });
    
    
});




// Deshabilitar el botón de decremento si la cantidad inicial es 1
// if (cantidad === 1) {
//     btnDecrementar.disabled = true;
// }

function incrementarProducto(){
    
  
    divsProductos.forEach(div => {
        const inputs = div.querySelectorAll('input');
        console.log(descripcion.value)
        inputs.forEach(input => {
            if(input.value> 0){
                textFinal = `${textFinal}${input.id} X ${input.value}\n`;
                totalFinal = parseInt(input.value) * parseInt(input.getAttribute("valor")) 
                valorFinal += totalFinal
            }
            console.log(input)
            console.log(input.value);  // Aquí accedes al valor de cada input
        });
    });
    console.log(valorFinal)
    
    console.log(totalFinal)
    // console.log(typeof(textoFinal) )
    descripcion.value = textFinal  
    // totalDefinitivo =  total1 + total2
    total.value = valorFinal

}