#include <stdlib.h>

// LeetCode's definition (or similar)
struct ListNode {
    int val;
    struct ListNode *next;
};

static int gcd(int a, int b) {
    // Iterative Euclid to avoid recursion overhead
    while (b != 0) {
        int t = a % b;
        a = b;
        b = t;
    }
    return a;
}

struct ListNode* insertGreatestCommonDivisors(struct ListNode* head) {
    struct ListNode* curr = head;

    while (curr != NULL && curr->next != NULL) {
        int g = gcd(curr->val, curr->next->val);

        struct ListNode* node = (struct ListNode*)malloc(sizeof(struct ListNode));
        node->val = g;                  // store gcd
        node->next = curr->next;        // new node points to next original node
        curr->next = node;              // current points to new node (insertion done)

        curr = node->next;              // move to next original node
    }
    return head;
}
