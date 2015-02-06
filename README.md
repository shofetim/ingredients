# Ingredient Parsing Library

A library of one function `parse`.

Given a product ingredient label, such as:

> Soy Protein Isolate, Calcium Citrate, Phytonutrient Blend (Carrot, Tomato,
> Broccoli, Cabbage, Spinach), Soy Lecithin, Enzyme Blend (Bromelain, Papain),
> Natural Flavors

Extract the ingredients:

broccoli, bromelain, cabbage, calcium, carrot, papain, soy lecithin, soy
protein, spinach, tomato


## How to Use

```python
from ingredients import parse

label = 'Organic Whole Grain Kamut Wheat.'
print parse(label)

label ="""
   Soy Protein Isolate, Calcium Citrate, Phytonutrient Blend (Carrot, Tomato,
   Broccoli, Cabbage, Spinach), Soy Lecithin, Enzyme Blend (Bromelain, Papain),
   Natural Flavors."""
print parse(label)

label = """Milled Wheat, Rye, Triticale, Oats, Oat Bran, Corn, Barley,
           Soya Beans, Brown Rice, Millet, Flax Seeds
print parse(label)

```

## Rational

I needed to extract structured information from ingredient labels, and was
unable to find any good solutions. It proved to take longer then desired to
develop the ingredient list, so I thought it may be of value to others.


## Contributions Welcome!

Please use a pull request. To add ingredients see the ingredients-list file.
