#include<iostream>
using namespace std;
void radixsort(int**,int);
void countsort(int*,int*,int,int);
int maxx(int*,int);
int main()
{
    int i,n;
    cout<<"enter the number of items : ";
    cin>>n;
    int* A=new int[n];
    cout<<"enter the items :\n";

    for(i=0;i<n;i++)
        cin>>A[i];

    radixsort(&A,n);
    cout<<"sorted order is:\n";

    for(i=0;i<n;i++)
        cout<<A[i]<<" ";

    return 0;
}
void radixsort(int** A,int n)
{
    int Max,exp,*temp;
    Max=maxx(*A,n);
    int *B=new int[n];
    for(exp=1;(Max/exp)>0;exp*=10)
    {
        countsort(*A,B,n,exp);
        temp=*A;
        *A=B;
        B=temp;
    }
    delete B;
}

void countsort(int* A,int* B,int n,int exp)
{
    int C[10]={0},i;

    for(i=0;i<n;i++)
        C[(A[i]/exp)%10]+=1;

    for(i=1;i<10;i++)
        C[i]+=C[i-1];

    for(i=n-1;i>=0;i--)
        B[--C[(A[i]/exp)%10]]=A[i];
}

int maxx(int* A,int n)
{
    int m=A[0];
    for(int i=1;i<n;i++)
        if(A[i]>m)
            m=A[i];
    return m;
}
