# Model Module

The model module contains classes with attribute that mirrors the attributes of each table. By storing them into a class, you will get some sort of type safety and text editor auto complete improves developer experience.

Everytime you retrieve rows from a table (for ex. the `emp` table), all of the resulting rows will be wrapped in this class.