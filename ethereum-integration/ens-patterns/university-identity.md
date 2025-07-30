# ENS University Identity Patterns

## Hierarchical Institution Identity

### Domain Structure
```
university.eth
├── departments.university.eth
│   ├── engineering.university.eth
│   ├── medicine.university.eth
│   └── sciences.university.eth
└── research.university.eth
    ├── quantum-computing.research.university.eth
    └── materials-science.research.university.eth
```

### Researcher Identity
```
researcher-name.department.university.eth
```

### Research Project Identity
```
project-name.research-area.university.eth
```

## Cardiff University Example
```
cardiff.eth
├── engineering.cardiff.eth
├── medicine.cardiff.eth
└── research.cardiff.eth
    └── ai-ethics.research.cardiff.eth
```

## Benefits

### Persistent Identity
- **Survives job changes** - researchers maintain identity across institutions
- **Global uniqueness** - no namespace conflicts
- **Hierarchical trust** - institutional validation flows down

### Institutional Control
- **Delegation authority** - universities control subdomain issuance
- **Multi-signature** - institutional governance for sensitive domains
- **Audit trails** - complete history of identity assignments

### Interoperability
- **Cross-institutional** - researchers collaborate across universities
- **Machine readable** - automated systems can verify affiliations
- **Future proof** - identity persists as technology evolves

This creates the first systematic institutional identity infrastructure using ENS.
