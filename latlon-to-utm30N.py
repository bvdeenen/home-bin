import math
import pyperclip
import re
from notify import notification


def latlon_to_utm30n(lat, lon):
    """Convert lat/lon to UTM Zone 30N (Easting, Northing)"""
    a = 6378137.0
    f = 1 / 298.257223563
    k0 = 0.9996
    b = a * (1 - f)
    e2 = 1 - (b**2 / a**2)
    e_prime2 = e2 / (1 - e2)

    lon0 = -3.0
    phi = math.radians(lat)
    lam = math.radians(lon)
    lam0 = math.radians(lon0)

    sin_phi = math.sin(phi)
    cos_phi = math.cos(phi)
    tan_phi = math.tan(phi)

    N = a / math.sqrt(1 - e2 * sin_phi**2)
    T = tan_phi**2
    C = e_prime2 * cos_phi**2
    A = cos_phi * (lam - lam0)

    # Meridional arc
    M = a * (
        (1 - e2 / 4 - 3 * e2**2 / 64 - 5 * e2**3 / 256) * phi
        - (3 * e2 / 8 + 3 * e2**2 / 32 + 45 * e2**3 / 1024) * math.sin(2 * phi)
        + (15 * e2**2 / 256 + 45 * e2**3 / 1024) * math.sin(4 * phi)
        - (35 * e2**3 / 3072) * math.sin(6 * phi)
    )

    easting = (
        k0
        * N
        * (
            A
            + (1 - T + C) * A**3 / 6
            + (5 - 18 * T + T**2 + 72 * C - 58 * e_prime2) * A**5 / 120
        )
        + 500000
    )

    northing = k0 * (
        M
        + N
        * tan_phi
        * (
            A**2 / 2
            + (5 - T + 9 * C + 4 * C**2) * A**4 / 24
            + (61 - 58 * T + T**2 + 600 * C - 330 * e_prime2) * A**6 / 720
        )
    )

    return round(easting, 2), round(northing, 2)


def main():

    try:
        # Get text from clipboard
        text = pyperclip.paste().strip()

        # Try to extract lat, lon (handles commas, spaces, etc.)
        numbers = re.findall(r"-?\d+\.?\d*", text)
        if len(numbers) < 2:
            raise ValueError("Could not find two numbers in clipboard")

        lat = float(numbers[0])
        lon = float(numbers[1])

        # Convert
        easting, northing = latlon_to_utm30n(lat, lon)

        # Format result
        result = f"{easting}, {northing}"

        # Put back to clipboard
        pyperclip.copy(result)

        notification("to UTM", message=f"✅ Converted: {lat}, {lon}  →  {result}")

    except Exception as e:
        notification(
            "to UTM error",
            message=f"Make sure the clipboard contains something like: 41.05167, -0.03281",
        )


# ====================== MAIN ======================
if __name__ == "__main__":
    main()
