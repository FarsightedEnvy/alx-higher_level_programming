#!/usr/bin/node

exports.nbOccurrences = function(list, searchElement) {
    return list.reduce(function(acc, curr) {
        return curr === searchElement ? acc + 1 : acc;
    }, 0);
};
