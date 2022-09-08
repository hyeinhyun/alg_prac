#include <stdio.h>

int h[1001];//init start index with 1
int cnt = 0;

bool compare(int x, int y){
    return x > y; // make priority
}

//pointer change
bool swap(int* i, int* j){//index
    int temp = *i;
    *i = *j;
    *j = temp;
}

void upHeapify(int index){
    //initialize
    if (index == 1){
        return; //do nothing
    }
    //compare with parent node
    if (compare(h[index],h[index/2])){
        swap(&h[index],&h[index/2]);
        upHeapify(index/2); //compare with upper parent
    }
}

void insert (int data){
    h[cnt++] = data; //add value to last array
    upHeapify(cnt);
}

void downHeapify(int index){
    int child;
    //check child
    if (index * 2 > cnt){
        //there is no children
        return;
    }
    //2child -> find priority
    if (index * 2 + 1 <= cnt){
        if (compare(h[index*2],h[index*2+1])){
            child = index * 2;
        }
        else{
            child = index * 2 + 1 ;
        }
    }
    //1child
    else{
        child = index * 2;
    }

    if (compare(h[child],h[index])){//no heap
        swap(&h[index],&h[child]);
        downHeapify(child);
    }

}

void pop (){
    //swap value
    swap(h[1],h[cnt]);
    cnt--;

}