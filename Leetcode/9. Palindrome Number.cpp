#include <cmath>
class Solution {
public:
    bool isPalindrome(int x) {
    bool pal = false;
    if(x < 0){
        return pal;
    }
    if(x == 0){
        pal = true;
        return pal;
    }
    int size = int( log10(x) + 1);

    int a,temp = 0;

    if(size <= 1){
        pal = true;
        return pal;
    }

    
    
    else if(size%2 == 0){
        size = int(size/2);
        for(int i =size-1; i >= 0; i--){
            a = x%10;
            temp = temp+a*pow(10,i);
            x = int(x/10);
        }
        
        if(temp == x){
            pal = true;
        }
    }
    else{
        size = int(size/2);
        for(int i =size-1; i >= 0; i--){
            a = x%10;
            temp = temp+a*pow(10,i);
            x = int(x/10);
        }
        x = int(x/10);
        cout << temp;
        
        if(temp == x){
            pal = true;
        }
        
    }

    return pal;

    }
};