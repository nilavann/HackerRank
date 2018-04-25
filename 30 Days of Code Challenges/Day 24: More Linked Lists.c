Node* removeDuplicates(Node *head){
    //Write your code here
    int arr[100],n = 1;
    Node* temp = head;
    arr[0] = temp->data;
    while(temp->next != NULL){
        int data = temp->next->data, flag = 0;
        for(int i = 0; i < n; i++){
            if(data == arr[i]){
                flag = 1;
                break;
            }
        }
        if(flag == 1){
            Node* temp1 = temp->next->next;
            temp->next = temp1;
            Node* t = head;
            while(t){
                t=t->next;
            }
        }else{
            arr[n++] = data;
            temp = temp->next;
        }
    }
    return head;
}