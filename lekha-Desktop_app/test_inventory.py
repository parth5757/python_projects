import pytest
from unittest import mock
from tkinter import Tk
from main import InventoryApp  # Assuming your class is in inventory_app.py

@pytest.fixture
def app():
    root = Tk()
    app = InventoryApp(root)
    yield app
    root.destroy()

# Test for adding a product
def test_add_product(app):
    with mock.patch.object(app.c, 'execute') as mock_execute, \
         mock.patch.object(app.conn, 'commit') as mock_commit, \
         mock.patch('tkinter.messagebox.showerror') as mock_error:
        # Setup product details
        app.product_name_entry.insert(0, "Test Product")
        app.quantity_entry.insert(0, "10")
        app.price_entry.insert(0, "15.99")
        app.image_entry.insert(0, "path/to/image.jpg")
        
        # Call the add_product method
        app.add_product()
        
        # Check if execute and commit are called
        mock_execute.assert_called_once_with("INSERT INTO inventory (product, quantity, price, image_path) VALUES (?, ?, ?, ?)", 
                                             ("Test Product", "10", "15.99", "path/to/image.jpg"))
        mock_commit.assert_called_once()

# Test for updating a product
def test_update_product(app):
    with mock.patch.object(app.c, 'execute') as mock_execute, \
         mock.patch.object(app.conn, 'commit') as mock_commit:
        # Setup product details for update
        product_id = 1
        app.product_name_entry.insert(0, "Updated Product")
        app.quantity_entry.insert(0, "20")
        app.price_entry.insert(0, "25.99")
        
        # Call the update_product method
        app.update_product(product_id)
        
        # Check if execute and commit are called
        mock_execute.assert_called_once_with("UPDATE inventory SET product=?, quantity=?, price=? WHERE id=?", 
                                             ("Updated Product", "20", "25.99", product_id))
        mock_commit.assert_called_once()

# Test for selling a product
def test_sell_product(app):
    with mock.patch.object(app.c, 'execute') as mock_execute, \
         mock.patch.object(app.conn, 'commit') as mock_commit, \
         mock.patch('tkinter.messagebox.showinfo') as mock_info, \
         mock.patch('tkinter.messagebox.showerror') as mock_error:
        # Setup product in the database (mock database response)
        product_id = 1
        app.product_id_entry.insert(0, product_id)
        app.sell_quantity_entry.insert(0, "5")
        
        # Simulate fetching product details from the database
        app.c.fetchone = mock.Mock(return_value=(1, "Test Product", 10, 15.99))
        
        # Call the sell_product method
        app.sell_product()
        
        # Check if the update quantity and insert into sales happened
        mock_execute.assert_any_call("UPDATE inventory SET quantity=? WHERE id=?", (5, product_id))
        mock_execute.assert_any_call("INSERT INTO sales (product_id, quantity, total_price) VALUES (?, ?, ?)",
                                     (product_id, "5", 79.95))
        mock_commit.assert_called()
        mock_info.assert_called_with("Success", "5 Test Product sold for $79.95")

# Test for generating a report
def test_generate_report(app):
    with mock.patch.object(app.c, 'execute') as mock_execute:
        # Mock the sales data
        mock_execute.return_value = [(1, 5, 79.95)]
        
        # Call the generate_report method
        app.generate_report()
        
        # Verify the SQL query for sales was executed
        mock_execute.assert_called_once_with("SELECT * FROM sales")

