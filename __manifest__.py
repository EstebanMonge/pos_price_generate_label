# @author: Esteban Monge
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    'name': "Point of Sale - Price generate label",
    'version': '12.0.1.0.0',
    'category': 'Point of Sale',
    'summary': """Point of Sale - print price \
                  labels.""",
    'author': "Esteban Monge",
    'website': "https://github.com/estebanmonge",
    'license': 'AGPL-3',
    'maintainers': ['estebanmonge'],
    'depends': ['point_of_sale'],
    'data': [
        'pos_price_generate_label.xml',
        'views/pos_config_view.xml'
    ],
    'qweb': [
        'static/src/xml/pos_price_generate_label.xml',
    ],
    'installable': True,
}
