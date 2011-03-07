'''
Created on Feb 17th, 2011

@author: Zhuiyang Chen
'''
import timeit;
from Node import Node;

initial_depth = 0;
depth_limit = 2;
TEST = False;
MIN = -1000;
MAX = 1000;

initial_state = [
                 ['-', '-', '-'],
                 ['-', '-', '-'],
                 ['-', '-', '-'],
                ];
                

    

if __name__ == '__main__':
    if (not TEST):
        
        root_node = Node(initial_state, 'max', initial_depth, depth_limit);
        root_node.expand();
        
        alphabeta = True;
        v = root_node.max_value(MIN, MAX, alphabeta);
        print "Alpha-Beta: On";
        print v;
        alphabeta = False;
        v = root_node.max_value(MIN, MAX, alphabeta);
        print "Alpha-Beta: Off";
        print v;
        
    else:
        test_state = [
                 ['x', '-', '-'],
                 ['-', 'x', '-'],
                 ['-', '-', 'x'],
                ];
        
        node = Node(test_state);
        assert node.evaluate() == MAX;
        
        test_state = [
                 ['-', '-', 'x'],
                 ['-', 'x', '-'],
                 ['x', '-', '-'],
                ];
        
        node = Node(test_state);
        assert node.evaluate() == MAX;
        
        test_state = [
                 ['x', 'x', 'x'],
                 ['-', '-', '-'],
                 ['-', '-', '-'],
                ];
        node = Node(test_state);
        assert node.evaluate() == MAX;
        
        test_state = [
                 ['x', '-', '-'],
                 ['x', '-', '-'],
                 ['x', '-', '-'],
                ];
        node = Node(test_state);
        assert node.evaluate() == MAX;
        
        test_state = [
                 ['o', '-', '-'],
                 ['-', 'o', '-'],
                 ['-', '-', 'o'],
                ];
        
        node = Node(test_state);
        assert node.evaluate() == MIN;
        
        test_state = [
                 ['-', '-', 'o'],
                 ['-', 'o', '-'],
                 ['o', '-', '-'],
                ];
        
        node = Node(test_state);
        assert node.evaluate() == MIN;
        
        
        test_state = [
                 ['o', 'o', 'o'],
                 ['-', '-', '-'],
                 ['-', '-', '-'],
                ];
        node = Node(test_state);
        assert node.evaluate() == MIN;
        
        test_state = [
                 ['o', '-', '-'],
                 ['o', '-', '-'],
                 ['o', '-', '-'],
                ];
        node = Node(test_state);
        assert node.evaluate() == MIN;
        
        test_state = [
                 ['x', 'x', 'o'],
                 ['-', 'o', '-'],
                 ['-', '-', '-'],
                ];
        node = Node(test_state);
        assert node.evaluate() == 3 * 1 + 2 - (3*1 + 4);