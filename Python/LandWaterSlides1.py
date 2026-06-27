#3633. Earliest Finish Time for Land and Water Rides I

int earliestFinishTime(int* landStartTime, int landStartTimeSize, int* landDuration, int landDurationSize, int* waterStartTime, int waterStartTimeSize, int* waterDuration, int waterDurationSize) {
    int minTime=INT_MAX;
    for(int i=0;i<landDurationSize;i++){
        for(int j=0;j<waterDurationSize;j++){
            //case1
            int land_finish=landStartTime[i]+landDuration[i];
            int water_start = fmax(land_finish, waterStartTime[j]);
            int water_finish = water_start + waterDuration[j];

            //case2
            int w_finish=waterStartTime[j]+waterDuration[j];
            int l_start = fmax(w_finish, landStartTime[i]);
            int l_finish = l_start + landDuration[i];

            //result
            minTime=fmin(minTime,fmin(water_finish, l_finish));
        }
    }
    return minTime;
}
