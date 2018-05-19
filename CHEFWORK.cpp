#include<iostream>
#include<algorithm>
using namespace std;
int main(){
  int n;
  cin>>n;
  long int coin[n],type[n],res;
  long long int author=1000000000,translater=1000000000,both=1000000000;
  for(int i=0;i<n;i++){
    cin>>coin[i];
  }
  for(int i=0;i<n;i++){
    cin>>type[i];}
    for(int i=0; i<n; i++)
    {
       if(type[i]==1)
       {
         if(author > coin[i])
         author=coin[i];
       }
       else if(type[i]==2)
       {
         if(translater > coin[i])
         translater=coin[i];
       }
       else
       {
         if(both > coin[i])
         both=coin[i];
       }
  }
  res=author+translater;
  if(res<both){cout<<res;}
  else{cout<<both;}
  return 0;
}
