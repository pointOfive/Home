// g++ -o a.out perm.cpp stringBuffer.cpp

#include <iostream>
#include "stringBuffer.h"

using namespace std;

bool perm(string_buffer a, int len_a, string_buffer b, int len_b){
  char * aa = a.get_char_array();
  char * bb = b.get_char_array();
  int matches_a, matches_b;
  
  if(len_a != len_b){return false;}
  for(int i = 0; i<len_a; i++){
    matches_a = 0;
    matches_b = 0;
    
    for(int j=0; j<len_a; j++){
      if(aa[i]==aa[j]){matches_a++;}
      if(aa[i]==bb[j]){matches_b++;}
    }
    
    if(matches_a != matches_b){return false;}
  }
  return true;
}

int main(){

  string_buffer sb (10);
  string_buffer sb2 (10);
  string_buffer sb3 (10);
  for(int i=65; i<69; i++){
    sb.append(char(i));
    sb.append(char(i));
    sb.append(char(i));
    sb2.append(char(i+20)); 
  }

  cout << sb.get_char_array() << "\n";
  cout << sb2.get_char_array() << "\n";
  cout << "perm? " << perm(sb,sb.get_end(),sb2,sb2.get_end()) << "\n";

  sb3.append(sb.get_char_array(),sb.get_end());
  sb.rev();
  cout << sb.get_char_array() << "\n";
  cout << sb3.get_char_array() << "\n";
  cout << "perm? " << perm(sb,sb.get_end(),sb3,sb3.get_end()) << "\n";
    
  return 0;
}
