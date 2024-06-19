#!/usr/bin/node

exports.logMe = function (item){
	if (typeof this.count === 'undefined'){
		this.count++;
	};
