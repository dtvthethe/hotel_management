# Generated by Django 2.1.7 on 2019-03-29 18:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_code', models.CharField(max_length=20)),
                ('adult', models.IntegerField(default=0)),
                ('child', models.IntegerField(default=0)),
                ('note', models.TextField()),
                ('arrive_date', models.DateField()),
                ('depart_date', models.DateField()),
                ('is_breakfast', models.BooleanField(default=True)),
                ('price_booking', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='BookingPayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('credit', models.IntegerField(default=0)),
                ('date_pay', models.DateTimeField(auto_now_add=True)),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotelmanagement.Booking')),
            ],
        ),
        migrations.CreateModel(
            name='BookingStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=150)),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='guests', to='hotelmanagement.Booking')),
            ],
        ),
        migrations.CreateModel(
            name='MinibarCharge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_confirm', models.IntegerField(default=0)),
                ('quantity', models.IntegerField(default=0)),
                ('date_order', models.DateTimeField(auto_now_add=True)),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotelmanagement.Booking')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField(default=0)),
                ('capacity', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='RoomCharge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_confirm', models.IntegerField(default=0)),
                ('date_charge', models.DateTimeField(auto_now_add=True)),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotelmanagement.Booking')),
            ],
        ),
        migrations.CreateModel(
            name='RoomStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='RoomType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='room',
            name='room_status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room_list', to='hotelmanagement.RoomStatus'),
        ),
        migrations.AddField(
            model_name='room',
            name='room_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rooms', to='hotelmanagement.RoomType'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='hotelmanagement.ProductType'),
        ),
        migrations.AddField(
            model_name='minibarcharge',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotelmanagement.Product'),
        ),
        migrations.AddField(
            model_name='bookingpayment',
            name='payment_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotelmanagement.PaymentType'),
        ),
        migrations.AddField(
            model_name='booking',
            name='booking_status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='status', to='hotelmanagement.BookingStatus'),
        ),
        migrations.AddField(
            model_name='booking',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booking_clients', to='hotelmanagement.Client'),
        ),
        migrations.AddField(
            model_name='booking',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booking_room', to='hotelmanagement.Room'),
        ),
    ]
