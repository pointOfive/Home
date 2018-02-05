// g++ -o a.out sum_path.cpp tree.cpp

#include <iostream>
#include "tree.h"

using namespace std;

bin_node * sums_to_val(int val, bin_node * n){
  if(val-n->obj==0){
    cout << n->obj << "\n";
    return n;
  }
  if(val-n->obj<0){
    return 0;
  }
  bin_node * out = sums_to_val(val-n->obj,n->left);
  if(out == 0){return 0;}else
  {
    cout << n->obj << "\n";
    return n;
  }
  out = sums_to_val(val-n->obj,n->right);
  if(out == 0){return 0;}
  {
    cout << n->obj << "\n";
    return n;
  }
}

int main(){

  int strt = 0;
  int len = 9;
  int sorted_list [9] = {1,2,3,4,5,6,7,8,9};
  bin_node * r = div_n_conqr(sorted_list, strt, len-1, 0);

  r->print();

  cout << "Path summing to 8:\n";
  sums_to_val(8, r);

}
