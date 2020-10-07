#include<iostream>
using namespace std;
void heapSort(int a[], int n);
void max_heap(int a[],int n,int i )
{
	int root=a[i];
	int largest=i;
	int left=2*i+1;
	int right=2*i+2;
	if(left < n && a[left]>root)
	{
		largest=left;
	}
	if(right < n &&  a[right]>a[largest])
	{
       	largest=right;
	}
	if(largest!=i)
	{
		int temp=a[i];
		a[i]=a[largest];
		a[largest]=temp;
		max_heap(a, n, largest);
	}
	
}
void heapSort(int a[], int n) {
    
    for (int i = n / 2 - 1; i >= 0; i--)
      max_heap(a, n, i);
  
    
    for (int i = n - 1; i >= 0; i--) {
      swap(a[0], a[i]);
  
     
      max_heap(a, i, 0);
    }
  }
  
  
void printArray(int a[], int n) {
    for (int i = 0; i < n; ++i)
    {
	
      cout<<a[i]<< " ";
    }
    cout<<"\n";
  }
int main()
{
	int a[]={1,3,2,6};
	int l=sizeof(a)/sizeof(a[0]);
	cout << "UnSorted array is \n";
    printArray(a, l);
	heapSort(a,l);
	cout << "Sorted array is \n";
    printArray(a, l);
    
}
