#include <stdio.h>
#include <windows.h>
#include <conio.h>
int main()
{
  HANDLE hout = GetStdHandle(STD_OUTPUT_HANDLE);
  COORD Pos;
  Pos.X = 68;
  Pos.Y = 12;
  SetConsoleCursorPosition(hout, Pos);
  printf("*");
  int num_i_left = 11;
  int num_j_up = 11;
  int num_i_right = 69;
  int num_j_down = 13;
  for (int k = 0; k < 12; k++)
  {
    for (int i = Pos.X; i > num_i_left; i--)
    {
      Pos.X -= 1;
      SetConsoleCursorPosition(hout, Pos);
      printf("*");
      Sleep(1);
    }
    num_i_left--;
    for (int j = Pos.Y; j > num_j_up; j--)
    {
      Pos.Y -= 1;
      SetConsoleCursorPosition(hout, Pos);
      printf("*");
      Sleep(1);
    }
    num_j_up--;
    if (Pos.X != 0)
    {
      for (int i = Pos.X; i < num_i_right; i++)
      {
        Pos.X += 1;
        SetConsoleCursorPosition(hout, Pos);
        printf("*");
        Sleep(1);
      }
      num_i_right++;
    }
    else
    {
      for (int i = 0; i < 79; i++)
      {
        printf("*");
        Sleep(1);
      }
    }
    if (num_j_down != 24)
    {
      for (int j = Pos.Y; j < num_j_down; j++)
      {
        Pos.Y += 1;
        SetConsoleCursorPosition(hout, Pos);
        printf("*");
        Sleep(1);
      }
      num_j_down++;
    }
    else break;
  }
  getchar();
}
