#include<stdio.h>
#include<stdlib.h>

int main()
{
	int t,a,b,rem;
	scanf("%d",&t);
	while(t!=0){
	scanf("%d%d",&a,&b);
	rem=a%b;printf("\n%d",rem);
	t--;}
	return 0;
}
