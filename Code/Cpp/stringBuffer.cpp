#include "stringBuffer.h"

  string_buffer::string_buffer(int len_){
    len = len_;
    char_array = new char [len_];
    end = 0;
    char_array[end] = '\0';
  }


  char * string_buffer::get_char_array(void){
    return char_array;
  }

  int string_buffer::get_len(void){
    return len;
  }

  int string_buffer::get_end(void){
    return end;
  }

  void string_buffer::append(char str[], int len_){
    for(int i=0; i<len_; i++){
      append(str[i]);
    }
  }
  
  void string_buffer::append(char c){
    if(end == (len-1)){
      char *tmp = new char [2*len];
      for(int i = 0; i<len; i++){
	tmp[i] = char_array[i];
      }
      //delete[] char_array;
      char_array = tmp;
      len *= 2;
      //delete[] tmp;
    }
    char_array[end++] = c;
    char_array[end] = '\0';
  }

  bool string_buffer::unique_chars(void){
    for(int i = 0; i < (end-1); i++){
      for(int j = i+1; j < end; j++){
	if(char_array[i]==char_array[j]){
	  return false;
        }
      }
    }
    return true;
  }
  
  void string_buffer::rev(void){
    char tmp;
    for(int i = 0; i<(end-1)/2; i++){
      tmp = char_array[i];
      char_array[i] = char_array[end-1-i];
      char_array[end-1-i] = tmp;
    }
  }  


