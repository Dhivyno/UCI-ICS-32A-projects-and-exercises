var readline = require('readline');
var rl = readline.createInterface(process.stdin, process.stdout);
var isUpper = function (char) { return char === char.toUpperCase() && isNaN(parseInt(char)); };
function perimeter(a, b) {
    var perimeter = (a + b + Math.sqrt(Math.pow(a, 2) + Math.pow(b, 2))).toFixed(2); // finds perimeter using pythgoras and rounds to 2 decimal places (for no particular reason)
    console.log("The perimeter of your triangle is " + perimeter + " to 2 decimal places");
    rl.close();
}
function concatenation(str1, str2) {
    var full_string = str1 + str2;
    console.log("The concatenated string is '" + full_string + "'");
    rl.close();
}
function name_age() {
    var name_input = "";
    var age_input = "";
    rl.question("What is your name? ", function (yourName) {
        name_input = yourName;
        rl.question("What is your age? ", function (age) {
            age_input = age;
            if (age_input == "1") {
                console.log("Your name is", name_input, "and you are", age_input, "year old");
                rl.close();
            }
            else if (!isNaN(parseInt(age_input)) && age_input.length === parseInt(age_input).toString().length) {
                console.log("Your name is", name_input, "and you are", parseInt(age_input), "years old");
                rl.close();
            }
            else {
                console.log("INVALID AGE INPUT");
                name_age();
            }
        });
    });
}
function char_search() {
    var sentence = "";
    var key = "";
    var count = 0;
    rl.question("Enter your sentence: ", function (sentence_input) {
        sentence = sentence_input;
        rl.question("Enter your key character to search for: ", function (key_input) {
            key = key_input;
            if (key.length > 1) {
                console.log("INVALID KEY CHARACTER");
                char_search();
            }
            else {
                for (var i = 0; i < sentence.length; i++) {
                    if (sentence[i] === key) {
                        count++;
                    }
                }
                console.log("The key character '" + key + "'", "was found in the sentence", count, "times");
                rl.close();
            }
        });
    });
}
function sum_nums(array) {
    var sum = 0;
    for (var i = 0; i < array.length; i++) {
        sum += array[i];
    }
    console.log("The sum of the numbers in the array is", sum);
    rl.close();
}
function max_length(array) {
    var max = 0;
    var max_index = 0;
    for (var i = 0; i < array.length; i++) {
        if (array[i].length > max) {
            max_index = i;
            max = array[i].length;
        }
    }
    console.log("The string with the longest length is '" + array[max_index] + "'", "with a length of", max, "characters");
    rl.close();
}
function license_plate() {
    var invalid = false;
    var digit_present = false;
    rl.question('Enter your license plate number: ', function (plate) {
        length = plate.length;
        if (!(isUpper(plate[length - 1]) && isUpper(plate[0]))) {
            invalid = true;
        }
        for (var i = 0; i < length; i++) {
            var char = plate[i];
            if (!isUpper(char) && isNaN(parseInt(char))) {
                invalid = true;
            }
            else { }
            if (!isNaN(parseInt(char))) {
                digit_present = true;
            }
            else if (!(char >= "A" && char <= "Z")) {
                invalid = true;
            }
        }
        if (digit_present == false) {
            invalid = true;
        }
        if (invalid) {
            console.log("INVALID PLATE NUMBER");
            license_plate();
        }
        else {
            rl.close();
        }
    });
}
function palindrome(word) {
    var palindrome = true;
    var j = word.length - 1;
    for (var i = 0; i <= j; i++) {
        if (!(word[i] === word[j])) {
            palindrome = false;
        }
        j--;
    }
    if (palindrome) {
        console.log("The word '" + word + "'", "is a palindrome!");
    }
    else {
        console.log("The word '" + word + "'", "is not a palindrome");
    }
    rl.close();
}
function p1() {
    console.log("\n---------------------------------------------------\nPROBLEM: PERIMETER OF RIGHT TRIANGLE GIVEN 2 SIDES\n---------------------------------------------------\n");
    var height = 0;
    var width = 0;
    rl.question("What is the height of your triangle? ", function (height_input) {
        height = parseInt(height_input);
        rl.question("What is the width of your triangle? ", function (width_input) {
            width = parseInt(width_input);
            perimeter(height, width);
        });
    });
}
function p2() {
    console.log("\n-----------------------------------------\nPROBLEM: CONCATENATION OF 2 INPUT STRINGS\n-----------------------------------------\n");
    var str1 = "";
    var str2 = "";
    rl.question("What is your first string? ", function (str1_input) {
        str1 = str1_input;
        rl.question("What is your second string? ", function (str2_input) {
            str2 = str2_input;
            concatenation(str1, str2);
        });
    });
}
function p3() {
    console.log("\n-----------------------------------------\nPROBLEM: OUTPUT NAME AND AGE FROM INPUT\n-----------------------------------------\n");
    name_age();
}
function p4() {
    console.log("\n-----------------------------------------\nPROBLEM: SUM OF NUMBERS FROM LIST OF NUMBERS\n-----------------------------------------\n");
    rl.question("Enter your numbers seperated by commas: ", function (list_input) {
        var array = list_input.split(",");
        var num_array = [];
        for (var i = 0; i < array.length; i++) {
            num_array.push(parseInt(array[i]));
        }
        sum_nums(num_array);
    });
}
function p5() {
    console.log("\n-------------------------------------------------\nPROBLEM: FIND LONGEST STRING FROM LIST OF STRINGS\n-------------------------------------------------\n");
    rl.question("Enter your strings seperated by commas: ", function (list_input) {
        var array = list_input.split(",");
        var str_array = [];
        for (var i = 0; i < array.length; i++) {
            str_array.push(array[i]);
        }
        max_length(str_array);
    });
}
function p6() {
    console.log("\n-----------------------------------------\nPROBLEM: VALIDATE A LICENSE PLATE NUMBER\n-----------------------------------------\n");
    license_plate();
}
function p7() {
    console.log("\n----------------------------------------------------------------\nPROBLEM: COUNT NUMBER OF OCCURENCES OF KEY CHARACTER IN SENTENCE\n----------------------------------------------------------------\n");
    char_search();
}
function p8() {
    console.log("\n---------------------------------------------------\nPROBLEM: CHECK WHETHER INPUT STRING IS A PALINDROME\n---------------------------------------------------\n");
    rl.question("What is your word? ", function (word) {
        palindrome(word);
    });
}
function menu() {
    rl.question("Which problem would you like to see? ", function (p_num) {
        if (p_num == 1) {
            p1();
        }
        else if (p_num == 2) {
            p2();
        }
        else if (p_num == 3) {
            p3();
        }
        else if (p_num == 4) {
            p4();
        }
        else if (p_num == 5) {
            p5();
        }
        else if (p_num == 6) {
            p6();
        }
        else if (p_num == 7) {
            p7();
        }
        else if (p_num == 8) {
            p8();
        }
        else {
            console.log("INVALID PROBLEM NUMBER");
            menu();
        }
    });
}
menu();
