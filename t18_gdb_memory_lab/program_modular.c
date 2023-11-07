#include <stdio.h>
#include <stdlib.h>

int add2sub1(int a, int b, int c) {
  int d = a + b - c;
  return d;
}

int main(int argc, char* argv[]) {
  int x, y, z, r;  
  printf("program to compute r = x + y - z\n");
  x = 4;
  y = 8;
  z = 2;
  r = add2sub1(x,y,z);
  printf("r = %d\n", r);
  exit(0);
}

