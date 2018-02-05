class bin_node {

public:
  
  int obj;
  bin_node * left;
  bin_node * right;
  bin_node * up;
  
  bin_node(int i);
  void add(bin_node *n);
  void print(void);
  bin_node * depth(bin_node *n);

};

int max_depth(bin_node *n);
bin_node * div_n_conqr(int a[], int strt, int end, bin_node * n);

