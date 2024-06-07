window.addEventListener('load' , () => {
    fetch('http://127.0.0.1:5500/api/hotel')
        .then(res => console.log(res))
})