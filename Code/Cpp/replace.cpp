// g++ -o a.out replace.cpp stringBuffer.cpp

#include <iostream>
#include "stringBuffer.h"

using namespace std;

void replace(string_buffer a, char find, string_buffer r){
  char * aa = a.get_char_array();
  char * rr = r.get_char_array();

  for(int c = 0; c<a.get_end(); c++){
    if(aa[c] == find){
      for(int k = a.get_end()+r.get_end()-1; k>(c+r.get_end()-1); k--){
	aa[k] = aa[k-r.get_end()+1];	
      }
      a.end=a.get_end()+r.get_end()-1;
      for(int i = 0; i<r.get_end(); i++){
	aa[i+c] = rr[i];
      }
      c = c + r.get_end() - 1;
    }      
  }
}

int main(){

  string_buffer sb (10);

  for(int i=65; i<69; i++){
    sb.append(char(i));
    sb.append(char(i));
    sb.append(char(i));
  }

  string_buffer sb3 (10);
  char under = '_';
  sb3.append(under);
  sb3.append(under);
  sb3.append(under);

  cout << sb.get_char_array() << "\n";
  replace(sb, 'B', sb3);
  cout << sb.get_char_array() << "\n";
  
  return 0;
}
