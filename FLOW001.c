#include<stdio.h>
#include<stdlib.h>

int main()
{
	int t,a,b,sum;
	scanf("%d",&t);
	while(t!=0){
	scanf("%d%d",&a,&b);
	sum=a+b;printf("\n%d",sum);
	t--;}
	return 0;
}
