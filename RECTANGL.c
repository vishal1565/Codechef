#include<stdio.h>
#include<stdlib.h>

 int main()
 {
   int t,side[4];
   int cmpfunc (const void * a, const void * b) {
   return ( *(int*)a - *(int*)b );
   }
   scanf("%d",&t);
   while(t!=0)
   {
     scanf("%d%d%d%d",&side[0],&side[1],&side[2],&side[3]);
     qsort(side, 4, sizeof(int), cmpfunc);
     if(side[0]==side[1]&&side[2]==side[3])
     {
       printf("YES\n");
     }
     else
     {
       printf("NO\n");
     }
     t--;
   }
   return 0;
 }
