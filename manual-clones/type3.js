function function3(p1,p2,p3,p4) {
    p5 = p1 + p2;
    p6 = p3 + p4;
    while(p5 > p6){
        p3 = p1 + p4;
        p5 -= p1;
    }
    return p3;
 }

function function3copy(p1,p2,p3,p4) {
//This is a fuction
p5 = p1 + p2;
p6 = p3 + p4;
//I have no clue what this loop does
while(p5 > p6){
    p1 += p2;
    p3 = p1 + p4;
    p5 -= p1;
}
return p3;
}

function function4(a,b){
    if(a<0 || b<0){
        print("An extra statement");
        return 0;
    }
    d = a *b;
    e = d*b;
    return a^2 + b^2
}

function function4copy(a,b){
    //This checks for negative values
if(a<0 || b<0){
    d = a+b
  return 0;
}
    //This returns the length of the hypotenuse of a triangle
    return a^2 + b^2
}