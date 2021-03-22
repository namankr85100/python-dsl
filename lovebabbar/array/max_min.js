function findMax(array){
    var max = 0;
    var a = array.length;
    for(counter =0 ;counter<a;counter++){
        if(array[counter]>max){
            max = array[counter];
        }
    }
    return max;
}

function findmin(array){
    var min = array[0];
    var a  = array.length;
    for(counter=0;counter<a;counter++){
        if (array[counter]<min){
            min= array[counter];

        }

    }
    return min;
}


console.log(findmin([1,2,3,4,56,12,0]))
console.log(findMax([2,44,12,423,1]))