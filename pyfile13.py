# in this program we will learn to use functions
def IPotter(name):
    text = '''Looking Slughorn straight in the eye, Harry leant forwards a little.
    'I am the Chosen One. I have to kill Voldemort. I need that memory.'
    'You are the Chosen One?'
    'Of course I am,' said Harry calmly.'''
    new_text = text.replace("Harry", name)
    print(new_text)

# Example usage
IPotter("Athar")
