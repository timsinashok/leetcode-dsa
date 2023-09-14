#include <iostream>

using namespace std;

class Node{
    public:
    int value;
    int* next;
    
    Node(int value){}        
};


class LinkedList{
    public:
    int num_items = 0;
    void append(int value);
    void add_front(int  value);
    
    private:
    int* head;
};


Node::Node(int value){
    value = value;
}


void LinkedList::append(int value){
    Node* ptr = new Node(value);
    *ptr = value;

}



int main(){
    LinkedList A;

    return 0;
}