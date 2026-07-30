# Copyright 2024 Camptocamp SA
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models


class IrMailServer(models.Model):
    _inherit = "ir.mail_server"

    def _prepare_email_message__(self, message, smtp_session):  # noqa: PLW3201
        """
        Define smtp_to based on context instead of To+Cc+Bcc
        """
        x_odoo_bcc_value = next(
            (value for key, value in message._headers if key == "X-Odoo-Bcc"), None
        )
        # Add Bcc field inside message to pass validation
        if x_odoo_bcc_value:
            message["Bcc"] = x_odoo_bcc_value

        smtp_from, smtp_to_list, message = super()._prepare_email_message__(
            message, smtp_session
        )

        return smtp_from, smtp_to_list, message
