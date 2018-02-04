// g++ -o a.out uniqueChars.cpp stringBuffer.cpp

#include <iostream>
#include "stringBuffer.h"

using namespace std;

int main(){

  string_buffer sb (10);
  
  sb.append("abcdefG", 7);
  cout << sb.get_char_array() << "\n";
  cout << "is unique: " << sb.unique_chars() << "\n";
  sb.append('c');  
  cout << sb.get_char_array() << "\n";
  cout << "is unique: " << sb.unique_chars() << "\n";

  return 0;
}
