#include <iostream>
using namespace std;
//このプログラムはコメントで説明できません

void print_matrix(const float matrix[],int limit){
    for(int i=0;i<limit;i++){
        cout<<"["<<i<<"]="<<matrix[i]<<"  ";
    }
    cout<<endl;
}


int main(void){
    const int N=4;
    float data[N][N]={
              {7, -1, 0, 1},
              {-1, 9, -2, 2},
              {0, -2, 8, -3},
              {1, 2, -3, 10}
    };
    float X[N]={1,1,1,1};
    float b[N]={-5,15,-10,20};
    float div;
    float sum=0;
    for(int count=0;count<100;count++){
        for(int i=0;i<N;i++){
            sum=0;
            for(int j=0; j<N;j++){
                if (i==j){
                    //対角
                    div=data[i][i];
                    continue;
                }
                sum-=data[i][j]*X[j];
            }
            sum+=b[i];
            X[i]=sum/div;
            print_matrix(X,N);
        }
    }
}
