import requests
from datetime import datetime

def fetch_solarWind(url):
    response = requests.get(url)
    if(response.status_code == 200):
        response_parsed = []
        for datas in response.json()[1:]:
            time_tag = datetime.strptime(datas[0], "%Y-%m-%d %H:%M:%S.%f").isoformat()
            density = datas[1]
            speed = datas[2]
            if density is not None and speed is not None:
                response_parsed.append((time_tag, float(density), float(speed)))
            else:
                continue
        return response_parsed
    else:
        raise Exception(f"Failed to fetch plasma datas from {url}, status code: {response.status_code}")


def fetch_mag(url):
    response = requests.get(url)
    if(response.status_code == 200):
        response_parsed = []
        for datas in response.json()[1:]:
            time_tag = datetime.strptime(datas[0], "%Y-%m-%d %H:%M:%S.%f").isoformat()
            bz = datas[3]
            if bz is not None:
                response_parsed.append((time_tag, float(bz)))
            else:
                continue
        return response_parsed
    else:
        raise Exception(f"Failed to fetch magnetic field datas from {url}, status code: {response.status_code}")


def fetch_kp(url):
    response = requests.get(url)
    if(response.status_code == 200):
        response_parsed = []
        for datas in response.json()[1:]:
            time_tag = datetime.strptime(datas[0], "%Y-%m-%d %H:%M:%S.%f").isoformat()
            kp = datas[1]
            if kp is not None:
                response_parsed.append((time_tag,float(kp)))
            else:
                continue
        return response_parsed
    else:
        raise Exception(f"Failed to fetch Kp index datas from {url}, status code: {response.status_code}")