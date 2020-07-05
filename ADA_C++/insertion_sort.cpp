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
void swap(int *x,int *y)
{
	int *temp=y;
	y=x;
	x=temp;
}

int main()
{
  int  x;
  cout<<"please enter your array size:";
  cin>>x;
  int a[x];
  for(int i=0; i<x; i++)
  {
  	cout<<"please enter your-:"<<i+1<<" number ";
  	cin>>a[i];	
  }
	int j=0;
	while(j<x)
	{
		for (int i=0; i<j; i++)
		{
			if(a[j]<a[i])
			{
				swap(&a[j],&a[i]);
//				int temp=a[j];
//				a[j]=a[i];
//				a[i]=temp;	
			}
		}
		j++;
	}
	print_array(a,x);
}

