#include <iostream>
#include "tree.h"

using namespace std;

  bin_node::bin_node(int i){
    obj = i;
    left = 0;
    right = 0;
  }

  void bin_node::add(bin_node *n){
    if(n->obj < obj){
      if(left==0){
	left = n;
	n->up = this;
      }else{
      left->add(n);
      }
    }else{
      if(right==0){
	right = n;
	n->up = this;
      }else{
      right->add(n);
      }
    }
  }

  void bin_node::print(void){
    cout << obj << "\n";
    if(left==0){
      cout << "-L\n";
    }else{
      left->print();
    }
    if(right==0){
      cout << "-R\n";
    }else{
      right->print();
    }    
  }

  bin_node * bin_node::depth(bin_node *n){
    if(left != 0){
       n->left = new bin_node (n->obj+1);
       left->depth(n->left);
    }
    if(right != 0){
       n->right = new bin_node (n->obj+1);
       right->depth(n->right);
    }
    return n;
  }

int max_depth(bin_node *n){
  if(n->left == 0 && n->right == 0){
    return n->obj;
  }
  if(n->left == 0){
    return max_depth(n->right);
  }
  if(n->right == 0){
    return max_depth(n->left);
  }
  int maxL = max_depth(n->left);
  int maxR = max_depth(n->right);
  if(maxL > maxR){
    return maxL;
  }else{
    return maxR;
  }
}

bin_node * div_n_conqr(int a[], int strt, int end, bin_node * n){

  int middle = strt+(end-strt)/2;
  if(middle<strt || middle > end || strt > end){return 0;}
  if(n==0){
    bin_node * root = new bin_node (a[middle]);
    root->print();
    div_n_conqr(a, strt, middle-1, root);
    div_n_conqr(a, middle+1, end, root);
    return root;
  }else{
    if(strt == end){
      bin_node * node = new bin_node (a[strt]);
      n->add(node);
    }else
    if(strt == middle){
      bin_node * node = new bin_node (a[middle]);
      n->add(node);
      div_n_conqr(a, middle+1, end, n);
    }else
    if(end == middle){
      bin_node * node = new bin_node (a[middle]);
      n->add(node);
      div_n_conqr(a, strt, middle-1, n);
    }else{
    bin_node * node = new bin_node (a[middle]);
    n->add(node);
    div_n_conqr(a, strt, middle-1, n);
    div_n_conqr(a, middle+1, end, n);
    }
  }
}
