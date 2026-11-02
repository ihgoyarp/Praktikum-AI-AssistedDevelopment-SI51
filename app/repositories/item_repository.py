from app.database import get_db


def list_items():
    """Return all items ordered by id."""
    return get_db().execute(
        "SELECT id, name, total_stock, available_stock FROM item ORDER BY id"
    ).fetchall()


def get_item(item_id):
    """Return a single item by id, or None if it does not exist."""
    return get_db().execute(
        "SELECT id, name, total_stock, available_stock FROM item WHERE id = ?",
        (item_id,),
    ).fetchone()


def create_item(name, total_stock, available_stock):
    """Insert a new item and return its id."""
    cursor = get_db().execute(
        "INSERT INTO item (name, total_stock, available_stock) VALUES (?, ?, ?)",
        (name, total_stock, available_stock),
    )
    return cursor.lastrowid


def decrease_available_stock(item_id, quantity):
    """Decrease stock only when enough is available.

    Returns True when a row was updated, False when stock is insufficient.
    """
    cursor = get_db().execute(
        "UPDATE item SET available_stock = available_stock - ? "
        "WHERE id = ? AND available_stock >= ?",
        (quantity, item_id, quantity),
    )
    return cursor.rowcount == 1


def increase_available_stock(item_id, quantity):
    """Return borrowed quantity to the item's available stock."""
    cursor = get_db().execute(
        "UPDATE item SET available_stock = available_stock + ? WHERE id = ?",
        (quantity, item_id),
    )
    return cursor.rowcount == 1
