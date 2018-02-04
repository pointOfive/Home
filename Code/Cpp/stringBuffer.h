class string_buffer {

  char * char_array;
  
public:
  int len, end;
  string_buffer(int);

  char * get_char_array(void);
  int get_len(void);
  int get_end(void);
  void append(char str[], int len_);
  void append(char c);
  bool unique_chars(void);
  void rev(void);
};


