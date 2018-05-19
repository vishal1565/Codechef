#include<iostream>
using namespace std;
int main(){
  int cse=0,mech=0,temp;
  for(int i=0;i<7;i++){
    cin>>temp;
    cse+=temp;
  }
  for(int i=0;i<7;i++){
    cin>>temp;
    mech+=temp;
  }
  if(cse>mech){cout<<"cse"<<endl;}
  else if(cse<mech){cout<<"mech"<<endl;}
  else{cout<<"draw"<<endl;}
  return 0;
}
