### The problem this application tries to solve

#### We'd like you to build a JSON REST API to help us solve this problem. Create a Github account if you do not have one already and put all of your source code on github. Your project should have API endpoints to create, update, delete, and retrieve information about providers. Batch operations are not necessary except for get. A provider should contain the following information:
- Name
- Email
- Phone Number
- Language
- Currency
#### Once a provider is created they should be able to start defining service areas. These service areas will be geojson polygons and should be stored in the database in a way that they can be retrieved and queried upon easily. There should be endpoints to create, update, delete, and get a polygon. Batch operations are not necessary except for get. A polygon should contain a name and price as well as the geojson information.
#### You should create an API endpoint to query this data. It should take a lat/lng pair as arguments and return a list of all polygons that include the given lat/lng. The name of the polygon, provider's name, and price should be returned for each polygon. This operation should be FAST. Mozio has thousands of providers and hundreds of thousands of service areas.