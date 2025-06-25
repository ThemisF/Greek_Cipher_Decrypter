# Greek_Cipher_Decrypter
### Python tool for short-text Greek monoalphabetic cipher recovery via literature-derived frequency sampling and iterative heuristic self-correction

## Overview  
In 2021, as a second-year **15 year old highshool student**, I was challenged by my math teacher to decrypt the following small Greek ciphertext:

  **```ΞΟΖ ΒΣΟΧΔΠ, Α ΞΣΦΘΚΧΟ ΣΝΦΣ ΦΧΘΝΞΣΝ ΞΟΖΓ ΙΧΞΝΤΝΧ ΞΧΦΘΝΛΝΧΘ ΟΘΣΝΞ ΛΝΖΠΞ. ΟΑ ΦΝΤΝΖΞΟΑ ΗΘΩΟΑ ΓΠΦΟΧ, ΒΖΤΝΞ ΟΣΤΣΝΩΞΣ ΟΑΓ ΝΞΟΖΘΝΧ ΟΖΠ ΒΧΧΘΖΠΡ, ΞΑΥΩΜΑΥΣ ΥΧΝ ΡΝΤΑΞΣ ΟΖ ΗΧΟΩΒΧ ΒΗΘΖΞΟΧ ΟΖΠ ΤΣΛΖΓΟΧΞ: «ΒΣΛΧΤΣ ΙΧΞΝΤΝΧ, ΛΝΧ ΦΝΤΝΣΞ ΥΧΝ ΒΝΧ ΓΠΦΟΣΞ ΞΖΠ ΕΝΑΛΑΜΑΥΧ ΟΖΠΞ ΒΠΜΖΠΞ ΟΩΓ ΗΣΘΧΞΒΣΓΩΓ ΣΗΖΦΩΓ ΥΧΝ ΟΖΠΞ ΜΘΠΤΖΠΞ ΟΩΓ ΧΘΦΧΝΩΓ ΙΧΞΝΤΣΩΓ. ΒΗΖΘΩ ΓΧ ΟΖΤΒΑΞΩ ΓΧ ΚΑΟΑΞΩ ΒΝΧ ΦΧΘΑ ΧΗΖ ΟΑ ΒΣΛΧΤΣΝΖΟΑΟΧ ΞΖΠ```**
 
After **1½ years** of my leisure time and **three major program versions**, I evolved the tool from classic **frequency analysis** to a **literature-driven sampling method with iterative self-correction** ultimately recovering a fully readable story!

## Iterations

### Version 1: Frequency-Analysis Prototype  
- **Approach:** Collected a large Greek text and computed global letter-frequency distributions.  
- **Process:** Mapped the most frequent ciphertext symbols to the most frequent Greek letters with 24 character key lists.  
- **Outcome:** The text was too short so the end result remained unintelligible gibberish. 

- **Lesson learned:**
In such small texts it is very difficult to use letter-frequency analysis because some letters that usually don’t appear often might have elevated local percentages of appearance. For example the letter Ξ in the word ΞΥΔΙ has 25% appearance but if you compare it to normal everyday speech and generally Greek literature the % is substantially smaller!*

### Version 2: Random Key Brute Force  
- **Approach:** Treated the key as a random 24-letter permutation and brute-forced by sampling millions of candidates.  
- **Process:**  
  1. Generate random strings of the 24 Greek letter alphabet keys.  
  2. Decrypt the ciphertext with each permutation.  
  3. Score by counting dictionary matches.  
- **Outcome:** The key-space (24! ≈ 10²³) was far too large  and the computations too time expensive so no readable plaintext was ever found with this method.

### Version 3: Literature-Derived Chunked Sampling & Iterative Self-Correction with frequency analisys with the aid of a Greek dictionary
- **Approach:** Used real Greek text statistics cut into chunks to generate realistic frequency orders, added a greek dictionary for automatically checking readability "Greekness", optimized the algorithm and added an iterative self-correction loop.
- **Process:**  
  1. **Chunk Sampling:** Chop multiple Greek literature sources into segments the size of the ciphertext and deriving a 24 letter frequency list out of each one. This approach aims to solve the problem the first version of the code faced.
  2. **Greek Dictionary:** Added a Greek dictinary for automating multiple processes that were done manually and most importantly quantifying how greek (how successfull was the decryption) the semi-decrypted text was after the key was used. 
  3. **Optimization:** After creating a bunch of frequency ordered 24 character lists (keys) from Greek literature, they were grouped based on similarity. This way only one had to be checked for verifying if the group's mapping was improving Greekness when used for decyphering
  5. **Iterative Correction:**  
     - Decrypt using the sampled keys that passed the previous test (improved Greekness).  
     - Detect improbable words (e.g. “Θασιλιάς” --> "Βασιλιάς" {corrected word}) and swap specific letters (Θ→Β) using the Greek dictionary.  
     - Re-score and repeat in a loop for a specific number of iterations if Greekness was improving.  
- **Outcome:** 
  
  Greekness rose above 95 % within 10 iterations, producing the following fully readable “1001 Nights” narrative !!!

  **```ΣΤΟ ΜΕΤΑΞΥ, Η ΣΕΧΡΖΑΤ ΕΙΧΕ ΧΑΡΙΣΕΙ ΣΤΟΝ ΒΑΣΙΛΙΑ ΣΑΧΡΙΓΙΑΡ ΤΡΕΙΣ ΓΙΟΥΣ. ΤΗ ΧΙΛΙΟΣΤΗ ΠΡΩΤΗ ΝΥΧΤΑ, ΜΟΛΙΣ ΤΕΛΕΙΩΣΕ ΤΗΝ ΙΣΤΟΡΙΑ ΤΟΥ ΜΑΑΡΟΥΦ, ΣΗΚΩΘΗΚΕ ΚΑΙ ΦΙΛΗΣΕ ΤΟ ΠΑΤΩΜΑ ΜΠΡΟΣΤΑ ΤΟΥ ΛΕΓΟΝΤΑΣ: «ΜΕΓΑΛΕ ΒΑΣΙΛΙΑ, ΓΙΑ ΧΙΛΙΕΣ ΚΑΙ ΜΙΑ ΝΥΧΤΕΣ ΣΟΥ ΔΙΗΓΗΘΗΚΑ ΤΟΥΣ ΜΥΘΟΥΣ ΤΩΝ ΠΕΡΑΣΜΕΝΩΝ ΕΠΟΧΩΝ ΚΑΙ ΤΟΥΣ ΘΡΥΛΟΥΣ ΤΩΝ ΑΡΧΑΙΩΝ ΒΑΣΙΛΕΩΝ. ΜΠΟΡΩ ΝΑ ΤΟΛΜΗΣΩ ΝΑ ΖΗΤΗΣΩ ΜΙΑ ΧΑΡΗ ΑΠΟ ΤΗ ΜΕΓΑΛΕΙΟΤΗΤΑ ΣΟΥ```**

## Usage  
```bash
git clone https://github.com/ThemisF/Greek_Cipher_Decrypter.git
python posostiaia-apokryptografisi-V5.0.py
```

## Example
This is how the code is used in practice:

![Usage example 0.5](https://raw.githubusercontent.com/ThemisF/Greek_Cipher_Decrypter/main/images/codeUse_1.png)
![Usage example 1](https://raw.githubusercontent.com/ThemisF/Greek_Cipher_Decrypter/main/images/codeUse_2.png)



