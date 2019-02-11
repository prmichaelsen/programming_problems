/** operations for a one-indexed max heap.
 * This implemenation is neither fast nor readable.
 */
const parent  = i => (i >> 1);
const left    = i => (i << 1);
const right   = i => (i << 1) + 1;

/** add element at end and bubble up */
function insert(heap, v) {
  let i = heap.length;
  heap[i] = v;
  while(i > 1 && heap[parent(i)] < v) {
    heap[i] = heap[parent(i)];
    heap[parent(i)] = v;
    i = parent(i);
  }
  return heap;
}

/** 
 * swap 1st and nth element and 
 * shift 1st element down to
 * its final position
 */
function shiftDown(heap) {
  let n = heap.length - 1;
  let i = 1;
  let max = heap[1];
  heap[1] = heap[n];
  heap = heap.slice(0, n);
  while(i < n && [left(i), right(i)].some(j => heap[j] > heap[i])) {
    let indexOfMax = i;
    if (heap[right(i)] === undefined)
      indexOfMax = left(i);
    else if(heap[left(i)] > heap[right(i)]) 
      indexOfMax = left(i);
    else
      indexOfMax = right(i);
    const temp = heap[indexOfMax];
    heap[indexOfMax] = heap[i];
    heap[i] = temp;
    i = indexOfMax;
  }
  return heap;
}

/** max heap */
class Heap {
  /** 
   * Patrick, why in gods name are so many of these
   * one liners? Perhaps you can consider it a good 
   * example of not ever doing something that's
   * fun to do.
   */
  constructor(arr) {
    this._heap = [0];
    arr.forEach(v => insert(this._heap, v));
    delete this._heap[0];
    this.enqueue = v => insert(this._heap, v) && this;
    this.enqueueMany = (...a) => (a.forEach(v => 
      insert(this._heap, v)
    )) || this;
    this.max = () => this._heap[1];
    this.dequeue = () => ([
      this.max(),
      this._heap = shiftDown(this._heap)
    ])[0];
    this.dequeueMany = n => 
      [...Array(n).keys()]
      .map(this.dequeue)
      .filter(v => v !== undefined);
    this.values = () => this._heap.slice(1, this._heap.length);
    this.sort = () => {
      let temp = [...this._heap];
      let n = temp.length;
      let result = this.dequeueMany(n);
      this._heap = temp;
      return result;
    }
  }
}

const heap = new Heap([50, 150, 51, 100]);
console.log(heap.values());
console.log(heap.max());
console.log(heap.enqueue(200).values());
console.log(heap.enqueueMany(30, 21, 70, 600, 5, 1, 2).values());
console.log(heap.sort());
console.log(heap.dequeue());
console.log(heap.dequeueMany(3));
console.log(heap.values());
console.log(heap.dequeueMany(50));
console.log(heap.values());
