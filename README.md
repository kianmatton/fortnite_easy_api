This is an easy and free to use library for experienced developers and beginners
This file will be used as documentation
use 
from fortnite_easy_api import item_search to import item search
then you can look up an item by using
item_search.name(the name of your item here) will return a dictionary
item_search.identifier(the identifier of your item here) will return a dictionary
item_search.rarity(rarity here legendary,epic,rare,uncommen,common) will return a list of dictionaries
item_search.cost(cost here) will return a list of dictionaries

you can use a dictionary by using for example

item = item_search.name('Ark')
print(item['cost']) will print the cost
print(item['identifier']) will print the id of the item etc.

the values that come with an item are:
identifier
name
type
rarity
cost
description
image_transparent
image_background
image_info
 
you can use from fortnite_easy_api import shop

then use

store = shop.get(specify a language here eg. en) will return a list of dictionaries
the to iterate over the items use
for item in store:
    print(item['name']) to print the name for every item in the shop

the values that come with a shop item are:
identifier
name
type
rarity
cost
featured
image_transparent
image_background
image_info

to look up player information you can use
from fortnite_easy_api import user_search
then use

playerinfo = user_search.getstats(specify platform pc, psn, xbox and specify the name you want to look up)
then use:
solo_stats = playerinfo['solo'] to get the solo stats
and then for example
print(solo_stats['wins']) to print the amount of wins

more functions for the recent matches of a user and weapon statistic lookups will come soon