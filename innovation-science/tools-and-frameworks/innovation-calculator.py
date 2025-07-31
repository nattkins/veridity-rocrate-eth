#!/usr/bin/env python3
"""
Innovation Science Calculator
Mathematical tools for analyzing breakthrough innovation viability
"""

def innovation_success_curve(constraint_complexity):
    """
    Model innovation success as function of constraint complexity
    Similar to bias-variance tradeoff in machine learning
    """
    # Underfitting region: too simple, no clear value
    if constraint_complexity < 2:
        underfitting_penalty = (2 - constraint_complexity) ** 2
        return max(0, 0.3 - underfitting_penalty * 0.15)

    # Overfitting region: too complex, becomes traditional solution
    elif constraint_complexity > 5:
        overfitting_penalty = (constraint_complexity - 5) ** 2
        return max(0, 0.2 - overfitting_penalty * 0.05)

    # Optimal zone: balanced complexity captures innovation value
    else:
        optimal_distance = abs(constraint_complexity - 3.5)
        return 0.9 - (optimal_distance ** 2 * 0.1)

def calculate_innovation_gospel_value(paradox_strength, peer_credibility, customer_readiness):
    """
    Calculate innovation success based on Gospel propagation model
    """
    miracle_impact = paradox_strength ** 1.5
    gospel_credibility = peer_credibility ** 2
    adoption_rate = customer_readiness ** 0.5

    gospel_value = miracle_impact * gospel_credibility * adoption_rate
    return min(1.0, gospel_value)

if __name__ == "__main__":
    print("Innovation Science Calculator")
    print("=" * 40)

    # Example: Spray-on dress analysis
    constraint_complexity = 3  # Mass producible + Unique + Luxury
    success_prob = innovation_success_curve(constraint_complexity)
    print(f"Spray-on dress constraint optimization: {success_prob:.2f}")

    # Example: Gospel value calculation
    gospel_value = calculate_innovation_gospel_value(0.8, 0.9, 0.7)
    print(f"Innovation gospel value: {gospel_value:.2f}")

