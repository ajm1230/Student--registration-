from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt
import random
import requests
from io import BytesIO

# --- Define Global Variables ---

# Template image URL
template_url = 'https://i.ibb.co/S7XVzFF6/Ekl-1.png'

# Font size
font_size = 35

# Admission Number
admission_number = random.randint(10000, 99999)
admission_number_x = 392
admission_number_y = 830

# Session Year
session_year_text = "2026-27"
session_year_x = 423
session_year_y = 777

# Student Name
student_name = 'Kamil'
student_name_x = 363
student_name_y = 1075

# Date of Admission
date_of_admission_text = '21/02/2026'
date_of_admission_x = 475
date_of_admission_y = 880

# Student Photo
student_photo_filename = '/content/student-photo.png'
student_photo_x = 1015
student_photo_y = 810
student_photo_width = 290
student_photo_height = 325

# Class
class_text = '12th'
class_x = 841
class_y = 1070

# School
school_text = 'Eklavya Public School'
school_x = 220
school_y = 1128

# Address
address_text = '123, Main Street, Anytown'
address_x = 470
address_y = 1170

# Aadhar No.
aadhar_no_text = '865676467554'
aadhar_no_x = 284
aadhar_no_y = 1221

# Email ID
email_id_text = 'kamil17299@gmail.com'
email_id_x = 881
email_id_y = 1225

# Date of Birth
date_of_birth_text = '01/01/2012'
date_of_birth_x = 332
date_of_birth_y = 1275

# Father's Name
father_name_text = 'Alam kalam'
father_name_x = 327
father_name_y = 1437

# Mother's Name
mother_name_text = 'Ammi'
mother_name_x = 357
mother_name_y = 1482

# Mathematics
mathematics_text = '✔'
mathematics_x = 343
mathematics_y = 1700

# Science
science_text = '✔'
science_x = 630
science_y = 1700

# Phone Number
phone_number_text = '8755765678'
phone_number_x = 895
phone_number_y = 1530

# Male Gender
male_gender_text = '✔'
male_gender_x = 799
male_gender_y = 1280

# Female Gender
female_gender_text = '✔'
female_gender_x = 935
female_gender_y = 1280

# Occupation
occupation_text = 'Business'
occupation_x = 308
occupation_y = 1530

# --- Image Processing ---

# Load the template image from URL
try:
    print(f"Downloading template from {template_url}...")
    response = requests.get(template_url)
    response.raise_for_status()  # Raises an HTTPError for bad responses
    img = Image.open(BytesIO(response.content)).convert('RGB')
    print("Template downloaded successfully.")
except requests.exceptions.RequestException as e:
    print(f"Fatal: Error downloading template image: {e}")
    exit()

draw = ImageDraw.Draw(img)

# Define font (using the global font_size)
try:
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", font_size)
except IOError:
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationMono-Regular.ttf", font_size)
    except IOError:
        font = ImageFont.load_default()
        print("Warning: Truetype font not found, falling back to default. Text appearance may vary.")

print(f"Using font: {font.getname()}")

# Place Session Year
draw.text((session_year_x, session_year_y), session_year_text, font=font, fill=(0, 0, 0))

# Place Admission Number
admission_number_text = str(admission_number)
draw.text((admission_number_x, admission_number_y), admission_number_text, font=font, fill=(0, 0, 0))

# Place Student Name
draw.text((student_name_x, student_name_y), student_name, font=font, fill=(0, 0, 0))

# Place Date of Admission
draw.text((date_of_admission_x, date_of_admission_y), date_of_admission_text, font=font, fill=(0, 0, 0))

# Place Class
draw.text((class_x, class_y), class_text, font=font, fill=(0, 0, 0))

# Place School
draw.text((school_x, school_y), school_text, font=font, fill=(0, 0, 0))

# Place Address
draw.text((address_x, address_y), address_text, font=font, fill=(0, 0, 0))

# Place Aadhar No.
draw.text((aadhar_no_x, aadhar_no_y), aadhar_no_text, font=font, fill=(0, 0, 0))

# Place Email ID
draw.text((email_id_x, email_id_y), email_id_text, font=font, fill=(0, 0, 0))

# Place Date of Birth
draw.text((date_of_birth_x, date_of_birth_y), date_of_birth_text, font=font, fill=(0, 0, 0))

# Place Father's Name
draw.text((father_name_x, father_name_y), father_name_text, font=font, fill=(0, 0, 0))

# Place Mother's Name
draw.text((mother_name_x, mother_name_y), mother_name_text, font=font, fill=(0, 0, 0))

# Place Mathematics
draw.text((mathematics_x, mathematics_y), mathematics_text, font=font, fill=(0, 0, 0))

# Place Science
draw.text((science_x, science_y), science_text, font=font, fill=(0, 0, 0))

# Place Phone Number
draw.text((phone_number_x, phone_number_y), phone_number_text, font=font, fill=(0, 0, 0))

# Place Male Gender
draw.text((male_gender_x, male_gender_y), male_gender_text, font=font, fill=(0, 0, 0))

# Place Female Gender
draw.text((female_gender_x, female_gender_y), female_gender_text, font=font, fill=(0, 0, 0))

# Place Occupation
draw.text((occupation_x, occupation_y), occupation_text, font=font, fill=(0, 0, 0))

# Load and paste Student Photo
try:
    student_photo = Image.open(student_photo_filename).convert('RGB')
    student_photo = student_photo.resize((student_photo_width, student_photo_height), Image.Resampling.LANCZOS)
    img.paste(student_photo, (student_photo_x, student_photo_y))
    print(f"Student photo '{student_photo_filename}' placed on the form.")
except FileNotFoundError:
    print(f"Warning: Student photo '{student_photo_filename}' not found. Skipping photo placement.")
except Exception as e:
    print(f"Error placing student photo: {e}")

# Save the final filled form
output_filename_final = 'filled_form_final.png'
img.save(output_filename_final)

print(f"Final form saved as {output_filename_final}")

# Display the modified image
plt.figure(figsize=(6,10))
plt.imshow(img)
plt.axis('off')

plt.show()