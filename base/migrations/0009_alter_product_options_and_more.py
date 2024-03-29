# Generated by Django 4.2.2 on 2023-06-16 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_alter_organisationsetting_country_delete_country'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
        migrations.AlterField(
            model_name='organisationsetting',
            name='country',
            field=models.CharField(blank=True, choices=[('DZA', 'Algeria'), ('AGO', 'Angola'), ('BEN', 'Benin'), ('BWA', 'Botswana'), ('BFA', 'Burkina Faso'), ('BDI', 'Burundi'), ('CMR', 'Cameroon'), ('CPV', 'Cape Verde'), ('CAF', 'Central African Republic'), ('TCD', 'Chad'), ('COM', 'Comoros'), ('COG', 'Republic of Congo'), ('CIV', "Côte d'Ivoire"), ('COD', 'Democratic Republic of the Congo'), ('DJI', 'Djibouti'), ('EGY', 'Egypt'), ('GNQ', 'Equatorial Guinea'), ('ERI', 'Eritrea'), ('ETH', 'Ethiopia'), ('GAB', 'Gabon'), ('GMB', 'Gambia'), ('GHA', 'Ghana'), ('GIN', 'Guinea'), ('GNB', 'Guinea-Bissau'), ('KEN', 'Kenya'), ('LSO', 'Lesotho'), ('LBR', 'Liberia'), ('LBY', 'Libya'), ('MDG', 'Madagascar'), ('MWI', 'Malawi'), ('MLI', 'Mali'), ('MRT', 'Mauritania'), ('MUS', 'Mauritius'), ('MYT', 'Mayotte'), ('MAR', 'Morocco'), ('MOZ', 'Mozambique'), ('NAM', 'Namibia'), ('NER', 'Niger'), ('NGA', 'Nigeria'), ('REU', 'Reunion'), ('RWA', 'Rwanda'), ('STP', 'São Tomé and Príncipe'), ('SEN', 'Senegal'), ('SYC', 'Seychelles'), ('SLE', 'Sierra Leone'), ('SOM', 'Somalia'), ('ZAF', 'South Africa'), ('SSD', 'South Sudan'), ('SDN', 'Sudan'), ('SWZ', 'Swaziland'), ('TZA', 'Tanzania'), ('TGO', 'Togo'), ('TUN', 'Tunisia'), ('UGA', 'Uganda'), ('ESH', 'Western Sahara'), ('ZMB', 'Zambia'), ('ZWE', 'Zimbabwe')], max_length=100, null=True, verbose_name='Country'),
        ),
    ]
