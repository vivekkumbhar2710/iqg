from qr_demo.qr_code import get_qr_code
import frappe
@frappe.whitelist()
def generate_qr_code(invoice_name): 
    cgst_rate = 0
    sgst_rate = 0
    igst_rate = 0
    cgst_amount = 0
    sgst_amount = 0
    igst_amount = 0
    doc=frappe.get_doc("Sales Invoice",invoice_name)
    for s in doc.taxes:
        if(s.account_head=="Output Tax SGST - AFPL"):
            sgst_rate=s.rate
            sgst_amount=s.tax_amount
            if(sgst_rate==None or sgst_rate==0):
                account_head_rate = frappe.get_value("Account",s.account_head,'tax_rate')
                sgst_rate = account_head_rate  if account_head_rate else 0
               
                
        if(s.account_head=="Output Tax CGST - AFPL"):
            cgst_rate=s.rate
            cgst_amount=s.tax_amount
            if(cgst_rate==None or cgst_rate==0):
                account_head_rate = frappe.get_value("Account",s.account_head,'tax_rate')
                cgst_rate = account_head_rate  if account_head_rate else 0
                
        if(s.account_head=="Output Tax IGST - AFPL"):
            igst_rate=s.rate
            igst_amount=s.tax_amount
            if(igst_rate==None or igst_rate==0):
                account_head_rate = frappe.get_value("Account",s.account_head,'tax_rate')
                igst_rate = account_head_rate  if account_head_rate else 0     
    no_data=0 
    qr_content =f'{doc.po_no if doc.po_no else 0},{no_data},{doc.customer},{no_data},{doc.posting_date},{doc.name},{doc.posting_date},{doc.name},{no_data},{doc.total_qty},{no_data},{doc.total},{doc.total},{cgst_amount},{sgst_amount},{igst_amount},{no_data},{cgst_rate},{sgst_rate},{igst_rate},{no_data},{doc.grand_total},{doc.company_gstin},{doc.currency}' 
    return get_qr_code(str(qr_content))  
