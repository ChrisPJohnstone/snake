// required header file 
#include <conio.h>
#include <iostream>
#include <windows.h>

using namespace std;

bool gameOver;
const char wallChar = '#';
const char snakeHeadChar = '0';
const char fruitChar = 'F';

const int height = 20;
const int width = 20;

int snakeX, snakeY, fruitX, fruitY, score;

const char dirUpChar = 'w';
const char dirDownChar = 's';
const char dirLeftChar = 'a';
const char dirRightChar = 'd';
enum eDirection {
    STOP=0,
    UP,
    DOWN,
    LEFT,
    RIGHT,
};
eDirection snakeDirection;

void Setup(){
    gameOver=false;
    snakeDirection = STOP;
    snakeX = width / 2;
    snakeY = height / 2;
    fruitX = rand() %width;
    fruitY = rand() %height;
}
void Draw(){
    system("CLS");
    for (int row = 0; row < height; row++) {
        for (int column = 0; column < width; column++) {
            if (row == 0 || row == height - 1) {
                cout << wallChar;
            } else if (column == 0 || column == width - 1) {
                cout << wallChar;
            } else if (row == snakeY && column == snakeX) {
                cout << snakeHeadChar;
            } else if (row == fruitY && column == fruitX) {
                cout << fruitChar;
            } else {
                cout << " ";
            }
        }
        cout << endl;
    }
}
void Input(){
    if (_kbhit()) {
        switch(_getch()) {
        case dirUpChar:
            snakeDirection = UP;
            break;
        case dirDownChar:
            snakeDirection = DOWN;
            break;
        case dirLeftChar:
            snakeDirection = LEFT;
            break;
        case dirRightChar:
            snakeDirection = RIGHT;
            break;
        default:
            break;
        }
    }
}
void Logic(){
    switch(snakeDirection) {
        case UP:
            snakeY--;
            break;
        case DOWN:
            snakeY++;
            break;
        case LEFT:
            snakeX--;
            break;
        case RIGHT:
            snakeX++;
            break;
        default:
            break;
    }
}

int main(){
    Setup();
    while (!gameOver){
        Draw();
        Input();
        Logic();
        Sleep(40);
    }
    return 0;
}

