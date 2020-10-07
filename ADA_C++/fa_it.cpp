#include<iostream>
using namespace std;
int fact(int n)
{
	int fact=1;
	for(int i=n; i>0; i--)
	{
		fact=fact*i;
	}
	return fact;
}
int main()
{
	int x;
	cout<<"input the number";
	cin>>x;
	cout<<"factorial of " <<x<<" is "<<fact(x)<<endl;
}
