#include<iostream>
using namespace std;
int linear_search( int a[],int x,int l)
{
	for(int i=0; i<l; i++)
	{
		if(a[i]==x)
		{
			cout<<"Position of "<< x << " in this array is "<<i;
			return 0;
		}
		
	}
	return -1;
}
int main()
{
	int a[]={23,9,45,36,67,89,84};
	int l=sizeof(a)/sizeof(a[0]);
	if (linear_search(a,0,l)!=0)
	{
		cout<<"Element is not present in array";
		
	}

	
}
