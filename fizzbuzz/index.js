/**
 * Fizzbuzz without conditionals
 */

handlers = [
	[function(i) {
		return "FizzBuzz";
	}, function(i) {
		return "Fizz";
	}],
	[function(i) {
		return "Buzz";
	}, function(i) {
		return i;
	}]
];

function fizzbuzz(n) {
	for (i = 1; i <= n; i++) {
		var handler = handlers[Math.ceil(i % 3 / i)][Math.ceil(i % 5 / i)];
		console.log(handler(i));
	}
}

fizzbuzz(100);
