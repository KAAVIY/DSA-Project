# -*- coding: utf-8 -*-
"""Pattern

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AQuHcpBMc4hlYwT6688EwYh3ipPoMhTx
"""

#include <iostream>
using namespace std;
 
void triangle(int n)
{
    int k = 2 * n - 2;
 
    for (int i = 0; i < n; i++) {
 
        for (int j = 0; j < k; j++)
            cout << " ";
 
        k = k - 1;
 
        for (int j = 0; j <= i; j++) {
            cout << "* ";
        }

        cout << endl;
    }
}
 
int main()
{
    int n = 5;
   
    triangle(n);
    return 0;
}