// g++ -o a.out compress.cpp stringBuffer.cpp

#include <iostream>
#include "stringBuffer.h"

using namespace std;

string_buffer compress(string_buffer a){
  string_buffer b = a;
  char * c = b.get_char_array();

  int j, dup;
  int i = 0;
  while(i<a.get_end()){
    j = i+1;
    dup=1;
    while(c[i]==c[j]){
      dup++;
      j++;
    }
    if(dup>1){
      c[i+1]= char(48+dup);
      i+=2;
    }
    if(dup>2){
      for(int k = i; k<=a.get_end(); k++){
	c[k] = c[k+dup-2];
      }
      a.end = a.get_end() - dup + 2;
    }
  }
  return b;
}

int main(){

  string_buffer sb (10);
  
  for(int i=65; i<69; i++){
    sb.append(char(i));
    sb.append(char(i));
    sb.append(char(i));
  }

  cout << sb.get_char_array() << "\n";
  cout << compress(sb).get_char_array() << "\n";
      
  return 0;
}
