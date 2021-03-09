const insertion_sort = (array) => {
	for (let i = 0; i < array.length; i++) {
		const key = array[i];

		let j = i - 1;

		while (j >= 0 && array[j] > key) {
			array[j + 1] = array[j];

			j--;
		}

		array[j + 1] = key;
	}
};

a = [1, 3, 2, 0, 5, 4, -1];

console.log(a);

insertion_sort(a);

console.log(a);
