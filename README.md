# Robotic Package Sorting Challenge

This repository contains the solution for the **Smarter Technologies Core Engineering Technical Screen**.

## Problem

Packages must be sorted into stacks based on volume and mass.

### Rules

A package is **bulky** if:
- Volume (width × height × length) ≥ 1,000,000 cm³
- OR any dimension ≥ 150 cm

A package is **heavy** if:
- Mass ≥ 20 kg

### Sorting Logic

| Condition | Stack |
|-----------|-------|
| Neither bulky nor heavy | STANDARD |
| Bulky OR heavy | SPECIAL |
| Bulky AND heavy | REJECTED |

## Implementation

The function:
