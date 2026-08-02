#3945. Digit Frequency Score
int digitFrequencyScore(int n) {
    int result=0;
    if(n<0){
        n=-n;
    }

    while(n>0){
        result+=n%10;
        n/=10;
    }

    return result;
}
