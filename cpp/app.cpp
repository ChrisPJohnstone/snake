// required header file 
#include <conio.h>
#include <iostream>
#include <windows.h>

using namespace std;

bool gameOver;
const char wallChar = '#';
const char snakeHeadChar = '0';
const char fruitChar = 'F';

const int boardHeight = 20;
const int boardWidth = 20;

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

int snakeX, snakeY, fruitX, fruitY, score;
eDirection snakeDirection;

void Setup(){
    gameOver=false;
    snakeDirection = STOP;
    snakeX = boardWidth / 2;
    snakeY = boardHeight / 2;
    fruitX = rand() %boardWidth;
    fruitY = rand() %boardHeight;
}
void Draw(){
    system("CLS");
    for (int row = 0; row < boardHeight; row++) {
        for (int column = 0; column < boardWidth; column++) {
            if (row == 0 || row == boardHeight - 1) {
                cout << wallChar;
            } else if (column == 0 || column == boardWidth - 1) {
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

