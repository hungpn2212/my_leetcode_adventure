class Solution {
public:
    int numTeams(vector<int>& rating) {
        int res=0;
        int n = rating.size();
        for (int i=0;i<n-2;i++){
            for (int j=i+1;j<n-1;j++){
                for(int k=j+1;k<n;k++){
                    if(((rating.at(i)<rating.at(j) && rating.at(j) < rating.at(k)))
                      || (rating.at(i)>rating.at(j) && rating.at(j) > rating.at(k)))
                        res++;
                }
            }
        }
        return res;
    }
};