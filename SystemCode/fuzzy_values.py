
low_academic_rank = [300, 600]
medium_academic_rank = [100, 299]
high_academic_rank = [1, 99]

low_employer_rank = [300, 600]
medium_employer_rank = [100, 299]
high_employer_rank = [1, 99]

low_faculty_student_rank = []
medium_faculty_student_rank = []
high_faculty_student_rank = []

low_international_faculty_rank = []
medium_international_faculty_rank = []
high_international_faculty_rank = []

low_international_student_rank = []
medium_international_student_rank = []
high_international_student_rank = []

low_citation_rank = []
medium_citation_rank = []
high_citation_rank = []

low_tuition_fee = [0, 20000]
medium_tuition_fee = [20001, 50000]
high_tuition_fee = [50001, 90000]

low_cost_of_living = [50, 75]
medium_cost_of_living = [76, 100]
high_cost_of_living = [101, 130]

low_international_student_percentage = [0, 0.15]
medium_international_student_percentage = [0.16, 0.3]
high_international_student_percentage = [0.31, 0.5]

def getAcademicRank(level):
    if level == 'high':
        return high_academic_rank
    if level == 'medium':
        return medium_academic_rank
    if level == 'low':
        return low_academic_rank

def getEmployerRank(level):
    if level == 'high':
        return high_employer_rank
    if level == 'medium':
        return medium_employer_rank
    if level == 'low':
        return low_employer_rank
