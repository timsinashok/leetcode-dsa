#include <iostream>
using namespace std;

class IntNode{
    private:
    int* next;
    int* prev;
    int elem;

    public:
    IntNode(int* n, int* p, int e);
};

IntNode::IntNode(int* n, int* p, int e){
    this-> next = n;
    this-> prev = p;
    this-> elem = e;
}


class DoublyLinkedList{
    private:
    
    public:
};

int main(){

    return 0;
}