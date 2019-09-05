#include<iostream>
using namespace std;
int* countsort(int* A,int n,int range)
{
    int* temp=new int[range];
    int* B=new int[n];
    int i;
    for(i=0;i<range;i++)
        temp[i]=0;
    for(i=0;i<n;i++)
        temp[A[i]]++;
    for(i=1;i<range;i++)
        temp[i]+=temp[i-1];
    for(i=0;i<n;i++)
        B[--temp[A[i]]]=A[i];
    delete temp;
    return B;
}

int main()
{
    int A[]={5,7,2,3,1,4,5,7,7};
    int *B=countsort(A,9,8);
    for(int i=0;i<9;i++)
        cout<<B[i]<<"\t";
    return 0;
}
