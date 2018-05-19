#include<bits/stdc++.h>
using namespace std;

int euclid(int m,int n);
int gcd(int nos[],int l);

int main(){
  int t,n,a[1000];
  int g;
  int count;
  cin>>t;
  while(t--){
    count=0;
    cin>>n;
    for(int i=0;i<n;i++){
      cin>>a[i];
    }
    g=gcd(a,n);
    if(g!=1){
      for(int i=0;i<n;i++){
        if(a[i]%g==0){
          count++;
          if(count==n){
            cout<<"-1"<<endl;
          }

        }
        else{
          cout<<count<<endl;
        }

      }
    }
    else{
      cout<<"0"<<endl;
    }
  }
  return 0;
}


int euclid(int m,int n){
  int temp=0;
  while(n!=0){
    temp=n;
    n=m%n;
    m=temp;
  }
  m=m<0 ? m *(-1):m;
  return m;
}

int gcd(int nos[],int l){
  int g=1;
  int flag=2;
  if(l==1){
    g=nos[1];
  }
  if(l>1){
    g=euclid(nos[0],nos[1]);
  }
  while(flag<l){
    g=euclid(g,nos[flag]);
    flag++;
  }
  return g;
}
