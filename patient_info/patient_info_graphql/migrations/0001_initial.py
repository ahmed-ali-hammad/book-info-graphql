# Generated by Django 4.1.4 on 2023-02-12 00:13

import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Allergy",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    model_utils.fields.AutoCreatedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="created",
                    ),
                ),
                (
                    "modified",
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="modified",
                    ),
                ),
                ("title", models.CharField(max_length=225)),
                ("description", models.TextField()),
                ("symptoms", models.TextField()),
                ("causes", models.TextField()),
            ],
            options={
                "verbose_name": "Allergy",
                "verbose_name_plural": "Allergies",
            },
        ),
        migrations.CreateModel(
            name="Doctor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    model_utils.fields.AutoCreatedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="created",
                    ),
                ),
                (
                    "modified",
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="modified",
                    ),
                ),
                ("first_name", models.CharField(max_length=225)),
                ("last_name", models.CharField(max_length=225)),
                (
                    "phone",
                    phonenumber_field.modelfields.PhoneNumberField(
                        max_length=128, region=None
                    ),
                ),
                ("email", models.EmailField(max_length=250)),
                ("city", models.CharField(max_length=255, verbose_name="city")),
                ("state", models.CharField(max_length=255, verbose_name="state")),
                ("zip_code", models.PositiveIntegerField(verbose_name="zip code")),
                ("practice", models.TextField()),
            ],
            options={
                "verbose_name": "Doctor",
                "verbose_name_plural": "Doctors",
            },
        ),
        migrations.CreateModel(
            name="Illness",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    model_utils.fields.AutoCreatedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="created",
                    ),
                ),
                (
                    "modified",
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="modified",
                    ),
                ),
                ("title", models.CharField(max_length=225)),
                ("description", models.TextField()),
                ("is_curable", models.BooleanField(default=True)),
                ("vaccine_available", models.BooleanField(default=False)),
                ("symptoms", models.TextField()),
                ("causes", models.TextField()),
                ("prevention", models.TextField()),
            ],
            options={
                "verbose_name": "Illness",
                "verbose_name_plural": "Illnesses",
            },
        ),
        migrations.CreateModel(
            name="Medication",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    model_utils.fields.AutoCreatedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="created",
                    ),
                ),
                (
                    "modified",
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="modified",
                    ),
                ),
                ("title", models.CharField(max_length=225)),
                ("description", models.TextField()),
                ("side_effect", models.TextField()),
                ("dosage_and_administration", models.TextField()),
                ("warnings", models.TextField()),
                ("contraindications", models.TextField()),
                ("Precautions", models.TextField()),
                ("adverse_reactions", models.TextField()),
            ],
            options={
                "verbose_name": "Medication",
                "verbose_name_plural": "Medications",
            },
        ),
        migrations.CreateModel(
            name="Patient",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    model_utils.fields.AutoCreatedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="created",
                    ),
                ),
                (
                    "modified",
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="modified",
                    ),
                ),
                ("first_name", models.CharField(max_length=225)),
                ("last_name", models.CharField(max_length=225)),
                ("email", models.EmailField(max_length=250)),
                (
                    "phone",
                    phonenumber_field.modelfields.PhoneNumberField(
                        max_length=128, region=None
                    ),
                ),
                ("date_of_birth", models.DateField()),
                ("gender", models.IntegerField(choices=[(1, "Male"), (2, "Female")])),
                ("weight", models.FloatField()),
                ("height", models.FloatField()),
                ("is_insured", models.BooleanField(default=False)),
                ("is_smoker", models.BooleanField(default=False)),
                ("is_married", models.BooleanField(default=False)),
                (
                    "primary_care_physician",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="patients",
                        to="patient_info_graphql.doctor",
                    ),
                ),
            ],
            options={
                "verbose_name": "Patient",
                "verbose_name_plural": "Patients",
            },
        ),
        migrations.CreateModel(
            name="Surgery",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    model_utils.fields.AutoCreatedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="created",
                    ),
                ),
                (
                    "modified",
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="modified",
                    ),
                ),
                ("title", models.CharField(max_length=225)),
                ("notes", models.TextField()),
                ("date_of_operation", models.DateTimeField()),
                ("discharge_date", models.DateTimeField(blank=True, null=True)),
                (
                    "patient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="surgeries",
                        to="patient_info_graphql.patient",
                    ),
                ),
                (
                    "surgeon",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="surgeries",
                        to="patient_info_graphql.doctor",
                    ),
                ),
            ],
            options={
                "verbose_name": "Surgery",
                "verbose_name_plural": "Surgeries",
            },
        ),
        migrations.CreateModel(
            name="MedicalRecord",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    model_utils.fields.AutoCreatedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="created",
                    ),
                ),
                (
                    "modified",
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="modified",
                    ),
                ),
                ("date_of_discovery", models.DateField()),
                ("physician_notes", models.TextField(blank=True, null=True)),
                ("is_cured", models.BooleanField(default=False)),
                ("required_surgery", models.BooleanField(default=False)),
                ("surgery_perfomed", models.BooleanField(default=False)),
                (
                    "allergies",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="medical_histories",
                        to="patient_info_graphql.allergy",
                    ),
                ),
                (
                    "illnesses",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="medical_histories",
                        to="patient_info_graphql.illness",
                    ),
                ),
                (
                    "patient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="medical_records",
                        to="patient_info_graphql.patient",
                    ),
                ),
                (
                    "surgeries",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="medical_history",
                        to="patient_info_graphql.surgery",
                    ),
                ),
            ],
            options={
                "verbose_name": "Medical Record",
                "verbose_name_plural": "Patients Medical Records",
            },
        ),
        migrations.AddField(
            model_name="illness",
            name="medication",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="related_illnesses",
                to="patient_info_graphql.medication",
            ),
        ),
        migrations.CreateModel(
            name="EmergencyContact",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    model_utils.fields.AutoCreatedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="created",
                    ),
                ),
                (
                    "modified",
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="modified",
                    ),
                ),
                ("first_name", models.CharField(max_length=225)),
                ("last_name", models.CharField(max_length=225)),
                ("email", models.EmailField(max_length=250)),
                (
                    "phone",
                    phonenumber_field.modelfields.PhoneNumberField(
                        max_length=128, region=None
                    ),
                ),
                (
                    "relationship",
                    models.IntegerField(
                        choices=[
                            (1, "SPOUSE"),
                            (2, "PARENT"),
                            (3, "SIBLING"),
                            (4, "RELATIVE"),
                            (5, "FRIEND"),
                        ]
                    ),
                ),
                (
                    "patient",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="emergency_contact",
                        to="patient_info_graphql.patient",
                    ),
                ),
            ],
            options={
                "verbose_name": "Emergency Contact",
                "verbose_name_plural": "Emergency Contacts",
            },
        ),
        migrations.AddField(
            model_name="allergy",
            name="medication",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="related_allergies",
                to="patient_info_graphql.medication",
            ),
        ),
        migrations.CreateModel(
            name="Address",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    model_utils.fields.AutoCreatedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="created",
                    ),
                ),
                (
                    "modified",
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="modified",
                    ),
                ),
                ("street_address_1", models.TextField(verbose_name="street address 1")),
                (
                    "street_address_2",
                    models.TextField(
                        blank=True, null=True, verbose_name="street address 2"
                    ),
                ),
                ("city", models.CharField(max_length=255, verbose_name="city")),
                ("state", models.CharField(max_length=255, verbose_name="state")),
                ("zip_code", models.PositiveIntegerField(verbose_name="zip code")),
                (
                    "patient",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="address",
                        to="patient_info_graphql.patient",
                    ),
                ),
            ],
            options={
                "verbose_name": "Address",
                "verbose_name_plural": "Addresses",
            },
        ),
    ]
