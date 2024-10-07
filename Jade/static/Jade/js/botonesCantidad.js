const btnDecrementar = document.querySelectorAll('.decrementar');
const btnIncrementar = document.querySelectorAll('.incrementar');
const inputCantidad = document.querySelectorAll('.cantidad');
console.log(inputCantidad)
let cantidad = 0

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

btnIncrementar.forEach(element => {
    element.addEventListener('click', () => {
        cantidad++;
        console.log(element.previousElementSibling.value)
        element.previousElementSibling.value++
        if (cantidad > 1) {
            element.disabled = false;
        }
    });
    
});




// Deshabilitar el botón de decremento si la cantidad inicial es 1
// if (cantidad === 1) {
//     btnDecrementar.disabled = true;
// }
