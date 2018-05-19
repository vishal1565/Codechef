#include<stdio.h>
#include<stdlib.h>

int main()
{
	int t,a,b,c;
	scanf("%d",&t);
	while(t!=0)
	{
		scanf("%d%d",&a,&b);
		c=(a+b)%10;
		printf("\n%d",c);
		t--;
	}
	return 0;
}
