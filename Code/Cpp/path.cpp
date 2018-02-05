// g++ -o a.out path.cpp tree.cpp

#include <iostream>
#include "tree.h"

using namespace std;

bool path(bin_node * a, bin_node * b){
  if(a == 0){
    return false;
  }
  if(a == b){
    return true;
  }else{
    return path(a->left, b) || path(a->right, b);
  }
}

int main(){

  bin_node * root = new bin_node (10);
  bin_node * add = new bin_node (5);
  bin_node * hold = add;
  root->add(add);
  add = new bin_node (15);
  root->add(add);

  for(int i = 1; i<20; i++){
    add = new bin_node (i);
    root->add(add);
  }

  cout << "path from root to right: " << path(root, add) << "\n";
  cout << "path from right to root: " << path(add, root) << "\n";
  cout << "path from left to right: " << path(hold, add) << "\n";
  cout << "path from root to left: " << path(root, hold) << "\n";

}

