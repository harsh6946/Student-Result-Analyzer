---

# 📂 Project 3: Student Result Analyzer

**Files to create:**  
- `result.py`  
- `README.md`  

---

### `result.py`
```python
def calculate_result(marks):
    total = sum(marks)
    percentage = total / len(marks)
    
    if percentage >= 90:
        grade = "A+"
    elif percentage >= 75:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 40:
        grade = "C"
    else:
        grade = "Fail"
    
    return total, percentage, grade

# Example usage
marks = [85, 92, 78, 88, 90]
total, percentage, grade = calculate_result(marks)

print(f"📊 Total Marks: {total}")
print(f"📈 Percentage: {percentage:.2f}%")
print(f"🏆 Grade: {grade}")
