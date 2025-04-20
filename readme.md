# project4 Vintage Shop

## Background information
Vintage Shop is a minimalist web application designed for selling vintage clothing and accessories. The site organizes products into clear categories, making it easy for users to browse unique items and place orders.

Admins can manage inventory by logging in as a superuser, with the ability to add, edit, or delete products through a simple interface.

### Goals
- External user’s goal: Browse and purchase unique vintage clothing and accessories with ease.
- Site owner's goal: Manage and sell vintage items efficiently.

### User stories
- First Time Visitor Goals
    1. As a First-Time Visitor, I want to quickly understand that this website sells vintage clothing and accessories.

    2. As a First-Time Visitor, I want to easily navigate the site to browse available products.

    3. As a First-Time Visitor, I want to view product details including images, names, prices, categories, and descriptions.

- Returning Visitor Goals
    1. As a Returning Visitor, I want to search for products by category or by using the search bar.

    2. As a Returning Visitor, I want to add unique items to my shopping bag with a single click (no size or quantity selection needed).

    3. As a Returning Visitor, I want to create an account to save my delivery details and view past orders.

    4. As a Returning Visitor, I want to log in and out of my account securely.

    5. As a Returning Visitor, I want to check my shopping bag before making a purchase.

    6. As a Returning Visitor, I want to complete the checkout process easily, including providing delivery information and making payment.

    7. As a Returning Visitor, I want to view my order history and saved delivery details in my profile.


- Frequent Visitor Goals
    1. As a Returning Visitor, I want to search for products by category or by using the search bar.

    2. As a Returning Visitor, I want to add unique items to my shopping bag with a single click (no size or quantity selection needed).

    3. As a Returning Visitor, I want to create an account to save my delivery details and view past orders.

    4. As a Returning Visitor, I want to log in and out of my account securely.

    5. As a Returning Visitor, I want to check my shopping bag before making a purchase.

    6. As a Returning Visitor, I want to complete the checkout process easily, including providing delivery information and making payment.

    7. As a Returning Visitor, I want to view my order history and saved delivery details in my profile.

- Site Owner Goals
    1. As the Site Owner, I want to add new vintage items to the store through the admin interface.

    2. As the Site Owner, I want to edit or delete products when necessary.

    3. As the Site Owner, I want sold items to automatically disappear from the shop, since each product is one-of-a-kind.

    4. As the Site Owner, I want a simple, clean layout that doesn’t require tracking quantity or size.


## Features

### Homepage Features

- **Eye-Catching Background Image**: The homepage features a striking, vintage-style background image that sets the tone for the website and captures the user's attention instantly.

- **Website Branding (Top Left)**: The site name is displayed clearly on the top left corner of the page, giving users an immediate sense of identity.

- **User Account and Shopping Bag (Top Right)**: On the top right corner, users can access their account or view their shopping bag at any time. These options are consistently available across all pages for easy access.

- **Search Functionality**: A search box is prominently positioned below the header, allowing users to quickly find vintage items they’re looking for. This feature remains visible across the entire site.

- **Category Navigation**: Dropdown menus for **Clothing** and **Accessories** allow users to filter items by category. These menus are available on every page to support seamless browsing.

> Except for the homepage’s unique vintage background image, all these elements are consistently present throughout the site to ensure a user-friendly and intuitive experience.
### Products
- View all products with image, name, price, and category.
- Filter products by category using dropdowns or URL query.
- Search for products using keywords.
- Click on any item to view detailed information on the product detail page.

### Shopping Bag
- Add unique items to the bag (each product can only be added once).
- View contents of the bag from any page.
- Proceed to checkout or continue shopping.

### Checkout
- Fill in delivery details.
- Secure payment integration via Stripe.
- Order confirmation page on successful checkout.

### User Accounts
- Register for a new account.
- Sign in and out securely.
- Access personal profile with:
  - Default delivery info
  - Order history

### Site Management (Admin)
- Superusers can add, edit, or delete products through the Django admin panel.
- Product info includes name, category, description, price, image, and SKU.


## Techonologies Used
### Project Structure

The project is built using Django and follows a modular app-based structure. The main custom apps include:

- `home` – Handles the homepage and overall layout
- `products` – Manages product listings and product details
- `bag` – Implements shopping bag functionality
- `checkout` – Handles checkout, payment, and order confirmation
- `profiles` – Manages user profiles, order history, and default delivery info

Third-party packages used include `django-allauth` for authentication and `crispy-forms` for form styling.


## Design

### Color Scheme
- **Primary Colors:**
  - **Black**: Used for key elements such as buttons (`.shop-now-button`, `.btn-black`) and text (`.text-black`). This creates a bold, high-contrast look that emphasizes important actions and ensures readability against the vintage-style background.
  - **White**: Applied to the background overlay (`.overlay`), button text, and various other elements. White offers a clean, minimalist contrast that aligns with the vintage aesthetic and provides visual balance.

- **Button Colors:**
  - **Outline Button**: `.btn-outline-black` has a **white background** with a **black border** and **black text**. On hover, it reverses to provide a more interactive and engaging visual experience. This style is chosen to maintain a sleek, modern look while aligning with the overall color scheme.

