# Copyright 2016 Hme
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Library General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

"""
Basic python keywords
"""

import os
import re
import sys
import datetime



print ("Hello")


if __name__ == "__main__":

    print(sys.version_info)
    print(sys.version)

    print(sys.platform)
    print("test")
    print(2 ** 100)

    # print est une fonction
    i = 5
    mykey= "temps"
    fois = 20
    print ('%d et le mot \'%s\' apparaissent %d fois,' % (i, mykey, fois))
    text = " c'est le texte"
    text1= 'c:\\user\\val'
    text2="""c'est le texte avec  triple-quote C:\\user """
    print (text)
    print (text1)
    print (text2)

    var = 10
    while True:
        var -=1
        if (var ==6):
            continue
        print (var)
        if(var == 0):
            break
    print ("end loop")


    trips = {'last': None, 'current': None, 'max' : 0 , 'avg' : 0}


    date_now = trips['current']= str(datetime.datetime.now())[0:19]
    print (date_now)
    print (trips)

    with open('random.bin', 'wb') as f:
        f.write(os.urandom(255))

    a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    print('First four:', a[:4])
    print('Last four: ', a[-4:])
    print('Middle two:', a[3:-3])

    first_twenty_items = a[:20]
    print (first_twenty_items)
    last_twenty_items = a[-20:]
    print(last_twenty_items)
    zero_twenty_items = a[-0:]
    print(zero_twenty_items)

    print ('Before' , a)
    a[2:7]=[99,22,14]
    print ('After', a)

    b= a[:]    #copy of a
    print('B est', b)

    a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    print("position impaire", a[::2])
    print("position a partir de la fin", a[::-2])

    a = [1,2,3,4,5,6,7,8,9,10]
    squares = [x**2 for x in a]
    print (squares)

    squares = map(lambda x:x**2,a)
    b =list(squares)
    print (b)

    even_squares = [x**2 for x in a if x % 2 ==0]
    print (even_squares)

    chile_ranks = {'ghost': 1, 'habanero': 2, 'cayenne': 3}
    rank_dict = {rank: name for name, rank in chile_ranks.items()}
    chile_len_set = {len(name) for name in rank_dict.values()}
    print(rank_dict)
    print(chile_len_set)
























