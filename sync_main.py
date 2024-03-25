import requests
import datetime


def download_image(number: int) -> None:
    print(f"start {number}")
    response = requests.get("https://www.python.org/static/img/python-logo.png")
    if response.status_code == 200:
        with open(f"static/image{number}.png", "wb") as f:
            f.write(response.content)

    print(f"stop {number}")


def main(count: int) -> None:
    for i in range(count):
        download_image(i)


if __name__ == "__main__":
    before = datetime.datetime.now()
    main(5)
    print(datetime.datetime.now() - before)
