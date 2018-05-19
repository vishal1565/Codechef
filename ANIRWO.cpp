#include<iostream>
#include<string>
using namespace std;
int main(){
  int t;
  cin>>t;
  while(t--){
    string str,res;
   // char res[1000];
    cin>>str;
    for(int i=0;i<str.length();i++){
      cout<<char(97+'z'-str[i]);
    }
    cout<<endl;
  }
  return 0;
} 
