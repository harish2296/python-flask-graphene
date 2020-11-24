# python-flask-graphene
Python flask grahene example

# Pre Config
  -Add the SQL file to your local db
# Run
  -Run App.Py
  -Visit localhost port 5000 endpoint /graphql 
# Sample Input Query
{
  allStudent {
    edges {
      node {
        name
        email
        studentMeta{
          edges {
            node {
              course
            }
          }
        }
      }
    }
  }
}

# Sample Input Mutation
mutation {
  createStudent(id: 3, name: "Rohit Sharma", email: "vijiharishv199622@gmail.com") {
    id
    name
    email
  }
}



