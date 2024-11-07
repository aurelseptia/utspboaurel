class User:
    def __init__(self, username, email, userId):
        self.username = username
        self.email = email
        self.userId = userId
    def login(self, username, email):
        print(f"{self.username} dengan email {self.email} berhasil login.")
    def logout(self):
        print(f"{self.username} berhasil logout.")
class BasicUser(User):
    def __init__(self, username, email, userId):
        super().__init__(username, email, userId)
    def viewProduct(self, productId):
        print(f"Menampilkan informasi produk dengan ID {productId}.")
    def addToCart(self, productId, quantity):
        print(f"Menambahkan {quantity} unit produk dengan ID {productId} ke keranjang belanja.")
class PremiumUser(BasicUser):
    def __init__(self, username, email, userId):
        super().__init__(username, email, userId)
    def applyVoucher(self, voucherCode, cartTotal):
        print(f"Voucher {voucherCode} diterapkan pada total belanja {cartTotal}.")
    def requestPrioritySupport(self, issueDescription):
        print(f"Menghubungi dukungan prioritas dengan deskripsi masalah: {issueDescription}")
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
premium_user = PremiumUser("aurelshop", "aurelseptia7@gmail.com", 101)
seller = Seller("sellerPro", "septiashop@gmail.com", 202)
premium_user.viewProduct(1001)  
premium_user.addToCart(1001, 3)  
premium_user.applyVoucher("VIPDISCOUNT", 250000)  
premium_user.requestPrioritySupport("Masalah pengiriman produk tidak sampai.") 
seller.addProduct("Smart TV", "Smart TV 50 inci, 4K UHD", 7000000, 15)  
seller.processOrder("ORD202", "Dalam pengiriman")  
premium_user.logout()
seller.logout()
