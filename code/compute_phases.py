#!/usr/bin/env python3
"""
Holographic Lattice Theory - Phase Pattern Calculator
Author: Ruqing Chen
Date: January 6, 2026
Repository: https://github.com/Ruqing1963/Mersenne-Prime-Prediction-M53-M60

This script computes normalized phase coordinates for Mersenne prime clusters.
"""

import numpy as np
import pandas as pd

# Known Mersenne prime exponents (M1-M52)
MERSENNE_EXPONENTS = [
    2, 3, 5, 7, 13,           # M1-M5
    17, 19, 31, 61, 89,       # M6-M10
    107, 127, 521, 607, 1279, # M11-M15
    2203, 2281, 3217, 4253, 4423,  # M16-M20
    9689, 9941, 11213, 19937, 21701,  # M21-M25
    23209, 44497, 86243, 110503, 132049,  # M26-M30
    216091, 756839, 859433, 1257787, 1398269,  # M31-M35
    2976221, 3021377, 6972593, 13466917, 20996011,  # M36-M40
    24036583, 25964951, 30402457, 32582657, 37156667,  # M41-M45
    42643801, 43112609, 57885161, 74207281, 77232917,  # M46-M50
    82589933, 136279841  # M51-M52
]

def compute_phase_coordinates(cluster):
    """
    Compute normalized phase coordinates for a 5-point cluster.
    
    φ_i = (n_{k+i} - n_k) / (n_{k+4} - n_k)
    
    Args:
        cluster: List of 5 consecutive Mersenne prime exponents
    
    Returns:
        List of 5 phase coordinates [0, φ_1, φ_2, φ_3, 1]
    """
    n_k = cluster[0]
    n_k4 = cluster[4]
    span = n_k4 - n_k
    
    if span == 0:
        return [0, 0, 0, 0, 0]
    
    phases = [(n - n_k) / span for n in cluster]
    return phases

def analyze_all_slices():
    """Analyze all 10 complete slices from M1-M50."""
    results = []
    
    for i in range(10):
        start_idx = i * 5
        cluster = MERSENNE_EXPONENTS[start_idx:start_idx + 5]
        
        if len(cluster) == 5:
            phases = compute_phase_coordinates(cluster)
            results.append({
                'Slice': f'Slice_{i+1:02d}',
                'Start': f'M{start_idx + 1}',
                'End': f'M{start_idx + 5}',
                'Exponents': cluster,
                'phi_1': round(phases[1], 3),
                'phi_2': round(phases[2], 3),
                'phi_3': round(phases[3], 3),
                'phi_4': round(phases[4], 3)
            })
    
    return pd.DataFrame(results)

def compute_scaling_ratio():
    """Compute the geometric scaling ratio Φ between consecutive primes."""
    ratios = []
    for i in range(1, len(MERSENNE_EXPONENTS)):
        ratio = MERSENNE_EXPONENTS[i] / MERSENNE_EXPONENTS[i-1]
        ratios.append(ratio)
    
    # Geometric mean
    phi = np.exp(np.mean(np.log(ratios)))
    return phi, ratios

if __name__ == '__main__':
    print("=" * 60)
    print("Holographic Lattice Theory - Phase Pattern Analysis")
    print("=" * 60)
    
    # Analyze slices
    df = analyze_all_slices()
    print("\nPhase Patterns for 10 Slices:")
    print(df[['Slice', 'Start', 'End', 'phi_1', 'phi_2', 'phi_3', 'phi_4']].to_string(index=False))
    
    # Compute scaling ratio
    phi, ratios = compute_scaling_ratio()
    print(f"\n\nGeometric Scaling Ratio Φ: {phi:.4f}")
    print(f"Mean ratio: {np.mean(ratios):.4f}")
    print(f"Std ratio: {np.std(ratios):.4f}")
    
    # Save to CSV
    df.to_csv('phase_patterns_computed.csv', index=False)
    print("\nResults saved to phase_patterns_computed.csv")
