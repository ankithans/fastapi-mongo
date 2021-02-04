import motor.motor_asyncio

MONGO_URI = "mongodb+srv://ankit:ankit@cluster0.ubbgm.mongodb.net/students?retryWrites=true&w=majority"
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
database = client.students
student_collection = database.get_collection("students_collection")

def student_helper(student):
    return {
        "id": str(student["_id"]),
        "fullname": student["fullname"],
        "email": student["email"],
        "course_of_Study": student["course_of_Study"],
        "year": student["year"],
        "GPA": student["gpa"],
    }