#include<iostream>
#include <string.h>
using namespace std;
int Binary_search(int a[],int x, int start ,int l,int mid )
{
	    if(a[mid]==x)
	       {
	     	  cout<<"Position of "<< x << " in this array is "<<mid;
		      return 0;
	    	}
		else if( mid==start)
		{
		 	return -1;
		}
		else
			{ 
			    if(x >a[mid])
			    {
			    	int new_mid=(mid+l)/2;
			    	return Binary_search(a,x,mid+1, l, new_mid);	
				}
				else
				{
					int new_mid=(start+mid)/2;
					
					return Binary_search(a, x,0, mid-1,new_mid);	
				}  	
			      	
		    }
	
}
int main()
	{
		int a[]={1,2,3,4,5,6,7,8};
		int x=10;
		int l=sizeof(a)/sizeof(a[0]);
		int mid=l/2;
		
		if (Binary_search(a,x,0,l,mid)!=0)
		{
			cout<<"Element "<<x<<" is not present in array";
			
		}
		
	}
