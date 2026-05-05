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

- Ensure one person can be a part of multiple departments per hospital (all departments belogn to same hospital)
- Start filling up dummy data, create different hospitals and test
- Restart migrations from the beginning
