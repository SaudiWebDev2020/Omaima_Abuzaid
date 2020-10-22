var arr=[8,6,7,5,3,0,9]
for (var i=0; i<arr.length; i++){
    console.log(arr[i]);
}// ouput 8 6 7 5 3 0 9

var arr=[7,3,8,4,2,0,1];
for(var i=0; i<arr.length; i++){
    if(arr[i]%2==0){
        console.log(arr[i]);
    }
    else{ console.log('that is odd!!');}
}// that is odd!!
// that is odd!!
//8
//4
//2
//0
//that is odd!!

var arr=[1,3,8,-5,0,-2,4,-1];
var newarr=[];
for(var i=0; i<arr.length; i++){
    if (arr[i]<0){
        newarr.push(arr[i]);
        arr[i]=arr[i]*-1;
    }
    else if (arr[i]==0){
        arr[i]='zero';}
    else { arr[i]=arr[i]*-1;
    }
}
console.log(arr);
console.log(newarr);
/// [-1, -3, -8, 5, "zero", 2, -4, 1]
///[-5, -2, -1]
