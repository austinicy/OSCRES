
low_academic_rank = [300, 600]
medium_academic_rank = [100, 299]
high_academic_rank = [1, 99]
none_academic_rank = [-1, -1]

low_employer_rank = [300, 600]
medium_employer_rank = [100, 299]
high_employer_rank = [1, 99]
none_employer_rank = [-1, -1]

low_faculty_student_rank = [300, 600]
medium_faculty_student_rank = [100, 299]
high_faculty_student_rank = [1, 99]
none_faculty_student_rank = [-1, -1]

low_international_faculty_rank = [300, 600]
medium_international_faculty_rank = [100, 299]
high_international_faculty_rank = [1, 99]
none_international_faculty_rank = [-1, -1]

low_international_student_rank = [300, 600]
medium_international_student_rank = [100, 299]
high_international_student_rank = [1, 99]
none_international_student_rank = [-1, -1]

low_citation_rank = [300, 600]
medium_citation_rank = [100, 299]
high_citation_rank = [1, 99]
none_citation_rank = [-1, -1]

low_tuition_fee = [0, 20000]
medium_tuition_fee = [20001, 50000]
high_tuition_fee = [50001, 90000]
none_tuition_fee = [-1, -1]

low_cost_of_living = [50, 75]
medium_cost_of_living = [76, 100]
high_cost_of_living = [101, 130]
none_cost_of_living = [-1, -1]

low_international_student_percentage = [0, 0.15]
medium_international_student_percentage = [0.16, 0.3]
high_international_student_percentage = [0.31, 0.5]
none_international_student_percentage = [-1.0, -1.0]


def getAcademicRank(level):
    if level == 'high':
        return high_academic_rank
    if level == 'medium':
        return medium_academic_rank
    if level == 'low':
        return low_academic_rank
    if level == 'none':
        return none_academic_rank



def getEmployerRank(level):
    if level == 'high':
        return high_employer_rank
    if level == 'medium':
        return medium_employer_rank
    if level == 'low':
        return low_employer_rank
    if level == 'none':
        return none_employer_rank


def getFacultyStudentRank(level):
    if level == 'high':
        return high_faculty_student_rank
    if level == 'medium':
        return medium_faculty_student_rank
    if level == 'low':
        return low_faculty_student_rank
    if level == 'none':
        return none_faculty_student_rank


def getInternationalFacultyRank(level):
    if level == 'high':
        return high_international_faculty_rank
    if level == 'medium':
        return medium_international_faculty_rank
    if level == 'low':
        return low_international_faculty_rank
    if level == 'none':
        return none_international_faculty_rank


def getInternationalStudentRank(level):
    if level == 'high':
        return high_international_student_rank
    if level == 'medium':
        return medium_international_student_rank
    if level == 'low':
        return low_international_student_rank
    if level == 'none':
        return none_international_student_rank


def getCitationRank(level):
    if level == 'high':
        return high_citation_rank
    if level == 'medium':
        return medium_citation_rank
    if level == 'low':
        return low_citation_rank
    if level == 'none':
        return none_citation_rank

def getWorkStudy(level):
    if level == 'yes':
        return 1
    if level == 'no':
        return 0
    if level == 'none':
        return -1

def getCostOfLiving(level):
    if level == 'high':
        return high_cost_of_living
    if level == 'medium':
        return medium_cost_of_living
    if level == 'low':
        return low_cost_of_living
    if level == 'none':
        return none_cost_of_living

def getInternationalStudentPercentage(level):
    if level == 'high':
        return high_international_student_percentage
    if level == 'medium':
        return medium_international_student_percentage
    if level == 'low':
        return low_international_student_percentage
    if level == 'none':
        return none_international_student_percentage