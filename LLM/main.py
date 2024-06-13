"""

To learn/check -> https://karpathy.ai/zero-to-hero.html

"""

import tiktoken

encoding = tiktoken.encoding_for_model('gpt-2')

encoded = encoding.encode("What is your name?")

print(encoded)

decoded = encoding.decode(encoded)

print(decoded)

print(encoding.encode("Payment"))

print(encoding.decode([19197]))
print(encoding.decode([434]))

"""
ML 
- Greedy selection
- Markov chains
- Backpropagation
"""




