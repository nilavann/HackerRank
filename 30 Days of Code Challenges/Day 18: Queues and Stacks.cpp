#include <iostream>

using namespace std;

class Solution {
    //Write your code here
    private:
        char stack[100],queue[1000];
        int top,start,end;
    public:
    Solution(){
        this->top=-1;
        this->start=-1;
        this->end=-1;
    }
    void pushCharacter(char ch){
        top++;
        stack[top]=ch;
    }
    void enqueueCharacter(char ch){
        end++;
        queue[end]=ch;
    }
    char popCharacter(){
        return stack[top--];
    }
    char dequeueCharacter(){
        start++;
        return queue[start];
    }
};