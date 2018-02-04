#include <iostream>
#include "ll.h"

using namespace std;

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


void print(ll_node n){
  cout << n.give_obj() << " ";
  while(n.give_node() != 0){
    n = *(n.give_node());
    cout << n.give_obj() << " ";
  }
  cout << "\n";
}

ll_node * dup(ll_node * n){
  ll_node * nn = new ll_node (n->give_obj());
  if(n->give_node()!=0){
  nn->point_to(dup(n->give_node()));
  }
  return nn;
}

bool eql(ll_node a, ll_node b){
  while(a.give_obj()==b.give_obj()){
    if(a.give_node()==0 && a.give_node()==0){
      return true;
    }
    a=*a.give_node();
    b=*b.give_node();
  }
  return false;
}

ll_node * rev(ll_node * &n){
  ll_node * local_n = n;
  if(local_n->give_node()==0){
    return local_n;
  }
  n = n->give_node();
  ll_node * next = rev(n);
  local_n->point_to(next->give_node());
  next->point_to(local_n);
  return local_n;
}

