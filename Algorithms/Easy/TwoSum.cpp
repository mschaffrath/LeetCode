/*
1. Two Sum

Given an array of integers, return indices of the two numbers
such that they add up to a specific target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

*/

#include <stdexcept>
#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> Ans;
        for(unsigned int i = 0; i < nums.size(); i++) {
            for(unsigned int j = i + 1; j < nums.size(); j++){
                if (nums[i] + nums[j] == target){
                    Ans.push_back(i);
                    Ans.push_back(j);
                    return Ans;
                }
            } 
        }
        throw invalid_argument("No two sum solution");
    }
};

int main(){
    
    int arr[] = {1,3,6,7,8};
    vector<int> nums (arr, arr + sizeof(arr) / sizeof(arr[0]) );
    int target = 8;

    Solution* Sol = new Solution();
    vector<int> Ans;
    Ans = Sol->twoSum(nums, target);

    cout << "Input vector: ";
    for(unsigned i = 0; i < nums.size(); ++i){
        cout << nums[i] << " ";
    }
    cout << endl;
    cout << "Target: " << target << endl;

    cout << "Answer: " << "[" << Ans[0] << "," << Ans[1] << "]" << endl;
    cout << endl;

}