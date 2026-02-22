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
            if(density and speed):
                response_parsed.append({"time_tag": time_tag, "density": float(density), "speed": float(speed)})
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
            if(bz):
                response_parsed.append({"time_tag": time_tag, "bz": float(bz)})
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
            if(kp):
                response_parsed.append({"time_tag": time_tag, "kp": float(kp)})
            else:
                continue
        return response_parsed
    else:
        raise Exception(f"Failed to fetch Kp index datas from {url}, status code: {response.status_code}")