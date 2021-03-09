function search(arr, key) {
	for (let i = 0; i < arr.length; i++) {
		if (arr[i] === key) {
			return i;
		}
	}
}

a = [1, 3, 2, 0, 5, 4, -1];
key = 3;

if (search(a, key)) {
	console.log(`${key} found at index ${search(a, key)}`);
} else {
	console.log(`${key} not found`);
}
