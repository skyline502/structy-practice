const fiveSort = (nums) => {
  let i = 0;
  let j = nums.length - 1;
  while (i < j) {
      // console.log(i, j, 'current indices')
      // console.log(nums[i], nums[j], 'current numbers')
      if (nums[j] === 5) {
          j--;
      } else if (nums[i] === 5) {
          // console.log('in swapping if', nums[i], nums[j]);
          [nums[i], nums[j]] = [nums[j], nums[i]]
          // console.log('swap')
          // console.log(nums, 'current numbers after swap')
          i++;
      } else {
          i++;
      }
  }
  // console.log(nums)
  return nums;
};
