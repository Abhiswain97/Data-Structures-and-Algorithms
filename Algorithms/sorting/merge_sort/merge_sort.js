// https://stackabuse.com/merge-sort-in-javascript/

merge = (left, right) => {
	let res = [];
	while (left.length && right.length) {
		if (left[0] < right[0]) res.push(left.shift());
		else res.push(right.shift());
	}

	return [...res, ...left, ...right];
};

mergeSort = (arr) => {
	if (arr.length < 2) {
		return arr;
	} else {
		let mid = arr.length / 2;

		let L = arr.splice(0, mid);

		return merge(mergeSort(L), mergeSort(arr));
	}
};

a = [1, 3, 2, 0, 5, 4, -1];

console.log(a);

console.log(mergeSort(a));
