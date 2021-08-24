# Say we wanted to represent a more complex object in python. For example, a 
# cat:

class cat:
  #variable color is now a required input when instantiating could add breed and size.
  def __init__(self,color):
    #self used to call the class/object atributes
      self.size=40
      self.color=color
      self.breed="persian"
  def meow(self): #call self
      print ("meow! I am a " + self.color + ", " + self.breed + " cat.")

#instantiation 
molly = cat("blue")
jesse = cat("orange")

#change atribute
print(molly.size)
jesse.breed = "tabby"
#jesse.color = "Orange"
print(molly.breed)

#call methods
molly.meow()
jesse.meow()

# We use classes because it allows us to store a variety of related data and 
# functions under a single variable. This is a pattern of thinking called 
# 'object-oriented' programming. It may not be relevant for all problems, 
# but like functions, it is useful for breaking problems down or classifying 
# complicated objects. 

# Many people use object-oriented programming, so it's useful to learn what 
# it looks like when you're coding with it.
