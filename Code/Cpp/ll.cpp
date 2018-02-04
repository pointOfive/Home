#include "ll.h"

  ll_node::ll_node(char v){
    obj = v;
    next = 0;
  }
  
  char ll_node::give_obj(void){
    return obj;
  }

  void ll_node::set_obj(char c){
    obj = c;
  }

  ll_node * ll_node::give_node(void){
    return next;
  }

  void ll_node::point_to(ll_node * n){
    next = n;
  }


