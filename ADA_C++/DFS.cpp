#include<iostream>
using namespace std;
#include<vector>
#include <cstring>
#include <iterator> 
#include <map> 
#include <list>
class Node
{ 
  public:
  	string name;
  	Node(string name1="")
  	{
  		name=name1;
	}
    string getname()
    {
    	return name;
	}
	
};

class Edge 
{
  public:
	Node src;
	Node dest;
  
    Edge(Node src1,Node dest1)
    {
    	src=src1;
    	dest=dest1;
    	
	}
	
	Node get_src()
	{
		return src;
	}
	Node get_dest()
	{
		return dest;
	}
	
//	void print_edge()
//	{
//		cout<<get_src().getname()<<"->"<< get_dest().getname();
//	}
//	
};
class Diagraph
{
	map<Node, vector <Node> > DG;

    public:
    void addNode(Node n1)
    {
    	
    		vector <Node> v1({n1});
    	
          	DG.insert({n1,v1});
      	
    	
	}
	void Edge(Edge E1)
	{
		Node src=E1.get_src();
		Node dest=E1.get_dest();
		
//		DG.insert({src,DG.find(src)});
	}
    
};
int main()
{
	
//	Node n1("nikhil");
//	Node n2("chiku");
//	Edge E1(n1,n2);
//	E1.print_edge();
	
	
}
