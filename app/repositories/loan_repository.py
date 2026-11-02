from app.database import get_db


def create_loan(student_id, item_id, quantity):
    """Insert a BORROWED loan and return its id."""
    cursor = get_db().execute(
        "INSERT INTO loan (student_id, item_id, quantity, status) "
        "VALUES (?, ?, ?, 'BORROWED')",
        (student_id, item_id, quantity),
    )
    return cursor.lastrowid


def get_loan(loan_id):
    """Return a single loan by id, or None if it does not exist."""
    return get_db().execute(
        "SELECT id, student_id, item_id, quantity, status, created_at "
        "FROM loan WHERE id = ?",
        (loan_id,),
    ).fetchone()


def update_loan_status(loan_id, status):
    """Update a loan status and return True when the row exists."""
    cursor = get_db().execute(
        "UPDATE loan SET status = ? WHERE id = ?",
        (status, loan_id),
    )
    return cursor.rowcount == 1


def get_loans_by_student(student_id):
    """Return all loans belonging to a student, ordered by id."""
    return get_db().execute(
        "SELECT id, student_id, item_id, quantity, status, created_at "
        "FROM loan WHERE student_id = ? ORDER BY id",
        (student_id,),
    ).fetchall()
