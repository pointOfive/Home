// g++ -o a.out next.cpp tree.cpp

#include <iostream>
#include "tree.h"

using namespace std;

int next_up(bin_node * n){
  int obj = n->obj;
  if(n->right==0 && n->up==0){
    return -1;
  }else
  if(n->right!=0){
    n = n->right;
    while(n->left != 0){
      n = n->left;
    }
    return n->obj;
  }
  if(n->up->obj < obj){
    return -1;
  }
  n = n->up;
  while(n->obj < obj){
    n = n->up;
  }
  return n->obj;
}

int main(){

  int strt = 0;
  int len = 9;
  int sorted_list [9] = {1,2,3,4,5,6,7,8,9};
  bin_node * r = div_n_conqr(sorted_list, strt, len-1, 0);
  r->print();

  cout << "\n" << r->right->obj << "\n" << next_up(r->right);
  
  return 0;
}
