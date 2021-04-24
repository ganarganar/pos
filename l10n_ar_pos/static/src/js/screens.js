odoo.define("l10n_ar_pos.screens", function (require) {
  "use strict";

  var screens = require("point_of_sale.screens");
  var core = require("web.core");
  var _t = core._t;

  screens.ClientListScreenWidget.include({
    save_client_details: function (partner) {
      var self = this;
      var fields = {};
      this.$(".client-details-contents .detail").each(function (idx, el) {
        if (self.integer_client_details.includes(el.name)) {
          var parsed_value = parseInt(el.value, 10);
          if (isNaN(parsed_value)) {
            fields[el.name] = false;
          } else {
            fields[el.name] = parsed_value;
          }
        } else {
          fields[el.name] = el.value || false;
        }
      });
      // if l10n_ar_afip_responsibility_type_id is "Responsable Inscripto", VAT is required
      if (!fields.vat && fields.l10n_ar_afip_responsibility_type_id == "1") {
        this.gui.show_popup("error", _t("Field 'C.U.I.T.' (NIF) is required."));
        return;
      }
      // if l10n_ar_afip_responsibility_type_id is "Responsable Inscripto", document type must be CUIT
      if (
        fields.l10n_latam_identification_type_id != "4" &&
        fields.l10n_ar_afip_responsibility_type_id == "1"
      ) {
        this.gui.show_popup(
          "error",
          _t(
            "C.U.I.T. document type is mandatory for responsability type 'Responsable Inscripto'"
          )
        );
        return;
      }
      this._super(partner);
    },
  });
});
