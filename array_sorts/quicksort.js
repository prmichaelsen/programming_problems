/** in-place quicksort  */
function quick(arr, start = 0, end = arr.length) {
  if (end - start < 2)
    return arr;
  const pivot = arr[start];
  let index = start + 1;
  let store = start + 1;
  while(store < end && index < end) {
    if (arr[index] < pivot) {
      const temp = arr[index];
      arr[index] = arr[store];
      arr[store] = temp;
      store++;
    }  
    index++;
  }
  const temp = arr[start];
  arr[start] = arr[store - 1];
  arr[store - 1] = temp;
  const mid = Math.floor((start + end)/2);
  quick(arr, start, mid);
  quick(arr, mid, end);
  return arr;
}

console.log(quick([]));

console.log(quick([
  50,
  10,
  60,
  30,
  100,
  20
]));


console.log(quick([
 1
]));
console.log(quick([
  100, 20
]));
