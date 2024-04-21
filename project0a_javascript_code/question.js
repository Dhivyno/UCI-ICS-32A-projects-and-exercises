"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var readline_1 = require("readline");
var rl = (0, readline_1.createInterface)({
    input: process.stdin,
    output: process.stdout
});
var question = function (questionText) {
    return new Promise(function (resolve) { return rl.question(questionText, resolve); })
        .finally(function () { return rl.close(); });
};
exports.default = question;
