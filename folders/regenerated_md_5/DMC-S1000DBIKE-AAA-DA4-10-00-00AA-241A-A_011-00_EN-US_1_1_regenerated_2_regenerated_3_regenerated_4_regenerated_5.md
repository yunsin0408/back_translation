```markdown
# Bike Chain Lubrication Procedure (DMC-S1000DBIKE-AAA-DA4-10-00-00AA-241A-A_011-00_EN-US_1_1)

## Introduction

This document details the procedure for lubricating a bike chain, ensuring smooth operation and extending the lifespan of components.

## Preliminary Requirements

### Safety Precautions

* **Warning:** ACME sticky lube 52B (internalRef: sup-0001) is a dangerous substance. Do not get it on your skin. Use in a well-ventilated area. If swallowed, seek immediate medical attention. If it gets in your eyes, wash with clean water and seek medical advice.
* **Warning:** AECMA Heavy duty Oil 1988 (internalRef: sup-0002) is a dangerous substance. Do not get it on your skin. Use in a well-ventilated area. If swallowed, seek immediate medical attention. If it gets in your eyes, wash with clean water and seek medical advice.
* **Warning:** AECMA Heavy duty Oil 1988 (internalRef: sup-0002) - applicable to app-0001 - is a dangerous substance. Do not get it on your skin. Use in a well-ventilated area. If swallowed, seek immediate medical attention. If it gets in your eyes, wash with clean water and seek medical advice.
* **Caution:** Avoid getting lubricant into the brake system. Oil contamination can reduce braking efficiency.

### Required Materials and Tools

#### Lubricants

* **Wet Lube**
    * **Short Name:** Wet lube
    * **Internal Ref:** sup-0001
    * **Description:** ACME sticky lube 52B - For wet conditions.
* **Dry Lube**
    * **Short Name:** Dry lube
    * **Internal Ref:** sup-0002
    * **Description:** AECMA Heavy duty Oil 1988 - For dry conditions

#### Supplies

* **Clean Cloth** `internalRef="seq-0001"`
* **Floor Covering** `internalRef="seq-0002"`

#### Figures

* **Figure** `internalRef="fig-0001"`
* **Figure** `internalRef="fig-0002"`
* **Figure** `internalRef="fig-0003"`
* **Figure** `internalRef="fig-0004"`

## Procedure Steps

### Step 1: Apply Penetrating Lubricant (stepNumber="1", stepTitle="Apply Penetrating Lubricant")

Apply lubricant to the following components (refer to figures for location):

* Derailleur pivots (fig-0001)
* Derailleur tension (fig-0002)
* Brake lever pivots (fig-0003) - Including derailleur pivots, derailleur tension, guide wheels, and control cables.

### Step 2: Lubricate the Chain (stepNumber="2", stepTitle="Lubricate the Chain")

Ensure the chain is clean and dry.

Position the floor covering (seq-0002) beneath the chain to catch drips.

#### Conditional Lubrication

* **Condition (conditionID="App-0001")**
    * Apply wet lube (sup-0002) to each chain roller (fig-0004) sparingly.
* **Condition (conditionID="App-0002")**
    * Apply dry lube (sup-0001) to each chain roller (fig-0004) sparingly.

Slowly turn the cranks rearward while applying lubricant.

**Caution:** Avoid getting lubricant onto the brake system.

Allow the lubricant to soak into the chain.

### Step 3: Check Lubricated Parts (stepNumber="3", stepTitle="Check Lubricated Parts")

Inspect the rear wheel rim and clean any excess lubricant.

Verify that all chain links move freely. Relubricate stubborn links as needed (refer back to Step 2).

Inspect all lubricated parts and wipe away excess lubricant with a clean cloth (seq-0001).

## Closing Requirements

No specific closing requirements.

## Internal References

* **Figure** `internalRef="fig-0001"`
* **Figure** `internalRef="fig-0002"`
* **Figure** `internalRef="fig-0003"`
* **Figure** `internalRef="fig-0004"`
* **Sequence** `internalRef="seq-0001"`
* **Sequence** `internalRef="seq-0002"`
* **Supply** `internalRef="sup-0001"`
* **Supply** `internalRef="sup-0002"`
* **Step** `internalRef="stp-0002"`
* **Application** `internalRef="app-0001"`
* **Application** `internalRef="app-0002"`
```