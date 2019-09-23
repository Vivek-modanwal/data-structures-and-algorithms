#include<stdio.h>
#include<stdlib.h>

int** allocate(int);
int** strassen(int**,int**,int);
int** create(int**,int,int,int);
int** addSubtract(int**,int**,int,int);
void Delete(int***,int,int);
void IO(int**,int,int);

int main()
{

    int N=64;
    int** A=allocate(N);
    int** B=allocate(N);
    IO(A,N,1);
    IO(B,N,1);
    printf("\nA ->\n\n");
    IO(A,N,0);
    printf("\nB ->\n\n");
    IO(B,N,0);
    int** C=strassen(A,B,N);
    printf("\nC ->\n\n");
    IO(C,N,0);

    return 0;
}

void IO(int** A,int N,int I)
{
    int i,j;
    for(i=0;i<N;i++)
    {
        for(j=0;j<N;j++)
        {
            if(I)
                scanf("%d",A[i]+j);
            else
                printf("%d  ",A[i][j]);
        }
        if(!I)
            printf("\n");
    }
}
int** create(int** A,int N,int x,int y)
{
    int i,j,ilimit,jlimit,m=0,n=0;

    int **C=allocate(N);

    ilimit=N*(x+1);
    jlimit=N*(y+1);

    for(i=N*x;i<ilimit;i++)
    {
        for(j=N*y;j<jlimit;j++)
        {
            C[m][n]=A[i][j];
            n++;
        }
        m++;
        n=0;
    }
    return C;
}
int** addSubtract(int** A,int **B,int N,int flag)
{
    int i,j;
    int **C=allocate(N);
    for(i=0;i<N;i++)
    {
        for(j=0;j<N;j++)
        {
            if(flag)
                C[i][j]=A[i][j]+B[i][j];
            else
                C[i][j]=A[i][j]-B[i][j];
        }
    }
    return C;
}
int** allocate(int N)
{
    int **C=malloc(N*sizeof(int*));
    int i;
    for(i=0;i<N;i++)
        C[i]=malloc(N*sizeof(int));
    return C;
}

void Delete(int*** A,int start,int end)
{
    int i;
    for(i=start;i<=end;i++)
        free(A[i]);
}

int** strassen(int** A,int **B,int N)
{
    if(N<=2)
    {
        int **C=allocate(N);
        C[0][0]=A[0][0]*B[0][0]+A[0][1]*B[1][0];
        C[0][1]=A[0][0]*B[0][1]+A[0][1]*B[1][1];
        C[1][0]=A[1][0]*B[0][0]+A[1][1]*B[1][0];
        C[1][1]=A[1][0]*B[0][1]+A[1][1]*B[1][1];
        return C;
    }

    int dim=N/2,i,j,m,n;
    int** mat[8];
    int** xy[10];
    int** P[8];
    mat[0]=create(A,dim,0,0);//a
    mat[1]=create(A,dim,0,1);//b
    mat[2]=create(A,dim,1,0);//c
    mat[3]=create(A,dim,1,1);//d
    mat[4]=create(B,dim,0,0);//e
    mat[5]=create(B,dim,0,1);//f
    mat[6]=create(B,dim,1,0);//g
    mat[7]=create(B,dim,1,1);//h


    xy[0]=addSubtract(mat[5],mat[7],dim,0);
    xy[1]=addSubtract(mat[2],mat[3],dim,1);
    xy[2]=addSubtract(mat[0],mat[3],dim,1);
    xy[3]=addSubtract(mat[4],mat[7],dim,1);
    xy[4]=addSubtract(mat[0],mat[2],dim,0);
    xy[5]=addSubtract(mat[4],mat[5],dim,1);
    xy[6]=addSubtract(mat[0],mat[1],dim,1);
    xy[7]=addSubtract(mat[6],mat[4],dim,0);
    xy[8]=addSubtract(mat[1],mat[3],dim,0);
    xy[9]=addSubtract(mat[6],mat[7],dim,1);


    P[1]=strassen(mat[0],xy[0],dim);
    P[2]=strassen(xy[6],mat[7],dim);
    P[3]=strassen(xy[1],mat[4],dim);
    P[4]=strassen(mat[3],xy[7],dim);
    P[5]=strassen(xy[2],xy[3],dim);
    P[6]=strassen(xy[8],xy[9],dim);
    P[7]=strassen(xy[4],xy[5],dim);

    Delete(mat,0,7);
    Delete(xy,0,9);

    int **C=allocate(N);

    m=0;n=0;
    for(i=0;i<dim;i++)
    {
        for(j=0;j<dim;j++)
        {
            C[m][n]=P[5][i][j]+P[4][i][j]-P[2][i][j]+P[6][i][j];
            n++;
        }
        m++;n=0;
    }

    m=0;n=dim;
    for(i=0;i<dim;i++)
    {
        for(j=0;j<dim;j++)
        {
            C[m][n]=P[1][i][j]+P[2][i][j];
            n++;
        }
        m++;n=dim;
    }

    m=dim;n=0;
    for(i=0;i<dim;i++)
    {
        for(j=0;j<dim;j++)
        {
            C[m][n]=P[3][i][j]+P[4][i][j];
            n++;
        }
        m++;n=0;
    }

    m=dim;n=dim;
    for(i=0;i<dim;i++)
    {
        for(j=0;j<dim;j++)
        {
            C[m][n]=P[1][i][j]+P[5][i][j]-P[3][i][j]-P[7][i][j];
            n++;
        }
        m++;n=dim;
    }

    Delete(P,1,7);

    return C;
}
