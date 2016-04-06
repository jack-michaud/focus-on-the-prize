# FOCUS on the prize

A Focus School Software implementation for comparing grades on a national level.

Also serves as a basic Python API. 

## Goals:
 * Compare logged in user's AP class grades to national standards


## Examples:
#### Initialize
```python

from focus_api import ASDFocusAPI

api = ASDFocusAPI('<username>', '<password>')

```

#### Retrieve course schedule
```python

api.get_schedule()

# returns (example):
[
   {
      "Period - Teacher":"Period 1 - MWH - 035 - Jennifer  Cava",
      "Course":"Study Period",
      "Term":"Full Year",
      "Meeting Days":"MWH",
      "Room":"Jr/Sr Area"
   },
   ...
]

```