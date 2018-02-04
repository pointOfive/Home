//g++ -o a.out dedup.cpp ll.cpp

#include <iostream>
#include "ll.h"

using namespace std;

void drop_match(ll_node * n, char c){
  if(n->give_node()!=0){
    if( n->give_node()->give_obj() == c ){
      n->point_to(n->give_node()->give_node());
        drop_match(n, c);
    }else{
      drop_match(n->give_node(), c);
    }
  }
}
    

int main(){

  ll_node a ('a');
  ll_node b ('b');
  a.point_to(&b);
  ll_node c ('c');
  ll_node d ('b');//d
  ll_node e ('a');//e
  b.point_to(&c);
  c.point_to(&d);
  d.point_to(&e);

  ll_node * n = &a;
  print(a);
  while( n->give_node() != 0 ){
    drop_match(n, n->give_obj());
    n = n->give_node();
    if(n == 0){break;}
  }
  print(a);
  
  return 0;
}
