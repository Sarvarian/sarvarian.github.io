#! /usr/bin/python3

import os
import pypandoc
import json
import jinja2

def read_line(array):
	res = ''
	for item in array:
		if item['t'] == 'Str':
			res += item['c']
		elif item['t'] == 'Space':
			res += ' '
		elif item['t'] == 'SoftBreak':
			res += ' '
		elif item['t'] == 'Quoted':
			quote_mark = item['c'][0]['t']
			item_item = item['c'][1][0]
			string = item_item['c']
			if quote_mark == 'SingleQuote':
				res += '\'' + string + '\''
			elif quote_mark == 'DoubleQuote':
				res += '\"' + string + '\"'
			else:
				raise Exception('Unknown type')
		else:
			raise Exception('Unknown type')
	return res


def read_page(path):
	res = {}
	doc = pypandoc.convert_file(path, 'json')
	data = json.loads(doc)['blocks']
	res['id'] = data[0]['c'][1][0].replace('-', '_')
	res['title'] = read_line(data[0]['c'][2])
	verse = None
	res['verses'] = []
	lines = []
	def update_verse():
		if verse is not None:
			verse['lines'] = lines
			res['verses'].append(verse)
	for block in data[1:]:
		if block['t'] == 'Header' and block['c'][0] == 2:
			update_verse()
			verse = {'title': read_line(block['c'][2]), 'id': block['c'][1][0]}
			lines = []
		elif block['t'] == 'Para':
			lines.append(read_line(block['c']))
		else:
			raise Exception('Unknown type')
	update_verse()
	return res


def read_content(data):
	paths = []
	for item in os.listdir('contents'):
		file_path = f'contents/{item}'
		if os.path.isfile(file_path) and item.endswith('.md'):
			paths.append(file_path)
	paths.sort()
	pages = []
	for path in paths:
		pages.append(read_page(path))
	data['pages'] = pages
	return data


def main():
	data = {
		'newline': '\n',
		'tab': '\t',
		'space': ' ',
	}
	data = read_content(data)
	env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))
	template = env.get_template('index.html.jinja')
	output = template.render(data)
	with open('index.html', 'w') as f:
		f.write(output)
	pass


if __name__ == '__main__':
	main()


