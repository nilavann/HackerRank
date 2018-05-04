/**
*   Return the second largest number in the array.
*   @param {Number[]} nums - An array of numbers.
*   @return {Number} The second largest number in the array.
**/
function getSecondLargest(nums) {
    // Complete the function
    nums = [ ...new Set(nums)];
    //console.log(nums);
    nums.sort(function(x,y) { return x < y;});
    return nums[1];
}