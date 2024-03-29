from fake_useragent import UserAgent
import requests
import json

ua = UserAgent()
def collect_data(type):

    offset = 0
    batch_size = 60
    result = []
    count = 0

    while True:
        for item in range(offset, offset + batch_size, 60):
            url = f"https://cs.money/1.0/market/sell-orders?limit=60&maxPrice=2&minPrice=1&offset={item}&type={type}"
            response = requests.get(
                url=url,
                headers={"user-agent": f"{ua.random}"}
            )

            offset += batch_size
            data = response.json()
            items = data.get("items")

            print(items)
            if items is not None:
                for i in items:
                    discount = i.get("pricing").get("discount")
                    if discount is not None and discount > 0.01:
                        item_full_name = i.get("asset").get("names").get("short")
                        item_3d = i.get("asset").get("images").get("steam")
                        item_price = i.get("pricing").get("computed")
                        item_discount = round(
                            i.get("pricing").get("discount") / i.get("pricing").get(
                            "priceBeforeDiscount") * 100,
                            3
                        )
                        result.append({
                            "full_name": item_full_name,
                            "3d": item_3d,
                            "price": item_price,
                            "discount": item_discount
                        })
        count += 1
        print(f"Page #{count}")
        print(f"url={url}")
        if items is None:
            break
        if len(items) < 60:
            break
    result = sorted(result, key=lambda x: x["discount"])
    with open("api/result.json", "w", encoding="utf-8") as file:
        json.dump(result, file, indent=4, ensure_ascii=False)

    print(len(result))



def main():
    collect_data()


if __name__ == "__main__":
    main()