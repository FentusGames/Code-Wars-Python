# Srot the inner ctonnet in dsnnieedcg oredr
def sort_the_inner_content(words):
    return " ".join(["".join((i[0], "".join(i[1]), i[2])) if type(i) is tuple else i for i in [(i[0], sorted(i[1:-1], reverse=True), i[-1]) if len(i) > 3 else i for i in words.split()]])
    
# Weight for weight
def order_weight(strng):
    return " ".join(sorted(sorted(strng.split(" ")), key=lambda strng: sum([int(char) for char in strng])))
    
def ds(a_string):
    return sum([int(char) for char in a_string])

def order_weight(strng):
    return " ".join(sorted(sorted(strng.split(" ")), key=ds))

# IP Validation
import re

def is_valid_IP(strng):
    if re.match(r"^([1][0-9][0-9]\.|^[2][5][0-5]\.|^[2][0-4][0-9]\.|^[1][0-9][0-9]\.|^[0-9][0-9].|^[0-9]\.)([1][0-9][0-9]\.|[2][5][0-5]\.|[2][0-4][0-9].|[1][0-9][0-9].|[0-9][0-9].|[0-9].)([1][0-9][0-9].|[2][5][0-5].|[2][0-4][0-9].|[1][0-9][0-9].|[0-9][0-9].|[0-9].)([1][0-9][0-9]|[2][5][0-5]|[2][0-4][0-9]|[1][0-9][0-9]|[0-9][0-9]|[0-9])$", strng):
        return True
    return False

# String incrementer
import re

def increment_string(strng):
    match = re.match('.*?([0-9]+)$', strng)
    if match:
        g = match.group(1)
        z = len(g)
        num = int(g)
        num += 1
        return "{0}{1}".format(strng.replace(g, ""),str(num).zfill(z))
    else:
        try:
            z = len(strng)
            num = int(strng)
            num += 1
            return "{0}".format(str(num).zfill(z))
        except:
            return "{0}1".format(strng)
            
# def triangular(n):
if n <= 0: return 0
    return n * (n + 1) / 2
    
# Digit*Digit
def square_digits(num):
    return int(''.join([str(n) for n in [int(i)**2 for i in str(num)]]))
    
# Josephus Permutation
def josephus(items,k):
    r = []
    b = 0
    for _ in range(0, len(items)):
        d = (b + k - 1) % len(items)
        r.append(items[d])
        del items[d]
        b = d if d < len(items) else 0
    return r

# Filter the number
import re

def filter_string(string):
    return int(re.sub('\D', '', string))
    
# Credit Card Mask
def maskify(cc):
    return '#' * (len(cc) - 4) + cc[-4:]
    
# Are there any arrows left?
def any_arrows(arrows):
    return False if [arrow for arrow in arrows if not('damaged' in arrow and arrow['damaged'])] == [] else True 

# Add Length
import re 

def add_length(str_):
    return [i + ' ' + str(len(i)) for i in re.split('\s+', str_)]
    
# Generate user links
import urllib

def generate_link(user):
    return 'http://www.codewars.com/users/{0}'.format(urllib.quote(user))
    
# Paths in the Grid
import functools
import operator

def number_of_routes(m, n):
    return functools.reduce(operator.mul, list(range(m + n - min([m, n]) + 1, m + n + 1)), 1) / functools.reduce(operator.mul, list(range(min([m, n]) - min([m, n]) + 1, min([m, n]) + 1)), 1)

# Human readable duration format
def format_duration(seconds):
    result = []

    for name, count in (('years', 31536000), ('days', 86400), ('hours', 3600), ('minutes', 60), ('seconds', 1)):
        value = seconds // count
        if value:
            seconds -= value * count
            if value == 1:
                name = name.rstrip('s')
            result.append("{} {}".format(value, name))
    return ' and '.join([', '.join(result[:-1]), result[-1]]) if len(result) >= 2 else ''.join(result) if len(result) == 1 else 'now'

# No zeros for heros
def no_boring_zeros(n):
    return -int(''.join(list(str(int(''.join(list(str(abs(n)))[::-1]))))[::-1])) if n < 0 else int(''.join(list(str(int(''.join(list(str(abs(n)))[::-1]))))[::-1]))
    
# Second Variation on Caesar Cipher
import functools
import operator


def code(plaintext, key, cipher=''):
    alphabet = [str(chr(l)) for l in range(ord('a'), ord('z') + 1)]
    for char in plaintext:
        if char.lower() in alphabet:
            cipher += alphabet[(alphabet.index(char.lower()) + key) % (len(alphabet))].upper() if char.isupper() else alphabet[(alphabet.index(char) + key) % (len(alphabet))]
        else:
            cipher += char
    return cipher

