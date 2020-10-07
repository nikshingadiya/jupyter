#include<iostream>
using namespace std;
void change(int [],int, int);

void change(int coins[],int l, int Amount)
{
      int combination[Amount+1]={0};
	  combination[0]=1;
	  for(int i=0; i<l; i++)
	  {
			  for (int j=1; j<=Amount; j++)
			  {
			          
					  if(j>= coins[i])
					  {
					  	
						  combination[j] += combination[j-coins[i]];
					  	
					  }	
			 }
			                         

    }
    
    cout<<"Possible way you can exchange "<<combination[Amount]<<endl;
     
}

int main()
{
	
	int coin_count;
	cout<< "How many coins you have"<<endl;
	cin>> coin_count;
	int coins[coin_count];
	int amount;
	for (int i = 0; i <coin_count; i++) 
	{
      cout<<"enter the "<<i+1<<" coin ";
      cin >> coins[i] ;
    }
	cout<<"how many amount u have"<<endl;
	cin>>amount;
	int l=sizeof(coins)/sizeof(coins[0]);
	change(coins, l, amount);
	
}
