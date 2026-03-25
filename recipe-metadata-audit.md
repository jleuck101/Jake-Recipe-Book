# Recipe Metadata Audit

## Strategy Summary
- Keep structured metadata first: `cuisine`, `dishType`, `base`, `mainIngredient`, and `equipment` should carry most of the filter/search value in the current app.
- Use tags as a small overlay for cross-cutting browse concepts that are not already covered by structured fields or free-text search.
- Be conservative: many recipes need structured field completion more than additional tags.

## Recurring Issues
- Missing `dishType` on 86 recipes.
- Missing `equipment` on 96 recipes.
- Missing `base` on 55 recipes.
- Missing `cuisine` on 51 recipes.
- Missing `mainIngredient` on 43 recipes.
- Tags are sparse by design: 96 recipes currently have no tags, which is fine if the tag layer stays intentionally small.
- A few tags look like one-off title/location labels rather than reusable browse concepts.
- Several recipes appear to need structured corrections before any tag decisions, for example the tonkatsu protein assignment.

## Recommended Tag Set To Use Sparingly
- `Meal Prep`
- `Copycat`
- `Freezer Friendly`
- `High Protein`
- `One Pot`
- `Party Food`
- `Comfort Food`

## Audit Table

| Recipe Title | Current Cuisine | Current Dish Type | Current Base | Current Main Ingredient | Current Equipment | Current Tags | Suggested Structured Changes | Suggested Catch-All Tags | Suggested Remove/Merge | Reason | Priority | My Decision | Final Approved Metadata |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 30-Minute Chicken with Lemon Butter Sauce (And It Cooks in One Pan!) |  |  |  | Chicken |  |  | dishType: Sauce / Dressing | One Pot |  | Structured metadata is underfilled; these fields are directly filterable in the current app. | High |  |  |
| Albondigas (Mexican Meatball Soup) | Mexican |  | No Base / Standalone | Beef |  |  | equipment: Blender |  |  | Structured metadata is underfilled; these fields are directly filterable in the current app. | Medium |  |  |
| Arroz Con Leche (Mexican Rice Pudding) | Mexican | Dessert | Rice |  |  |  |  |  |  | Current metadata is workable; no high-value changes stand out beyond optional cleanup. | Low |  |  |
| Atole De Avena (Oatmeal Drink) | Mexican | Drink |  |  |  |  | base: Dough / Batter \| equipment: Food Processor |  |  | Structured metadata is underfilled; these fields are directly filterable in the current app. | High |  |  |
| Beef, Bacon, Cheese and Peppers | Mexican |  |  |  |  |  | mainIngredient: Beef |  |  | Structured metadata is underfilled; these fields are directly filterable in the current app. | High |  |  |
| Best Migas Recipe (Quick and Easy) | Spanish |  |  |  |  |  |  |  |  | Current metadata is workable; no high-value changes stand out beyond optional cleanup. | High |  |  |
| Butter Chicken | Indian |  |  | Chicken |  |  |  |  |  | Current metadata is workable; no high-value changes stand out beyond optional cleanup. | High |  |  |
| Butter Chicken (Murgh Makhani) | Indian |  |  | Chicken |  |  |  |  |  | Current metadata is workable; no high-value changes stand out beyond optional cleanup. | High |  |  |
| Butter-Basted Chicken Breasts |  | Dinner | No Base / Standalone | Chicken |  |  |  |  |  | Current metadata is workable; no high-value changes stand out beyond optional cleanup. | Low |  |  |
| CANES-STYLE SAUCE (Closest Copycat) |  | Sauce / Dressing |  |  |  | Copycat Recipe |  | Copycat | Copycat Recipe -> Copycat | Normalize the copycat tag to a shorter exact-match label. | High |  |  |
| Chicken and Sausage Gumbo | Cajun |  |  | Chicken; Sausage |  |  | dishType: Dinner \| base: Soup / Stew / Curry | Comfort Food |  | Structured metadata is underfilled; these fields are directly filterable in the current app. | High |  |  |
| Chicken and Vermicelli Soup with Lime |  |  | Pasta / Noodles; Soup / Stew / Curry | Chicken |  |  |  |  |  | Current metadata is workable; no high-value changes stand out beyond optional cleanup. | High |  |  |
| Chicken Au Poivre |  |  |  | Chicken |  |  | cuisine: French \| base: No Base / Standalone |  |  | Structured metadata is underfilled; these fields are directly filterable in the current app. | High |  |  |
| Chicken Burrito | Mexican |  |  |  |  |  | dishType: Dinner \| base: Tortilla / Wrap \| mainIngredient: Chicken | Freezer Friendly |  | Structured metadata is underfilled; these fields are directly filterable in the current app. | High |  |  |
| Chicken Burritos with Cilantro Lime Rice | Mexican |  |  |  |  |  | dishType: Dinner \| base: Rice \| mainIngredient: Chicken | Freezer Friendly |  | Structured metadata is underfilled; these fields are directly filterable in the current app. | High |  |  |
| Chicken Cutlets |  |  | No Base / Standalone | Chicken |  |  |  |  |  | Current metadata is workable; no high-value changes stand out beyond optional cleanup. | High |  |  |
| Chicken Meatballs in a Cream Sauce (Tefteli) |  |  |  |  |  |  | dishType: Sauce / Dressing \| base: No Base / Standalone \| mainIngredient: Chicken |  |  | Structured metadata is underfilled; these fields are directly filterable in the current app. | High |  |  |
| Chicken Meatballs, Italian Style | Italian |  | No Base / Standalone | Chicken |  |  |  |  |  | Current metadata is workable; no high-value changes stand out beyond optional cleanup. | Low |  |  |
| Chicken Milanese |  |  | No Base / Standalone | Chicken |  |  |  |  |  | Current metadata is workable; no high-value changes stand out beyond optional cleanup. | High |  |  |
| Chicken Piccata |  | Dinner | No Base / Standalone | Chicken |  |  |  |  |  | Current metadata is workable; no high-value changes stand out beyond optional cleanup. | Low |  |  |
| Chicken Potpie with Cornbread Biscuits |  |  |  | Chicken |  |  | dishType: Dinner | Comfort Food |  | Structured metadata is underfilled; these fields are directly filterable in the current app. | High |  |  |
| Chicken Pozole Verde | Mexican |  |  |  |  |  | mainIngredient: Chicken |  |  | Structured metadata is underfilled; these fields are directly filterable in the current app. | High |  |  |
| Chicken Satay |  |  |  | Chicken |  |  | cuisine: Southeast Asian \| dishType: Dinner \| base: No Base / Standalone |  |  | Structured metadata is underfilled; these fields are directly filterable in the current app. | High |  |  |
| Chicken Souvlaki with Tzatziki Sauce and Greek Salad | Greek |  |  |  |  |  | dishType: Sauce / Dressing \| mainIngredient: Chicken |  |  | Structured metadata is underfilled; these fields are directly filterable in the current app. | High |  |  |
| Chicken Tagine with Pistachios, Dried Figs, and Chickpeas |  |  |  | Chicken |  |  | cuisine: North African \| dishType: Dinner \| base: Soup / Stew / Curry | Comfort Food |  | Structured metadata is underfilled; these fields are directly filterable in the current app. | High |  |  |
| Chicken Tikka Masala Recipe | Indian |  |  | Chicken |  |  |  |  |  | Current metadata is workable; no high-value changes stand out beyond optional cleanup. | High |  |  |
| Chicken with Garlic-Chili-Ginger Sauce |  |  |  | Chicken |  |  | dishType: Sauce / Dressing \| base: Soup / Stew / Curry | Comfort Food |  | Structured metadata is underfilled; these fields are directly filterable in the current app. | High |  |  |
| Chile Relleno | Mexican |  | No Base / Standalone | Cheese / Dairy |  |  |  |  |  | Current metadata is workable; no high-value changes stand out beyond optional cleanup. | Low |  |  |
| Chocolate PB Protein Baked Oats + Cheesecake Swirl |  | Breakfast | Dough / Batter |  | Oven | Meal Prep |  | Freezer Friendly; High Protein |  | Suggested tags add cross-cutting browse value beyond the structured filters. | Medium |  |  |
| Chole Samosa Chaat | Indian |  |  |  |  |  |  |  |  | Current metadata is workable; no high-value changes stand out beyond optional cleanup. | High |  |  |
| Chopped Cheese |  |  | Bread / Bun | Beef |  |  |  |  |  | Current metadata is workable; no high-value changes stand out beyond optional cleanup. | High |  |  |
| Choripán (Argentinian Chorizo Sandwich) | South American |  | Bread / Bun | Sausage |  |  | dishType: Dinner |  |  | Structured metadata is underfilled; these fields are directly filterable in the current app. | Medium |  |  |
| Chorizo Potato Crispy Tacos | Mexican |  |  |  |  |  | dishType: Dinner \| base: Tortilla / Wrap \| mainIngredient: Sausage |  |  | Structured metadata is underfilled; these fields are directly filterable in the current app. | High |  |  |
| Completos (Chilean Hot Dogs) | South American |  | Bread / Bun | Sausage |  |  | dishType: Dinner |  |  | Structured metadata is underfilled; these fields are directly filterable in the current app. | Medium |  |  |
| Cottage Pie |  |  |  |  |  |  |  | Freezer Friendly |  | Suggested tags add cross-cutting browse value beyond the structured filters. | High |  |  |
| Creamy Black Bean Soup Recipe (Sopa De Frijoles) | Mexican |  | Soup / Stew / Curry | Beans / Lentils |  |  |  |  |  | Current metadata is workable; no high-value changes stand out beyond optional cleanup. | Low |  |  |
| Creamy Cajun-Style Chicken Pasta | Cajun |  | Pasta / Noodles | Chicken |  |  | dishType: Dinner |  |  | Structured metadata is underfilled; these fields are directly filterable in the current app. | Medium |  |  |
| Creamy Garlic Chicken |  | Dinner | No Base / Standalone | Chicken |  |  |  |  |  | Current metadata is workable; no high-value changes stand out beyond optional cleanup. | Low |  |  |
| Creamy Turmeric Pasta |  |  | Pasta / Noodles |  |  |  | dishType: Dinner |  |  | Structured metadata is underfilled; these fields are directly filterable in the current app. | High |  |  |
| Creamy White Chili |  |  | Soup / Stew / Curry | Chicken |  |  | dishType: Dinner | Comfort Food |  | Structured metadata is underfilled; these fields are directly filterable in the current app. | High |  |  |
| Crisp Chicken Schnitzel with Lemony Herb Salad |  |  |  | Chicken |  |  |  |  |  | Current metadata is workable; no high-value changes stand out beyond optional cleanup. | High |  |  |
| Easy Burritos Recipe | Mexican |  |  |  |  |  | dishType: Dinner \| base: Tortilla / Wrap | Freezer Friendly |  | Structured metadata is underfilled; these fields are directly filterable in the current app. | High |  |  |
| Frida’s Crunchwraps | Mexican; Tex-Mex | Dinner | Tortilla / Wrap | Beef |  |  |  |  |  | Current metadata is workable; no high-value changes stand out beyond optional cleanup. | Low |  |  |
| Frijoles Refritos (Refried Beans) | Mexican |  |  |  |  |  | mainIngredient: Beans / Lentils \| equipment: Blender |  |  | Structured metadata is underfilled; these fields are directly filterable in the current app. | High |  |  |
| Garlicky Chicken with Lemon-Anchovy Sauce Recipe |  |  |  | Chicken |  |  | dishType: Sauce / Dressing |  |  | Structured metadata is underfilled; these fields are directly filterable in the current app. | High |  |  |
| Gyudon (Japanese Simmered Beef and Rice Bowls) | Japanese |  | Rice | Beef |  |  | dishType: Dinner | Freezer Friendly |  | Structured metadata is underfilled; these fields are directly filterable in the current app. | Medium |  |  |
| Honey Garlic Gochujang Chicken Bowl with Chili Oil Egg |  |  |  |  |  |  | dishType: Dinner \| base: Soup / Stew / Curry \| mainIngredient: Chicken | Comfort Food |  | Structured metadata is underfilled; these fields are directly filterable in the current app. | High |  |  |
| Honey-Garlic Chicken |  |  |  |  |  |  | mainIngredient: Chicken |  |  | Structured metadata is underfilled; these fields are directly filterable in the current app. | High |  |  |
| How to Make an Easy & Delightful Mexican Vegetable Soup | Mexican |  | Soup / Stew / Curry |  |  |  |  |  |  | Current metadata is workable; no high-value changes stand out beyond optional cleanup. | High |  |  |
| How to Make Chicken Tacos | Mexican |  |  |  |  |  | dishType: Dinner \| base: Tortilla / Wrap \| mainIngredient: Chicken |  |  | Structured metadata is underfilled; these fields are directly filterable in the current app. | High |  |  |
| How to Make Homemade Beef Tamales | Mexican |  |  |  |  |  | mainIngredient: Beef |  |  | Structured metadata is underfilled; these fields are directly filterable in the current app. | High |  |  |
| How to Make Mexican Pasta Soup with Spinach | Mexican |  |  |  |  |  | dishType: Dinner \| base: Soup / Stew / Curry | Freezer Friendly |  | Structured metadata is underfilled; these fields are directly filterable in the current app. | High |  |  |
| How to Make Mole Poblano (Quick and Easy Recipe) | Mexican |  |  |  |  |  |  |  |  | Current metadata is workable; no high-value changes stand out beyond optional cleanup. | High |  |  |
| How to Make Tacos Al Pastor at Home │Surprise Your Family Today! |  |  |  |  |  |  | dishType: Dinner \| base: Tortilla / Wrap |  |  | Structured metadata is underfilled; these fields are directly filterable in the current app. | High |  |  |
| Instant Pot Chicken Tinga (No-Blend) | Mexican |  | Tortilla / Wrap | Chicken | Instant Pot | Meal Prep |  |  |  | Current metadata is workable; no high-value changes stand out beyond optional cleanup. | Low |  |  |
| Julia Child's Creamy Chicken and Mushroom (Lightened Up) |  |  |  |  |  |  | mainIngredient: Chicken |  |  | Structured metadata is underfilled; these fields are directly filterable in the current app. | High |  |  |
| Korean Bbq-Style Meatballs |  |  |  | Beef |  |  | base: No Base / Standalone | Freezer Friendly |  | Structured metadata is underfilled; these fields are directly filterable in the current app. | High |  |  |
| Lemon Herbed Greek Chicken Wraps & Garlic Cucumber Tzatziki | Greek |  |  | Chicken |  |  | dishType: Dinner \| base: Tortilla / Wrap |  |  | Structured metadata is underfilled; these fields are directly filterable in the current app. | High |  |  |
| Lemony Hummus Pasta |  |  | Pasta / Noodles |  |  |  | dishType: Dinner \| mainIngredient: Beans / Lentils |  |  | Structured metadata is underfilled; these fields are directly filterable in the current app. | High |  |  |
| Light and Fluffy Buttermilk Pancakes | American (general) | Breakfast | Dough / Batter |  |  |  |  |  |  | Current metadata is workable; no high-value changes stand out beyond optional cleanup. | Low |  |  |
| Make Your Own Genuine Cornish Pasty \| Cornish Pasty Association \| Genuine Cornish Pasty : Cornish Pasty Association |  |  |  |  |  |  |  | Freezer Friendly |  | Suggested tags add cross-cutting browse value beyond the structured filters. | High |  |  |
| Marinated Chicken for Tacos & More |  |  |  |  |  |  | dishType: Dinner \| base: Tortilla / Wrap \| mainIngredient: Chicken |  |  | Structured metadata is underfilled; these fields are directly filterable in the current app. | High |  |  |
| Marry Me Chicken Recipe |  |  |  | Chicken |  |  |  | Freezer Friendly |  | Suggested tags add cross-cutting browse value beyond the structured filters. | High |  |  |
| Mayo-Marinated Chicken with Chimichurri Recipe |  |  |  |  |  |  | mainIngredient: Chicken |  |  | Structured metadata is underfilled; these fields are directly filterable in the current app. | High |  |  |
| Microwave Sticky Toffee Pudding |  | Dessert |  |  | Microwave |  |  | Comfort Food |  | Suggested tags add cross-cutting browse value beyond the structured filters. | High |  |  |
| Moroccan-Spiced Chicken Meatballs |  |  | No Base / Standalone | Chicken |  |  |  |  |  | Current metadata is workable; no high-value changes stand out beyond optional cleanup. | High |  |  |
| Nashville Hot Chicken Sandwich |  |  | Bread / Bun | Chicken |  | Nashville | dishType: Dinner |  | Nashville | City tag looks one-off unless you intentionally build a larger city-style tag cluster. | High |  |  |
| No-Waste Tacos De Carnitas with Salsa Verde | Mexican |  | Tortilla / Wrap | Pork |  |  | dishType: Dinner |  |  | Structured metadata is underfilled; these fields are directly filterable in the current app. | Medium |  |  |
| One Pan Spanish Chicken and Rice | Spanish |  |  |  |  |  | dishType: Dinner \| base: Rice \| mainIngredient: Chicken | One Pot |  | Structured metadata is underfilled; these fields are directly filterable in the current app. | High |  |  |
| Oyakodon (Japanese Chicken and Egg Rice Bowl) | Japanese |  | Rice | Chicken; Egg |  |  |  |  |  | Current metadata is workable; no high-value changes stand out beyond optional cleanup. | Low |  |  |
| Pambazo (Mexican Chorizo and Potato Sandwich) | Mexican |  | Bread / Bun | Sausage |  |  | dishType: Dinner |  |  | Structured metadata is underfilled; these fields are directly filterable in the current app. | Medium |  |  |
| Parmesan-Crusted Chicken |  |  |  | Chicken |  |  |  |  |  | Current metadata is workable; no high-value changes stand out beyond optional cleanup. | High |  |  |
| Pasta E Ceci (Italian Pasta and Chickpea Stew) | Italian |  |  |  |  |  | dishType: Dinner \| base: Soup / Stew / Curry \| mainIngredient: Beans / Lentils |  |  | Structured metadata is underfilled; these fields are directly filterable in the current app. | High |  |  |
| Pasta with Spicy Sausage, Broccoli Rabe and Chickpeas |  |  | Pasta / Noodles | Sausage |  |  | dishType: Dinner |  |  | Structured metadata is underfilled; these fields are directly filterable in the current app. | High |  |  |
| Peri Peri Chicken and Rice (Nando's Peri Peri Sauce!) |  |  |  |  |  |  | cuisine: South African \| dishType: Sauce / Dressing \| base: Rice \| mainIngredient: Chicken | Copycat |  | Structured metadata is underfilled; these fields are directly filterable in the current app. | High |  |  |
| Philly Cheesesteak |  |  | Bread / Bun | Beef |  | Philadelphia | dishType: Dinner | Freezer Friendly | Philadelphia | City tag looks one-off and is already covered by the recipe title/search. | High |  |  |
| Placeholder | Italian-American; Italian; Chinese; Korean; Thai; Vietnamese; Middle Eastern; French; Mediterranean; Caribbean; Southern (us); Central American; South American; Eastern European; German / Austrian; North African; West African; Filipino; Indonesian / Malaysian; Indian; Pakistani; South Asian (other); British / Irish | Lunch; Dinner; Breakfast; Dessert; Side; Dip / Spread; Sauce / Dressing; Snack; Drink; Cocktail; Prep / Pantry; Appetizer | Pasta / Noodles; Bread / Bun; Rice; Soup / Stew / Curry; Tortilla / Wrap; Grains (other); Potatoes; Salads / Greens; Dough / Batter; Pita / Flatbread | Lamb; Veg-Forward; Cheese / Dairy; Tofu / Tempeh; Shellfish; Fish; Chicken; Pork; Turkey; Mushroom | Air Fryer; Grill; No-Cook; Blender; Food Processor; Slow Cooker; Rice Cooker |  |  |  |  | Current metadata is workable; no high-value changes stand out beyond optional cleanup. | Low |  |  |
| Quick Esquites (Elote-Style Corn in a Cup) — 10 oz, One-Pan | Mexican | Side |  | Veg-Forward |  |  |  |  |  | Current metadata is workable; no high-value changes stand out beyond optional cleanup. | Low |  |  |
| Rotel Dip | Tex-Mex | Dip / Spread |  |  |  |  |  | Party Food |  | Suggested tags add cross-cutting browse value beyond the structured filters. | High |  |  |
| Serious Eats' Halal Cart-Style Chicken and Rice with White Sauce | Middle Eastern |  |  | Chicken |  |  | dishType: Sauce / Dressing \| base: Rice |  |  | Structured metadata is underfilled; these fields are directly filterable in the current app. | High |  |  |
| Smashed Chicken Burgers with Cheddar and Parsley |  |  | Bread / Bun | Chicken |  |  | dishType: Dinner |  |  | Structured metadata is underfilled; these fields are directly filterable in the current app. | High |  |  |
| Sopa De Habas (Creamy Fava Bean Soup) | Mexican |  | Soup / Stew / Curry |  |  |  | mainIngredient: Beans / Lentils \| equipment: Blender |  |  | Structured metadata is underfilled; these fields are directly filterable in the current app. | High |  |  |
| Sorta Samin's Netflix Buttermilk Chicken with Pistachio Pesto |  |  |  | Chicken |  |  |  |  |  | Current metadata is workable; no high-value changes stand out beyond optional cleanup. | High |  |  |
| Spaghetti Verde | Mexican |  | Pasta / Noodles |  |  |  |  |  |  | Current metadata is workable; no high-value changes stand out beyond optional cleanup. | High |  |  |
| Spanish Migas with Fried Eggs | Spanish |  |  |  |  |  |  |  |  | Current metadata is workable; no high-value changes stand out beyond optional cleanup. | High |  |  |
| Spicy Peri-Peri Chicken Rice Bowl |  |  | Rice | Chicken |  |  |  |  |  | Current metadata is workable; no high-value changes stand out beyond optional cleanup. | High |  |  |
| Sticky Coconut Chicken and Rice |  |  | Rice | Chicken |  |  | dishType: Dinner |  |  | Structured metadata is underfilled; these fields are directly filterable in the current app. | High |  |  |
| Stir-Fried Chicken with Ketchup |  |  |  | Chicken |  |  |  |  |  | Current metadata is workable; no high-value changes stand out beyond optional cleanup. | High |  |  |
| Strip Steak with Dijon Sauce |  | Dinner | No Base / Standalone | Beef |  |  |  |  |  | Current metadata is workable; no high-value changes stand out beyond optional cleanup. | Low |  |  |
| Super-Garlicky Extra-Creamy Peri-Peri Chicken & Broccoli Pasta |  |  | Pasta / Noodles | Chicken |  |  | dishType: Dinner |  |  | Structured metadata is underfilled; these fields are directly filterable in the current app. | High |  |  |
| Sweet Corn Tamales with a Savory Filling | Mexican |  |  |  |  |  |  |  |  | Current metadata is workable; no high-value changes stand out beyond optional cleanup. | High |  |  |
| The Best Chili | American (general) |  | Soup / Stew / Curry | Beef; Pork |  |  | dishType: Dinner | Comfort Food |  | Structured metadata is underfilled; these fields are directly filterable in the current app. | Medium |  |  |
| The Best Chili Ever |  |  | Soup / Stew / Curry |  |  |  | dishType: Dinner | Comfort Food |  | Structured metadata is underfilled; these fields are directly filterable in the current app. | High |  |  |
| The Best Crispy Roast Potatoes Ever |  | Side | Potatoes |  | Oven |  | mainIngredient: Veg-Forward | Comfort Food |  | Structured metadata is underfilled; these fields are directly filterable in the current app. | Medium |  |  |
| The Best Turkey Meatloaf |  |  | No Base / Standalone | Turkey |  |  | dishType: Dinner | Comfort Food |  | Structured metadata is underfilled; these fields are directly filterable in the current app. | High |  |  |
| The Commerce Inn Patty Melt |  |  | Bread / Bun | Beef |  |  |  |  |  | Current metadata is workable; no high-value changes stand out beyond optional cleanup. | High |  |  |
| The Mole Enchiladas That Led to 3 Marriages in My Family | Mexican |  | Tortilla / Wrap | Chicken |  |  |  |  |  | Current metadata is workable; no high-value changes stand out beyond optional cleanup. | Low |  |  |
| Tonkatsu (Japanese Breaded Pork Cutlets) | Japanese |  |  | Chicken |  |  | dishType: Dinner \| base: No Base / Standalone \| mainIngredient: Pork |  | Chicken from Main Ingredient | Current main ingredient appears incorrect for tonkatsu. | High |  |  |
| Tortilla Soup | Mexican |  |  |  |  |  | base: Soup / Stew / Curry \| equipment: Blender |  |  | Structured metadata is underfilled; these fields are directly filterable in the current app. | High |  |  |
| Weeknight Chicken Tagine |  |  |  | Chicken |  |  | cuisine: North African \| dishType: Dinner \| base: Soup / Stew / Curry | Comfort Food |  | Structured metadata is underfilled; these fields are directly filterable in the current app. | High |  |  |
| White Chicken Chili |  |  | Soup / Stew / Curry | Chicken |  |  | dishType: Dinner | Comfort Food |  | Structured metadata is underfilled; these fields are directly filterable in the current app. | High |  |  |
