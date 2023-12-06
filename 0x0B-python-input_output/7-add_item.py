#!/usr/bin/python3
"""This module for add items function"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    list_items = load_from_json_file('add_item.json')
# For FileNotFoundError Exception error
except Exception:
    list_items = []

for arg in sys.argv[1:]:
    list_items.append(arg)
# OR we can make this to extend the list
# dataList.extend(sys.argv[1:])

save_to_json_file(list_items, 'add_item.json')
