# Simple Shipping Cost Calculator

This is a basic Python script that calculates shipping costs using three different shipping methods based on the weight of a package in pounds:

- **Ground Shipping**
- **Ground Shipping Premium**
- **Drone Shipping**

## 📦 Shipping Rates

### Ground Shipping
| Weight (lb)       | Rate per lb | Flat Charge |
|-------------------|-------------|-------------|
| Less than 2       | $1.50       | $20         |
| 2 - 6             | $3.00       | $20         |
| 6 - 10            | $4.00       | $20         |
| Over 10           | $4.75       | $20         |

### Ground Shipping Premium
- **Flat rate:** $125 (regardless of weight)

### Drone Shipping
| Weight (lb)       | Rate per lb | Flat Charge |
|-------------------|-------------|-------------|
| Less than 2       | $4.50       | None        |
| 2 - 6             | $9.00       | None        |
| 6 - 10            | $12.00      | None        |
| Over 10           | $14.25      | None        |

## 💻 How to Use

1. Clone or download this repository.
2. Open the Python script (`shipping_calculator.py`) in your code editor.
3. Modify the `weight` variable at the top of the file to test different package weights:
   ```python
   weight = 41.5
