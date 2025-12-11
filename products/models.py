from django.db import models

# ドーナツの種類（カテゴリ）管理
class Category(models.Model):
    name = models.CharField(max_length=50)  # カテゴリ名
    slug = models.SlugField(unique=True)  # URLに使われる短い識別子（例：donut、drink）
    description = models.TextField(blank=True)  # 説明文（任意）
    created_at = models.DateTimeField(auto_now_add=True)  # 登録日時
    updated_at = models.DateTimeField(auto_now=True)  # 更新日時

    def __str__(self):
        return self.name

# 商品情報（名前・価格・カテゴリ・説明）
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)  # カテゴリと紐付け
    name = models.CharField(max_length=100)  # 商品名
    price = models.DecimalField(max_digits=6, decimal_places=2)  # 価格 (例: 120.00)
    description = models.TextField(blank=True)
    stock = models.PositiveIntegerField(default=0)  # 在庫数、0以上しか保存できない
    is_available = models.BooleanField(default=True)  # 販売中かどうかのフラグ（True＝販売中）
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.name
