# Greek_Cipher_Decrypter
Python tool for short-text Greek monoalphabetic cipher recovery via literature-derived frequency sampling and iterative heuristic self-correction

# Greek Cipher Decryption Project

## Overview  
In 2021, as a second-year calculus student, I was tasked with decrypting an 893-character Greek ciphertext inspired by a “1001 Nights” tale. Over 1½ years and three major program versions, I evolved the tool from classic frequency analysis to a literature-driven sampling method with iterative self-correction—ultimately recovering a fully readable story.

## Iterations

### Version 1: Frequency-Analysis Prototype  
- **Approach:** Collected a large Greek corpus (books, articles) and computed global letter-frequency distributions.  
- **Process:** Mapped the most frequent ciphertext symbols to the most frequent Greek letters.  
- **Outcome:** The 893-letter sample was too short and skewed; the output remained unintelligible gibberish.

### Version 2: Random Key Brute Force  
- **Approach:** Treated the key as a random 24-letter permutation and brute-forced by sampling millions of candidates.  
- **Process:**  
  1. Generate random strings of the 24 Greek letters.  
  2. Decrypt the ciphertext with each permutation.  
  3. Score by counting dictionary matches.  
- **Outcome:** The key-space (24! ≈ 10²³) was far too large—no readable plaintext was ever found.

### Version 3: Literature-Derived Sampling & Iterative Self-Correction  
- **Approach:** Used real Greek text statistics cut into 893-character chunks to generate realistic frequency orders, then refined with a dictionary loop.  
- **Process:**  
  1. **Chunk Sampling:** Chop multiple Greek literature sources into segments the size of the ciphertext.  
  2. **Frequency Lists:** For each segment, rank the 24 letters by their local frequency—these “24-sized lists” capture the true variability of short Greek passages.  
  3. **Key Generation:** Randomly select one of these literature-derived lists and map ciphertext symbols to plaintext letters in that order.  
  4. **Iterative Correction:**  
     - Decrypt with the sampled key.  
     - Detect improbable words (e.g. “Θασιλιας”) and swap specific letters (Θ→Β) using the Greek dictionary.  
     - Re-score and repeat for 10 rapid loops.  
- **Outcome:** Greekness rose above 95 % within 10 iterations, producing a fully readable “1001 Nights” narrative—including names like Σεχρζατ and Μααρούφ.

