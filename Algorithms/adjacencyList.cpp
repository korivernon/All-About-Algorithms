#include<iostream>
#include<stdio.h>
#include<vector>

using namespace std;

void addEdge(vector<int> adj[], int u, int v){
    // when you add an edge, you are adding to the existing adjacency list. 
    adj[u].push_back(v);
    // whhen you add to an adjacency list, with every iteration you are adding to the existing edge
    adj[v].push_back(u);
}

void printGraph(vector<int> adj[], int V){
    for (int v = 0; v < V; v++){
        cout << "\n["
        << v << "]";
        // auto automaticall determines the type 
        for (int x : adj[v])
             cout << "-> " << x;
    }
    cout << "\n";
}

// Driver
int main() 
{ 
    int V = 5; 
    vector<int> adj[V]; 
    addEdge(adj, 0, 1); 
    addEdge(adj, 0, 4); 
    addEdge(adj, 1, 2); 
    addEdge(adj, 1, 3); 
    addEdge(adj, 1, 4); 
    addEdge(adj, 2, 3); 
    addEdge(adj, 3, 4); 
    printGraph(adj, V); 
    return 0; 
} 