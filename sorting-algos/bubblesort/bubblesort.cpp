#include <iostream>
using namespace std;

void printArr(int arr[], int size){
    int i=0;
    while(i < size){
        cout << arr[i++] << " ";
    }
    cout << "\n";
}

void swap(int i, int j, int* arr){
    int TEMP = arr[i];
    arr[i] = arr[j];
    arr[j] = TEMP; 
}

bool isSorted(int arr[], int size){
    int index=0;
    while(index < size-1){
        if(arr[index] > arr[index+1]){
            return false;
        }
        index++;
    }
    return true;
}

void bubble(int* arr, int end){
    int index = 0;
    while(index < end-1){
        if(arr[index] > arr[index+1]){
            swap(index, index+1, arr);
        }
        index++;
    }
}

void bubblesort(int* arr, int size){
    int end = size;
    while(!isSorted(arr, size)){
        bubble(arr, end--);
    }
}

int main(){
    int arr[] = {4,6,2,8,9,86,12,34,1,0};
    int arraySize = sizeof(arr)/sizeof(arr[0]);
    bubblesort(arr, arraySize);
    int i=0;
    while(i < arraySize){
        cout << arr[i++] << " ";
    }
    return 0;
}