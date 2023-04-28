# Generated by Django 4.1.8 on 2023-04-28 06:50

from django.db import migrations, models
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0006_remove_homepage_carousel_image_1_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="HomePageCarousel",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "body",
                    wagtail.fields.StreamField(
                        [
                            (
                                "carousel_item",
                                wagtail.blocks.StructBlock(
                                    [
                                        (
                                            "image",
                                            wagtail.images.blocks.ImageChooserBlock(
                                                required=True
                                            ),
                                        ),
                                        (
                                            "heading",
                                            wagtail.blocks.CharBlock(
                                                max_length=200, required=True
                                            ),
                                        ),
                                        (
                                            "subheading",
                                            wagtail.blocks.CharBlock(
                                                max_length=300, required=True
                                            ),
                                        ),
                                        (
                                            "button_text",
                                            wagtail.blocks.CharBlock(
                                                max_length=50, required=True
                                            ),
                                        ),
                                        (
                                            "button_link",
                                            wagtail.blocks.CharBlock(
                                                max_length=300, required=True
                                            ),
                                        ),
                                    ]
                                ),
                            )
                        ],
                        use_json_field=None,
                        verbose_name="Carousel items",
                    ),
                ),
            ],
        ),
    ]