// g++ -o a.out tree2ll.cpp tree.cpp

#include <iostream>
#include "tree.h"

using namespace std;



void tree2ll(bin_node * n, bin_node * ll_tree, int level){
  if(n==0){
    ll_tree->right = 0;
  }else{
    bin_node * ll_node = new bin_node (level);
    ll_node->left = n;
    ll_tree->right = ll_node;
    tree2ll(n->left, ll_node, level+1); 

    while(ll_node->right != 0){ll_node = ll_node->right;}
    tree2ll(n->right, ll_node, level+1);
  }
}


int main(){

  int strt = 0;
  int len = 9;
  int sorted_list [9] = {1,2,3,4,5,6,7,8,9};

  bin_node * r = div_n_conqr(sorted_list, strt, len-1, 0);
  r->print();
  
  bin_node * l = new bin_node (0);
  tree2ll(r, l, 1);
  for(int i = 1; i<=max_depth(r); i++){
    r = l->right;
    while(r->right!=0){
      if(r->obj==i){
	cout << r->obj << ": " << r->left->obj << "\n";
      }
      r = r->right;
    }
  }

  return 0;
}
