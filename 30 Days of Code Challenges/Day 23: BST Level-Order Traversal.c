void levelOrder(Node* root){
    //Write your code here
    Node* queue[100];
    int start=-1,end=-1;
    Node* n = root;
    
    while(n != NULL){
        printf("%d ",n->data);
        if(n->left != NULL)
            queue[++end] = n->left;
        if(n->right != NULL)
            queue[++end] = n->right;
        if( start != end){
            n = queue[++start];
        }else{
            n = NULL;
        }
    }
}