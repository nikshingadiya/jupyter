#include<iostream>
using namespace std;
class Node
{
	public:
	Node *left=NULL;
    int data;
	Node *right=NULL;
	public:
    Node(int key){
        data=key;
        Node *left=NULL;
        Node *right=NULL;
		
	}
	
};
void inorder(Node *root);

void inorder(Node *root) 
{ 
    if(root == NULL)
            return;
        
        //First recur on left subtree 
        inorder(root->left);
        //Then read the data of child
        cout << root->data << " ";
        // Recur on the right subtree
        inorder(root->right);
} 
Node* insert(Node* root, int data) {
        if(root == NULL){
            return new Node(data);
        }
     else{
            Node* cur;
            if(data <= root->data) {
                cur = insert(root->left, data);
                root->left = cur;
            }
            else {
                cur = insert(root->right, data);
                root->right = cur;
            }
           
        return root;
     }
    }

	




	



int main(){
    Node Tree(0);
    Node* root = NULL;
    //Number of nodes to be inserted
    int t;
    cin>>t;
    while(t--){
        int data;
        cin>>data;
        root=insert(root,data);
        
    }
    inorder(root);
}

