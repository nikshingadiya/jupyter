#include<iostream>
using namespace std;
#include<vector>
#include <cstring>
#include <iterator> 
#include <map> 
#include <list>

void showlist(list <string> g)
{
	list <string> :: iterator it;
	for(it=g.begin(); it!=g.end(); ++it)
	{
		cout<<*it<<endl;
	}


}
void dictn(map <string,string> g)
{
//    map <string,string> :: iterator itr;
	for (auto itr = g.begin(); itr != g.end(); ++itr) { 
        cout << '\t' << itr->first 
             << '\t' << itr->second << '\n'; 
    } 

}
int main()
{
	list <string> List;
	map<string, string> d1;
	d1.insert({"nik", "ronak"});

	cout<<d1.find("k")<<endl;
	List.push_front("nikhil");
	List.push_front("Mehul");
	showlist(List);
	
	
}
