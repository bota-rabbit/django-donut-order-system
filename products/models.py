from django.db import models


# ドーナツの種類（カテゴリ）管理
class Category(models.Model):
    name = models.CharField(max_length=50)  # カテゴリ名
    description = models.TextField(blank=True)  # 説明文（任意）

    def __str__(self):
        return self.name


# 商品情報（名前・価格・カテゴリ・説明）
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL)  # カテゴリと紐付け
    name = models.CharField(max_length=100)  # 商品名
    price = models.DecimalField(max_digits=6, decimal_places=2)  # 価格 (例: 120.00)
    description = models.TextField(blank=True)
    stock = models.PositiveIntegerField(default=0)  # 在庫数、0以上しか保存できない

    def __str__(self):
        return self.name
