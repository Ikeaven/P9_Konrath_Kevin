function main(){
    rates = document.getElementsByClassName("rating");

    for(rate of rates){
        var number = rate.innerHTML
        var out = ""
        var count = 0
        for(let i = 0; i < number; i++){
            out += '<i class="bi bi-star-fill text-warning"></i>'
            count += 1
        }
        for (count; count <5; count++ ){
            out += '<i class="bi bi-star text-warning"></i>'
        }
        rate.innerHTML = out
        rate.hidden = false

    }
}



window.addEventListener('load', ()=>{
    main()
})