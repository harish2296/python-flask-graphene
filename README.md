# python-flask-graphene
Python flask grahene example

# Pre Config
  -Add the SQL file to your local db
# Run
  -Run App.Py
  -Visit localhost port 5000 endpoint /graphql 
# Sample Input
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


