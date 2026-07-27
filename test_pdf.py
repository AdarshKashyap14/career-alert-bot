from pdf_reader import check_pdf_for_cse


pdf = "https://www.isro.gov.in/media_isro/pdf/recruitmentNotice/2026/July/Advertisement_Final_17072026.pdf"


if check_pdf_for_cse(pdf):
    print("CSE Eligible ✅")
else:
    print("Not CSE ❌")