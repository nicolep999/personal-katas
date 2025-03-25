import os
import django
from django.db.models import Q, Count, F

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Profile, Product, Order

# Create queries within functions


def populate_db():
    profile1 = Profile.objects.create(
        full_name="John Doe",
        email="jVnGp@example.com",
        phone_number="1234567890",
        address="123 Main Street",
        is_active=True,
    )
    profile2 = Profile.objects.create(
        full_name="Jane Doe",
        email="8V2Z0@example.com",
        phone_number="9876543210",
        address="456 Elm Street",
        is_active=False,
    )

    product1 = Product.objects.create(
        name="Product 1",
        description="Description for Product 1",
        price=9.99,
        in_stock=10,
        is_available=True,
    )
    product2 = Product.objects.create(
        name="Product 2",
        description="Description for Product 2",
        price=19.99,
        in_stock=5,
        is_available=False,
    )

    order1 = Order.objects.create(
        profile=profile1,
        total_price=29.98,
        is_completed=True,
    )
    order2 = Order.objects.create(
        profile=profile2,
        total_price=9.99,
        is_completed=False,
    )
    order1.products.add(product1, product2)
    order2.products.add(product1)


def get_profiles(search_string=None):
    if search_string is None:
        return ""
    profiles = (
        Profile.objects.filter(
            Q(email__icontains=search_string)
            | Q(full_name__icontains=search_string)
            | Q(phone_number__icontains=search_string)
        )
        .order_by("full_name")
        .annotate(orders_count=Count("order"))
    )
    if not profiles.exists():
        return ""
    result = [
        f"Profile: {profile.full_name}, email: {profile.email}, phone number: {profile.phone_number}, orders: {profile.orders_count}"
        for profile in profiles
    ]

    return "\n".join(result)


def get_loyal_profiles():
    loyal_profiles = Profile.objects.get_regular_customers()
    if not loyal_profiles.exists():
        return ""
    result = []
    for profile in loyal_profiles:
        result.append(f"Profile: {profile.full_name}, orders: {profile.order_count}")
    return "\n".join(result)


def get_last_sold_products():
    last_order = Order.objects.last()
    if not last_order:
        return ""
    products = last_order.products.all().order_by("name")
    return f"Last sold products: {', '.join([product.name for product in products])}"


def get_top_products() -> str:
    top_products = (
        Product.objects.annotate(
            orders_count=Count("order"),
        )
        .filter(
            orders_count__gt=0,
        )
        .order_by(
            "-orders_count",
            "name",
        )[:5]
    )

    if not top_products.exists():
        return ""

    return "Top products:\n" + "\n".join(
        f"{p.name}, sold {p.orders_count} times" for p in top_products
    )


def apply_discounts():
    orders = Order.objects.annotate(total_products=Count("products")).filter(
        total_products__gt=2, is_completed=False
    )
    updated_orders = 0
    if orders:
        updated_orders = orders.update(
            total_price=F("total_price") - (10 / 100) * F("total_price")
        )

    return f"Discount applied to {updated_orders} orders."


def complete_order():
    order = Order.objects.filter(is_completed=False).first()

    if not Order.objects.all() or not order:
        return ""

    for product in order.products.all():
        if product.is_available:
            product.in_stock -= 1

            if product.in_stock == 0:
                product.is_available = False

            product.save()

    order.is_completed = True
    order.save()

    return f"Order has been completed!"
