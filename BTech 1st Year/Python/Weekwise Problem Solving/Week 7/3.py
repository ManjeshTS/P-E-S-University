# Function to apply discounts
def apply_discount(base_price, discount_rate=0.10, loyalty_discount=0.05, promo_discount=0.03, is_member=False, is_promo_day=False):
    price_after_discount = base_price * (1 - discount_rate)
    if is_member:
        price_after_discount *= (1 - loyalty_discount)
    if is_promo_day:
        price_after_discount *= (1 - promo_discount)
    return price_after_discount

# Function to add service charges
def add_service_charge(discounted_price, service_type="dine-in", dine_in_charge=5, takeout_rate=0.02):
    if service_type == "dine-in":
        total_price = discounted_price + dine_in_charge
    elif service_type == "takeout":
        total_price = discounted_price * (1 + takeout_rate)
    else:
        raise ValueError("Invalid service type. Use 'dine-in' or 'takeout'.")
    return total_price

# Function to calculate the final price
def calculate_final_price(base_price, service_type="dine-in", tax_rate=0.08, luxury_tax_rate=0.02, luxury_threshold=100, is_member=False, is_promo_day=False):
    # Step 1: Apply discounts
    discounted_price = apply_discount(base_price, is_member=is_member, is_promo_day=is_promo_day)

    # Step 2: Add service charge
    price_with_service_charge = add_service_charge(discounted_price, service_type=service_type)

    # Step 3: Apply tax
    final_price = price_with_service_charge * (1 + tax_rate)
    if base_price > luxury_threshold:
        final_price *= (1 + luxury_tax_rate)
    
    return round(final_price, 2)


print("Scenario 1: Regular customer, dine-in")
print(calculate_final_price(120, service_type="dine-in"))

print("\nScenario 2: Member, takeout, promo day")
print(calculate_final_price(80, service_type="takeout", is_member=True, is_promo_day=True))

print("\nScenario 3: Non-member, dine-in, no promo")
print(calculate_final_price(150, service_type="dine-in", is_member=False, is_promo_day=False))

print("\nScenario 4: High-value order, member, takeout")
print(calculate_final_price(200, service_type="takeout", is_member=True, is_promo_day=False))