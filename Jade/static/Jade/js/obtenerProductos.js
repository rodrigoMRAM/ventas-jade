const pastafrolaCantidad = document.querySelector("#Pastafrola");
const chipaCantidad = document.querySelector("#Chipa");
const alfajorMaicena = document.querySelector("#Maicena");
const scon = document.querySelector("#Scon");
const descripcion = document.getElementById("id_descripcion");
const total = document.getElementById("id_total")
const lista = document.querySelector(".lista")
const boton = document.getElementById("boton")
const divsProductos = document.querySelectorAll('div.productos');



var valorFinal = 0
var textFinal = ""
boton.addEventListener('click', ()=>{
    // if(chipaCantidad.value> 0){
        //     var textoFinal =  `Chipa X ${chipaCantidad.value}\n`;
        //     descripcion.value = `Chipa X ${chipaCantidad.value}\n`;
    //     var total1 = parseInt(chipaCantidad.value) * parseInt(chipaCantidad.getAttribute("valor"))
    // }else{
    //     var total1 = 0
    //     var textoFinal = " "
        
    // }
    // if(pastafrolaCantidad.value> 0){
    //     var textoFinal1 =  `Pastafrola X ${pastafrolaCantidad.value}\n`;
    //     descripcion.value = `Pastafrola X ${pastafrolaCantidad.value}\n`
    //     var total2 = parseInt(pastafrolaCantidad.value) * parseInt(pastafrolaCantidad.getAttribute("valor"))
    // }else{
        //     var total2 = 0
    //     var textoFinal1 = " "
    
    // }
    divsProductos.forEach(div => {
        const inputs = div.querySelectorAll('input');
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
    // total.value = totalDefinitivo
    // console.log(totalDefinitivo)
    
})

// chipaCantidad.addEventListener('change', (e)=>{
//     descripcion.value += `Chipa X${e.target.value} \n` 
//     })


