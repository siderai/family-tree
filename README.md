# REST API for working with family trees

## Endpoints:

POST /people - create a person

GET /people/id - get person data with parent ids (id=int)
  
GET /people/id/ancestors - get the whole family tree of a person
  
GET /people/id/ancestors/?depth=N - get last N generations of ancestors

## Stack:

Python3
• Django
• DRF
• PostgreSQL
• Docker
• Linux
• Git

## Acquired skills: 
1. Worked with nested serializators (DRF)
2. Created custom recursive field to serialize the same table (people)
3. Added dynamic depth parameter, provided by url request
