# Numpy

Modules that has to be imported

```py
import numpy as np
```

## 1D Arrays

Can contain only one type
Accept operations (+, -, \*, /, ...)

```py
height = [1.73, 1.68, 1.71, 1.89, 1.79]
weight = [65.4, 59.2, 63.6, 88.4, 68.7]

np_height = np.array(height)
np_weight = np.array(weight)

bmi = np_weight / np_height**2 # [21.85171573 20.97505669 21.75028214 24.7473475  21.44127836]
bmi[1] # 20.97505669
bmi > 23 # [False False False True False]
bmi[bmi > 23] # 24.7473475

python_list = [1, 2, 3]
numpy_array = np.array([1, 2, 3])

python_list + python_list # [1, 2, 3, 1, 2, 3]
numpy_array + numpy_array # [2, 4, 6]
```

## 2D Arrays

```py
np_2d = np.array([[1.73, 1.68, 1.71], [65.4, 59.2, 63.6]])
np_2d.shape # (2, 3)
np_2d[0][2] # 1.71
np_2d[0, 2] # 1.71
# Select multiple
np_2d[:, 1:3] # # [[ 1.68  1.71 ] [ 59.2  63.6 ]]
```

## Methods

```py
height = np.round(np.random.normal(1.75, 0.20, 5000), 2)
weight = np.round(np.random.normal(60.32, 15, 5000), 2)
np_city = np.column_stack((height, weight))
np.mean(np_city[:, 0]) # 1.7472
np.median(np_city[:, 0]) # 1.75
np.corrcoef(np_city[:, 0], np_city[:, 1]) # Correlation coefficient
np.std(np_city[:, 0]) # Standard deviation
```

## Data sourcing

- Structured data `csv`, `json`, `xml`, `xlsx` files
- Unstructured data `pdf`, `docx`, `txt`, `xlsx` files
- Binary and proprietary data `?` files
- databases
- websites
- API endpoints
