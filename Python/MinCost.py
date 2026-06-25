#2144. Minimum Cost of Buying Candies With Discount
int minimumCost(int* cost, int costSize) {
    int total=0;
    int max=0, maxArray[costSize];
    for (int i = 0; i < costSize - 1; i++) {
        for (int j = 0; j < costSize - i - 1; j++) {
            if (cost[j] < cost[j + 1]) {
                int temp = cost[j];
                cost[j] = cost[j + 1];
                cost[j + 1] = temp;
            }
        }
    }

    for(int i=0; i<costSize; i+=3){
        total+=cost[i];

        if(i+1<costSize){
            total+=cost[i+1];
        }
    }

    return total;
}
