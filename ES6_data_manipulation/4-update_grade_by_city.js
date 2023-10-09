export default function updateStudentGradeByCity(students, city, newGrades) {
    const studentsByCity = students.filter((student) => student.location === city);
    const studentsId = studentsByCity.map((student) => student.id);
    const newStudents = students.map((student) => {
        if (studentsId.includes(student.id)) {
        const studentGrade = newGrades.filter((grade) => grade.studentId === student.id);
        return { ...student, grade: studentGrade[0].grade };
        }
        return student;
    });
    return newStudents;
}
