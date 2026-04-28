# FreightGuard
### Algorithmic Matching + Escrow for Micro-Logistics
**Google Solutions Challenge 2026 | Open Innovation Track**
**Team:** Padmanava Parui & Aditya Kumar Thakur

---

## The Problem : 
> *"Why is booking cargo vehicles harder than passenger transport?"*
> **Razorpay Fix My Itch — Score: 92.1/100 (Highest in Logistics)**

Unlike passenger transport, cargo matching involves complex constraints
(weight, volume, driver ratings) and a massive trust deficit.
Shippers fear non-delivery, and drivers refuse routes without
guaranteed payment.

---

## The Solution:
FreightGuard is an API-first Logistics Escrow Engine.
We replace the manual "call-an-agent" model with two layers:

1. **Algorithmic Matching** — Hungarian Algorithm matches pending
   loads to available trucks based on weight capacity, wasted space
   minimization, and driver ratings. 
2. **Financial Trust** — The moment a match is confirmed, the
   shipper's funds are locked into a Razorpay Escrow Order.
   Funds release only on delivery confirmation.

---

## Tech Stack 
| Layer | Technology |
|-------|-----------|
| Backend | FastAPI (Python) |
| Optimization | NumPy + SciPy `linear_sum_assignment` |
| FinTech | Razorpay Orders API |
| Testing | Swagger UI / OpenAPI |
| Infra | GitHub Codespaces |

---

## How to Run

**1. Clone the repo**
```bash
git clone https://github.com/your-repo/FreightGuard-Backend
cd FreightGuard-Backend
```

**2. Install dependencies**
```bash
pip install fastapi uvicorn scipy numpy razorpay
```

**3. Run the server**
```bash
python main.py
```

**4. Open Swagger UI**
> http://localhost:8000/docs

**5. Hit the endpoint**
- Click `POST /run-logistics-engine`
- Click "Try it out" → "Execute"
- Watch the terminal for the optimization output

---

## Sample Output
```json
{
  "status": "success",
  "optimized_matches": [
    {
      "load_id": "L1",
      "truck_id": "T1",
      "escrow_order_id": "mock_order_L1_T1",
      "status": "FUNDS_LOCKED_IN_ESCROW"
    }
  ]
}
```

---

## Roadmap
| Phase | Timeline | Feature |
|-------|----------|---------|
| Phase 1 [Completed] | Today | Matching engine + Razorpay escrow |
| Phase 2 | Next Round | Google Maps Geofencing — auto payment release on delivery |
| Phase 3 | Production | ML dynamic pricing, multi-city, fleet analytics |

---

## Why This Matters
India's logistics sector loses billions annually to inefficient
matching and payment disputes. FreightGuard solves both in a
single API call.