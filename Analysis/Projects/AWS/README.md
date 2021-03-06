# AWS Deployment

## Proceed as follows:
1. Read the one-page [report](Pr_Default.pdf)
2. Visit the API call [generator](https://3.94.204.113:5000/generate)
   - Each new session requires acceptance of the Flask server's dummy certificate as shown for Firefox below
   - (this is because I do not proxy HTTP traffic through apache2 to my Flask server to have a "valid" certificate)
   - (this is my server on my AWS instance so (a) it is safe to access it and (b) you should do so to see my work)   
   <img src="images/cert1.jpeg" alt="Click 'Advanced'" width="300"><img src="images/ws.jpeg" alt="ws" width="50"><img src="images/cert2.jpeg" alt="Click 'Accept the Risk and Continue'" width="300">
3. Copy the contents of the API call generator page
4. <a href='https://3.94.204.113:5000/default?account_amount_added_12_24m=0&account_days_in_dc_12_24m=0.0&account_days_in_rem_12_24m=0.0&account_days_in_term_12_24m=0.0&account_incoming_debt_vs_paid_0_24m=nan&account_status=nan&account_worst_status_0_3m=nan&account_worst_status_12_24m=nan&account_worst_status_3_6m=nan&account_worst_status_6_12m=nan&age=24&avg_payment_span_0_12m=100&avg_payment_span_0_3m=nan&merchant_category=Diversified%20entertainment&merchant_group=Entertainment&has_paid=False&max_paid_inv_0_12m=0.0&max_paid_inv_0_24m=0.0&name_in_email=F1+L&num_active_div_by_paid_inv_0_12m=nan&num_active_inv=0&num_arch_dc_0_12m=0&num_arch_dc_12_24m=0&num_arch_ok_0_12m=0&num_arch_ok_12_24m=0&num_arch_rem_0_12m=0&num_arch_written_off_0_12m=nan&num_arch_written_off_12_24m=nan&num_unpaid_bills=10&status_last_archived_0_24m=0&status_2nd_last_archived_0_24m=0&status_3rd_last_archived_0_24m=0&status_max_archived_0_6_months=0&status_max_archived_0_12_months=0&status_max_archived_0_24_months=0&recovery_debt=0&sum_capital_paid_account_0_12m=0&sum_capital_paid_account_12_24m=0&sum_paid_inv_0_12m=100000&time_hours=23.5105555555556&worst_status_active_inv=nan'>Paste</a> them into the address bar of another browser window
5. View (or, if not rendering in github, download and view) my development [notebook](Pr_Default.ipynb)
6. Examine my [custom pipeline module](custom_pipeline.py)
7. Examine my [Flask Server setup](webserver#flask-server-setup) in [routes.py](default.py) and [default.py](default.py)
8. Have a look at my final batch [predictions](default_preds.csv)
9. Call me maybe
