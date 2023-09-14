#include <iostream>

using namespace std;

class Node{
    public:
    int value;
    int* next;
    
    Node(int value){}        
};

Node::Node(int value){
    value = value;
}

class LinkedList{
    public:
    int num_items = 0;
    void append(int value);
    void add_front(int  value);
    
    private:
    int* head;

    LinkedList(){};
};

LinkedList::LinkedList(){

};

void LinkedList::append(int value){
    Node* N = new Node(value);
    N->next = 
}






int main(){
    LinkedList A;

    return 0;
}