#include<iostream>
using namespace std;
//void display(int m[5]) {
//	cout<<m<<endl;
//    cout << "Displaying marks: " << endl;
//
//    // display array elements    
//    for (int i = 0; i < 5; ++i) {
//        cout << "Student " << i + 1 << ": " << m[i] << endl;
//    }
//}
//
//int main() {
//
//    // declare and initialize an array
//    int marks[5] = {88, 76, 90, 61, 69};
//    int *c= marks;
//    cout<<sizeof(c)<<endl;
//    // call display function
//    // pass array as argument
//    display(marks);
//
//    return 0;
//}
////void Fun(int a[])
////{
////	
////
////	cout<<sizeof(a)<<endl;
//////	 for (int i=0; i<=2; i++)
//////	 {
//////	 
//////	 	cout<<b[i]<<endl;
//////	 }
////
////}
////
////
////
////int main()
////{
////	int a[]={1,2,3,4,5};
////	cout<<sizeof(a)<<endl;
//////	cout<<"how many number you want input(positive number):-";
//////	int x;
//////	cin>>x;
//////	int b[x];
//////	int temp=0;
//////	int min=0;
//////	int i=0;
//////	for ( i=0; i<x; i++)
//////	{
//////		cout<<"input number "<<i<<"-:";
//////		cin>>b[i];		
//////	}
//////	cout<<sizeof(b)<<endl;
////////	cout<<sizeof(b)/sizeof(b[0])<<endl;
////Fun(a);
////	
////}
void Test(int b[])
{
	cout<<b[0]<<endl;
	b[0]=5;
}
int main()
{
	int a[]={2,3,4,5,6};
	Test(a);
	cout<<a[0]<<endl;
	
}


