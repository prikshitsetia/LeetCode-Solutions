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
class Solution
{
public:
    ListNode *reverseKGroup(ListNode *head, int k)
    {
        int t = 0;
        ListNode *temp = head;
        while (t < k)
        {
            if (temp == NULL)
            {
                return head;
            }
            temp = temp->next;
            t += 1;
        }

        ListNode *curr = head;
        ListNode *prev = NULL;
        int i = 0;
        while (i < k and curr != NULL)
        {
            ListNode *n = curr->next;
            curr->next = prev;

            prev = curr;
            curr = n;
            i += 1;
        }
        head->next = reverseKGroup(curr, k);
        return prev;
    }
};