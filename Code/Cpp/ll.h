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


void print(ll_node n);
ll_node * dup(ll_node * n);
bool eql(ll_node a, ll_node b);
ll_node * rev(ll_node * &n);

