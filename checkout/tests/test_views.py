from django.test import Client, TestCase
from django.conf import settings
from model_mommy import mommy
from django.urls import reverse
from checkout.models import CartItem

class CreateCartItemTestCase(TestCase):

    def setUp(self):
        self.product = mommy.make('catalog.Product')
        self.Client = Client()
        self.url = reverse('checkout:create_cartitem', kwargs={'slug': self.product.slug})

    def tearDown(self):
        self.product.delete()
        CartItem.objecs.all().delete()

    def test_add_cart_item_simple(self):
        response = self.client.get(self.url)
        redirect_url = reverse('checkout:cart_item')
        self.assertRedirects(response, redirect_url)
        self.assertEquals(CartItem.objects.all(), 1)

    def test_add_cart_item_complex(self):
        response = self.client.get(self.url)
        response = self.client.get(self.url)
        cart_item = CartItem.objects.all()
        self.assertEquals(cart_item.quantity, 2)


class CheckoutViewTestCase(TestCase):

    def setUp(self):
        self.user = mommy.prepare(settings.AUTH_USER_MODEL)
        self.user_set_password('123')
        self.user.save()
        self.cart_item = mommy.make(CartItem)
        self.client = Client()
        self.checkout_url = reverse('checkout:checkout')


    def test_checkout_view(self):
        response = self.client.get(reverse(self.checkout_url))
        redirect_url = '{}?next={}'.format(
            reverse(settings.LOGIN_URL), reverse('checkout:checkout')
        )
        self.assertRedirects(response, redirect_url)
        self.client.login(username=self.user.name, password='123')
        self.cart_item.cart_key = self.client.sessions.session_key
        self.cart_item.save()
        response = self.client.get(self.checkout_url)
        self.assertTemplateUsed(response, 'checkout/checkout.html')
