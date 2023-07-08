## Interview take-home assignment for Microtrade 2002 Kft.

### Packages used:
  - Django
  - Django Rest Framework
  - DRF Spectacular (To allow OpenAPI docs generation)

To see the interactive Swagger documentation for the endpoints please launch the project and navigate to the /docs endpoint

### Endpoints:
  - /company/
    - GET - Return a list of companies.
      - Optional query params:
        - name: filter the list by the name or email address of the company
        - order: order the returned list by the provided field name
      - Example request: http://127.0.0.1:8000/api/company/?name=Dog&order=name
    - POST - Create a company with the provided JSON body as specified by the assignment description
  - /admin/
    - Default Django admin panel
      - username: admin
      - password: 1234
  - /docs/
    - Provides an endpoint the access the interactive SwaggerUI Documentation of the app through browsers
  - /docs/schema
    - Responds with a schema.yaml file, containing the OpenAPI documentation of the application
### Models:
![kép](https://github.com/hanubence/microtrade/assets/32911312/c1964455-9468-4283-a46b-c50992506f81)


