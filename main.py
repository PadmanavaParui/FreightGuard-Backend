from fastapi import FastAPI#, HTTPException
# from pydantic import BaseModel
import razorpay
import numpy as np
from scipy.optimize import linear_sum_assignment
import uvicorn

app = FastAPI(title="FreightGuard Escrow Engine")

USE_MOCK_RAZORPAY = True

# TODO: Drop your Razorpay Test Keys here for the demo
rzp_client = razorpay.Client(auth=("rzp_test_YOUR_KEY", "YOUR_SECRET"))

LARGE_PENALTY = 999999

# --- MOCK DATA ---
loads = [
    {"id": "L1", "weight": 500, "payout": 2000},  # 500kg, ₹2000 payout
    {"id": "L2", "weight": 1200, "payout": 5500},
    {"id": "L3", "weight": 800, "payout": 3200}
]

trucks = [
    {"id": "T1", "max_capacity": 600, "driver_rating": 4.8},
    {"id": "T2", "max_capacity": 1500, "driver_rating": 4.9},
    {"id": "T3", "max_capacity": 1000, "driver_rating": 4.2}
]

@app.post("/run-logistics-engine")
def run_engine():
    print("\n[SYSTEM] Initializing Bipartite Matching Algorithm...")
    
    num_loads = len(loads)
    num_trucks = len(trucks)
    
    # Building the Cost Matrix (Infinity = incompatible match)
    # cost_matrix = np.full((num_loads, num_trucks), np.inf)
    # LARGE_PENALTY = 999999
    cost_matrix = np.full((num_loads, num_trucks), LARGE_PENALTY, dtype = float)
    
    for i, load in enumerate(loads):
        for j, truck in enumerate(trucks):
            if truck["max_capacity"] >= load["weight"]:
                # Optimization logic: Prefer higher rated drivers, penalize wasted capacity
                wasted_space = truck["max_capacity"] - load["weight"]
                rating_penalty = (5.0 - truck["driver_rating"]) * 100
                cost_matrix[i, j] = wasted_space + rating_penalty

    print(f"[ENGINE] Cost Matrix Built:\n{cost_matrix}")

    # Executing Hungarian Algorithm
    row_ind, col_ind = linear_sum_assignment(cost_matrix)
    
    matches = []
    print("\n[SYSTEM] Triggering Razorpay Escrow Creation...")
    
    for i, j in zip(row_ind, col_ind):
        if cost_matrix[i, j] != LARGE_PENALTY:
            load = loads[i]
            truck = trucks[j]
            
            # Creating the Razorpay Order (Escrow Hold)
            try:
                order_data = {
                    "amount": load["payout"] * 100, # Razorpay expects paise
                    "currency": "INR",
                    "receipt": f"escrow_{load['id']}_{truck['id']}",
                    "notes": {"truck_id": truck["id"], "load_id": load["id"]}
                }
                # order = rzp_client.order.create(data=order_data)
                
                if USE_MOCK_RAZORPAY:
                    order = {"id": f"mock_order_{load['id']}_{truck['id']}"}
                else:
                    order = rzp_client.order.create(data = order_data)

                match_result = {
                    "load_id": load["id"],
                    "truck_id": truck["id"],
                    "escrow_order_id": order["id"],
                    "status": "FUNDS_LOCKED_IN_ESCROW"
                }
                matches.append(match_result)
                print(f"[SUCCESS] Matched {load['id']} -> {truck['id']} | Escrow ID: {order['id']}")
                
            except Exception as e:
                print(f"[ERROR] Razorpay API failed: {e}")


    #adding summary block, after the loop execution
    print("\n" + "="*50)
    print("    FREIGHTGUARD OPTIMIZATION COMPLETE")
    print("="*50)
    for m in matches:
        print(f"    COMPLETED : {m['load_id']} -> {m['truck_id']} | {m['status']}")
        print(f"    Escrow ID: {m['escrow_order_id']}")
    print("="*50)


    return {"status": "success", "optimized_matches": matches}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)