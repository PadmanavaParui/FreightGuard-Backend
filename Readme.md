# FreightGuard: Algorithmic Matching + Escrow for Micro-Logistics

**Google Solutions Challenge 2026 | Open Innovation Track**
**Team:** Padmanava Parui & Aditya Kumar Thakur

## The Problem : 
`Why is booking cargo vehicles harder than passenger transport?`
	- Razorpay "Itch" #1 (Score : 92.1)
	- Unlike passenger transport, cargo matching involves complex constraints (weight, volume, driver ratings) and a massive **trust deficit**. Shippers fear cargo theft, and gig-drivers refuse ad-hoc routes without guaranteed upfront payment.

## The Solution:
FreightGuard is an API-first Logistics Escrow Engine. We replace manual cargo-booking with a **Bipartite Matching Algorithm** and secure the transaction using automated **Razorpay Escrow**.
1. **Algorithmic Matching:** Uses the Hungarian Algorithm (`scipy.optimize.linear_sum_assignment`) to match an array of pending loads to available trucks based on capacity, wasted space minimization, and driver ratings. 
2. **Financial Trust:** The moment a match is made, the shipper's funds are locked into a Razorpay Order (Escrow). Funds are only released when delivery is confirmed. 

## Tech Stack 
* **Backend:** FastAPI (Python) 
* **Optimization Engine:** NumPy, SciPy (Linear Sum Assignment) 
* **FinTech Integration:** Razorpay API (Orders & Webhooks) 
* **Testing:** Swagger UI / OpenAPI

## How to Run the Prototype
1. **Install Dependencies:**
```bash
   pip install fastapi uvicorn scipy numpy razorpay
```
