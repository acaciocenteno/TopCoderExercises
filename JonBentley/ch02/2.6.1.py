#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import tornado.ioloop
import tornado.web

from math import floor

# Find a word's anagrams given a dictionary. Case in which the dict 
# could be previously processed. I decided to do it as a WebService
# As the benefit of having a pre-processed dictionary is only 
# important in a long running application.


# Creates a python dict that uses as key the words' signatures and has as value a list of words
# with that signature.
#
# Once a request is received, we calculate the requested words' signatures, and lookup on this
# dictonary for their anagrams.
def create_dictionary(filename):
	dictionary = {}

	with open(filename, 'r') as f:
		for line in f:
			sanitized = line[:-1].lower()
			signature = ''.join( sorted( list(sanitized) ) )
			category  = dictionary.get( signature, [] )
			category.append(sanitized)
			dictionary[signature] = category

	return dictionary


class MainHandler(tornado.web.RequestHandler):
	def initialize(self, dictionary):
		self.dictionary = dictionary

	# Remove all non-letter characters and lowers the case of all letters.
	def sanitize(self, word):
		sanitized = map(lambda x: x if x.islower() else 
			x.lower() if x.isupper() else None, list(word) )
		sanitized = filter(lambda x: x is not None, sanitized)
		return sanitized

	def find_anagrams(self, word):
		sanitized = self.sanitize(word)
		signature = ''.join( sorted( sanitized ) )
		return self.dictionary.get(signature, [])

	def get(self):
		words = self.get_query_arguments('w')

		if not words:
			self.write("Expected one or more words to lookup on querystring 'w'.")
			self.set_status(400)
			self.finish()
			return

		self.write("<html><body>")

		for word in words:
			self.write("<p>{0}:</p>\n<ul>\n".format(word))
			anagrams = self.find_anagrams(word)
			for anagram in anagrams:
				self.write("\t<li>{0}</li>\n".format(anagram))
			self.write('</ul>\n\n')

		self.write("</body></html>")
		self.finish()


if __name__ == "__main__":
	if len(sys.argv) < 2:
		print 'Please, specify a dictionary file.'
		sys.exit(1)

	if not os.access(sys.argv[1], os.R_OK):
		print 'File [{0}] does not exist or is not accessible.'
		sys.exit(2)

	d = create_dictionary(sys.argv[1])

	application = tornado.web.Application([
		(r".*", MainHandler, dict(dictionary=d)),
	], autoreload=True)

	application.listen(8080)
	tornado.ioloop.IOLoop.instance().start()