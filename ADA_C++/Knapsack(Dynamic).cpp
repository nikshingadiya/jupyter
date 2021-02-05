#include<iostream>
using namespace std;
void printarray(int a[], int l)
{
	for (int i=0; i<l; i++)
	{
		cout<<a[i]<<endl;
		
	}
	
}
void printarray2d(int b[], int r,int c)
{
	
	
}
void knapsack(int wt[], int val[], int lw, int lv,int max)
{
	int ksac[lv+1][lw+1];
	for (int i=0; i<=lv; i++)
	{
		
	
			for (int j=0; j<=lw; j++)
			{
				ksac[i][j]=0;
				cout<<ksac[i][j]<<" ";
			}
			cout<< endl;
    }
    
}
int main()
{
	int weight[]={10,20,40};
	int value[] ={60,80,10};
	int lw=sizeof(weight)/sizeof(weight[0]);
	int lv=sizeof(value)/sizeof(value[0]);
	knapsack(weight, value, lw, lv, 50);
	
	
	
}
