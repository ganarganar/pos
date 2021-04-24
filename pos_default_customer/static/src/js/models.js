odoo.define("pos_default_customer.models", function (require) {
    "use strict";
  
    var models = require("point_of_sale.models");
  
    var _super_order = models.Order.prototype;
    models.Order = models.Order.extend({
      initialize: function () {
        _super_order.initialize.apply(this, arguments);
        if (this.pos.config.partner_id) {
          this.set_client(
            this.pos.db.get_partner_by_id(this.pos.config.partner_id[0])
          );
        }
      },
    });
  });
  