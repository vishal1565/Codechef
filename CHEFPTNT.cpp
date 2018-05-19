#include<iostream>

using namespace std;

int min(int a,int b){
    if(a<=b){return a;}
    else{return b;}
}
int main(){
  int t,n,m,x,K,e,o,*output;
  string s;
  cin >> t;
  output=new int[t];
  for(int i=0;i<t;i++){
    e = 0;
    o = 0;
    cin>>n;
    cin>>m;
    cin>>x;
    cin>>K;
    cin>>s;
    if(n>K){
      output[i] = 0;
      continue;
    }
    for(int j=0;s[j]!=NULL;j++){
      if(s[j]=='E')
        e++;
      else
        o++;
    }
    for(int k=1;k<=m;k++){
      if(k%2==1&&o>0){
        n-=min(x,o);
        o-=x;
      }
      else if(k%2==0&&e>0){
        n-=min(x,e);
        e-=x;
      }
    }
    if(n<=0){
      output[i]=1;
    }
    else{
      output[i]=0;
    }
  }
  for(int i=0;i<t;i++){
    if(output[i]==1)
      cout<<"yes"<<endl;
    else
      cout<<"no"<<endl;
  }
}
