/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* rotateRight(struct ListNode* head, int k) {
   struct ListNode *tmp=head;
   int l=0;
   while (tmp!=NULL){
    l++;
    tmp=tmp->next;
   }
   if (l==0)return head;
   k=k%l;
   for (int i=0;i<k;i++){
    struct ListNode *x1=head,*nn=(struct ListNode*)malloc(sizeof(struct ListNode));
    while (x1->next!=NULL){
        x1=x1->next;
    }
    nn->val=x1->val;
    nn->next=head;
    head=nn;
    x1=head;
    while (x1->next->next!=NULL){
        x1=x1->next;
    }
    struct ListNode *f=x1->next;
    x1->next=x1->next->next;
    free(f);
   }
   return head;
}