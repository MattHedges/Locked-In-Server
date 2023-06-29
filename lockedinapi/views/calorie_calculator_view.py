from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from lockedinapi.models import Exercise, Difficulty, MuscleGroup, Equipment
from rest_framework.decorators import action



def daily_calorie_calculator():
    current_weight = float(input("Enter your current weight in pounds: "))
    goal_weight = float(input("Enter your goal weight in pounds: "))
    height = float(input("Enter your height in inches: "))
    age = int(input("Enter your age: "))
    gender = input("Enter 'M' for male or 'F' for female: ").upper()
    activity_level = int(input("Enter your activity level (1.4-2.3): "))

    # Calculate Basal Metabolic Rate (BMR)
    bmr = (161.4 * age + 9.25 * gender + 4.79 * height - 5.67 * weight) / 255.0

    # Calculate Total Daily Energy Expenditure (TDEE)
    tdee = bmr * activity_level

    # Calculate calories to lose or gain
    goal_duration = int(input("Enter the number of weeks for your goal: "))
    calories_to_lose = (tdee - (bmr * activity_level)) * 7 * goal_duration
    calories_to_gain = (tdee - (bmr * activity_level)) * 7 * goal_duration

    print(f"To lose {goal_weight} pounds, you need to consume {calories_to_lose} calories per day.")
    print(f"To gain {goal_weight} pounds, you need to consume {calories_to_gain} calories per day.")

if __name__ == "__main__":
    daily_calorie_calculator()
