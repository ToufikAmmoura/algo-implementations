#include <iostream>
#include <vector>
using namespace std;

void printArr(int* arr, int size){
    int i=0;
    while(i < size){
        cout << arr[i++] << " ";
        cout << "prr";
    }
    cout << "\n";
}

void swap(int i, int j, int* arr){
    int TEMP = arr[i];
    arr[i] = arr[j];
    arr[j] = TEMP;
}

int partition(){
    
}


void quicksort(int* arr, int begin, int end){
    // wat we nodig hebben is de quicksort variant die met swap werkt en niet met insert
    int left = begin;
    int right = end;
    
    while(true){
        int pivot = arr[left + (right-end)/2]; // kies dit misschien random
        while(arr[left] < pivot){
            left++;
        }

        while(arr[right] > pivot){
            right--;
        }

        if(left >= right){
            break;
        } else{
            swap(left++, right--, arr);
        }

    }

    if(left == right){
        quicksort(arr, begin, left-1);
        quicksort(arr, right, end);
    } else{
        quicksort(arr, begin, right);
        quicksort(arr, left, end);
    }
}

int main(){
    int arr[] = {4,6,2,8,9,86,12,34,1,0};
    int arraySize = sizeof(arr)/sizeof(arr[0]);
    cout << "begin";
    quicksort(arr, 0, arraySize-1);
    cout << "end";
    printArr(arr, arraySize);
    return 0;
}