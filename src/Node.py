'''
Created on Feb 17, 2011

@author: Zhuiyang Chen
'''
import copy;
MIN = -1000;
MAX = 1000;

class Node(object):
    '''
    contains a tic tac toe board with pointer to parent and children to allow easy traversal of the tree
    '''
    MAX = 1000;
    MIN = -1000;
    def __init__(self, state, minmax = 'max', depth = 0, depth_limit = 0):
        '''
        Constructor
        '''
        # pointer to parent
        self.parent = None;
        # pointer to children
        self.children = [];
        # 2 dim array holding game state, - represents empty square
        self.state = copy.deepcopy(state);
        # contains x for max o for min
        self.minmax = minmax;
        
        # set terminal boolean according if evaluation function shows win or loss
        self.depth = depth;
        self.depth_limit = depth_limit;
        
        if (self.terminal_test()):
            self.terminal = True;
        else:
            self.terminal = False;
        
        
    def max_value(self, a, b, alphabeta = True):
        if (self.terminal):
            return self.evaluate();
        
        v = MIN;
        
        for child in self.children:
            v = max([v, child.min_value(a, b, alphabeta)]);
            if (alphabeta):
                if v >= b:
                    return v;
            a = max([a, v]);
        return v;
    
    def min_value(self, a, b, alphabeta = True):
        if (self.terminal):
            return self.evaluate();
         
        v = MAX;
        
        for child in self.children:
            v = min([v, child.max_value(a, b, alphabeta)]);
            if (alphabeta):
                if v <= a:
                    return v;
            b = min([b, v]);
        return v;
            
    def terminal_test(self, terminal_test = False):
        # check win/loss condition
        terminal_test = True;
        if (self.evaluate(terminal_test)):
            return True;
        
        # check if depth limit has been hit
        if (self.depth_limit > 0 and (self.depth == self.depth_limit)):
            return True;
            
        
    def evaluate(self, terminal_test = False):
        x3 = x2 = x1 = o3 = o2 = o1 = 0;
        
        counts = {
            'x_row': [0, 0, 0],
            'o_row': [0, 0, 0],
            'x_col': [0, 0, 0],
            'o_col': [0, 0, 0],
            'x_dag': [0, 0],
            'o_dag': [0, 0],
        };
        # count rows
        for i in range(0, len(self.state)):
            for j in range(0, len(self.state[i])):
                if (self.state[i][j] == 'x'):
                    counts['x_row'][i] = counts['x_row'][i] + 1;
                    counts['x_col'][j] = counts['x_col'][j] + 1;
                    
                    #count diagonals
                    if (i == j):
                        counts['x_dag'][0] = counts['x_dag'][0] + 1;
                    if (i == abs(j - (len(self.state)-1))):
                        counts['x_dag'][1] = counts['x_dag'][1] + 1;
                elif(self.state[i][j] == 'o'):
                    counts['o_row'][i] = counts['o_row'][i] + 1;
                    counts['o_col'][j] = counts['o_col'][j] + 1;
                    
                    #count diagonals
                    if (i == j):
                        counts['o_dag'][0] = counts['o_dag'][0] + 1;
                    if (i == abs(j - (len(self.state)-1))):
                        counts['o_dag'][1] = counts['o_dag'][1] + 1;
        
        for k, v in counts.items():
            type = k[0:1];
            for value in v:
                if (type == 'x'):
                    if (value == 3):
                        x3 = x3 + 1;
                    elif (value == 2):
                        x2 = x2 + 1;
                    elif (value == 1):
                        x1 = x1 + 1;
                        
                if (type == 'o'):
                    if (value == 3):
                        o3 = o3 + 1;
                    elif (value == 2):
                        o2 = o2 + 1;
                    elif (value == 1):
                        o1 = o1 + 1;
                 
        
        if (x3 > 0):
            if (terminal_test):
                return True;
            else:
                return MAX;
        if (o3 > 0):
            if (terminal_test):
                return True;
            else:
                return MIN;
        else:
            if (terminal_test):
                return False;
            else:
                return 3*x2 + x1 - (3*o2 + o1);
    
    def expand(self):
        if (self.depth_limit > self.depth+1 or self.depth_limit == 0):
            expand = True;
        else:
            expand = False;
        for i in range(0, len(self.state)):
            for j in range(0, len(self.state[i])):
                if (self.state[i][j] == '-'):
                    
                    # setup new child node
                    if (self.minmax == 'max'):
                        child_node = Node(self.state, 'min', self.depth+1, self.depth_limit);
                        child_node.state[i][j] = 'x';
                    elif(self.minmax == 'min'):
                        child_node = Node(self.state, 'max', self.depth+1, self.depth_limit);
                        child_node.state[i][j] = 'o';
                    
                    # set up parent child relationship with child node
                    child_node.parent = self;
                    self.children.append(child_node);
                    
                    # further expand the tree if depth limit not reached and game has not reached terminal state
                    if (expand and (not child_node.terminal)):
                        child_node.expand();
        
    
    def __str__(self):
        return self._string_representation();
    def __repr__(self):
        return self._string_representation();
    
    def _string_representation(self):
        for row in self.state:
            print row;
        return "";