def chunk(l, n):
    n = max(1, n)
    return [l[i:i + n] for i in range(0, len(l), n)]

def encode_str(plaintext, key):
    cipher = '{0}{1}'.format(plaintext[0].lower(), code(plaintext[0].lower(), key))
    encrypted = code(plaintext, key, cipher=cipher)
    return chunk(encrypted, int((len(encrypted) - len(encrypted) % 5) / 5 + 1 if len(encrypted) % 5 >= 1 else (len(encrypted) - len(encrypted) % 5) / 5))

def decode(encryptedtext):
    key = functools.reduce(operator.sub, [ord(c) for c in ''.join(encryptedtext)[:2]])
    encrypted = code(''.join(encryptedtext)[2:], key)
    return(encrypted)
    
# Largest Numeric Palindrome
from collections import Counter
import functools
from itertools import combinations
import operator


def numeric_palindrome(*args):
    numbers = list(args)
    largest = 0
    for process in range(2, len(numbers) + 1):
        for c in combinations(numbers, process):
            number = functools.reduce(operator.mul, c)
            list_of_numbers = [int(digit) for digit in str(number)]
            
            numeric_palindrome = []
            
            while True:
                doubles = [k for k, v in Counter(list_of_numbers).items() if v > 1]
                if doubles:
                    smallest_doubles = min(doubles)
                    numeric_palindrome.insert(0, smallest_doubles)
                    numeric_palindrome.append(smallest_doubles)
                    list_of_numbers.remove(smallest_doubles)
                    list_of_numbers.remove(smallest_doubles)
                else:
                    if not list_of_numbers:
                        number = int(''.join(map(str, numeric_palindrome)))
                        if number > largest:
                            largest = number
                        break
                    if numeric_palindrome and numeric_palindrome != [0, 0]:
                        numeric_palindrome.insert(int(len(numeric_palindrome) / 2), max(list_of_numbers))
                        number = int(''.join(map(str, numeric_palindrome)))
                        if number > largest:
                            largest = number
                        break
                    else:
                        number = max(list_of_numbers)
                        if number > largest:
                            largest = number
                        break
    return largest

# Valid Phone Number
import re

def validPhoneNumber(phoneNumber):
    return bool(re.search('(?<!\w)(\([0-9]{3}\)\s[0-9]{3}\-[0-9]{4})(?!\w)', phoneNumber))
    
import re

def validPhoneNumber(phoneNumber):
    print(phoneNumber)
    return bool(re.search('(?<!\w)(\([0-9]{3}\)\s[0-9]{3}\-[0-9]{4})(?!\w)', phoneNumber))
    
# Countdown to Christmas
from datetime import date
from dateutil.rrule import rrule, DAILY

def days_until_christmas(day):
    return len(list(rrule(DAILY, dtstart=day, until=date(day.year + 1 if day.day > 25 and day.month == 12 else day.year, 12, 24))))

# Directions Reduction
import re

def dirReduc(arr):
    o = ' '.join(arr)
    while True:
        s = 'NORTH SOUTH|SOUTH NORTH|EAST WEST|WEST EAST'
        o = re.sub(s, '', o, 1)
        o = ' '.join(o.split())
        if not re.search(s, o):
            break
    if o == '':
        return []
    else:
        return o.split(' ')

def reduce(arr, i):
    arr.pop(i + 1)
    arr.pop(i)
    dirReduc(arr)

def dirReduc(arr):
    for i, c in enumerate(arr):
        if c == "NORTH":
            if i + 1 < len(arr):
                if arr[i + 1] == "SOUTH":
                    reduce(arr, i)
        if c == "SOUTH":
            if i + 1 < len(arr):
                if arr[i + 1] == "NORTH":
                    reduce(arr, i)
        if c == "EAST":
            if i + 1 < len(arr):
                if arr[i + 1] == "WEST":
                    reduce(arr, i)
        if c == "WEST":
            if i + 1 < len(arr):
                if arr[i + 1] == "EAST":
                    reduce(arr, i)
    return arr

