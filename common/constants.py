class Users:
    STANDARD_USERNAME = "standard_user"
    PROBLEM_USERNAME = "problem_user"
    PERFORMANCE_GLITCH_USERNAME = "performance_glitch_user"
    PASSWORD = "secret_sauce"
    EMPTY_USERNAME = ""
    EMPTY_PASSWORD = ""
    LOCKED_USERNAME = "locked_out_user"
    LOCKED_PASSWORD = "secret_sauce"


class Title:
    TITLE = "Swag Labs"


class Alerts:
    EMPTY_ALERT = "Epic sadface: Username is required"
    INVALID_DATA_ALERT = (
        "Epic sadface: Username and password do not match any user in this service"
    )
    LOCKED_USER_ALERT = "Epic sadface: Sorry, this user has been locked out."
    FIRSTNAME_REQUIRED = "Error: First Name is required"
    LASTNAME_REQUIRED = "Error: Last Name is required"
    POSTAL_CODE_REQUIRED = "Error: Postal Code is required"


class MainFooter:
    TWITTER = "Twitter"
    FACEBOOK = "Facebook"
    LINKEDIN = "LinkedIn"
    FOOTER_COPY = (
        "© 2020 Sauce Labs. All Rights Reserved. " "Terms of Service | Privacy Policy"
    )


class MainHeader:
    PRODUCT_LABEL = "Products"


class Cart:
    YOUR_CART = "Your Cart"
    REMOVE = "REMOVE"


class Product:
    NAME = "Sauce Labs Bike Light"
    DESCRIPTION = (
        "A red light isn't the desired state in testing but it sure "
        "helps when riding your bike at night. Water-resistant with 3 "
        "lighting modes, 1 AAA battery included."
    )
    PRICE = "$9.99"


class SauceLabs:
    TITLE = "Cross Browser Testing, Selenium Testing, Mobile Testing | Sauce Labs"


class PersonalData:
    FIRSTNAME = "ALEXANDER"
    LASTNAME = "EVGRAFOV"
    POSTAL_CODE = "603106"


class CheckoutSubheader:
    CHECKOUT = "Checkout: Your Information"


class Overview:
    OVERVIEW = "Checkout: Overview"
    PAYMENT_INFO = "SauceCard #31337"
    SHIPPING_INFO = "FREE PONY EXPRESS DELIVERY!"


class Finish:
    FINISH = "Finish"
    COMPLETE_HEADER = "THANK YOU FOR YOUR ORDER"
    COMPLETE_TEXT = (
        "Your order has been dispatched, and "
        "will arrive just as fast as the pony can "
        "get there!"
    )


class Filter:
    AZ = "az"
    ZA = "za"
    LOHI = "lohi"
    HILO = "hilo"
