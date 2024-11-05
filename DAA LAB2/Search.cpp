/**Name:Raunak Thanawala
 * Date:10/8/24
 * Experiment: Binary and Linear Search
 */
#include <iostream>
#include <cstdlib>

namespace searching_project {

//Conducts Linear Search
int LSearch(const int karr[], int n, int key) {
    for(int i = 0; i < n; ++i) {
        if (karr[i] == key) { 
            return i; 
        }
    }
    return -1;
}

//Conducts Binary Search
int BSearch(const int karr[], int start, int end, int key) {
    if(start <= end)
    {
        int mid = (start + end) / 2;
        if(karr[mid] == key) {
            return mid;
        }   else if(karr[mid] > key) {
            return BSearch(karr, start, mid-1, key);
        }   else {
            return BSearch(karr, mid+1, end, key);
        }
    }
    return -1;
}

//Checks if Given Array is Sorted
bool IsSorted(const int karr[], int n) {
    for(int i = 0; i < n-1; i++) {
        if(karr[i] > karr[i+1]) {
            return false;
        }
    }
    return true;
}

}  // namespace searching_project

int main() {
    int n;
    std::cout << "Enter the size of array: "<< std::endl;
    std::cin >> n;
    if(n == 0) {
        std::cerr << "Array is Empty"<< std::endl;
        std::exit(EXIT_FAILURE);
    }
    int* arr = new int[n];
    std::cout << "Enter the array: "<< std::endl;
    for(int j = 0; j < n; ++j) {
        std::cin >> arr[j];
    }
    int key;
    std::cout << "Enter the element to be searched in array: "<< std::endl;
    std::cin >> key;
    int linear_search_result = searching_project::LSearch(arr,n,key);
    if(linear_search_result != -1) {
        std::cout << "Index at which " << key << " is located is "
                  << linear_search_result << " through Linear Search" << std::endl;
    }
    else {
        std::cout << key << " not found in array with Linear Search" << std::endl;
    }
    //Ensure Array is Sorted Before Binary Search
    bool is_sorted = searching_project::IsSorted(arr,n);
    if(!is_sorted) {
        std::cout<< "Array not sorted";
        std::exit(EXIT_FAILURE);
    }
    int binary_search_result = searching_project::BSearch(arr, 0, n-1, key);
    if(binary_search_result != -1) {
        std::cout << "Index at which " << key << " is located is "
                  << binary_search_result << " through Binary Search" << std::endl;
    }
    else {
        std::cout << key << " not found in array with Binary Search" << std::endl;
    }
}