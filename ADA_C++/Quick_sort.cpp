#include<iostream>
using namespace std;
int Partion_sort(int *,int ,int );

void print_array(int a[],int size)
{
	for (int i=0; i<size; i++)
	{
		cout<<a[i]<<" ";
		
	}
}
Quick_sort(int a[],int lb,int ub)
{
	if(lb<ub)
	{
		int loc=Partion_sort(a,lb,ub);
		Quick_sort(a,lb,loc-1);
		Quick_sort(a,loc+1,ub);
		
	}
	
}

int Partion_sort(int a[],int lb,int ub)
{
	int start=lb;
	int end=ub;
	int pivot=a[lb];
	while(start<end)
	{
	 
			while(a[start]<=pivot)
			{
			
				start++;
			}
			while(a[end]>pivot)
			{
			    end--;
			}
			if(end>start)
			{
                int temp=a[end];
                a[end]=a[start];
                a[start]=temp;
                

				
			}
    }
    int temp=a[end];
    a[end]=a[lb];
    a[lb]=temp;
    return end;
	
}

int main()
{
		  int  x;
		  cout<<"please enter your array size:";
		  cin>>x;
		  int a[x];
		  int b[x];
		  for(int i=0; i<x; i++)
		  {
		  	cout<<"please enter your-:"<<i+1<<" number ";
		  	cin>>a[i];	
		  	b[i]=a[i];
		  	
		  }
			
			Quick_sort(a,0,x-1);
			cout<<"unsorted array"<<endl;
			print_array(b,x);
			cout<<endl;
			cout<<"Sorted Array :"<<endl;
			print_array(a,x);
			
}
