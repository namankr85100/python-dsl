function nthlargest(arr,highest){
    var x=0,y=0,z=0,temp=0,size=arr.length,flag=false,result=false;

    while(x<size){
        y=x+1;

        if(y<size){
            for(z=y;z<size;z++){
                if(arr[x]<arr[z]){
                    temp = arr[x];
                    arr[x]=arr[z];
                arr[z]=temp;                }
            else{
continue;
            }
        }



    }

    if(flag){
        flag = false;

    }else{
        x++;
        if(x===highest){
            result = true;
        } 
    }
    if(result){
        break;
    }

    return (arr[(highest-1)]);


}

console.log(nthlargest([43,56,89,90,99,652],4));