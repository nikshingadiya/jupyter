#include <iostream>
using namespace std;
int main()
{
	string main_p="nikniknik";
	string find_p="nikn";
	int N=main_p.length();
	int M=find_p.length();
	int x=0;
	for (int i=0; i<=N-M; i++)
	{
	
				int j=i;
				int k=0;
				while(k<M)
				{
					if(main_p[j]==find_p[k])
					{
						j++;
						k++;
					}
					else
					{
						break;
					}
				}
				if(k==M)
				{
					x=x+1;
				
				}
				
				
    }
	cout<<"Matching Pair: "<<x<<endl;
}
