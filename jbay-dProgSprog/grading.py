import os
import re
import sys
# Path to bbfetch repository
sys.path += [os.path.expanduser('~/repos/bbfetch')]
import blackboard.grading

class Grading(blackboard.grading.Grading):
    # Username used to log in to Blackboard
    username = '201303582'
    # Blackboard course id (of the form '_NNNNN_1')
    course = '_63345_1'
    # Names of classes/groups of students to display
    classes = ['Class DA4']
    # auids of students that should be excluded even though part of class
    negative_list = []
    #auids of students that should be included even though not part of class
    positive_list = []
    # Regex pattern and replacement text to abbreviate group names
    student_group_display_regex = (r'Class (\S+)', r'\1')
    # Regex pattern and replacement text to abbreviate handin names
    assignment_name_display_regex = (r'Exercises for Week 0*(\d)', r'W\1')
    # Template indicating where to save each handin
    # attempt_directory_name = '~/dProgSprog2017/W{assignment}-{class_name}/{group}_{id}'
    # Case-insensitive regex used to capture comments indicating a score of 0
    rehandin_regex = r'genaflevering|genaflever|re-?handin'
    # Case-insensitive regex used to capture comments indicating a score of 1
    accept_regex = r'accepted|godkendt'

    def get_attempt_directory_name(self, attempt):
        """
        Return a path to the directory in which to store files
        relating to the given handin.
        """

        name = attempt.student.name
        class_name = self.get_student_group_display(attempt.student)
        attempt_id = attempt.id
        if attempt_id.startswith('_'):
            attempt_id = attempt_id[1:]
        if attempt_id.endswith('_1'):
            attempt_id = attempt_id[:-2]

        return '{base}/{class_name}/{assignment}/{name}_{id}'.format(
            base=os.path.expanduser('~/dProgSprog2017'),
            class_name=class_name,
            assignment=self.get_assignment_name_display(attempt.assignment),
            name=name, id=attempt_id)

if __name__ == "__main__":
    Grading.execute_from_command_line()
