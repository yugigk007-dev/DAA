from http.server import BaseHTTPRequestHandler
import json

def interpolation_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high and arr[low] <= target <= arr[high]:
        if low == high:
            return low if arr[low] == target else -1

        if arr[high] == arr[low]:
            break

        pos = low + int(((target - arr[low]) * (high - low))
                        / (arr[high] - arr[low]))

        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    return -1


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        arr = [2, 5, 10, 15, 23, 35, 48, 60, 75, 90, 105, 120]
        target = 35

        index = interpolation_search(arr, target)

        response = {
            "array": arr,
            "target": target,
            "index": index
        }

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()

        self.wfile.write(json.dumps(response).encode())