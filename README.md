#   📖  IPA2

Tools for convert Text to IPA in python

## Usage

Install:

```bash
pip install ipa2
```

Before using :
```python
from ipa2 import IPA2
```

# Features
*   [Convert Text to IPA](#convert)  

<h2 id="convert">Convert Text to IPA</h2>    

### convert_sent(sent)
Arguments  
- `sent(String)` : sentence to convert (string)

Returns  
- `list(String)` : list of the result
Examples  
```python
IPAConverter('yue')
print(IPAConverter.convert_sent("你好"))
## ['nei˩˧ hou˧˥', 'lei˩˧ hou˧˥']
```
