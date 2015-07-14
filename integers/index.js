/**
 * https://www.interviewcake.com/question/product-of-other-numbers
 */

function get_products_of_all_ints_except_at_index(numbers) {
	var products = [];
	var before = 1;
	for (i = 0; i < numbers.length; i++) {
		var after = 1;
		for (n = i + 1; n < numbers.length; n++) {
			after = after * numbers[n];
		}
		products.push(before * after);
		before = before * numbers[i];
	}

	return products;
}

console.log(get_products_of_all_ints_except_at_index([1, 7, 3, 4]));
