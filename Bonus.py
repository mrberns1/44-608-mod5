# coding: utf-8
import pandas as pd
zips = pd.Series({'Boston': '02215', 'Miami': '3310'})
zips
zips.str.match(r'\d{5}')
cities = pd.Series(['Boston, MA 02215', 'Miami, FL 33101'])
cities
cities.str.contains(r' [A-Z]{2} ')
cities.str.match(r' [A-Z]{2} ')
contacts = [['Mike Green', 'demo1@deitel.com', '5555555555'], ['Sue Brown', 'demo2@deitel.com', '5555551234']]
contactsdf = pd.DataFrame(contacts, columns = ['Name', 'Email', 'Phone'])
contactsdf
import re
def get_formatted_phone(value): result = re.fullmatch(r'(\d{3})(\d{3})(\d{4})', value) return '-'.join(result.groups()) if result else value 
def get_formatted_phone(value): result = re.fullmatch(r'(\d{3})(\d{3})(\d{4})', value) return '-' .join(result.groups()) if result else value
formatted_phone = contactsdf['Phone'].map(get_formatted_phone)
def get_formatted_phone(value): result = re.fullmatch(r'(\d{3})(\d{3})(\d{4})', value) return "-" .join(result.groups()) if result else value
def get_formatted_phone(value): result = re.fullmatch(r'(\d{3})(\d{3})(\d{4})', value) return - .join(result.groups()) if result else value
def get_formatted_phone(value): result = re.fullmatch(r'(\d{3})(\d{3})(\d{4})', value) 
return '-'.join(result.groups()) if result else value
def get_formatted_phone(value): result = re.fullmatch(r'(\d{3})(\d{3})(\d{4})', value)return '-'.join(result.groups()) if result else value
#I wrote this code different ways and tried it multiple times and it will not work. There is an issue with the 'return' line in the syntax
#missybernskoetter
