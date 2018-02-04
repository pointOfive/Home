//g++ -o a.out pali.cpp ll.cpp

#include <iostream>
#include "ll.h"

using namespace std;


int kth_from_end(ll_node * &n, int k){
  if(n->give_node() == 0){
    return(k);
  }
  ll_node * nn = n;
  n = n->give_node();
  k = kth_from_end(n, k);
  k--;
  if(1 == k){
    n = nn;
    return 1;
  }else{
    return(k);
  }
}

bool pali(ll_node * n){
  ll_node * e = n;
  int k = 1;
  int k2 = kth_from_end(e, k);
  while(k > k2){
    if(e->give_obj() != n->give_obj()){
      return false;
    }
    k++;
    n = n->give_node();
    k2 = kth_from_end(e, k);
  }
  return true;
}


int main(){

  ll_node a ('a');
  ll_node b ('b');
  ll_node c ('c');
  ll_node d ('b');
  ll_node e ('a');
  a.point_to(&b);
  b.point_to(&c);
  c.point_to(&d);
  d.point_to(&e);

  print(a);
  ll_node * n = &a;
  kth_from_end(n, 4);
  cout << "4th from end " << n->give_obj()  << "\n";
  
  print(a);
  cout << "Pali? " << pali(&a) << "\n";
  a.set_obj('b');
  print(a);
  cout << "Pali? " << pali(&a) << "\n";
  a.set_obj('a');
  
  n = dup(&a);
  rev(n);
  print(*n);
  cout << "Pali? " << eql(a, *n) << "\n";

  return 0;
}
