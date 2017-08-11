/**
 * https://www.interviewcake.com/question/product-of-other-numbers
 */

function get_products_of_all_ints_except_at_index(numbers) {
	var products = [];
	var before = 1;
	for (var i = 0; i < numbers.length; i++) {
		products.push(before);
		before = before * numbers[i];
	}

	var after = 1;
	for (var j = numbers.length - 1; j >= 0; j--) {
		products[j] = products[j] * after;
		after = after * numbers[j];

	}

	return products;
}

console.log(get_products_of_all_ints_except_at_index([1, 7, 3, 4]));
