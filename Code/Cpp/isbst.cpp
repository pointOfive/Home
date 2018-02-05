// g++ -o a.out balanced.cpp tree.cpp

#include <iostream>
#include "tree.h"

using namespace std;


bool check_bin_search(bin_node * n){
  if(n->left == 0 && n->right == 0){
    return true;
  }
  if(n->left == 0 && n->right != 0){
    return n->right->obj > n->obj && check_bin_search(n->right);
  }
  if(n->left != 0 && n->right == 0){
    return n->left->obj < n->obj && check_bin_search(n->left);
  }
  if(n->left->obj > n->obj || n->right->obj < n->obj){
    return false;
  }
  return check_bin_search(n->left) && check_bin_search(n->right);
}


int main(){

  int strt = 0;
  int len = 9;
  int sorted_list [9] = {1,2,3,4,5,6,7,8,9};
  bin_node * r = div_n_conqr(sorted_list, strt, len-1, 0);

  r->print();
  cout << "is bst? " << check_bin_search(r) << "\n";
  
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
  cout << "is bst? " << check_bin_search(root) << "\n";
    
  return 0;
}
