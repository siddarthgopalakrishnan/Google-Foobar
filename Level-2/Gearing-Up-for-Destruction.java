public static int[] Solution(int[] pegs) {
    int a = pegs[0];
    int sign = -1;
    for(int i: pegs) {
        a += 2*i*sign;
        sign *= -1;
    }

    a += pegs[pegs.length-1]*sign;
    a *= 2;
    int b=0;
    if(pegs.length%2 == 0) b = 3;
    else b = 1;

    if(a%b==0) {
        a /= b;
        b = 1;
    }

    float prev = ((float)a) / ((float)b);
    for(int i = 0; i < pegs.length - 2; i++) {
        int width = pegs[i+1] - pegs[i];
        if(prev < 0 || prev > (width-1))
            return new int[] {-1, -1};
        prev = width - prev;
    }

    return new int[] {a, b};
}