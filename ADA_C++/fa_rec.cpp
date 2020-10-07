#include<iostream>
using namespace std;
int fact(int n)
{
	if(n==1 or n==0)
	{
		
		return 1;
	
	}
	else
	{
		return n*fact(n-1);
	}
}
int main()
{
	int x;
	cout<<"input the number";
	cin>>x;
	cout<<"factorial of " <<x<<" is "<<fact(x)<<endl;
}
