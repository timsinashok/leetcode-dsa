#include <iostream>


using namespace std;

// Forward declaration to resolve issue with redefinition
template <typename T>
class LinkedList;


// Node Class
template <typename T>
class Node{
    private:
        T value;
        Node<T>* next;
        friend class LinkedList<T>;
    public:
        Node(T value);        
};

template <typename T> Node<T>::Node(T value){
    this -> value = value;
}



// Class Linked List
template <typename T>
class LinkedList{
    private:
        int size;
        Node<T>* head;
    public:
        LinkedList();
        void addFront(Node<T>* n);
        
};

template <typename T> LinkedList<T>::LinkedList(){
    head = NULL;
};


template <typename T>  void LinkedList<T>::addFront(Node<T>* n){
    n->next = head;
    this->head = n;
}



int main(){

    Node <int> a(5);
    return 0;
}