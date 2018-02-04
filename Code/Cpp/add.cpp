//g++ -o a.out save.cpp ll.cpp

#include <iostream>
#include "ll.h"

using namespace std;

ll_node add(ll_node f1, ll_node s1){

  ll_node * n1 = &f1;
  ll_node * n2 = &s1;
  ll_node result ('$');
  ll_node * runner = &result;
  ll_node * add;
  int add_next = 0;
  char val;
  char tmp1, tmp2;

  val = n1->give_obj()+n2->give_obj()-'0'+add_next;
  if(val>'9'){
    val = val - ':'+'0';
    add_next = 1;
  } 
  add = new ll_node (val);
  runner->point_to(add);
  runner=runner->give_node();

  while(n1->give_node() != n1 or n2->give_node() != n2){
    if(n1->give_node() == n1){tmp1='0';}else{n1=n1->give_node(); tmp1=n1->give_obj();}
    if(n2->give_node() == n2){tmp2='0';}else{n2=n2->give_node(); tmp2=n2->give_obj();}
    val = tmp1+tmp2-'0'+add_next;
    if(val>'9'){
      val = val - ':'+'0';
      add_next = 1;
    }
    add = new ll_node (val);
    runner->point_to(add);
    runner=runner->give_node();
  }
  if(add_next==1){
    add = new ll_node ('1');
    runner->point_to(add);
    runner=runner->give_node();
  }

return result;
}


ll_node * add_rec(ll_node * f1, ll_node * s1){
// MUST 0-pad -- does not currently work if numbers have different lengths...
  // i.e., 100's must enter the same recursive function
  ll_node * n1 = f1;
  ll_node * n2 = s1;
  ll_node * runner;
  int add_next = 0;
  int tmp1, tmp2;
  char val;
  
  if(n1->give_node() == n1 and n2->give_node() == n2){
    val = n1->give_obj() + n2->give_obj()-'0';
    ll_node * add = new ll_node(val);
    return add;
  }
  runner = add_rec(n1->give_node(), n2->give_node());

    if(runner->give_obj()>'9'){
      runner->set_obj(runner->give_obj() - ':'+'0');
      add_next = 1;
    }
    if(n1->give_node() == n1){tmp1='0';}else{tmp1=n1->give_obj();}
    if(n2->give_node() == n2){tmp2='0';}else{tmp2=n2->give_obj();}
    val = tmp1+tmp2-'0'+add_next;
    ll_node * add = new ll_node(val);
    add->point_to(runner);
    return add;
}


int main(){
  
  ll_node f1('4');
  //ll_node f0('3');//
  ll_node f2('5');
  ll_node f3('5');
  f1.point_to(&f2);//2
  //f0.point_to(&f2);//
  f2.point_to(&f3);
  print(f1);
  f3.point_to(&f3);
  
  ll_node s1('3');
  ll_node s2('5');
  ll_node s3('5');
  s1.point_to(&s2);
  s2.point_to(&s3);
  print(s1);
  s3.point_to(&s3);

  cout << "add forward\n";
  print(*add_rec(&f1, &s1));

  cout << "add in reverse\n";
  print(add(f1, s1));
 
  return 0;
}
