from fastapi import FastAPI, Query
from faker import Faker
import random

app = FastAPI()
faker = Faker() #faker provides fake data

#Customized data
CARS = {
    "Toyota": ["Supra", "Corolla", "Camry"],
    "BMW": ["M3", "M4", "M8"],
    "Audi": ["R8", "A5", "Hybrid"],
    "Mercedes": ["S-class", "GLS", "SL"]
}

@app.get("/")
def root():
    return {"message":"Hello visit /generate/users/ or /generate/cars/"}

@app.get("/generate/users/")
def generate_fake_users(count: int = Query(10)):
    # Generate fake user data.
    users = [{"name": faker.name(),"number": faker.basic_phone_number(), "email": faker.email(), "address": faker.address()} for _ in range(count)] #here _ is used which is a throwaway variable indicating that variable will not be used. 
    return {"users": users}

@app.get("/generate/cars/")
def generate_fake_cars(count: int = Query(10)):#count determines how many cars to be generated & Query passes count parameter by default in URL if not provided
    cars = []
    for _ in range(count):
        brand = random.choice(list(CARS.keys()))#this selects random cars key which is brand
        model = random.choice(CARS[brand])#it randomly selects value of brand which is model
        colour = faker.color_name()
        owner = random.randint(1, 3)
        year = random.randint(2000, 2023)
        
        cars.append({
            "brand":brand,
            "model":model,
            "colour": colour,
            "owner": owner,
            "year": year
        })
    return {"cars": cars}
        