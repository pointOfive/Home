//g++ -o a.out circ.cpp ll.cpp

#include <iostream>
#include "ll.h"

using namespace std;

ll_node * find_circ(ll_node * n){
  ll_node * r = n->give_node();
  if(r==0){return 0;}
  n = n->give_node()->give_node();
  
  while(n != 0){
    if(r==n){return n;}
    r = r->give_node();
    n = n->give_node();
    if(n==0){return 0;}
    n =	n->give_node();
  }
  return 0;
}

int main(){

  ll_node a ('a');
  ll_node b ('b');
  a.point_to(&b);
  ll_node c ('c');
  b.point_to(&c);
  ll_node d ('b');//d
  c.point_to(&d);
  ll_node e ('a');
  d.point_to(&b);
  // d.point_to(&e);  

  cout << (&b == d.give_node()) << "\n";  
  print(find_circ(&a)->give_obj());

  return 0;
}
