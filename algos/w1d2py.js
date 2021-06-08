/*
	Acronyms
	Create a function that, given a string, returns the string’s acronym
	(first letter of each word capitalized).
	Do it with .split first if you need to, then try to do it without
*/

const str1 = " there's no free lunch - gotta pay yer way. ";
const expected1 = "TNFL-GPYW";

const str2 = "Live from New York, it's Saturday Night!";
const expected2 = "LFNYISN";

//split version
function acronymization(str) {  
    let placeholder = str.trim();
    let newArr = placeholder.split(" ");
	let acronymized = ""
    for(let counter = 0; counter < newArr.length; counter++)    {
        acronymized += newArr[counter][0]
        acronymized = acronymized.toUpperCase();
    }
    return acronymized
}

console.log(acronymization(str1));

function acronymize(str) {
	var caps = "";
    let newArr = str1.split(" ");
    for (const word of newArr) {
		caps += word[0].toUpperCase()
	}
	console.log(caps)
}
//non-split version
function noSplitAcro(str) {
	var caps = "";
	if (str[0] != " ") {
		caps += str[0].toUpperCase();
	}
	for (let index = 1; index < str.length; index++) {
		if (str[index-1] === " " && str[index] != " ") {
			caps += str[index].toUpperCase();
		}
	}
	return caps;
}

/*****************************************************************************/

/*
	String: Reverse
	Given a string,
	return a new string that is the given string reversed
*/

const str1 = "creature";
const expected1 = "erutaerc";

const str2 = "dog";
const expected2 = "god";

function reverseString(str) {
	let reverse = str.split().reverse();
	return reverse.join();
}

//non method version
function reverseString2(str) {
    let reverse = "";
    for (let index = 0; index < str.length; index++) {
        reverse += str[str.length-1-index];
    }
    return reverse;
}

