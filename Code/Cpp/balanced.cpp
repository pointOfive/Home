// g++ -o a.out balanced.cpp tree.cpp

#include <iostream>
#include "tree.h"

using namespace std;

bool bal(bin_node *n){

  if(n->left == 0 && n->right == 0){
    return true;
  }
  
  if(n->left == 0 && (max_depth(n->right) - n->obj) == 1){
    return true;
  }
  
  if(n->right == 0 && (max_depth(n->left) - n->obj) == 1){
    return true;
  }

  if(n->left != 0 && n->right != 0){
    return (bal(n->right) && bal(n->left));
  }
  
  return false;
}



int main(){

  int strt = 0;
  int len = 9;
  int sorted_list [9] = {1,2,3,4,5,6,7,8,9};
  bin_node * r = div_n_conqr(sorted_list, strt, len-1, 0);

  r->print();
  cout << "max depth: " << max_depth(r) << "\n";
  cout << "balaned? " << bal(r) << "\n";
  
  bin_node * root = new bin_node (10);
  bin_node * add = new bin_node (5);
  root->add(add);
  add = new bin_node (15);
  root->add(add);
  for(int i = 1; i<20; i++){
    add = new bin_node (i);
    root->add(add);
  }

  root->print();
  cout << "max depth: " << max_depth(root) << "\n";
  cout << "balaned? " << bal(root) << "\n";
    
  return 0;
}
