#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:


# BMI = (weight in pounds * 703) / (height in inches * height in inches)


# In[5]:


name = input("Enter you name: ")

weight = int(input("Enter the weight in pounds: "))

height = int(input("Enter the the height in inches: "))

BMI = round((weight * 703) / (height * height),2)

print(BMI)

if BMI > 0:
    if BMI < 18.5:
        print(name + ", you are underweight.")
    elif BMI <= 24.9:
        print(name + ", you are normal weight.")
    elif BMI <= 29.9:
        print(name + ", you are overweight.") 
    elif BMI <= 34.9:
        print(name + ", you are obese.")
    elif BMI <=39.9:
        print(name + ", you are severely obese.")
    else:
        print(name + ", you are over morbidly obese.")
else:
    print("Enter the valid input")


# In[ ]:





# In[ ]:


# BMI Categories:
# Underweight = <18.5
# Normal weight = 18.5–24.9
# Overweight = 25–29.9
# Obesity = 30 -34.9
# Severely obese = 35.39.9
# Over Morbidly obese = 40 and over


# In[4]:



        


# In[ ]:





# In[ ]:





# In[ ]:




