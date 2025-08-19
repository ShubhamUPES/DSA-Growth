// Definition for singly-linked list
struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode* swapPairs(struct ListNode* l) {
    if (l == NULL || l->next == NULL) return l;

    // swap values
    int temp = l->val;
    l->val = l->next->val;
    l->next->val = temp;

    // move recursion to next pair
    swapPairs(l->next->next);

    return l;
}
