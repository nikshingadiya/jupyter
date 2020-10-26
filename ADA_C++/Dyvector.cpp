#include<iostream>
#include<vector>
using namespace std;
#include<algorithm>  
void printvec(vector <int>a)
{
	for (int i=0; i<a.size(); i++)
	{
		cout<<a[i]<<endl;
		
	}
	
}
void print2dvec(vector<vector<int>>B)
{
	for (int i=0; i<B.size(); i++)
	{
	
		for (int j=0; j<B[i].size(); j++)
		{
			cout<<B[i][j]<<" ";
			
		}
		cout<<endl;
    }
    cout<<endl;
	
}
void recursive(vector<vector<int>>B,vector<int>w, vector<int>v,int r,int c,int we)
{
	if(we<=0  or ( r<=0 and c<=0) )
	{
		return ;
	}
	else
	{
		if(B[r][c]==B[r-1][c])
		{
			
            
			cout<<w[r-1]<<"       "<<v[r-1]<<endl;
			we=we-w[r-1];
			c=c-w[r-1];
			r=r-2;
			return recursive(B,w,v,r,c,we);
			
		}
		else
		{
			cout<<w[r]<<"       "<<v[r]<<endl;
			we=we-w[r];
			c=c-w[r];
			r=r-1;
			return recursive(B,w,v,r,c,we);
			
		}
	}
	
}
void final_sol(vector<vector<int>>B,vector<int>w, vector<int>v,int we)
{
	int c=B[0].size();
	int r=B.size();
	cout<<"Optimal things and get maximum profit"<<endl;
	
	cout<<"Weight "<<"Value "<<endl;
	cout<<"\n";
	recursive(B,w,v,r-1,c-1,we);	
}
bool comp(int a, int b)   
{   
    return (a < b);   
}   
void ksc(vector<int>w, vector<int>v,int max_w)
{
	vector< vector<int> > ksc_table(v.size(),vector<int>(max_w+1,0));
	for (int i=1; i<v.size(); i++)
	{
		for (int j=1; j<=max_w; j++)
		{
			if(j<w[i])
			{
				ksc_table[i][j]=ksc_table[i-1][j]; 
				
			}
			else
			{
				int a,b;
				a=v[i]+ksc_table[i-1][j-w[i]];
				b=ksc_table[i-1][j];
				ksc_table[i][j]=max(a,b,comp);
			}
		}
	}
	print2dvec(ksc_table);
	final_sol(ksc_table,w,v,max_w);
}
int main()
{
	
	vector<int> weight{0,1,3,4,5};
	vector<int> value{0,1,4,5,7};

    ksc(weight,value,9);
       
}
