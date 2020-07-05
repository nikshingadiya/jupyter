#include<iostream>
using namespace std;
int main()
{
	cout<<"input array size (positive number):-";
	int x;
	cin>>x;
	int b[x];
	int temp=0;
	for (int i=0; i<x; i++)
	{
		cout<<"input number "<<i+1<<"-:";
		cin>>b[i];		
	}	
	for (int j=0; j<x; j++)
	{
		for (int i=0; i<x-(j+1); i++)
		{
		

			if(b[i+1]<b[i])
			{
				temp=b[i];
				b[i]=b[i+1];
				b[i+1]=temp;
				
			}
		}
    }
    cout<<"Sorted Array:"<<endl;
    for (int i=0; i<x; i++)
    {
    	cout<<b[i]<<" ";
	}
		
}
