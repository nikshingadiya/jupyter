#include<iostream>
using namespace std;
void  print_array(int p[],int size)
{
	static int i;
	if (i==size)
	{
		i=0;
		cout<<endl;
		return;
	}
	cout<<p[i]<<" ";
	i=i+1;
	print_array(p,size);
}
int * minimum(int a[],int size,int start)
{
    int min;
	int index;
	int i;
	if(size==start+1)
	{
		return a;
	}
	else
	{
		for(i=start; i<size-1; i++)
		{
		   min=a[i];
		   index=i;
		   if(min>a[i+1])
		   {
			   	min=a[i+1];
	
			   	index=i+1;
		   
		   }
	    
	   }

		int temp=a[start];
		a[start]=min;
		a[index]=temp;
		start=start+1;
		return minimum(a,size,start);
    }
	
}
int main()
{
	cout<<"input array size (positive number):-";
	int x=0;
	cin>>x;
	int c[x];
	int temp=0;
	int i=0;
	for (i=0; i<x; i++)
	{
		cout<<"input number "<<i+1<<"-:";
		cin>>c[i];		
	}

    print_array(minimum(c,x,0),x);

}