### Typography
- **Font Family**: The site uses `'Libre Baskerville', serif`, which is a sophisticated and classic typeface. The choice reflects the vintage nature of the shop, providing a sense of elegance and timelessness that complements the product offering.
- **Text Color**: The default text color is **light grey (#555)** for readability, offering a softer, less stark contrast compared to pure black. This creates a more comfortable reading experience while still maintaining legibility.
- **Font Size**: Font sizes are set to be legible and user-friendly, ensuring a balance between aesthetics and functionality. Headings and buttons have slightly larger font sizes for emphasis and better user engagement.

### Wireframe

Below is the wireframe for this project:

- **Home page**
- **Dress page**
- **Product page**
- **Shopping bag page**
- **Checkout page**
- **Sign in page**
- **My profile page**
## Testing
### Homepage
This test ensures that all key elements on the homepage work correctly, including logo, search box, two category dropdowns, my account and shoping bag.
- **Logo**
- Clicking the logo redirects the user to the homepage.
- The logo is visible and styled correctly on all screen sizes.
- ![Screenshot of Logo](media/readme/home.png)
- **Search Box**
- Users can type into the search box.
- Submitting a query redirects to the products page with relevant results.
- ![Screenshot of Search Box](media/readme/search.png)
- **Category Dropdowns**
- The Clothing and Accessories dropdown menus are functional.
- Clicking a category link redirects to the filtered product list.
- Menus collapse/expand correctly on all screen sizes.
- ![Screenshot of Category Dropdowns1](media/readme/dropdown1.png)
- ![Screenshot of Category Dropdowns2](media/readme/dropdown2.png)
- **My Account Links**
- The link is visible in the navbar.
- It is linked to product management, signin/signout, and my profile.
- Redirects appropriately depending on whether the user is logged in or not:
  - Not Logged in: goes to the login/register page.
  -![Screenshot of My Account Not Logged In](media/readme/not_logged_in.png)
  -![Screenshot of Register](media/readme/register.png)
  -![Screenshot of Sign In](media/readme/sign_in.png)
  - Logged in: goes to the profile page.
  - ![Screenshot of My Account Link Logged In](media/readme/logged_in.png)
  - ![Screenshot of My Account Link My Profile](media/readme/my_profile.png)
- **Shopping Bag Icon**
- Clicking the icon redirects to the shopping bag page.
- Accurately displays total price if the bag is not empty.
- ![Screenshot of Shopping Bag Icon](path/to/your/shopping_bag.png)
- **Shop Now Button**
- A "Shop Now" button is present on the homepage and links correctly to the products listing page.
- ![Screenshot of Shopp Now button](path/to/your/shop_now.png)

### Product Page
This test ensures that all key elements on the product listing page are displayed correctly and link to the appropriate product detail pages.
- **Product Listings**
- All products are displayed on the page.  
- Each product includes the **name**, **price**, and **category**.  
- Product images are shown.
-- ![Screenshot of product listing page](path/to/your/product.png)
- **Navigation to Product Detail**
- Clicking on a product image or name redirects the user to the corresponding **product detail page**. 
-- ![Screenshot of product detail page](path/to/your/product_detail.png) 

### Product Detail Page

This test ensures that each individual product detail page displays the correct product information and provides functional interaction options.

-**Product Information**
- The **product name**, **price**, **category**, and **description** are clearly displayed.
- The product image is shown correctly, or a placeholder appears if no image is uploaded.

-**Action Buttons**
- **Add to Bag** button:
  - Clicking it adds the product to the shopping bag.
  - The shopping bag icon updates with the correct item count.

- **Keep Shopping** button:
  - Clicking it returns the user to the product listing page.
-- ![Screenshot of product detail page](path/to/your/product_detail.png) 

### Shopping Bag Page

This test ensures that all elements on the shopping bag page display correctly and work as intended.
-**Product Information**
#### Bag Contents
- Each item in the bag is listed with:
  - **Product name**
  - **Price**
  - **Remove** button

- Clicking the **Remove** button removes the item from the bag and updates the total accordingly.
- ![Screenshot of Shopping Bag Icon](path/to/your/shopping_bag.png)
- ![Screenshot of Delete an item](path/to/your/delete.png)
#### Action Buttons
- **Keep Shopping** button:
  - Redirects to the product listing page (`products` page).

- **Secure Checkout** button:
  - Redirects to the checkout page to complete the purchase.

### Check Out Page
This test ensures that all elements of the checkout process work as intended and that the page functions properly depending on user login status.

#### **Form Fields**

- Customer name, email address, delivery address, and payment details are all present.
- All form fields are required and validate user input.
- Appropriate error messages appear for missing or invalid fields.
#### **Order Summary**

- Displays all items in the bag with:
  - Product names
  - Individual prices
- Delivery fee is shown clearly.
- Total price (including delivery) is calculated correctly.

- ![Screenshot of check out page1](path/to/your/checkout1.png)

#### **Login Requirement**

- If the user is **not logged in**, they are prompted to:
  - Log in, or
  - Create an account
- Once authenticated, they are redirected back to the checkout page with their bag contents preserved.
- ![Screenshot of check out page2](path/to/your/checkout2.png)

### Product management
#### **Add Product**
From My Account, when Product Management clicked, users are directed to Add a Product page.
- ![Screenshot of add a product page1](path/to/your/project_management1.png)
- ![Screenshot of add a product page2](path/to/your/project_management2.png)
#### **Edit Product**

#### **Delete Product**

## Deployment
This application is hosted on Heroku.

You can access it directly by visiting the following URL:

## Credits

- The images used on this website are sourced from various platforms. Below are the appropriate credits for each image:

- Much of the database setup and management structure for this project was inspired by the Database Management Systems walkthrough provided by [Code Institute]