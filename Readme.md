Project 2: Fast-Food Chain Menu API (Talha)

Topic Description: This project involves creating an API to manage the menu of a fast-food restaurant.
 You will handle menu items, their descriptions, prices, and categories.

Core Features (API Endpoints to Implement):

GET /api/menu: Retrieve a list of all menu items. The response should include the item name, price, and category.

GET /api/menu/{itemId}: Get detailed information for a single menu item using its unique ID. This should include the item name, description, price, and ingredients.

POST /api/menu: Add a new item to the menu. The request body will contain the new item's details (name, price, etc.). This endpoint requires authentication.

PUT /api/menu/{itemId}: Update the price or description of an existing menu item. This endpoint requires authentication.

DELETE /api/menu/{itemId}: Remove an item from the menu. This endpoint requires authentication.

POST /api/menu/{itemId}/purchase: New Feature. "Purchase" a specific menu item. This endpoint should update the stock level of the item and create a new transaction record. This endpoint requires authentication.

GET /api/menu/receipt/{transactionId}: New Feature. Get a receipt for a specific menu item purchase.
