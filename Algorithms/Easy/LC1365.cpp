class Solution {
public:
    int numberOfSmaller(vector<int>& nums, int val){
        int res = 0;
        for (int i=0;i<nums.size();i++){
            if (nums[i] < val) res++;
        }
        return res;
    }
    vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
        vector<int> res;
        for (int i=0; i<nums.size();i++){
            res.push_back(numberOfSmaller(nums, nums[i]));
        }
        return res;
    }
};