
class Q(object):

    def __init__(self):
        self.mode = 'in'
        self.q = {'in': [], 'out': []}

    def flip(self):
        if self.mode == 'in':
            self.q['out'] = self.q[self.mode][-1::-1]
            self.q[self.mode] = []
            self.mode = 'out'    
        else:
            self.q['in'] = self.q[self.mode][-1::-1]
            self.q[self.mode] = []
            self.mode = 'in'
        
    def ssq_push(self, obj):
        if self.mode == 'in':
            self.q[self.mode].append(obj)
        else:
            self.flip()
            self.q[self.mode].append(obj)

    def ssq_exit(self):
        if self.mode == 'out':
            return self.q[self.mode].pop()
        else:
            self.flip()
            return self.q[self.mode].pop()

    def ssq_peek(self):
        if self.mode == 'out':
            return self.q[self.mode][-1]
        else:
            self.flip()
            return self.q[self.mode][-1]

class shelter(object):

    def __init__ (self):
        self.dogs = Q()
        self.cats = Q()
        self.date = 0

    def add_dog(self):
        self.dogs.ssq_push(('d',self.date))
        self.date+=1

    def get_dog(self):
        return self.dogs.ssq_exit()

    def add_cat(self):
        self.cats.ssq_push(('c',self.date))
        self.date+=1

    def get_cat(self):
        return self.cats.ssq_exit()

    def get_(self):
        if self.cats.ssq_peek()[1] < self.dogs.ssq_peek()[1]:
            return self.cats.ssq_exit()
        else:
            return self.dogs.ssq_exit()

