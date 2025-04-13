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

## Deployment
This application is hosted on Heroku.

You can access it directly by visiting the following URL:

## Credits

- The images used on this website are sourced from various platforms. Below are the appropriate credits for each image:

- Much of the database setup and management structure for this project was inspired by the Database Management Systems walkthrough provided by [Code Institute]