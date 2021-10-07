class Solution {
public:
    int repeatedNTimes(vector<int>& A) {
        int res = 0;
        for (int i=0;i<A.size();i++){
            if (exist(A, A[i])){
                res = A[i];
                break;
            }
        }
        return res;
    }
    int exist(vector<int>& A, int n){
        int res=0;
        for (int i=0;i<A.size();i++){
            if (A[i] == n) res++;
        }
        if (res>1) return 1;
        else return 0;
    }
};