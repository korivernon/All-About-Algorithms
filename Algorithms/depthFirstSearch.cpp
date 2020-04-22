#include<iostream>
#include<vector>
#include<list>
using namespace std;

#define MAX 1000

class Stack{
    private:
    int tops;
    
    public:
    int a[MAX];
    Stack() {tops = -1;}
    int size() {return tops+1;}
    void push(int e){
        a[++tops] = e; //before when pushing
    }
    int pop(){
        return a[tops--]; //after when deleting
    }
    int top() {return a[tops];}
    bool isEmpty() {return tops == -1;}
};

class Graph{
    int V; // number of vertices
    list<int> *adj; // adjacency list of pointer objects
    public:
    Graph(int vertices){
        this->V = vertices; // initialize V
        adj = new list<int>[vertices]; // initializing new adjacency list for number of vertices
    }
    void addEdge(int v, int u){
        adj[v].push_back(u);
    }
    void DFS(int s){
        vector<bool> visited(V,false);
        /*
        what this does is initialized a 
        vector of size v and initializes 
        everything to false
        */
       Stack stack;
       stack.push(s);
       while(!stack.isEmpty()){
           s = stack.top();
           stack.pop();

           if (!visited[s]){
               cout << s << " ";
               visited[s] = true;
           }
           for (auto i = adj[s].begin(); i != adj[s].end();++i){
               if (!visited[*i]){
                   stack.push(*i);
               }
           }
       }
    }
};
// Driver program to test methods of graph class 
int main() 
{ 
    Graph g(5); // Total 5 vertices in graph 
    g.addEdge(1, 0); 
    g.addEdge(0, 2); 
    g.addEdge(2, 1); 
    g.addEdge(0, 3); 
    g.addEdge(1, 4); 
  
    cout << "Following is Depth First Traversal\n"; 
    g.DFS(0); 
  
    return 0; 
} 