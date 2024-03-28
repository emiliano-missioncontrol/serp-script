from googlesearch import search
from urllib.parse import urlparse

MAX_RESULTS = 25

SLEEP_INTERVAL = 9

TARGET_DOMAIN = "missioncontrol.com.mx"

queries = [
    "mission control",
    "yamaha yc61 precio",
    "mcintosh rs150",
    "tornamesa mcintosh",
    "mision control",
    "blue microphones",
    "yamaha hs7",
    "missioncontrol",
    "stagepas 600bt",
    "yamaha yc61",
    "dali spektor 2",
    "mcintosh mt5",
    "tornamesa mcintosh mt5",
    "yamaha hs5",
    "yamaha hs8",
    "mission control switch",
    "amplificador mcintosh",
    "mcintosh ma12000",
    "blue spark",
    "chandler limited",
    "microfonos blue",
    "monitores yamaha hs5",
    "amplificador carver",
    "mcintosh mc275",
    "mcintosh tornamesa",
    "cambridge cxn 100",
    "cambridge cxn v2",
    "blue mics",
    "mcintosh mha50",
    "tocadiscos mcintosh",
    "blue dragonfly mic",
    "yamaha revstar rss02t",
    "blue spark sl",
    "blue mouse microphone",
    "dynaudio lyd 7",
    "mcintosh mt5-6",
    "dynaudio lyd 8",
    "misioncontrol",
    "anthem mrx 1140",
    "anthem avr",
    "audifonos mcintosh",
    "yamaha mg10xu",
    "mcintosh audio",
    "mx123",
    "mc intosh",
    "yamaha ck61",
    "dali 3",
    "marantz",
    "rs150"
]


def isTargetDomain(url):
    parsed_url = urlparse(url)
    return parsed_url.netloc == TARGET_DOMAIN


def main():
    for query in queries:
        results = search(query, num_results=MAX_RESULTS,
                         sleep_interval=5, lang="es")
        print(query + ": ")
        for idx, result in enumerate(results):
            if (isTargetDomain(result)):
                print("\tPosición: " + str(idx + 1))


if __name__ == "__main__":
    main()
