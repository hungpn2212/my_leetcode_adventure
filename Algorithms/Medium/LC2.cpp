/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode *createNode(int val) {
        return new ListNode(val);
    }
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode *result = NULL;
         if (!l1 || !l2)
             return result;
        
         bool carry = 0;
         ListNode *retVal = createNode(0);
         result = retVal;
         while (1) {
             int val1 = 0;
             int val2 = 0;

             if (l1)
                 val1 = l1->val;
             if (l2)
                 val2 = l2->val;

             int sum = val1 + val2 + carry;
             carry = (sum >= 10);
             int digit = sum % 10;

             result->val = digit;


             if (l1)
                 l1 = l1->next;
             if (l2)
                 l2 = l2->next;

             if (!l1 && !l2 && !carry)
                 break;

             result->next = createNode(0);
             result = result->next;
         }
 
 return retVal;
    }
};