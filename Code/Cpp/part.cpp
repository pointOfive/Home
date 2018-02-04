//g++ -o a.out part.cpp ll.cpp

#include <iostream>
#include "ll.h"

using namespace std;

ll_node partition(ll_node * n, char part){
  ll_node above ('^');
  ll_node * above_end = &above; 
  ll_node below ('_');
  ll_node * below_end = &below;
  while(n->give_node() !=0){
    if(n->give_obj() <= part){
      below_end->point_to(n);
      below_end = below_end->give_node();
    }else{
      above_end->point_to(n);
      above_end = above_end->give_node();
    }
    n = n->give_node();
  }
  if(n->give_obj() <= part){
    below_end->point_to(n);
    below_end = below_end->give_node();
  }else{
    above_end->point_to(n);
    above_end = above_end->give_node();
  }
  
  above_end->point_to(0);  
  below_end->point_to(above.give_node());
  
  return(*(below.give_node()));
}


int main(){

  ll_node a ('e');
  ll_node b ('d');
  a.point_to(&b);
  ll_node c ('c');
  ll_node d ('b');
  ll_node e ('a');
  b.point_to(&c);
  c.point_to(&d);
  d.point_to(&e);

  print(a);
  ll_node n = partition(&a, 'd');
  print(n);

  return 0;
}
