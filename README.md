# Design patterns

Personal project exploring various software design patterns. Each pattern is categorised as either **creational**, **structural**, or **behavioural**.

## Creational

### Factory

Provides a generic interface for creating objects where we can specify the type
of object we wish to be created. The factory method is used ***to create one
product***

### Abstract factory

An abstract factory contains one or more factory methods to create a family of
related object. This pattern is about creating ***families of related products
***

### Singleton

Permits only one object to be instantiated. This can be useful for such things
as creating a cache of information to be shared by various elements on the
system. In this way a singleton would act as a kind of object oriented 'global'
variable.

Singleton is a good candidate in several scenarios:

* you need to control concurrent access to a shared resource (such as a the
  current state of a UI)
* you need a global point of access for the resource from multiple parts of the
  system
* if you need to have only one instance (such as a database connection)
