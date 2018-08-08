/////////////////////////////////////////////////////////
//SOR法を用いた連立方程式を解くアルゴリズム////////////////////
/////難しいことはいいのでmainのみ見てください//////////////////
/////////////////////////////////////////////////////////




#include <iostream>
#include <time.h>
using namespace std;

//行列の列を書き出す
/////難しいことはいいのでmainのみ見てください//////////////////
void print_row(const float row[],int last){
    for(int i = 0 ; i < last ; i++){
        cout << "[" << i << "]=" << row[i] << "  ";
    }
    //改行
    cout << endl;
}

int main(void){
    clock_t end;
    clock_t start = clock();
    const int N=4;
    float A[N][N]={
                 {7, -1, 0,  1},
                 {-1, 9, -2, 2},
                 {0, -2, 8, -3},
                 {1, 2, -3, 10}
    };
    float X[N] = { 1, 1,  1, 1};
    float b[N] = {-5,15,-10,20};
    int loop = 100;
    float sum = 0;
    float w = 1.5;
    //何回繰り返す？
    for( int count = 0 ;count < loop ; count++){

        //メインとなる処理
        for( int i = 0 ; i < N ; i++ ){
            sum = 0;
            for( int j = 0 ; j < N ; j++ ){
                //xに代入し右辺に以降し和をとる
                sum -= X[j] * A[i][j];
            }
            //引く
            X[i] = X[i] + w *(b[i] + sum) / A[i][i];
        }
        //ここで表示
        print_row(X,N);

    }

    end = clock();

    cout << "duration = " << (double)(end - start) / CLOCKS_PER_SEC << "sec.\n";
}