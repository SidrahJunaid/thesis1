import re
text="#python"
text = re.sub(r'#([^\s]+)', r'\1', text)
print(text)