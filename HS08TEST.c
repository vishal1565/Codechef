#include<stdio.h>
#include<stdlib.h>

int main()
{
	int x;float y;
	scanf("%d%f",&x,&y);
	if(x>0&&x<=2000&&y>=0&&y<=2000&&x%5==0&&y>(x+0.5)){
	y=y-x-0.5;
	printf("%.2f",y);}
	else printf("%.2f",y);
	return 0;
} 
