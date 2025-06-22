from itertools import combinations
from math import radians, sin, cos, sqrt, atan2
from typing import List, Tuple, Dict


def haversine(coord1: Tuple[float, float], coord2: Tuple[float, float]) -> float:
    lon1, lat1 = coord1
    lon2, lat2 = coord2
    EarthR = 6371

    phi1, phi2 = radians(lat1), radians(lat2)
    dphi = radians(lat2 - lat1)
    dlambda = radians(lon2 - lon1)

    a = sin(dphi / 2) ** 2 + cos(phi1) * cos(phi2) * sin(dlambda / 2) ** 2
    return 2 * EarthR * atan2(sqrt(a), sqrt(1 - a))


def find_distant_street_pairs(
    edges: List[Tuple[Tuple[float, float], Tuple[float, float], str]],
    min_distance_km: float = 10
) -> List[Tuple[Tuple[str, str], float]]:
    street_coords: Dict[str, List[Tuple[float, float]]] = {}
    for start, end, name in edges:
        if name:
            street_coords.setdefault(name, []).extend([start, end])

    street_centers = {
        name: (
            sum(c[0] for c in coords) / len(coords),
            sum(c[1] for c in coords) / len(coords)
        )
        for name, coords in street_coords.items()
    }

    distant_pairs = []
    for (name1, coord1), (name2, coord2) in combinations(street_centers.items(), 2):
        dist = haversine(coord1, coord2)
        if dist >= min_distance_km:
            distant_pairs.append(((name1, name2), dist))

    distant_pairs.sort(key=lambda x: -x[1])
    return distant_pairs