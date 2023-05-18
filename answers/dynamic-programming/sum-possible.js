const sumPossible = (n, nums) => {
    if (nums.length === 0 && n === 0) return true;
    let index = 0;
    while (index < nums.length) {
        let num = nums[index];
        let remainder = n % nums[index];
        let multiple = Math.floor(n / num);
        if (remainder === 0) return true;
        for (let number of nums) {
             let product = multiple * num;
            //  console.log(product, 'the product...')
            //  console.log(number, 'current number...')
             if (product + number === n) {
                return true;
             }
        }
        index++;
    }
    return false;
}
