### System heirarchy

System
 └── Hospitals
      ├── Departments
      ├── Users (with roles)
      └── Patients

### Django app structure

project/
 ├── accounts/      # users, roles
 ├── hospitals/     # hospital + departments
 ├── patients/      # patient records
 └── core/          # shared utilities