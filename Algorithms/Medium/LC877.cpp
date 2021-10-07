class Solution {
public:
    bool stoneGame(vector<int>& piles) {
        int n = piles.size();
        sort(piles.begin(), piles.begin()+n);
        int sum = 0;
        int maxScore=0;
        for (int i=0;i<n;i++){
            sum += piles.at(i);
            if (i%2==1)
                maxScore+=piles.at(i);
        }
        if (maxScore>sum-maxScore) return true;
        else return false;
    }
};