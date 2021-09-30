class MongoDB:

    def findd(self):
        import pymongo
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        print(client.list_database_names())
        db = client["customersdb"]
        customers = db["customers"]
        for x in customers.find():
            print(x)

    def insertvalue(self):
        import pymongo
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        print(client.list_database_names())
        db = client["customersdb"]
        customers = db["customers"]
        collection = customers.my_gfg_collection

        emp_rec1 = {
            "name": "Mr.Geek",
            "eid": 24,
            "location": "delhi"
        }
        emp_rec2 = {
            "name": "Mr.Shaurya",
            "eid": 14,
            "location": "delhi"
        }

        # Insert Data
        rec_id1 = collection.insert_one(emp_rec1)
        rec_id2 = collection.insert_one(emp_rec2)

        print("Data inserted with record ids", rec_id1, " ", rec_id2)

        # Printing the data inserted
        cursor = collection.find()
        for record in cursor:
            print(record)

    def updatevalue(self):
        import pymongo
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        print(client.list_database_names())
        db = client["customersdb"]
        customers = db["customers"]
        collection = customers.my_gfg_collection

        # update all the employee data whose eid is 24
        result = collection.update_many(
            {"eid": 24},
            {
                "$set": {
                    "name": "Mr.Ankush"
                },
                "$currentDate": {"lastModified": True}

            }
        )

        print("Data updated with id", result)

        # Print the new record
        cursor = collection.find()
        for record in cursor:
            print(record)

    def deletevalue(self):
        import pymongo
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        print(client.list_database_names())
        db = client["customersdb"]
        customers = db["customers"]
        collection = customers.my_gfg_collection

        # Created or Switched to collection names: my_gfg_collection
        collection = db.my_gfg_collection

        emp_rec1 = {
            "name": "Mr.som",
            "eid": 24,
            "location": "delhi"
        }
        emp_rec2 = {
            "name": "Mr.Shaurya",
            "eid": 14,
            "location": "Noida"
        }
        emp_rec3 = {
            "name": "Mr.Coder",
            "eid": 14,
            "location": "gurugram"
        }

        # Insert Data
        rec_id1 = collection.insert_one(emp_rec1)
        rec_id2 = collection.insert_one(emp_rec2)
        rec_id3 = collection.insert_one(emp_rec3)
        print("Data inserted with record ids", rec_id1, " ", rec_id2, rec_id3)

        # Printing the document before deletion
        cursor = collection.find()
        for record in cursor:
            print(record)

        # Delete Document with name : Mr Coder
        result = collection.delete_one({"name": "Mr.Coder"})

        # If query would have been delete all entries with eid:14
        # use this
        # result = collection.delete_many("eid":14})

        cursor = collection.find()
        for record in cursor:
            print(record)











x= MongoDB()

#find
x.findd()
#insert
x.insertvalue()

# update
x.updatevalue()

#delete
x.deletevalue()

