# Mersenne Prime Prediction M53-M60

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.XXXXXXX.svg)](https://doi.org/10.5281/zenodo.XXXXXXX)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

**Pre-registered conjecture for Mersenne prime distribution using Holographic Lattice Theory**

> ⚠️ **DISCLAIMER**: This is a PRE-REGISTERED CONJECTURE, not a peer-reviewed proof. The predictions are unverified and the underlying mathematical framework has not been formally proven.

## 🎯 Primary Prediction

| Rank | Exponent n | Digits | SHA-256 Hash |
|------|-----------|--------|--------------|
| **M53** | **214,357,007** | **64,527,887** | `ED7537058511466EA56C20D05105ED9A83C029FCDD1B78FB3922C1A458D5F2D6` |

## 📊 Complete Prediction Table (M53-M60)

| Rank | Predicted Exponent n | Predicted Digits | SHA-256 Hash |
|------|---------------------|------------------|--------------|
| M53 | 214,357,007 | 64,527,887 | `ED7537...D5F2D6` |
| M54 | 1,120,219,861 | 337,219,780 | `5514D3...297DFD` |
| M55 | 1,618,549,043 | 487,231,812 | `ABFD93...AAEEBB` |
| M56 | 2,338,559,557 | 703,976,574 | `BA77D0...6D623F` |
| M57 | 3,378,866,489 | 1,017,140,165 | `099FBD...035076` |
| M58 | 4,881,953,303 | 1,469,617,175 | `82EACF...1A3D1B` |
| M59 | 7,053,687,349 | 2,123,371,202 | `DEBEA4...1C3162` |
| M60 | 10,191,516,059 | 3,067,952,036 | `0EF2DA...25B778` |

> See [data/predictions_M53_M60.csv](data/predictions_M53_M60.csv) for complete SHA-256 hashes.

## 📁 Repository Structure

```
.
├── paper/
│   ├── main.tex                    # LaTeX source
│   └── main.pdf                    # Compiled PDF
├── data/
│   ├── known_mersenne_primes.csv   # M1-M52 exponents
│   ├── predictions_M53_M60.csv     # Pre-registered predictions
│   ├── phase_patterns.csv          # Holographic slice data
│   └── residual_analysis.csv       # Quantitative analysis
├── scripts/
│   ├── compute_phases.py           # Phase coordinate calculator
│   ├── residual_analysis.py        # MSE & compression analysis
│   └── verify_hash.py              # SHA-256 verification
├── figures/
│   ├── residual_analysis.png       # Gene morphology & twin gravity
│   └── holographic_slices/         # 11 slice diagrams
└── README.md
```

## 🔬 Theory Summary

**Holographic Lattice Theory** proposes that Mersenne prime exponents exhibit fractal self-similarity when decomposed into normalized 5-point clusters:

$$\varphi_i = \frac{n_{k+i} - n_k}{n_{k+4} - n_k}$$

### Key Findings

| Metric | Value |
|--------|-------|
| Mean Squared Error (MSE) | 9.05 × 10⁻⁴ |
| Geometric Feature Preservation | 94.8% |
| Twin Gap Compression | 41.0% |

## ✅ Verification Criteria

| Result | Condition |
|--------|-----------|
| **Strong Confirmation** | M53 discovered within ±1% of 214,357,007 |
| **Weak Confirmation** | M53 discovered within ±10% of prediction |
| **Falsification** | M53 outside ±10% range, or prime found between M52 and predicted M53 |

## 🔐 Hash Verification

To verify prediction integrity:

```python
python scripts/verify_hash.py
```

When M53 is discovered, verify with:

```python
from scripts.verify_hash import verify_single_prediction
is_valid, hash = verify_single_prediction('M53', actual_exponent, actual_digits)
```

## 📄 Citation

If you reference this work:

```bibtex
@misc{chen2026holographic,
  author = {Chen, Ruqing},
  title = {Holographic Lattice Theory: A Conjectural Framework for Mersenne Prime Distribution},
  year = {2026},
  publisher = {GitHub},
  url = {https://github.com/Ruqing1963/Mersenne-Prime-Prediction-M53-M60}
}
```

## 📚 References

1. [GIMPS - Great Internet Mersenne Prime Search](https://www.mersenne.org/)
2. [The Prime Pages: Mersenne Primes](https://primes.utm.edu/mersenne/)
3. Wagstaff, S. S. (1983). Divisors of Mersenne numbers. *Mathematics of Computation*, 40(161), 385-397.

## 📧 Contact

- **Author**: Ruqing Chen
- **Affiliation**: GUT Geoservice Inc., Montreal
- **Email**: ruqing@hotmail.com

## 📜 License

This work is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

---

*Timestamped: January 6, 2026*
