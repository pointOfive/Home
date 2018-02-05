// g++ -o a.out ancestors.cpp tree.cpp

#include <iostream>
#include "tree.h"

using namespace std;


bool is_ancestor(bin_node * check, bin_node * n1){
  if(check == n1){
    return true;
  }else
  if(check->left !=0 && check->right !=0){
    return is_ancestor(check->left, n1) || is_ancestor(check->right, n1);
  }else
  if(check->left !=0){
    return is_ancestor(check->left, n1);
  }else
  if(check->right !=0){
    return is_ancestor(check->right, n1);
  }else{
    return false;
  }
}

bin_node * lcd(bin_node * check, bin_node * n1, bin_node * n2){
  if(is_ancestor(check->left, n1)&&is_ancestor(check->left, n2)){
    return lcd(check->left, n1, n2);
  }
  if(is_ancestor(check->right, n1)&&is_ancestor(check->right, n2)){
    return lcd(check->right, n1, n2);
  }
  return check;
}

int main(){

  int strt = 0;
  int len = 9;
  int sorted_list [9] = {1,2,3,4,5,6,7,8,9};
  bin_node * r = div_n_conqr(sorted_list, strt, len-1, 0);

  r->print();


  cout << "\nright: " << r->right->obj << " right right: " << r->right->right->obj << "\n";
  cout << "closest shared ancestor: " << lcd(r, r->right, r->right->right)->obj << "\n";

  cout << "\nright left: " << r->right->left->obj << " right right: " << r->right->right->obj << "\n";
  cout << "closest shared ancestor: " << lcd(r, r->right->left, r->right->right)->obj << "\n";  

}
