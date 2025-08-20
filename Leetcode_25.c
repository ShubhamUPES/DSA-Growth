struct ListNode* reverseKGroup(struct ListNode* head, int k) {
    if (!head) return NULL;

    // check if at least k nodes remain
    struct ListNode* temp = head;
    for (int i = 0; i < k; i++) {
        if (!temp) return head; // less than k nodes, leave as is
        temp = temp->next;
    }

    // reverse first k nodes
    struct ListNode* prev = NULL;
    struct ListNode* cur = head;
    struct ListNode* next = NULL;
    int count = 0;

    while (cur && count < k) {
        next = cur->next;
        cur->next = prev;
        prev = cur;
        cur = next;
        count++;
    }

    // connect with recursion
    head->next = reverseKGroup(cur, k);

    return prev; // prev is new head after reversing k nodes
}
