#!/usr/bin/env python3
"""
Holographic Lattice Theory - SHA-256 Hash Verification
Author: Ruqing Chen
Date: January 6, 2026
Repository: https://github.com/Ruqing1963/Mersenne-Prime-Prediction-M53-M60

This script generates and verifies SHA-256 hashes for prediction integrity.
"""

import hashlib

# Pre-registered predictions
PREDICTIONS = {
    'M53': {'exponent': 214357007, 'digits': 64527887},
    'M54': {'exponent': 1120219861, 'digits': 337219780},
    'M55': {'exponent': 1618549043, 'digits': 487231812},
    'M56': {'exponent': 2338559557, 'digits': 703976574},
    'M57': {'exponent': 3378866489, 'digits': 1017140165},
    'M58': {'exponent': 4881953303, 'digits': 1469617175},
    'M59': {'exponent': 7053687349, 'digits': 2123371202},
    'M60': {'exponent': 10191516059, 'digits': 3067952036},
}

# Expected hashes (pre-registered)
EXPECTED_HASHES = {
    'M53': 'ED7537058511466EA56C20D05105ED9A83C029FCDD1B78FB3922C1A458D5F2D6',
    'M54': '5514D3E42570CD946D508F8B203A3861375DDA89EAB1B5BCE95E59706F297DFD',
    'M55': 'ABFD9348340DDE39CDF394FA554088B2D88DE0FEB416C28495DC16B198AAEEBB',
    'M56': 'BA77D0C8A3449883D705607C2E99E62E10B895452A42A4B2D8F36062E16D623F',
    'M57': '099FBD0A4AE691BDD3B72449530B12F9A8164FE433EC2B5EC314903394035076',
    'M58': '82EACFBB7ED18F332FC3102D29B52D82597894485D178AC6C04C47C0B71A3D1B',
    'M59': 'DEBEA475060E7290D73B5EAF46AE19CEF3C1FB843DE7FFFA9E7C6305CD1C3162',
    'M60': '0EF2DAF8017255408BE94B34CE8F7C513294BD5FED3ADE5B547881C1F925B778',
}

def generate_hash(rank, exponent, digits):
    """
    Generate SHA-256 hash from prediction parameters.
    
    Hash input format: "Rank|Exponent|Digits"
    Example: "M53|214357007|64527887"
    """
    input_string = f"{rank}|{exponent}|{digits}"
    hash_obj = hashlib.sha256(input_string.encode('utf-8'))
    return hash_obj.hexdigest().upper()

def verify_all_predictions():
    """Verify all pre-registered prediction hashes."""
    print("=" * 70)
    print("SHA-256 Hash Verification for Mersenne Prime Predictions")
    print("=" * 70)
    
    all_valid = True
    
    for rank, data in PREDICTIONS.items():
        computed_hash = generate_hash(rank, data['exponent'], data['digits'])
        expected_hash = EXPECTED_HASHES[rank]
        
        is_valid = computed_hash == expected_hash
        status = "✓ VALID" if is_valid else "✗ INVALID"
        
        print(f"\n{rank}:")
        print(f"  Exponent: {data['exponent']:,}")
        print(f"  Digits:   {data['digits']:,}")
        print(f"  Expected: {expected_hash}")
        print(f"  Computed: {computed_hash}")
        print(f"  Status:   {status}")
        
        if not is_valid:
            all_valid = False
    
    print("\n" + "=" * 70)
    if all_valid:
        print("ALL HASHES VERIFIED SUCCESSFULLY")
    else:
        print("WARNING: Some hashes do not match!")
    print("=" * 70)
    
    return all_valid

def verify_single_prediction(rank, exponent, digits):
    """
    Verify a single prediction against the pre-registered hash.
    
    This function can be used when a new Mersenne prime is discovered
    to verify that the prediction was not tampered with.
    """
    if rank not in EXPECTED_HASHES:
        return None, "Unknown rank"
    
    computed_hash = generate_hash(rank, exponent, digits)
    expected_hash = EXPECTED_HASHES[rank]
    
    return computed_hash == expected_hash, computed_hash

if __name__ == '__main__':
    verify_all_predictions()
    
    # Example: How to verify when M53 is discovered
    print("\n" + "=" * 70)
    print("VERIFICATION EXAMPLE:")
    print("When M53 is discovered, run:")
    print("  verify_single_prediction('M53', <actual_exponent>, <actual_digits>)")
    print("=" * 70)
