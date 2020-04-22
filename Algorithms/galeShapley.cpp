#include<iostream>
#include<string.h>
#include<stdio.h>
using namespace std;

/*
The Gale-Shapley Algorithm is as follows...
while (there exist a free man m who still has a woman to propose to)
{
    w = m's highest ranked woman whom he has not yet proposed to
    if (w free) {
        (m,w) are paired
    } else {
        some pair (m',w) already exists
        if (w prefers m to m'){
            (m,w) is paired
            m' is freed
        } else {
            (m', w) remains engaged
        }
    }
}
The input will be a 2D matrix with size (2*n)n where n is 
the cardinality of the set of men OR women
*/
#define N  4 
bool wPreferM1OverM(int prf[2*N][N], int w, int m, int m1){
    for (int i = 0; i < N; i++){
        // if the woman prefers m1 to m
        if (prf[w][i]==m1) return true;
        // if the woman prefers m to m1, return false
        if (prf[w][i] == m) return false;
    }
}

void stableMarriage(int prf[2*N][N]){
    // store the partner of the woman and indicates the partner assigned to woman N+i
    int wPartner[N];
    // array that stores the availability of women
    bool mFree[N];

    // initialize all men and women as free
     memset(wPartner, -1, sizeof(wPartner));
     memset(mFree, false, sizeof(mFree));

     // go one by one to all women according to m's pref list
     // one m is the picked free man
     // we can retain a count of free men
     int freeCnt = N; //lol no pun intended

     while (freeCnt > 0){
         int m;
         //it's important to track m outside of the loop so we can retain the value of m
         for (m = 0; m < N; m++){
             if (mFree[m]==false){
                 break;
                 //pick a free man
             }
        // here we want to to ensure that the man is free as we iterate 
         } for (int i = 0; i < N && mFree[m] == false; i++){
             int w = prf[m][i];
             // if wPartner w
             if (wPartner[w-N] == -1){
                 // if the woman is free
                 mFree[m] = true;
                 wPartner[w-N] = m;
                 freeCnt--;
             }
             int m1 = wPartner[w-N];
             if (wPreferM1OverM(prf, w, m, m1)==false) {
                 wPartner[w-N] = m; //pair m and w
                 mFree[m] = true; //ensure that m is paired to w
                 mFree[wPartner[m1]] = false; // free m1
             }
         }
     }
     cout << "Woman \tMan" <<endl;
     for (int i = 0; i < N; i++)
         cout << " " << i+N << "\t" << wPartner[i] << endl;
}

// Driver
int main() 
{ 
    int prefer[2*N][N] = { {7, 5, 6, 4}, 
        {5, 4, 6, 7}, 
        {4, 5, 6, 7}, 
        {4, 5, 6, 7}, 
        {0, 1, 2, 3}, 
        {0, 1, 2, 3}, 
        {0, 1, 2, 3}, 
        {0, 1, 2, 3}, 
    }; 
    stableMarriage(prefer); 
  
    return 0; 
} 