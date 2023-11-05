// required header file 
#include <conio.h>
#include <iostream>
#include <windows.h>

using namespace std;

bool gameOver;
const char wallChar = '#';
const char snakeHeadChar = 'O';
const char snakeTailChar = 'o';
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
int tailX[100], tailY[100], nTail;
eDirection snakeDirection;

void Setup(){
    gameOver=false;
    snakeDirection = STOP;
    snakeX = boardWidth / 2;
    snakeY = boardHeight / 2;
    fruitX = (rand() % (boardWidth - 1)) + 1;
    fruitY = (rand() % (boardHeight - 1)) + 1;
}

void Draw(){
    system("CLS");
    for (int row = 0; row <= boardHeight; row++) {
        for (int column = 0; column <= boardWidth; column++) {
            if (row == 0 || row == boardHeight) {
                cout << wallChar;
            } else if (column == 0 || column == boardWidth) {
                cout << wallChar;
            } else if (row == snakeY && column == snakeX) {
                cout << snakeHeadChar;
            } else if (row == fruitY && column == fruitX) {
                cout << fruitChar;
            } else {
                bool tailSpace = false;
                for (int k = 0; k < nTail; k++) {
                    if (row == tailY[k] && column == tailX[k]) {
                        cout << snakeTailChar;
                        tailSpace = true;
                    }
                }
                if (!tailSpace) {
                    cout << " ";
                }
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
    int prevX = tailX[0];
    int prevY = tailY[0];
    tailX[0] = snakeX;
    tailY[0] = snakeY;
    int prevX2, prevY2;
    
    for (int i = 1; i < nTail; i++) {
        prevX2 = tailX[i];
        prevY2 = tailY[i];
        tailX[i] = prevX;
        tailY[i] = prevY;
        prevX = prevX2;
        prevY = prevY2;
    }
    
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
    
    if (
        snakeX <= 0 ||
        snakeX >= boardWidth ||
        snakeY <= 0 ||
        snakeY >= boardHeight
    ) {
        gameOver = true;
    } else if (snakeX == fruitX && snakeY == fruitY) {
        nTail += 1;
        score += 10;
        fruitX = (rand() % (boardWidth - 1)) + 1;
        fruitY = (rand() % (boardHeight - 1)) + 1;
    } else {
        for (int i = 0; i < nTail; i++) {
            if (snakeX == tailX[i] && snakeY == tailY[i]) {
                gameOver = true;
            }
        }
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

