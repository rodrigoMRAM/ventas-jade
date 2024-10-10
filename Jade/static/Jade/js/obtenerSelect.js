const miSelect = document.getElementById('id_direccion')
const agregar_venta = document.getElementById("agregar_venta")
const personalizada = document.getElementById("id_direccion_personalizada")
const label = document.querySelector('label[for="id_direccion_personalizada"]')
console.log(miSelect.value)
label.classList.add('oculto')
miSelect.addEventListener('change', (e)=>{
    if(e.target.value == "Otros"){
        personalizada.classList.toggle('oculto')
        label.classList.toggle('oculto')
      
    }else{
        personalizada.classList.add('oculto')
        label.classList.add('oculto')
    }
})

agregar_venta.addEventListener("click" , ()=>{
    if(direccion){
        const direccion = document.getElementById("direccion")
        miSelect.value = direccion.value
    }
})



