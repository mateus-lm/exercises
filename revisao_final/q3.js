const forma = function(arg1, arg2, forma){
    if (forma == "retangulo"){
        return "o retangulo tem " + arg1 * arg2 + " de area"
    } else if (forma == "losango"){
        return "o losango tem " + (arg1 * arg2)/2 + " de area"
    } else if (forma == "triangulo"){
        return `o triângullo tem ${(arg1 * arg2)/2} de area`
    }
}

console.log(forma(5,3,"triangulo"))