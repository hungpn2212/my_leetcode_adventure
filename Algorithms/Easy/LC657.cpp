class Solution {
public:
    bool judgeCircle(string moves) {
        int up = 0, down = 0, left = 0, right = 0;
        for (int i=0;i<moves.size();i++){
            if (moves[i]=='L') left++;
            if (moves[i]=='R') right++;
            if (moves[i]=='U') up++;
            if (moves[i]=='D') down++;
        }
        if ((up==down) && (left==right)) return 1;
        else return 0;
    }
};