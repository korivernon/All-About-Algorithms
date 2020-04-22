#include<iostream>
#include<stdio.h>

#define NODE 5

using namespace std; 

int graph[NODE][NODE] = {
{0, 0, 1, 0, 0},
{1, 0, 1, 1, 0},
{1, 1, 0, 1, 1},
{0, 1, 1, 0, 1},
{0, 0, 1, 1, 0}
};

void traverse(int u, bool visited[]){
    visited[u] = true; //set visited to true for v
    for (int v = 0; v < NODE; v++){
        if (graph[u][v]){
            //if the graph exists.
            if(!visited[v]){
                traverse(v,visited);
            }
        }
    }
}
bool isConnected(){
    bool *vis = new bool[NODE];
    //create an aray of nodes
    memset(vis,false,NODE);
    for(int u; u < NODE; u++){
        traverse(u, vis);
        for (int i = 0; i < NODE; i++){
            if(!vis[i]) return false; // if there is a node not visited by traversal then the graph is not connected
        }
    }
    return true;
    delete [] vis;
}
int main(){
	if(isConnected())
		cout << "The Graph is connected.\n";
	else
		cout << "The Graph is not connected.\n";
}