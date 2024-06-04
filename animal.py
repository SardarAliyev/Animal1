import requests

# Konfiqurasiya
BASE_URL = "https://your-server-url.com/api"  # Server URL-ni dəyişdirin

def get_orders(limit=100):
    """
    Yüz sifarişin id-si haqqında məlumat tələb edən funksiya.
    """
    try:
        response = requests.get(f"{BASE_URL}/orders?limit={limit}")
        response.raise_for_status()
        return response.json()  # Sifarişlərin siyahısını JSON formatında qaytarır
    except requests.exceptions.RequestException as e:
        print(f"Error fetching orders: {e}")
        return []

def get_pet_info(order_id):
    """
    Verilən sifariş id-si üçün ev heyvanı haqqında məlumat əldə edən funksiya.
    """
    try:
        response = requests.get(f"{BASE_URL}/orders/{order_id}/pet")
        response.raise_for_status()
        return response.json()  # Ev heyvanı haqqında məlumatı JSON formatında qaytarır
    except requests.exceptions.RequestException as e:
        print(f"Error fetching pet info for order {order_id}: {e}")
        return None

def process_orders_with_pet_info():
    """
    Sifarişləri işləyən və ev heyvanı haqqında məlumat olan sifarişlər üçün nəticə verən funksiya.
    """
    orders = get_orders()
    if not orders:
        print("No orders retrieved.")
        return

    for order in orders:
        order_id = order.get("id")
        pet_info = get_pet_info(order_id)
        if pet_info:
            pet_id = pet_info.get("id")
            print(f"Order {order_id} for pet {pet_id}")

if __name__ == "__main__":
    process_orders_with_pet_info()
