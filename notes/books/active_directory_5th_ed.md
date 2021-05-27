# Active Directory, 5th Edition

## Chapter 4. Naming Contexts and Application Partitions

3 predefined naming contexts within Active Directory:

- A Domain naming context for each domain
- The Configuration naming context for the forest
- The Schema naming context for the forest

### Getting list of naming contexts and application partitions:

- query the RootDSE entry using LDP utility

## Chapter 5. Active Directory Schema

### Tools to view schema elements

- LDP
- ADSI Edit
- Active Directory Schema MMC snap-in (requires DDL registration by executing command `regsvr32 schmmgmt.dll`)

## Location of schema container

- Under configuration container
- Example: If contoso.com is the forest then DN for the schema container will be `cn=schema,cn=Configuration,dc=contoso,dc=com`

### Structure of schema

- 2 types of objects: `classSchema` and `attributeSchema`

### Protocols and standards

- LDAP
- X.500

### OID namespace

- Microsoft's namespace: `1.3.6.1.4.1.311`
