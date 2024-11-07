# inheritance hierarki
class User:
    def __init__(self, username, email, userId):
        self.username = username
        self.email = email
        self.userId = userId
    def login(self, username, email):
        print(f"{self.username} dengan email {self.email} berhasil login.")

    def logout(self):
        print(f"{self.username} berhasil logout.")
class Seller(User):
    def __init__(self, username, email, userId):
        super().__init__(username, email, userId)
        self.products = []  
    def addProduct(self, productName, description, price, stock):
        product = {
            'productName': productName,
            'description': description,
            'price': price,
            'stock': stock
        }
        self.products.append(product)
        print(f"Produk {productName} telah ditambahkan dengan harga {price} dan stok {stock}.")
    def processOrder(self, orderId, status):
        print(f"Pesanan {orderId} telah diproses. Status: {status}")
class Admin(User):
    def __init__(self, username, email, userId):
        super().__init__(username, email, userId)
    def removeUser(self, userId):
        print(f"Pengguna dengan ID {userId} telah dihapus dari sistem.")
    def generateReport(self, reportType, startDate, endDate):
        print(f"Menhasilkan laporan {reportType} dari {startDate} hingga {endDate}.")
seller = Seller("seller_user", "septiashop@gmail.com", "S12345")
admin = Admin("admin_user", "aurelseptia7@email.com", "A12345")
seller.login(seller.username, seller.email)
admin.login(admin.username, admin.email)
seller.addProduct("Laptop", "Laptop gaming dengan spesifikasi tinggi", 15000000, 10)
seller.addProduct("Smartphone", "Smartphone terbaru dengan kamera 108MP", 5000000, 50)
seller.processOrder("ORD123", "Dalam pengiriman")
admin.removeUser("S12345")
admin.generateReport("Transaksi", "2024-01-01", "2024-10-31")
seller.logout()
admin.logout()
