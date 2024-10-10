const miSelect = document.getElementById('id_direccion')
const agregar_venta = document.getElementById("agregar_venta")
const personalizada = document.getElementById("id_direccion_personalizada")
const label = document.querySelector('label[for="id_direccion_personalizada"]')
console.log(miSelect.value)
miSelect.addEventListener('change', (e)=>{
    if(e.target.value == "Otros"){
        personalizada.style.display = "block"
        label.style.display = "block"
    }else{
        const direccion = document.getElementById("direccion")
        const label_direccion = document.getElementById("label_direccion")
        direccion.remove()
        label_direccion.remove()
    }
})

agregar_venta.addEventListener("click" , ()=>{
    if(direccion){
        const direccion = document.getElementById("direccion")
        miSelect.value = direccion.value
    }
})



