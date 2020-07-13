#include<iostream>
using namespace std;
class node
{
	public:
	node *left=NULL;
	int data;
	node *right=NULL;
	public:
    node(int key){
        data=key;
		
	}
	
};
void display(node *root);

void display(node *root) 
{ 
    if (root==NULL) 
    { 
        return;
    } 
   
    display(root->left); 
    cout <<"display= "<<root->data <<endl; 
    display(root->right); 
} 
void insert(node *root, int key)
{

	if(root->left==NULL)
	{
		root->left=new node(key) ;
		cout<<"left="<<key<<endl;
		
		root==NULL;
		return;
	}
    else if(root->right==NULL)
	{
		root->right=new node(key);
		cout<<"right="<<key<<endl;

		root=NULL;
		return;
	}
	insert(root->right,key);

	

}
int main()
{
  int a[]={2,3,4,5,6,8,9};
  node *head;
  
  node *root= new node(a[0]);
  head=root;
  for(int i=1; i<sizeof(a)/sizeof(a[0]); i++)
  {
  
  insert(head,a[i]);
 
  }
 
 
  display(head);

}
