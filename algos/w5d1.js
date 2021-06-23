
const nums1 = [1, 2, 3, 4, 10];
const expected1 = true;
// Explanation: between indices 3 & 4
const nums2 = [1, 2, 4, 2, 1];
const expected2 = false;

function balancePoint(nums) {
    let point = 2;
    let left = 0; //3, 6, 10
    let right = 0; //17, 14, 10
    for (let i = 0; i < point; i++) {
        left += nums[i];
    }
    for (let j = nums.length - 1; j >= point; j--) {
        right += nums[j];
    }

    while(left != right && point < nums.length - 1) {
        left += nums[point];
        right -= nums[point];
        point++;
        if (left == right)  {
            return true;
        }
    }
    return false;
}
