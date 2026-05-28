from models import Student

def test_add_student(db_session):
    new_student = Student(
        name="Иван Васильевич",
        email="test@yandex.ru"
    )
    db_session.add(new_student)
    db_session.commit()

    saved = db_session.query(Student).filter_by(email="test@yandex.ru").first()
    assert saved is not None
    assert saved.name == "Иван Васильевич"

    # чистим
    db_session.delete(saved)
    db_session.commit()


def test_update_student(db_session):
    student = Student(name="Old Name", email="test@yandex.ru")
    db_session.add(student)
    db_session.commit()

    student.name = "New Name"
    db_session.commit()

    updated = db_session.query(Student).filter_by(email="test@yandex.ru").first()
    assert updated.name == "New Name"

    db_session.delete(updated)
    db_session.commit()


def test_delete_student(db_session):
    student = Student(name="To Delete", email="test@yandex.ru")
    db_session.add(student)
    db_session.commit()

    db_session.delete(student)
    db_session.commit()

    deleted = db_session.query(Student).filter_by(email="test@yandex.ru").first()
    assert deleted is None