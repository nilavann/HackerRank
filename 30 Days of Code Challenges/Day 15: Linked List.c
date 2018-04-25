Node* insert(Node *head,int data)
{
    //Complete this function
    Node *temp2 = (struct Node *) malloc( sizeof(struct Node) );
    temp2->next = NULL;
    temp2->data = data;
    if(head == NULL)
        head = temp2; 
    else{
        Node *temp;
        temp = head;
        while(temp->next != NULL){
            temp=temp->next;   
        }
        temp->next = temp2;
    }
    /**/
    return head;
}