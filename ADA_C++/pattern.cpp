#include<iostream>
using namespace std;
int main()
{
	int n=0;
	scanf("%d",&n);
	for (int i=0; i<(n+1); i++)
	{
		
		if(i%5==0)
		{
		
		for (int j=0; j<(n*4+1); j++)
		{
			printf("*");
		}
		printf("\n");
		
	   }
	   else
	   {
	   	for (int j=0; j<(n*4+1); j++)
		{
			if(j%10==0)
			{
			
			printf("*");
		    }
		    else
		    {
		    	printf(" ");
			}
		}
		printf("\n");
		
	   }
		
	}
}
