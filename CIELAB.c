#include<stdio.h>
#include<stdlib.h>

int main()
{
  int a,b;
  scanf("%d%d",&a,&b);
  b=a-b;
  if(b%10<9)
  {
    b++;
  }
  else
  {
    b--;
  }
  printf("%d\n",b);
}
