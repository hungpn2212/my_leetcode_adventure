class Solution {
public:
    int maxCoins(vector<int>& piles) {
        int n = piles.size();
        sort(piles.begin(), piles.begin()+n);
        int check=0;
        for (int i=n/3;i<n;i+=2){
            check+=piles.at(i);
        }
        return check;
    }
};