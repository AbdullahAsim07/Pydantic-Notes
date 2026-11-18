<div align="center">
	<img src="https://readme-typing-svg.herokuapp.com?font=Fira%20Code&amp;size=28&amp;duration=2500&amp;pause=800&amp;color=4F8EF7&amp;center=true&amp;vCenter=true&amp;width=650&amp;lines=Pydantic+v2+Practice+Repository%3BData+Validation+and+Serialization+with+Python" alt="Pydantic v2 Practice Repository — Data Validation and Serialization with Python" width="650" />
</div>

<div align="center">
  
	<a href="https://www.python.org/">
		<img src="https://img.shields.io/badge/Python-3.12%2B-blue?logo=python&amp;logoColor=white" alt="Python 3.12+" />
	</a>
	<a href="https://docs.pydantic.dev/latest/">
		<img src="https://img.shields.io/badge/Pydantic-v2.0+-green?logo=pydantic&amp;logoColor=white" alt="Pydantic v2" />
	</a>
	<a href="https://fastapi.tiangolo.com/">
		<img src="https://img.shields.io/badge/FastAPI-Ready-009688?logo=fastapi&amp;logoColor=white" alt="FastAPI Ready" />
	</a>
	<a href="LICENSE">
		<img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="MIT License" />
	</a>
</div>

---

# 📝 Pydantic-Notes

> **By [`AbdullahAsim07`](https://github.com/AbdullahAsim07)**

Welcome to the **Pydantic-Notes** repository! This project is a hands-on, example-driven guide to mastering data validation, serialization, and advanced modeling with **Pydantic v2**. Each file is a focused lesson, packed with best practices, real-world patterns, and modern Python techniques.

---

## 🏗️ Pydantic V2 Data Validation & Serialization Pipeline

```mermaid
flowchart LR
		A[📥 Raw Input Data] --> B[🛡️ Before Field Validators]
		B --> C[🔄 Type Coercion & Field Constraints]
		C --> D[🧪 After Field Validators]
		D --> E[🏷️ Model Validators]
		E --> F[🧮 Computed Fields]
		F --> G[📤 Serialization (Dict/JSON)]
```

---

## 📂 Repository Structure

| 📄 **File**              | 🧩 **Core Concept**                | 🏷️ **Key Decorators/Features**                | 🎯 **Learning Outcome**                                      |
|--------------------------|------------------------------------|-----------------------------------------------|-------------------------------------------------------------|
| `1.Pydantic.py`          | BaseModel & Field Constraints      | `BaseModel`, `Field`, `Optional`, `List`, `EmailStr` | Type safety, field validation, constraints, defaults         |
| `2.field_validator.py`   | Field-Level Validation             | `@field_validator` (`mode='before'`, `mode='after'`) | Custom field validation logic, pre/post processing           |
| `3.model_validator.py`   | Model-Level (Cross-Field) Validation | `@model_validator(mode='after')`              | Enforce rules across multiple fields                        |
| `4.compute_validator.py` | Computed/Derived Fields            | `@computed_field`, `@property`                 | Dynamic calculations (e.g., BMI)                            |
| `4.nested_model.py`      | Nested/Hierarchical Models         | Nested `BaseModel` classes                     | Model complex, hierarchical data structures                 |
| `serialization.py`       | Model Serialization                | `model_dump()`, `model_dump_json()`, options   | Export models to dict/JSON, include/exclude fields          |

---

## 🚀 Quick Start

```bash
# 1️⃣ Clone the repository
git clone https://github.com/AbdullahAsim07/Pydantic-Notes.git
cd Pydantic-Notes

# 2️⃣ Create & activate a virtual environment
python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate

# 3️⃣ Install dependencies
pip install --upgrade pip
pip install "pydantic[email]"

# 4️⃣ Run any example script
python 1.Pydantic.py
```

---

## 💡 Code Showcase: Patient Model Example

<details>
<summary>🔎 <b>Expand for a complete Patient Model with Field, Model Validator, and Computed Field</b></summary>

```python
from pydantic import BaseModel, Field, model_validator, computed_field
from typing import Optional

class Patient(BaseModel):
		name: str = Field(..., max_length=50, description="Full name")
		age: int = Field(..., ge=0, le=120)
		weight_kg: float = Field(..., gt=0)
		height_cm: float = Field(..., gt=0)
		emergency_contact: Optional[str] = Field(None, max_length=15)

		@model_validator(mode='after')
		def check_emergency_contact(cls, values):
				age = values.get('age')
				contact = values.get('emergency_contact')
				if age is not None and age < 18 and not contact:
						raise ValueError('Minors must provide an emergency contact.')
				return values

		@computed_field
		@property
		def bmi(self) -> float:
				return round(self.weight_kg / ((self.height_cm / 100) ** 2), 2)

# Example usage
patient = Patient(name="Alice", age=17, weight_kg=60, height_cm=165, emergency_contact="1234567890")
print(patient.bmi)  # 22.04
```

</details>

---

## 📄 License

This repository is licensed under the [MIT License](LICENSE).

---

<div align="center">
	⭐️ If you found this project helpful, please consider <b>starring</b> the repo!
</div>
