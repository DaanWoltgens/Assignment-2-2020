function function1(p1, p2, p3) {
    return p1 * p2;
}

function function1copy(a, b) {
    return a*b;
}

function function2(p1, p2) {
    p3 = p1 + p1;
    while(p1 > 0){
        p3 += 1;
        p2 += p1;
        p1--;
    }
    return p2;
}

function function2copy(c,d) {
   while(c > 0){
c += d;
 c--;
    }
        return d;
}

function function3(p1,p2,p3,p4, p7) {
    p5 = p1 + p2;
    p6 = p3 + p4;
    while(p5 > p6){
        p1 += p2;
        p7 += 3;
        p3 = p1 + p4;
        p5 -= p1;
    }
    return p3;
 }

function function3copy(x,y,z,a) {
//This is a fuction
p5 = x + y;
p6 = z + a;
g = 1;
//I have no clue what this loop does
while(p5 > p6){
    x += y;
    g += 1;
    z = x + a;
    p5 -= x;
}
return z;
}

function function4(a,b,c){
    c *= 2;
    if(a<0 || b<0 ){
        return 0;
    }
    return a^2 + b^2
}

function function4copy(x1,y1){
    d = x1 + x2;
    //This checks for negative values
if(x1<0 || y1<0){
  return 0;
}
    //This returns the length of the hypotenuse of a triangle
    return x1^2 + y1^2
}