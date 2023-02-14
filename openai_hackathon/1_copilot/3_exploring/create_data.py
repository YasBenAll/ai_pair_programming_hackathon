import numpy as np
import pandas as pd

COLUMNS = ["Agriculture", "Beverages", "Cosmetics"]

N_COLS = len(COLUMNS)
N_ROWS = 50

COUNTRIES = np.array(["UK", "US", "EU", "JP", "RU", "TK", "PRC", "MX"])

np.random.seed(42)

df = pd.DataFrame(np.random.randint(0, 10, size=(N_ROWS, N_COLS)), columns=COLUMNS)
df.index = COUNTRIES[np.random.randint(0, len(COUNTRIES), N_ROWS)]


with open("trade.csv", "w") as f:
    df.to_csv(f, index=True)
