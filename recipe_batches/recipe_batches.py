#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  batches = 0
  amounts = []
  for rec_key, rec_val in recipe.items():
    for ing_key, ing_val in ingredients.items():
      if len(recipe) != len(ingredients):
        return 0
      elif rec_key == ing_key and ing_val >= rec_val:
        print(f'recipe:{rec_key}:{rec_val}, amount on hand:{ing_key}:{ing_val}')
        amount = int(ing_val/rec_val)
        print(f'{amount}') #add an array to push these values to, and then sort by lowest, if lowest greater than 1 return
        amounts.append(amount)
       
  amounts.sort()
  print(f'amounts:{amounts}')
  batches = amounts[0]    
  return amounts[0]

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))