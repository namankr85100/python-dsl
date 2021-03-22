function reverse(array){
    var output = [];
    for(var i =0;i<=array.length;i++){
        output.push(array.pop());

    }
    return output;
}
console.log(reverse([1,2,3,4,5,6,7]))


