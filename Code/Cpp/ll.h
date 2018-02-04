class ll_node {

  char obj;
  ll_node * next;

public:

  ll_node(char v);
  char give_obj(void);
  void set_obj(char c);
  ll_node * give_node(void);
  void point_to(ll_node * n);
};