# IPv4 Parser
def ipv4__parser(ip_addr, mask):
    #net_addr
    net_addr = '.'.join(map(str, [int(ip_addr_octet) & int(mask_octet) for ip_addr_octet, mask_octet in zip(ip_addr.split('.'), mask.split('.'))]))
    
    #host_addr
    host_bit_mask = ''.join('1' if x == '0' else '0' for x in ''.join([format(int(mask_octet), '08b') for mask_octet in mask.split('.')]))
    host_bit_mask = [host_bit_mask[i:i+8] for i in range(0, len(host_bit_mask), 8)]
    host_addr = '.'.join(map(str, [int(ip_addr_octet) & int(host_bit_mask, 2) for ip_addr_octet, host_bit_mask in zip(ip_addr.split('.'), host_bit_mask)]))
    return net_addr, host_addr

# Unlucky Days
from datetime import date
from dateutil.rrule import rrule, DAILY, FR
 
def unlucky_days(year):
    return len(list(rrule(DAILY, dtstart=date(year, 1, 1), until=date(year, 12, 13), bymonthday=[13], byweekday=[FR])))

from datetime import date
from dateutil.rrule import rrule, DAILY, FR
 
def unlucky_days(year):
    count = 0
    for day_date in rrule(DAILY, dtstart=date(year, 1, 1), until=date(year, 12, 13), bymonthday=[13], byweekday=[FR]):
            count +=1
    return count
    
import calendar
from datetime import date
from dateutil.rrule import rrule, DAILY
 
def unlucky_days(year):
    max_day = calendar.monthrange(year,12)[1]
    count = 0
    for day_date in rrule(DAILY, dtstart=date(year, 1, 1), until=date(year, 12, max_day)):
        if day_date.weekday() == 4 and day_date.day == 13:
            count +=1
    return count
    
# So Many Permutations!
import itertools

def permutations(string):
    seen = set()
    seen_add = seen.add
    return [''.join(i) for i in itertools.permutations(list(string)) if not (i in seen or seen_add(i))]
    
# Opposite number
def opposite(number):
    return -number

# Roman Numerals Encoder
def solution(n):
    ints = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
    nums = ('M', 'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I')
    result = []
    for i in range(len(ints)):
        count = int(n / ints[i])
        result.append(nums[i] * count)
        n -= ints[i] * count
    return ''.join(result)

# Nested List Depth
def list_depth(l):
    if l == []:
        return 1
    elif isinstance(l, list):
        return 1 + max(list_depth(item) for item in l)
    else:
        return 0
        
# Conference Traveller
def conference_picker(cities_visited, cities_offered):
    for city_offered in cities_offered:
        if city_offered not in cities_visited:
            return city_offered
    return 'No worthwhile conferences this year!'
            
            
# validDate Regex
import re
valid_date = re.compile('(\\[)(((0[1-9]|1[0-2])-([01][1-9]|10|2[0-8]))|((0[13-9]|1[0-2])-(29|30))|((0[13578]|1[0-2])-31))(\\])')

# Base64 Encoding
from base64 import b64encode, b64decode

def repad(data):
    return data + "=" * (-len(data)%4)

def to_base_64(string):
    return b64encode(b'{0}'.format(string)).rstrip("=")
    
def from_base_64(string):
    return b64decode(b'{0}'.format(repad(string)))
    
# I love big nums and I cannot lie
from functools import cmp_to_key

def biggest(nums):
    
    def cmp(x, y):
        return -1 if x<y else ( 0 if x==y else 1)
    def maxnum(x):
        return ''.join(sorted((str(n) for n in x), key=cmp_to_key(lambda x,y:cmp(y+x, x+y))))
        
    return(str(int(maxnum(nums))))

# Days in the year
import calendar

def year_days(year):
    if calendar.isleap(year):
        return '{0} has 366 days'.format(year)
    else:
        return '{0} has 365 days'.format(year)
        
# Last
def last(*args):
    last = None
    try:
        last = args[-1][-1]
    except:
        last = args[-1]
    return last

# Return to Sanity
def mystery():
    results = {'sanity': 'Hello', 'TEST': 'TEST'}
    return results

def mystery():
    results = {'sanity': 'Hello'}
    return results

# Job Matching #1
def match(candidate, job):
    if 'min_salary' in candidate and 'max_salary' in job:
        if (candidate['min_salary'] - (candidate['min_salary'] / 10)) <= job['max_salary']:
            return True
        else:
            return False
    else:
        raise Exception('min_salary or max_salary npot set in candidate or job.')

# Remove the time
import re

def shorten_to_date(long_date):
    return re.sub('(?<=[(?:Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday|Tues|Thur|Thurs|Sun|Mon|Tue|Wed|Thu|Fri|Sat)\s(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Sept|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)\s\d{1,2}]),\s\d{1,2}[p,a]m', '',long_date)
    
# Multiply
def multiply(a, b):
    for i in [a, b]:
        if i < 0:
            return None
    return a * b
    
    