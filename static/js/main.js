const imgBox = document.getElementById('img-box')
const image = document.getElementById('id_image')
const btnBox = document.getElementById('btn-box')

const btns = [...btnBox.children]

const url = ""



image.addEventListener('change' ()=>{
    const img_data = image.files[0]
    const url = URL.createObjectURL(img_data)
    console.log(url)
    imgBox.innerHTML = <img src="${url}" width="80%">
    btnBox.classList.remove('not-visible')
})

let filter = null
btns.forEach(btn => btn.addEventListner('click', ()=>{
    filter = btn.getAttribute('data-filter')
}))


