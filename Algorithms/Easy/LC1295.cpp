class Solution {
public:
    int findNumbers(vector<int>& nums) {
        int res=0;
        for (int i=0; i<nums.size();i++){
            if (evenNumbers(nums[i])) res++;
        }
        return res;
    }
    bool evenNumbers(int n){
        int check=0;
        while (n>0){
            check++;
            n/=10;
        }
        if (check%2==0) return 1;
        else return 0;
    }
};