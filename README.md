# REST API for working with family trees

## Endpoints:

POST v1/people - create a person

GET v1/people/id - get person object which contains parent ids (id=int)
  
GET v1/people/id/ancestors - get the whole family tree of a person
  
GET v1/people/id/ancestors/?depth=N - get last N generations of ancestors

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
2. Created custom recursive field to serialize the same table (People)
3. Added dynamic depth parameter, provided by url request, to show certain amount of generations
