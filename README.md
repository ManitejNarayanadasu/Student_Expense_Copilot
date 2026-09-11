# 💷 Student Expense Copilot

> An AI-powered personal expense analysis platform designed to help students
> understand their spending, discover financial patterns, and make smarter
> everyday decisions.

[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-150458?logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Status](https://img.shields.io/badge/Status-In%20Development-orange)]()

---

## 🎯 Project Overview

Managing personal finances as a student can be difficult.

Bank statements contain transaction descriptions that are often unclear,
making it difficult to understand where money is actually going.

**Student Expense Copilot** aims to solve this problem by transforming
raw financial transactions into meaningful spending information.

The long-term goal is to build a system that can:

- Automatically categorise expenses.
- Detect recurring payments.
- Analyse spending trends.
- Compare monthly expenses.
- Generate personalised financial insights.

Rather than relying on AI for every operation, the project will combine
traditional data processing, algorithms, and AI where each is most useful.

---

## 🏗️ Current Architecture

The current implementation focuses on the first stage of the data pipeline.

```text
Bank CSV
   │
   ▼
CSV Ingestion
   │
   ▼
Pandas DataFrame
   │
   ▼
Transaction Processing
   │
   ▼
Future Database