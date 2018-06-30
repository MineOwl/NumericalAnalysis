/////////////////////////////////////////////////////////
//ガウス・ザイデル法を用いた連立方程式を解くアルゴリズム//////////
/////////////////////////////////////////////////////////


#include <iostream>
using namespace std;

//行列の列を書き出す
void print_row(const float row[],int last){
    for(int i = 0 ; i < last ; i++){
        cout << "[" << i << "]=" << row[i] << "  ";
    }
    //改行
    cout << endl;
}


int main(void){
    const int N=4;
    float data[N][N]={
                 {7, -1, 0,  1},
                 {-1, 9, -2, 2},
                 {0, -2, 8, -3},
                 {1, 2, -3, 10}
    };
    float X[N] = { 1, 1,  1, 1};
    float b[N] = {-5,15,-10,20};
    int loop = 100;
    float sum = 0;

    //何回も繰り返す
    for( int count = 0 ;count < loop ; count++){
        for( int i= 0 ; i < N ; i++){
            sum = 0;
            for( int j = 0; j < N ; j++){
                if ( i==j ){
                    //対角はほっとく
                    continue;
                }
                //右辺に移項
                sum -= data[i][j]*X[j];
            }
            sum += b[i];
            //対角で割る
            X[i] = sum / data[i][i];
            print_row(X,N);
        }
    }
}