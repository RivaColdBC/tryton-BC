#This file is part of Tryton.  The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.
from trytond.model import ModelView, ModelSQL, fields


class Category(ModelSQL, ModelView):
    _name = 'product.category'

    account_expense = fields.Property(type='many2one',
            relation='account.account', string='Account Expense',
            domain="[('kind', '=', 'expense'), ('company', '=', company)]",
            states={
                'invisible': "not company",
            })
    account_revenue = fields.Property(type='many2one',
            relation='account.account', string='Account Revenue',
            domain="[('kind', '=', 'revenue'), ('company', '=', company)]",
            states={
                'invisible': "not company",
            })
    customer_taxes = fields.Many2Many('product.category-customer-account.tax',
            'product', 'tax', 'Customer Taxes', domain=[('parent', '=', False)])
    supplier_taxes = fields.Many2Many('product.category-supplier-account.tax',
            'product', 'tax', 'Supplier Taxes', domain=[('parent', '=', False)])

Category()


class CategoryCustomerTax(ModelSQL):
    'Category - Customer Tax'
    _name = 'product.category-customer-account.tax'
    _table = 'product_category_customer_taxes_rel'
    _description = __doc__
    product = fields.Many2One('product.category', 'Category',
            ondelete='CASCADE', select=1, required=True)
    tax = fields.Many2One('account.tax', 'Tax', ondelete='RESTRICT',
            required=True)

CategoryCustomerTax()


class CategorySupplierTax(ModelSQL):
    'Category - Supplier Tax'
    _name = 'product.category-supplier-account.tax'
    _table = 'product_category_supplier_taxes_rel'
    _description = __doc__
    product = fields.Many2One('product.category', 'Category',
            ondelete='CASCADE', select=1, required=True)
    tax = fields.Many2One('account.tax', 'Tax', ondelete='RESTRICT',
            required=True)

CategorySupplierTax()


class Template(ModelSQL, ModelView):
    _name = 'product.template'

    account_category = fields.Boolean('Use Category\'s accounts',
            help='Use the accounts defined on the category')
    account_expense = fields.Property(type='many2one',
            string='Account Expense', relation='account.account',
            domain="[('kind', '=', 'expense'), ('company', '=', company)]",
            states={
                'invisible': "not bool(company) or bool(account_category)",
                'required': "not bool(account_category)",
            }, help='This account will be used instead of the one defined ' \
                    'on the category.', depends=['account_category'])
    account_revenue = fields.Property(type='many2one',
            string='Account Revenue', relation='account.account',
            domain="[('kind', '=', 'revenue'), ('company', '=', company)]",
            states={
                'invisible': "not bool(company) or bool(account_category)",
                'required': "not bool(account_category)",
            }, help='This account will be used instead of the one defined ' \
                    'on the category.', depends=['account_category'])
    account_expense_used = fields.Function('get_account', type='many2one',
            relation='account.account', string='Account Expense Used')
    account_revenue_used = fields.Function('get_account', type='many2one',
            relation='account.account', string='Account Revenue Used')
    taxes_category = fields.Boolean('Use Category\'s Taxes', help='Use the taxes ' \
            'defined on the category')
    customer_taxes = fields.Many2Many('product.template-customer-account.tax',
            'product', 'tax', 'Customer Taxes', domain=[('parent', '=', False)],
            states={
                'invisible': "not bool(company) or bool(taxes_category)",
            }, depends=['taxes_category'])
    supplier_taxes = fields.Many2Many('product.template-supplier-account.tax',
            'product', 'tax', 'Supplier Taxes', domain=[('parent', '=', False)],
            states={
                'invisible': "not bool(company) or bool(taxes_category)",
            }, depends=['taxes_category'])
    customer_taxes_used = fields.Function('get_taxes', type='many2many',
            relation='account.tax', string='Customer Taxes Used')
    supplier_taxes_used = fields.Function('get_taxes', type='many2many',
            relation='account.tax', string='Customer Taxes Used')

    def __init__(self):
        super(Template, self).__init__()
        self._error_messages.update({
            'missing_account': 'There is no account ' \
                    'expense/revenue define on the product ' \
                    '%s (%d)',
            })

    def default_taxes_category(self, cursor, user, context=None):
        return False

    def get_account(self, cursor, user, ids, name, arg, context=None):
        account_obj = self.pool.get('account.account')
        res = {}
        name = name[:-5]
        for product in self.browse(cursor, user, ids, context=context):
            if product[name]:
                res[product.id] = product[name].id
            else:
                if product.category[name]:
                    res[product.id] = product.category[name].id
                else:
                    self.raise_user_error(cursor, 'missing_account',
                            (product.name, product.id), context=context)
        return res

    def get_taxes(self, cursor, user, ids, name, arg, context=None):
        res = {}
        name = name[:-5]
        for product in self.browse(cursor, user, ids, context=context):
            if product.taxes_category:
                res[product.id] = [x.id for x in product.category[name]]
            else:
                res[product.id] = [x.id for x in product[name]]
        return res

Template()


class TemplateCustomerTax(ModelSQL):
    'Product Template - Customer Tax'
    _name = 'product.template-customer-account.tax'
    _table = 'product_customer_taxes_rel'
    _description = __doc__
    product = fields.Many2One('product.template', 'Product Template',
            ondelete='CASCADE', select=1, required=True)
    tax = fields.Many2One('account.tax', 'Tax', ondelete='RESTRICT',
            required=True)

TemplateCustomerTax()


class TemplateSupplierTax(ModelSQL):
    'Product Template - Supplier Tax'
    _name = 'product.template-supplier-account.tax'
    _table = 'product_supplier_taxes_rel'
    _description = __doc__
    product = fields.Many2One('product.template', 'Product Template',
            ondelete='CASCADE', select=1, required=True)
    tax = fields.Many2One('account.tax', 'Tax', ondelete='RESTRICT',
            required=True)

TemplateSupplierTax()
