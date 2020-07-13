#include<iostream>
using namespace std;
int show(int *,int ,int,int);
int divide(int *,int ,int);

int divide(int arr[],int lb,int ub)
{

   static int x;
	if(lb<ub)
	{
	   
	    int mid=(lb+ub)/2;
       
		divide(arr,lb,mid);
		divide(arr,mid+1,ub);
	    x+=show(arr,lb,ub,mid);
	    
	    
	
		
	}
	return x-1;
	
}
//void merge_sort(int *arr, int low, int high)
//{
//    int mid;
//    if (low < high)
//	{
//
//        mid=(low+high)/2;
//        merge_sort(arr,low,mid);
//        merge_sort(arr,mid+1,high);
//       
//        merge(arr,low,high,mid);
//    }
//}

int show(int *arr, int low, int high, int mid)
{
    int i, j, k, c[50];
    i = low;
    k = low;
    j = mid + 1;
    int x=0;
    static int m=0;
    while (i <= mid && j <= high) {
        if (arr[i] < arr[j]) {
            c[k] = arr[i];
            k++;
            i++;
        }
        else  {
            c[k] = arr[j];
            k++;
            m++;
            
            if(x==0)
            {
            	x++;
			}
            j++;
        }
    }
    while (i <= mid) {
        c[k] = arr[i];
        k++;
        i++;
    }
    while (j <= high) {
        c[k] = arr[j];
        
      
        k++;
        j++;
       
    }
    
    for (i = low; i < k; i++)  {
        arr[i] = c[i];
    }
    cout<<m<<endl;

    return m;
}




 
int main()
{
	int a[]={3,2,1};
	
	int size=sizeof(a)/sizeof(a[0]);
	int mid=(size-1)/2;
	int con=divide(a,0,size-1);
	cout<<con<<endl;
	for (int i=0; i<size; i++)
	{
		cout<<a[i]<<" ";
	}
	
	
}
