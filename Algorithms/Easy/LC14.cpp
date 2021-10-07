class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string tmp = "";
        if (!strs.size()){
            return tmp; 
        }
        sort(strs.begin(), strs.end());

            for(int j = 0; j < (strs.front()).size(); j++){
                if(((strs.front())[j] == (strs.back())[j])){
                 tmp = tmp + (strs.front())[j];
               }
                else{
                    break;
                }
            }
        
        return tmp; 
    
    }
};