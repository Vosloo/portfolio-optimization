from pathlib import Path

class Asset:
    def __init__(self, path):
        self._path = Path(path)
        self._name = None
        self._data_points = None

    @property
    def path(self) -> Path:
        return self._path

    @property
    def name(self) -> str:
        if self._name is None:
            with open(self._path, 'r') as f:
                self._name = f.readline().strip()

        return self._name
    
    @property
    def data_points(self) -> list[float]:
        if self._data_points is None:
            with open(self._path, 'r') as f:
                lines = f.readlines()
            
            self._data_points = []
            for line in lines[2:]: # Skip first two lines with name and size
                _, value = line.strip().split()
                self._data_points.append(float(value))

        return self._data_points
