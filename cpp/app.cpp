// required header file 
#include <conio.h>
#include <iostream>
#include <windows.h>

using namespace std;

bool gameOver;

const int height = 20;
const int width = 20;
const char wallChar = '#';

void Setup(){
    gameOver=false;
}
void Draw(){
    system("CLS");
    for (int row = 0; row < height; row++) {
        for (int column = 0; column < width; column++) {
            if (row == 0 || row == height - 1) {
                cout << wallChar;
            } else if (column == 0 || column == width - 1) {
                cout << wallChar;
            } else {
                cout << " ";
            }
        }
        cout << endl;
    }
}
void Input(){}
void Logic(){}

int main(){
    Setup();
    while (!gameOver){
        Draw();
        Input();
        Logic();
    }
    return 0;
}

