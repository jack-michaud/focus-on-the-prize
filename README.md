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

#### Retrive course history

```python

api.retrieve_course_history()

# returns (example):

[
    {
       "comment":"25",
       "grade_title":"A-",
       "affects_gpa":"Y",
       "credits_earned":"1",
       "course_num_key":"LA4000",
       "report_card_comment_id":null,
       "reason_code":null,
       "grad_subject_id":"8",
       "last_updated_date":"2015-06-18",
       "course_period_id":"10313",
       "course_id":"2839",
       "carries_credits":null,
       "gradelevel_title":"11",
       "grade_performance":null,
       "course_history":"Y",
       "id":"183693",
       "marking_period_year":null,
       "modified_date":null,
       "percent_grade":"92",
       "weighted_gpa_points":"4.2",
       "marking_period_id":"291",
       "gpa_points":"3.7",
       "student_id":"167",
       "conduct":null,
       "grade_scale_id":"90",
       "school_id":"1",
       "report_card_grade_id":"751",
       "_is_exam_grade":"",
       "internal_notes":null,
       "course_title":"Advanced  Language and Composition",
       "sub_syear":"2014",
       "credits":"1",
       "location_title":"Academy for Science and Design",
       "course_num":"LA4000",
       "grad_subject_short_name":"English",
       "teacher":"Sockey, Patricia",
       "course_weight":"1",
       "modified_staff_id":null,
       "syear":"2014",
       "_mp_title":null,
       "mp":null,
       "last_updated_user":"372",
       "varchar_gpa_points":null,
       "course_comment":null
    }
    ...
]