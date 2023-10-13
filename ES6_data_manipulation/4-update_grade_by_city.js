export default function updateStudentGradeByCity(studentsList, city, newGrades) {
  return studentsList
    .filter((student) => student.location === city)
    .map((student) => {
      const matchingGrade = newGrades.find((grade) => grade.studentId === student.id);
      const updatedStudent = { ...student };
      updatedStudent.grade = matchingGrade ? matchingGrade.grade : 'N/A';
      return updatedStudent;
    });
}
