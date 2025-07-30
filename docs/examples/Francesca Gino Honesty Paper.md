# RO-Crate ENS+IPFS+EAS Workflow Example: Francesca Gino Dishonesty Paper

## Overview

This artifact demonstrates, in pseudocode and structured metadata, how the infamous Francesca Gino “dishonesty” experiment could have been packaged, validated, and attested using RO-Crate, ENS, IPFS, and EAS. The goal is to show how such a workflow could have made fraud detection faster and more transparent.

---

## 1. Prepare Dataset and Schema

- **Dataset:** Original experiment data (e.g., CSV file from the dishonesty study)
    
- **Schema:** JSON Schema or RO-Crate profile describing expected columns, value ranges, and provenance fields
    
- **RO-Crate:** Package the dataset, schema, and publication metadata in a machine-readable format
    

---

## 2. Upload to IPFS

- Upload the RO-Crate (as a zip or directory) to IPFS → get `DATA_CID`
    
- Upload the schema file to IPFS → get `SCHEMA_CID`
    

---

## 3. Register ENS Names

- Register `gino-dishonesty-data.eth` → set content hash to `DATA_CID`
    
- Register `gino-dishonesty-schema.eth` → set content hash to `SCHEMA_CID`
    

---

## 4. EAS Attestation

- Use Ethereum Attestation Service (EAS) to create an attestation that:
    
    - The data at `gino-dishonesty-data.eth` matches the schema at `gino-dishonesty-schema.eth`
        
    - Include metadata: who attested, when, validation method, etc.
        

---

## 5. Validation Workflow (Pseudocode with Comments)

```
# Step 1: Resolve ENS names to IPFS CIDs

data_ens = 'gino-dishonesty-data.eth'
schema_ens = 'gino-dishonesty-schema.eth'

data_cid = resolve_ens_to_ipfs(data_ens)
schema_cid = resolve_ens_to_ipfs(schema_ens)

# Step 2: Fetch data and schema from IPFS

data = fetch_from_ipfs(data_cid)
schema = fetch_from_ipfs(schema_cid)

# Step 3: Validate data against schema and provenance
if validate(data, schema) and check_provenance(data):
    attestation = create_eas_attestation(
        subject=data_ens,
        schema=schema_ens,
        result='match',
        validator='validator-eth-address',
        timestamp=now()
    )
    publish_attestation(attestation)
    print('Validation succeeded and attestation published!')
else:
    print('Validation failed: data does not match schema or provenance')
    # Optionally, publish a negative attestation or alert
```

---

## 6. RO-Crate Metadata Example (JSON-LD)

```
{
  "@context": "https://w3id.org/ro/crate/1.1/context",
  "@graph": [
    {
      "@id": "./",
      "@type": "Dataset",
      "name": "Dishonesty Experiment Data (Francesca Gino, 2012)",
      "description": "Dataset from the infamous dishonesty experiment, later found to be fraudulent. Packaged for transparency and validation.",
      "datePublished": "2012-06-01",
      "author": [
        {"name": "Francesca Gino"},
        {"name": "Dan Ariely"}
      ],
      "hasPart": [
        {"@id": "dishonesty_data.csv"},
        {"@id": "gino_paper.pdf"}
      ],
      "citation": {
        "@id": "https://doi.org/10.1037/a0023771"
      },
      "ensName": "gino-dishonesty-data.eth",
      "schemaReference": {
        "@id": "gino-dishonesty-schema.eth"
      },
      "easAttestation": {
        "@id": "eas://<ATTESTATION_UID>"
      }
    },
    {
      "@id": "dishonesty_data.csv",
      "@type": "File",
      "name": "Dishonesty Experiment Data (CSV)",
      "encodingFormat": "text/csv"
    },
    {
      "@id": "gino_paper.pdf",
      "@type": "File",
      "name": "Original Paper (2012)",
      "encodingFormat": "application/pdf",
      "contentUrl": "https://datacolada.org/98"
    }
  ]
}
```

---

## 7. Commentary & Rationale

- **Automated validation** would have flagged inconsistencies or impossible values immediately.
    
- **Provenance checks** (timestamps, authorship, file hashes) would have made tampering obvious.
    
- **Public, immutable attestations** allow the community to see who validated what, and when.
    
- **Community re-validation** could have caught fraud much earlier, or even deterred it.
    

---

## 8. Extending the Workflow

- **Negative Attestations:** Validators can publish negative attestations if fraud or mismatches are found.
    
- **Transparency:** All updates to ENS or IPFS are public and auditable.
    
- **Reproducibility:** Anyone can fetch, validate, and re-attest to the data at any time.
    

---

## 9. References

- [Data Colada: Blog post on the Gino case](https://datacolada.org/98)
    
- [Original Paper DOI](https://doi.org/10.1037/a0023771)
    
- [RO-Crate Specification](https://www.researchobject.org/ro-crate/)
    
- [Ethereum Name Service (ENS)](https://ens.domains/)
    
- [IPFS](https://ipfs.tech/)
    
- [Ethereum Attestation Service (EAS)](https://docs.attest.sh/)