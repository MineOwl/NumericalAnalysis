/////////////////////////////////////////////////////////
//ガウス・ザイデル法を用いた連立方程式を解くアルゴリズム//////////
/////////////////////////////////////////////////////////


#include <iostream>
#include <random>
#define NUM 4
using namespace std;
///////////////
void MakeRandomMatrix(int N , float (&data)[NUM][NUM] , int start , int last);

void PrintRow(const float row[],int last);

int main(void){
    
    float data[NUM][NUM]={
                 {7, -1, 0,  1},
                 {-1, 9, -2, 2},
                 {0, -2, 8, -3},
                 {1, 2, -3, 10}
    };
    float b[NUM] = {-5,15,-10,20};
    
   /*
    float data[NUM][NUM];

    MakeRandomMatrix( NUM , data , 3 , 6);
    float b[NUM] = { 1, 2, 3 };
    */

    float X[NUM];
    int loop = 100;
    float sum = 0;

    //何回も繰り返す
    for( int count = 0 ;count < loop ; count++){

        //以下メインーーーーーーーーーー
        //縦に動かす
        for( int i= 0 ; i < NUM ; i++){
            sum = 0;
            //横に動かす
            for( int j = 0; j < NUM ; j++){
                if ( i==j ){
                    //対角はほっとく
                    continue;
                }
                //代入したあと右辺に移項
                sum -= data[i][j]*X[j];
            }
            sum += b[i];
            //対角で割る
            X[i] = sum / data[i][i];
        }
        //以上メインーーーーーーーーーー
        PrintRow(X,NUM);

    }
}



void MakeRandomMatrix(int N , float (&data)[NUM][NUM] , int start , int last){
    for( int i= 0 ; i < N ; i++){
        for( int j = 0; j < N ; j++){
            data[i][j] = rand() % last + start;
            cout <<data[i][j] <<",";
        }
        cout<<endl;
    }
}

void PrintRow(const float row[],int last){
    for(int i = 0 ; i < last ; i++){
        cout << "[" << i << "]=" << row[i] << "  ";
    }
    //改行
    cout << endl;
}
