# my_amts/management/commands/load_bus_data.py
from django.core.management.base import BaseCommand
from my_amts.models import Bus

class Command(BaseCommand):
    help = 'Load initial bus data'

    def add_arguments(self, parser):
        parser.add_argument('file_path', nargs='?', type=str, help='Path to the JSON file containing bus data')

    def handle(self, *args, **kwargs):
        file_path = kwargs.get('file_path')
        
        if file_path:
            import json
            import os
            
            if not os.path.exists(file_path):
                self.stdout.write(self.style.ERROR(f'File not found: {file_path}'))
                return

            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    buses = json.load(f)
                self.stdout.write(self.style.SUCCESS(f'Loaded data from {file_path}'))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Error reading file: {str(e)}'))
                return
        else:
            # Default AMTS bus routes data
            buses = [
                {
                    'bus_number': '33',
                    'stops': [
                        {'name': 'Gokul Park', 'coordinates': [23.03145, 72.65191]},
                        {'name': 'Gandhi Park', 'coordinates': [23.02777, 72.64104]},
                        {'name': 'Khodiyar Nagar', 'coordinates': [23.03268, 72.63918]},
                        {'name': 'Bapu Nagar', 'coordinates': [23.03388, 72.63406]},
                        {'name': 'Bapu Nagar Char Rasta', 'coordinates': [23.03495, 72.62937]},
                        {'name': 'Bombay Housing', 'coordinates': [23.03504, 72.61747]},
                        {'name': 'Sharda Ben', 'coordinates': [23.03180, 72.61150]},
                        {'name': 'Kalupur', 'coordinates': [23.03017, 72.60041]},
                        {'name': 'Sarangpur', 'coordinates': [23.02396, 72.59961]},
                        {'name': 'Raipur', 'coordinates': [23.01696, 72.59397]},
                        {'name': 'MNC', 'coordinates': [23.01971, 72.58615]},
                        {'name': 'Lal Darwaja', 'coordinates': [23.02458, 72.57865]}
                    ]
                },
                {
                    'bus_number': '58',
                    'stops': [
                        {'name': 'Thakkar Nagar', 'coordinates': [23.03910, 72.63885]},
                        {'name': 'India Colony', 'coordinates': [23.03869, 72.63423]},
                        {'name': 'Vijay Chowk', 'coordinates': [23.03863, 72.63121]},
                        {'name': 'Bapu Nagar Char Rasta', 'coordinates': [23.03495, 72.62937]},
                        {'name': 'Bombay Housing', 'coordinates': [23.03504, 72.61747]},
                        {'name': 'Sharda Ben', 'coordinates': [23.03180, 72.61150]},
                        {'name': 'Kalupur', 'coordinates': [23.03017, 72.60041]},
                        {'name': 'Sarangpur', 'coordinates': [23.02396, 72.59961]},
                        {'name': 'Raipur', 'coordinates': [23.01696, 72.59397]},
                        {'name': 'Gita Mandir', 'coordinates': [23.01483, 72.59125]},
                        {'name': 'Jamalpur', 'coordinates': [23.01063, 72.57777]},
                        {'name': 'Paldi', 'coordinates': [23.01370, 72.56476]}
                    ]
                },
                {
                    'bus_number': '56',
                    'stops': [
                        {'name': 'Naroda', 'coordinates': [23.06424, 72.64280]},
                        {'name': 'Krishna Nagar', 'coordinates': [23.05705, 72.64326]},
                        {'name': 'Bajrang Ashram', 'coordinates': [23.04768, 72.64113]},
                        {'name': 'Thakkar Nagar', 'coordinates': [23.03910, 72.63885]},
                        {'name': 'Bapu Nagar Char Rasta', 'coordinates': [23.03495, 72.62937]},
                        {'name': 'Bombay Housing', 'coordinates': [23.03504, 72.61747]},
                        {'name': 'Sharda Ben', 'coordinates': [23.03180, 72.61150]},
                        {'name': 'Kalupur', 'coordinates': [23.03017, 72.60041]},
                        {'name': 'Sarangpur', 'coordinates': [23.02396, 72.59961]},
                        {'name': 'Raipur', 'coordinates': [23.01696, 72.59397]},
                        {'name': 'Lal Darwaja', 'coordinates': [23.02458, 72.57865]}
                    ]
                },
                {
                    "bus_number": "31_5",
                    "stops": [
                        {"name": "Lal Darwaja","coordinates": [23.02458, 72.57865]},
                        {"name": "VS Hospital","coordinates": [23.02163, 72.57138]},
                        {"name": "Anjali Char Rasta","coordinates": [23.00315, 72.55187]},
                        {"name": "Vasna","coordinates": [23.00180, 72.54801]},
                        {"name": "Vishala","coordinates": [22.99528, 72.53205]},
                        {"name": "Khursid Park","coordinates": [22.99112, 72.51860]},
                        {"name": "Ambar Tower","coordinates": [22.98896, 72.51259]},
                        {"name": "Sarkhej","coordinates": [22.98752, 72.50353]},
                        {"name": "Ujala","coordinates": [22.98042, 72.49255]},
                        {"name": "Sanand Chowkdi","coordinates": [22.98701, 72.49388]},
                        {"name": "LJ College","coordinates": [22.98712, 72.48893]}
                    ]
                },
                {
                    "bus_number": "130",
                    "stops": [
                        {"name": "Naroda","coordinates": [23.06424, 72.64280]},
                        {"name": "Krishna Nagar","coordinates": [23.05705, 72.64326]},
                        {"name": "Vijay Park","coordinates": [23.05123, 72.64201]},
                        {"name": "Bajrang Ashram","coordinates": [23.04768, 72.64113]},
                        {"name": "Khodiyar Nagar","coordinates": [23.03268, 72.63918]},
                        {"name": "Soni ni Chali","coordinates": [23.02203, 72.63830]},
                        {"name": "Rabari Colony","coordinates": [23.00433, 72.63713]},
                        {"name": "Purvadeep Society","coordinates": [22.99605, 72.63437]},
                        {"name": "Jashoda Nagar","coordinates": [22.98375, 72.62412]},
                        {"name": "Ghodasar","coordinates": [22.97839, 72.61015]},
                        {"name": "Isanpur","coordinates": [22.97552, 72.60076]},
                        {"name": "Narol","coordinates": [22.97288, 72.58951]},
                        {"name": "Chandola","coordinates": [22.98203, 72.58568]},
                        {"name": "Danilimda","coordinates": [22.99608, 72.57912]},
                        {"name": "Chadra Nagar","coordinates": [22.99980, 72.55804]},
                        {"name": "Anjali Char Rasta","coordinates": [23.00315, 72.55187]}
                    ]
                },

                {
                    "bus_number": "401",
                    "stops": [
                        {"name": "Vasna Terminus", "coordinates": [23.0075, 72.5159]},             
                        {"name": "Jawaharnagar", "coordinates": [23.0180, 72.5238]},             
                        {"name": "Anjali Cinema", "coordinates": [23.0235, 72.5262]},            # approximate
                        {"name": "Bhaththa (Vasna)", "coordinates": [23.0288, 72.5285]},         # approximate
                        {"name": "Anandnagar", "coordinates": [23.0350, 72.5320]},              # approximate
                        {"name": "Fatehnagar", "coordinates": [23.0420, 72.5370]},              # approximate
                        {"name": "Jain Merchant Society", "coordinates": [23.0470, 72.5410]},   # approximate
                        {"name": "Mahalakshmi Society", "coordinates": [23.0505, 72.5445]},     # approximate
                        {"name": "Paldi", "coordinates": [23.0515, 72.5405]},                    # approximate central Paldi
                        {"name": "Pritamnagar", "coordinates": [23.0535, 72.5450]},             # approximate
                        {"name": "Arvind Sales Emporium", "coordinates": [23.0555, 72.5475]},   # approximate
                        {"name": "V.S Hospital", "coordinates": [23.0565, 72.5500]},            # approximate
                        {"name": "Sanyas Ashram", "coordinates": [23.0590, 72.5550]},           # approximate
                        {"name": "Gandhigram Metro Station", "coordinates": [23.0610, 72.5585]},# approximate
                        {"name": "Natraj Cinema", "coordinates": [23.0635, 72.5620]},           # approximate
                        {"name": "Vallabh Sadan", "coordinates": [23.0655, 72.5645]},           # approximate
                        {"name": "Mill Owners Association", "coordinates": [23.0670, 72.5670]}, # approximate
                        {"name": "Mount Carmel School", "coordinates": [23.0690, 72.5690]},     # approximate
                        {"name": "Income Tax Office", "coordinates": [23.0710, 72.5710]},       # approximate
                        {"name": "Usmanpura", "coordinates": [23.0730, 72.5725]},               # approximate
                        {"name": "Champaner Society", "coordinates": [23.0750, 72.5750]},       # approximate
                        {"name": "Vadaj", "coordinates": [23.0785, 72.5775]},                   # approximate
                        {"name": "Collector Office", "coordinates": [23.0810, 72.5800]},        # approximate
                        {"name": "Keshavnagar Tanki", "coordinates": [23.0830, 72.5820]},      # approximate
                        {"name": "Railway River Bridge", "coordinates": [23.0850, 72.5840]},    # approximate
                        {"name": "Railway Over Bridge", "coordinates": [23.0870, 72.5860]},     # approximate
                        {"name": "Chandkheda Gam", "coordinates": [23.0890, 72.5880]},         # approximate
                        {"name": "Siddhi Complex", "coordinates": [23.0910, 72.5895]},         # approximate
                        {"name": "Chandkheda (Sarathi Bunglows)", "coordinates": [23.0930, 72.5910]} # approximate
                    ]
                },
                {
                    "bus_number": "11",
                        "stops": [
                        {"name": "Vadaj", "coordinates": [23.0785, 72.5775]},
                        {"name": "Champaner Society", "coordinates": [23.0750, 72.5750]},
                        {"name": "Usmanpura", "coordinates": [23.0730, 72.5725]},
                        {"name": "Income Tax Office", "coordinates": [23.0710, 72.5710]},
                        {"name": "Ashram Road", "coordinates": [23.0650, 72.5660]},
                        {"name": "Gandhigram", "coordinates": [23.0610, 72.5585]},
                        {"name": "Paldi", "coordinates": [23.0515, 72.5405]},
                        {"name": "Kankaria Lake", "coordinates": [23.0103, 72.6002]},
                        {"name": "Maninagar", "coordinates": [22.9963, 72.6032]}
                    ]
                },
                {
                    "bus_number": "89",
                    "stops": [
                        {"name": "Chandkheda Gam", "coordinates": [23.0890, 72.5880]},
                        {"name": "Motera Stadium", "coordinates": [23.0917, 72.5972]},
                        {"name": "Sabarmati", "coordinates": [23.0830, 72.5810]},
                        {"name": "Usmanpura", "coordinates": [23.0730, 72.5725]},
                        {"name": "Navrangpura", "coordinates": [23.0375, 72.5610]},
                        {"name": "University Area", "coordinates": [23.0365, 72.5535]},
                        {"name": "Vastrapur Lake", "coordinates": [23.0352, 72.5298]},
                        {"name": "Vastrapur", "coordinates": [23.0378, 72.5285]}
                    ]
                }
            ]

        # Add validation before creating buses
        for bus_data in buses:
            # Validate bus number
            if not isinstance(bus_data['bus_number'], str):
                raise ValueError(f"Invalid bus number format: {bus_data['bus_number']}")
            
            # Validate stops
            for stop in bus_data['stops']:
                if not isinstance(stop['name'], str):
                    raise ValueError(f"Invalid stop name in bus {bus_data['bus_number']}")
                if not len(stop['coordinates']) == 2:
                    raise ValueError(f"Invalid coordinates for stop {stop['name']}")
                lat, lon = stop['coordinates']
                # if not (22.9 <= lat <= 23.2 and 72.4 <= lon <= 72.7):
                #     self.stdout.write(self.style.WARNING(f"Warning: Coordinates might be out of usual Ahmedabad range for stop {stop['name']}: {lat}, {lon}"))

        # Clear existing buses ONLY if we are reloading everything or if requested
        # Ideally we should probably upsert, but for now let's wipe to ensure fresh state if the user wants.
        # But maybe they want to append?
        # The original script deleted all. Let's keep it that way for "load" command purity, or check if we should specific flag.
        # Given the user says "add all", they likely want to establish the full database.
        
        # Instead of deleting all, we now upsert to prevent data loss of existing buses not in the new file
        # unless specifically requested? For now, user requested "not to delete any bus data".
        
        # Bus.objects.all().delete() # Commenting out destruction

        # Create or Update buses
        created_count = 0
        updated_count = 0
        
        for bus_data in buses:
            bus, created = Bus.objects.update_or_create(
                bus_number=bus_data['bus_number'],
                defaults={
                    'stops': bus_data['stops']
                }
            )
            if created:
                created_count += 1
                self.stdout.write(self.style.SUCCESS(f'Successfully created bus {bus.bus_number}'))
            else:
                updated_count += 1
                self.stdout.write(self.style.SUCCESS(f'Successfully updated bus {bus.bus_number}'))
                
        self.stdout.write(self.style.SUCCESS(f'Operation Complete: {created_count} created, {updated_count} updated.'))