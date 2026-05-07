# 04-05-26

“Patients request appointments, receptionists confirm them, doctors complete them and add records.”

- created the following models:
- User
- Hospital
- Department
- Hospital membership

## TODO

- Start filling up data, create different hospitals and models
- The following model connects hospitals to users (doctors, receptionists and CMO), add a model to connect users to departments
- One person can be a part of multiple departments but only inside one hospital.
- There can only be one CMO in one hospital (Use uniqeu constraints) ✅

```python
class HospitalMembership(models.Model):
    choices = [
        ("CMO", "Cheif Of Medical Staff"),
        ("DOC", "Doctor"),
        ("REC", "Receptionist"),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    hospital = models.OneToOneField(Hospital, on_delete=models.DO_NOTHING)
    role = models.CharField(max_length=3, choices=choices, null=True, blank=True)
```

# 05-05-26

## Completed

- Studied about unique constraints, added them.
- Now one hospital membership (staff) can be a part of one hospital
- Each hospital can only have one CMO

## TODO

- Ensure one person can be a part of multiple departments per hospital (all departments belong to same hospital)
- Start filling up dummy data, create different hospitals and test
- Restart migrations from the beginning

# 06-05-26

## Completed 

- Created Patient model, this will keep patient entry record for a user per hospital
- Added uuid to each patient because in case of emergency, walkin or manual creation of patient record by staff, there is no need for a user fk.

## TODO

- Ensure one person can be a part of multiple departments per hospital (all departments belong to the same hospital)
- Create visit records (model)

# 07-05-26

## Completed

- Created visiting records model for the patient
- Implemented `def clean()`

## TODO

- Study more on `def clean()` and other model constraints
- Implement those constraints (`def clean()`) to department membership