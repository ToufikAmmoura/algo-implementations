#include <iostream>
#include <vector>
using namespace std;

void printArr(int arr[], int size){
    int i=0;
    while(i < size){
        cout << arr[i++] << " ";
    }
    cout << "\n";
}

void insert(int* arr, int index, int el, int size){
    // we hebben denk ik een insert functie nodig (ookal kost dit performance)
    int newArr[size+1];
    int i=0;
    while(i < index){
        arr[i] = newArr[i]; // copying one array into the other
        i++;
    }
    
    newArr[i] = el; // i will be equal to index so we insert the element
    
    while(i < size){
        newArr[i+1] = arr[i]; // newArr is now one element bigger so i+1 
        i++;
    }
}

void quicksort(int* arr, int begin, int end){


}

int main(){
    int arr[] = {4,6,2,8,9,86,12,34,1,0};
    int arraySize = sizeof(arr)/sizeof(arr[0]);

    quicksort();
    printArr(arr, arraySize);
    return 0;
}