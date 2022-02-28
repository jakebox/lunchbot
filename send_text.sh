# curl -X POST \
#   --header "Content-Type: application/json" \
#   --header "Authorization: Bearer KEY017D6900D5CE1F9E3A37F3C50637B764_327Pr2tHI9UFyVlY7Kfv9X" \
#   --data '{
#     "from": "+12182203065",
#     "to": "+17734311992",
#     "text": "Hello, world!"
#   }' \
#   https://api.telnyx.com/v2/messages

curl -X POST \
  --header "Content-Type: application/json" \
  --header "Authorization: Bearer KEY017D6900D5CE1F9E3A37F3C50637B764_327Pr2tHI9UFyVlY7Kfv9X" \
  --data '{
    "from": "+12182203065",
    "to": "+17734311992",
    "text": "Monday: 11/29\n • Grilled Cheese, Tomato Soup and Broccoli \n• Vegetarian Spinach Florentine Lasagna with Roasted Vegetables and Garlic Bread"
  }' \
  https://api.telnyx.com/v2/messages

Monday: 11/29
 • Grilled Cheese, Tomato Soup and Broccoli

Tuesday: 11/30
 • Choice of Braised Pork or Southwest Chicken Burrito Bowl with Beans, Rice, Cheese, Sour Cream, and Fresh Salsa
 • Vegetarian Fajita Vegetable and Rice Burrito Bowl with Cheese, Sour Cream, and Fresh Salsa

Wednesday: 12/1
 • Curried Chicken over Basmati Rice with Cauliflower
 • Vegetarian Potato and Pea Samosa with Basmati Rice and Cauliflower

Thursday: 12/2
 • Citrus Glazed Salmon with Teriyaki Bok Choy and Jasmine Rice
 • Vegetarian Sweet Thai Chili Tofu over Jasmine Rice with Bok Choy

Friday: 12/3
 • Beef and Cheese Lasagna with Roasted Italian Vegetables and Garlic Bread
 • Vegetarian Spinach Florentine Lasagna with Roasted Vegetables and Garlic Bread
