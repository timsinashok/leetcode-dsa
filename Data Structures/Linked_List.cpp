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

// Finished Node Class Definition




// Class Linked List ////
template <typename T>
class LinkedList{
    private:
        int size;
        Node<T>* head;
    public:
        LinkedList();
        void addFront(T val);
        int getSize();
        
};

template <typename T> LinkedList<T>::LinkedList(){
    head = NULL;
};


template <typename T>  void LinkedList<T>::addFront(T val){
    Node<T>* N = val;
    n->next = head;
    this->head = n;
}

template <typename T> int LinkedList<T>::getSize(){
    return size;
}

/// Finished Linked List Class Definition ///


int main(){

    Node <int> a(5);
    return 0;
}