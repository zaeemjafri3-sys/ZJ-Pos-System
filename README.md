# ZJ POS System

A complete **point-of-sale (POS) desktop application for Windows**. It manages inventory, billing, customer credit and sales reports for small shops, and works fully offline.

> This repository contains the ready-to-use Windows program only. The source code is private.

## Features

**Inventory**
- Product table with purchase price, sell price, stock quantity, stock value, units sold and stock available
- Inventory Check (read-only search) and Inventory Update (protected by the admin password)
- Add, edit inline, edit with a form, multi-select delete, and undo (Ctrl+Z)
- Low stock alert popup, and low-stock rows highlighted in red
- Live summary bar: items, stock units, units left, units sold and inventory value
- Export the inventory to PDF

**Sales and billing**
- Fast billing screen with live product search and suggestions, stock shown beside the bill
- Undo and redo for bill items (Ctrl+Z / Ctrl+Y), clear bill, automatic bill numbers
- Sell, or Sell and Print with a receipt preview
- Customer name and phone suggestions, amount paid, and automatic credit / balance
- Stock is deducted automatically after every sale

**Sales history**
- Day-by-day sales summary, bills of a day, and the items of each bill
- Every report can be exported to PDF

**Customers**
- Customer list with search, total bills, total purchased, total paid and credit balance
- Customers over the credit alert limit are highlighted
- Customer details with full bill history, editable name and phone, PDF export

**Security and settings**
- Admin and shop passwords (admin password required for sensitive actions)
- Change shop name, admin password, shop password
- Configurable stock alert and credit alert limits
- Machine-locked license activation and a 30-day free trial

**Usability**
- Full keyboard navigation (arrow keys, Enter, Esc, Ctrl+Z, Ctrl+Y, Ctrl+A, Delete)
- Fullscreen desktop interface, works offline

## How it works

1. **First run:** choose *Enter Activation Key* or *Start 30-Day Free Trial*.
2. **Setup:** create the admin account, then the shop name and shop password.
3. **Login:** sign in with the shop password to open the main menu.
4. **Inventory:** add your products and set purchase and sell prices.
5. **Sales:** search products, build the bill, sell, and optionally print the receipt.
6. **Reports:** review sales by day, bill and item, and track customer credit.

## Screenshots

### Getting started
| <img src="screenshots/01_welcome.png" width="300"><br><sub>Welcome: activate or start trial</sub> | <img src="screenshots/01b_activation_key.png" width="300"><br><sub>Enter activation key</sub> | <img src="screenshots/02_admin_setup.png" width="300"><br><sub>Admin setup</sub> |
| :---: | :---: | :---: |
| <img src="screenshots/03_shop_setup.png" width="300"><br><sub>Shop setup</sub> | <img src="screenshots/04_shop_login.png" width="300"><br><sub>Shop login</sub> | <img src="screenshots/05_main_menu.png" width="300"><br><sub>Main menu</sub> |

### Inventory
| <img src="screenshots/06_inventory_menu.png" width="300"><br><sub>Inventory menu</sub> | <img src="screenshots/07_admin_gate.png" width="300"><br><sub>Admin password gate</sub> | <img src="screenshots/08_inventory_check.png" width="300"><br><sub>Inventory check</sub> |
| :---: | :---: | :---: |
| <img src="screenshots/09_low_stock_alert.png" width="300"><br><sub>Low stock alert</sub> | <img src="screenshots/10_inventory_update_menu.png" width="300"><br><sub>Update menu</sub> | <img src="screenshots/11_add_product.png" width="300"><br><sub>Add product</sub> |
| <img src="screenshots/12_edit_mode.png" width="300"><br><sub>Edit mode</sub> | <img src="screenshots/13_delete_mode.png" width="300"><br><sub>Multi-select delete</sub> | <img src="screenshots/14_delete_confirm.png" width="300"><br><sub>Delete confirmation</sub> |

### Sales and billing
| <img src="screenshots/15_sales_menu.png" width="300"><br><sub>Sales menu</sub> | <img src="screenshots/16_sales_screen.png" width="300"><br><sub>Sales screen</sub> | <img src="screenshots/17_product_suggestions.png" width="300"><br><sub>Product suggestions</sub> |
| :---: | :---: | :---: |
| <img src="screenshots/18_bill.png" width="300"><br><sub>Building a bill</sub> | <img src="screenshots/19_confirm_sale.png" width="300"><br><sub>Sell or Sell & Print</sub> | <img src="screenshots/20_customer_info.png" width="300"><br><sub>Customer and credit</sub> |
| <img src="screenshots/21_receipt_preview.png" width="300"><br><sub>Receipt preview</sub> |

### Sales history
| <img src="screenshots/22_sales_summary.png" width="300"><br><sub>Sales summary</sub> | <img src="screenshots/23_daily_bills.png" width="300"><br><sub>Daily bills</sub> | <img src="screenshots/24_bill_items.png" width="300"><br><sub>Bill items</sub> |
| :---: | :---: | :---: |

### Customers
| <img src="screenshots/25_customers.png" width="300"><br><sub>Customer list</sub> | <img src="screenshots/25b_customer_details.png" width="300"><br><sub>Customer details and bill history</sub> | <img src="screenshots/25c_customer_bill_items.png" width="300"><br><sub>Customer bill items</sub> |
| :---: | :---: | :---: |

### Settings
| <img src="screenshots/26_settings.png" width="300"><br><sub>Settings</sub> | <img src="screenshots/27_stock_alert.png" width="300"><br><sub>Stock alert</sub> | <img src="screenshots/28_credit_alert.png" width="300"><br><sub>Credit alert</sub> |
| :---: | :---: | :---: |
| <img src="screenshots/29_change_password.png" width="300"><br><sub>Change password</sub> |

## Download and install

1. Download **`ZJ_Pos_System.exe`** from the [Releases](../../releases) page.
2. Run the file. If Windows SmartScreen appears, click **More info**, then **Run anyway**.
3. On the first screen choose **Start 30-Day Free Trial** or **Enter Activation Key**.

**Requirements:** Windows 10 or 11. No other software needs to be installed.

## Activation

1. Open **Settings**, then **Activate Software**.
2. Tap **Copy Machine ID** and send it to the developer.
3. Enter the activation key you receive and press **Activate**.

The key works only on that PC. During the free trial, the days left are shown on the main menu.

## Receipt printing

Receipts print to a Zebra-compatible printer over a serial port (`COM4`). Connect the printer and make sure it uses that port.

## Where data is stored

- Database: `%LOCALAPPDATA%\ZJ_Pos_System_AppData\pos.db` (SQLite)
- License and trial files: `C:\ProgramData\ZJ_Pos_System_License`

Everything stays on the PC. Nothing is sent online.

## Contact

For activation keys and support, contact **Zaeem at zaeem.jafri.3@gmail.com**.
