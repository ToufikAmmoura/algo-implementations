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

void quicksort(int* arr, int size){

}

int main(){
    int arr[] = {4,6,2,8,9,86,12,34,1,0};
    int arraySize = sizeof(arr)/sizeof(arr[0]);

    quicksort(arr, arraySize);
    printArr(arr, arraySize);
    return 0;
}