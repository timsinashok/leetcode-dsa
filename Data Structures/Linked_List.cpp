#include <iostream>
#include <string>
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
        void removeFront();
        int getSize();
        T front();
        bool empty();
        
};

template <typename T> bool LinkedList<T>::empty(){
    if(heac == nullptr) return true;
    else return false;
}

template <typename T> LinkedList<T>::LinkedList(){
    head = NULL;
};


template <typename T>  void LinkedList<T>::addFront(T val){
    Node<T>* N = new Node;
    N->value = val;
    N->next = head;
    this->head = N;
}

template <typename T> void LinkedList<T>::removeFront(){
    Node<T>* temp = new Node;
    temp = head;
    head = head->next;
    delete temp;
}


template <typename T> int LinkedList<T>::getSize(){
    return size;
}

template <typename T> T LinkedList<T>::front(){
    return head->value;
}

/// Finished Linked List Class Definition ///


int main(){

    Node <int> a(5);
    return 0;
}