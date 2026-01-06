#!/usr/bin/env python3
"""
Holographic Lattice Theory - Residual Analysis
Author: Ruqing Chen
Date: January 6, 2026
Repository: https://github.com/Ruqing1963/Mersenne-Prime-Prediction-M53-M60

This script performs quantitative residual analysis comparing
the Ancestral Gene (M6-M8) with Deep-Space Replica (M50-M52).
"""

import numpy as np
import matplotlib.pyplot as plt

# Mersenne prime exponents
M6, M7, M8 = 17, 19, 31
M50, M51, M52 = 77232917, 82589933, 136279841

def normalize_triplet(n1, n2, n3):
    """Normalize a triplet to [0, 1] interval."""
    span = n3 - n1
    return [0, (n2 - n1) / span, 1]

def compute_residuals():
    """Compute residuals between ancestral and deep-space genes."""
    
    # Normalize both triplets
    gene_phases = normalize_triplet(M6, M7, M8)
    deepspace_phases = normalize_triplet(M50, M51, M52)
    
    # Compute residuals
    residuals = [d - g for g, d in zip(gene_phases, deepspace_phases)]
    
    # MSE
    mse = np.mean([r**2 for r in residuals])
    
    return {
        'gene_phases': gene_phases,
        'deepspace_phases': deepspace_phases,
        'residuals': residuals,
        'mse': mse
    }

def compute_twin_compression():
    """Compute twin gap compression ratio."""
    
    # Ancestral twin gap (normalized)
    ancestral_gap = (M7 - M6) / (M8 - M6)
    
    # Deep-space twin gap (normalized)
    deepspace_gap = (M51 - M50) / (M52 - M50)
    
    # Compression
    compression = 1 - (deepspace_gap / ancestral_gap)
    
    return {
        'ancestral_gap': ancestral_gap,
        'deepspace_gap': deepspace_gap,
        'compression_ratio': compression
    }

def plot_residual_analysis(save_path='figures/residual_analysis.png'):
    """Generate the residual analysis visualization."""
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    # === Left Panel: Gene Morphology Residuals ===
    residual_data = compute_residuals()
    nodes = ['Start', 'Middle', 'End']
    residuals = residual_data['residuals']
    colors = ['blue' if r >= 0 else 'red' for r in residuals]
    
    bars1 = ax1.bar(nodes, residuals, color=colors, edgecolor='black', linewidth=1.5, width=0.6)
    ax1.set_ylabel('Phase Deviation', fontsize=11)
    ax1.set_title('Gene Morphology Residuals', fontsize=12, fontweight='bold')
    ax1.axhline(y=0, color='black', linestyle='-', linewidth=0.5)
    ax1.set_ylim(-0.06, 0.01)
    ax1.grid(axis='y', linestyle=':', alpha=0.7)
    
    for bar, val in zip(bars1, residuals):
        if val >= 0:
            ax1.text(bar.get_x() + bar.get_width()/2., 0.002, f'{val:.4f}', 
                    ha='center', va='bottom', fontsize=10, fontweight='bold')
        else:
            ax1.text(bar.get_x() + bar.get_width()/2., val - 0.003, f'{val:.4f}', 
                    ha='center', va='top', fontsize=10, fontweight='bold', color='white')
    
    # === Right Panel: Twin Gravity Contraction ===
    twin_data = compute_twin_compression()
    twins = ['Ancestral Twin\n(M6-M7)', 'Deep Space Twin\n(M50-M51)']
    gaps = [twin_data['ancestral_gap'], twin_data['deepspace_gap']]
    
    bars2 = ax2.bar(twins, gaps, color=['blue', 'purple'], edgecolor='black', linewidth=1.5, width=0.5)
    ax2.set_ylabel('Relative Gap Size', fontsize=11)
    ax2.set_title('Twin Gravity Contraction', fontsize=12, fontweight='bold')
    ax2.set_ylim(0, 0.14)
    ax2.grid(axis='y', linestyle=':', alpha=0.7)
    
    for bar, val in zip(bars2, gaps):
        ax2.text(bar.get_x() + bar.get_width()/2., val + 0.003, f'{val:.4f}', 
                ha='center', va='bottom', fontsize=10, fontweight='bold')
    
    ax2.annotate('', xy=(1, gaps[1]), xytext=(1, gaps[0]),
                arrowprops=dict(arrowstyle='<->', color='darkred', lw=2))
    ax2.text(1.22, (gaps[0] + gaps[1])/2, f'{twin_data["compression_ratio"]*100:.1f}%\nCompression', 
             fontsize=9, color='darkred', fontweight='bold', ha='left', va='center')
    
    plt.tight_layout()
    plt.savefig(save_path, dpi=200, bbox_inches='tight')
    plt.close()
    print(f"Figure saved to {save_path}")

if __name__ == '__main__':
    print("=" * 60)
    print("Holographic Lattice Theory - Residual Analysis")
    print("=" * 60)
    
    # Compute residuals
    residual_data = compute_residuals()
    print("\n=== Gene Morphology Residuals ===")
    print(f"Gene phases (M6-M8):       {residual_data['gene_phases']}")
    print(f"Deep-space phases (M50-M52): {residual_data['deepspace_phases']}")
    print(f"Residuals:                 {residual_data['residuals']}")
    print(f"MSE: {residual_data['mse']:.6e}")
    
    # Compute twin compression
    twin_data = compute_twin_compression()
    print("\n=== Twin Gap Compression ===")
    print(f"Ancestral gap (M6-M7): {twin_data['ancestral_gap']:.4f}")
    print(f"Deep-space gap (M50-M51): {twin_data['deepspace_gap']:.4f}")
    print(f"Compression ratio: {twin_data['compression_ratio']*100:.1f}%")
    
    # Generate plot
    import os
    os.makedirs('figures', exist_ok=True)
    plot_residual_analysis()
