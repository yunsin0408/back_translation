# Bike Chain Lubrication Procedure

## Introduction

This document details the procedure for lubricating a bike chain, ensuring smooth operation and extending the lifespan of components.

## Preliminary Requirements

### Safety Precautions

**Warning:** ACME sticky lube 52B (internalRef: sup-0001) is a dangerous substance. Do not get it on your skin. Use in a well-ventilated area. If swallowed, seek immediate medical attention. If it gets in your eyes, wash with clean water and seek medical advice.

**Warning:** AECMA Heavy duty Oil 1988 (internalRef: sup-0002) is a dangerous substance.  Do not get it on your skin. Use in a well-ventilated area. If swallowed, seek immediate medical attention. If it gets in your eyes, wash with clean water and seek medical advice.

Avoid getting lubricant into the brake system. Oil contamination can reduce braking efficiency.

### Required Materials And Tools

#### Lubricants

*   **Item:** ACME sticky lube 52B - For wet conditions. (shortName: Wet lube, internalRef: sup-0001)
*   **Item:** AECMA Heavy duty Oil 1988 - For dry conditions (Applicable to app-0001). (shortName: Dry lube, internalRef: sup-0002)

#### Supplies

*   **Item:** Clean cloth (internalRef: seq-0001)
*   **Item:** Floor covering (internalRef: seq-0002)

#### Figures

*   **Item:** Derailleur pivots (internalRef: fig-0001)
*   **Item:** Derailleur tension (internalRef: fig-0002)
*   **Item:** Brake lever pivots (internalRef: fig-0003)
*   **Item:** Chain lubrication (internalRef: fig-0004)

## Procedure Steps

### Step 1: Apply Penetrating Lubricant (stepNumber: 1, stepTitle: Apply Penetrating Lubricant)

Apply lubricant to the following components (refer to figures for location):

*   Derailleur pivots (fig-0001)
*   Derailleur tension (fig-0002)
*   Brake lever pivots (fig-0003) - Including derailleur pivots, derailleur tension, guide wheels, and control cables.

### Step 2: Lubricate the Chain (stepNumber: 2, stepTitle: Lubricate the Chain)

Ensure the chain is clean and dry.

Position the floor covering (seq-0002) beneath the chain to catch drips.

#### Conditional Lubrication

*   **Condition:** Wet Conditions (conditionType: App-0001, conditionValue: Wet Conditions)
    *   Apply wet lube (sup-0002) to each chain roller (fig-0004) sparingly.
*   **Condition:** Dry Conditions (conditionType: App-0002, conditionValue: Dry Conditions)
    *   Apply dry lube (sup-0001) to each chain roller (fig-0004) sparingly.

Slowly turn the cranks rearward while applying lubricant.

**Caution:** Avoid getting lubricant onto the brake system.

Allow the lubricant to soak into the chain.

### Step 3: Check Lubricated Parts (stepNumber: 3, stepTitle: Check Lubricated Parts)

Inspect the rear wheel rim and clean any excess lubricant.

Verify that all chain links move freely. Relubricate stubborn links as needed (refer back to Step 2).

Inspect all lubricated parts and wipe away excess lubricant with a clean cloth (seq-0001).

## Closing Requirements

No specific closing requirements.

## Internal References

*   **Reference:** Derailleur pivots (id: fig-0001)
*   **Reference:** Derailleur tension (id: fig-0002)
*   **Reference:** Brake lever pivots (id: fig-0003)
*   **Reference:** Chain lubrication (id: fig-0004)
*   **Reference:** Clean cloth (id: seq-0001)
*   **Reference:** Floor covering (id: seq-0002)
*   **Reference:** ACME sticky lube 52B (id: sup-0001)
*   **Reference:** AECMA Heavy duty Oil 1988 (id: sup-0002)
*   **Reference:** Step 2 (Lubricate the Chain) (id: stp-0002)
*   **Reference:** Wet Conditions (id: app-0001)
*   **Reference:** Dry Conditions (id: app-0002)