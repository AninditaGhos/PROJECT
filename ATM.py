print("Welcome to ATM")
card=input("insert u r card: ")
if card == "Yes" :
	language= input("Enter u r language: ")
	if language== "English" or language == "Hindi":
		pin = int(input("Enter u r 4 dight pin: "))
		if pin>999 and pin<10000:
			print('1 - Withdraw/WITHDRAW')
			print("2 - Balance enquiry/BALANCE ENQUIRY")
			print("3 - Deposite/DEPOSITE")
			print("4 - bill pay/BILL PAY")
			t_type=int(input("Choose transactions: "))
			if t_type== 1 :
				ac_type=input("enter account type ")
				if ac_type=="saving" or ac_type=="current":
					w_draw_am= int(input("Enter withdraw amount: "))
					if w_draw_am>=500 and w_draw_am<=20000 and w_draw_am%500==0:
						a=w_draw_am//2000
						A=w_draw_am%2000
						b=A//500
						B=A%500
						print("notes of 2000",a,"notes of 500",b)
						rc=input("enter rc yes or not: ")
						if rc=="yes":
							print("amount rc")
							k_n=input("enter key name: ")
							if k_n=="enter" or k_n=="ENTER":
								print("Thank you")
							else:
								print("invalid key name")
						else:
							print("not rc amount")
					else:
						print("not avilable amount")
				else:
					print("account not avilable")
			elif t_type == 2 :
				ac_type=input("enter account type: ")
				if ac_type=="saving" or ac_type=="current":
					bal_enquiry=input("enter balance enquiry yes or not: ")
					if bal_enquiry=="yes":
						print("total amount")
						print("enquiry done")
						k_n=input("enter key name: ")
						if k_n=="enter" or k_n=="ENTER":
							print("Thank you")
						else:
							print("invalid key")
					else:
						print("invalid")
				else:
					print("invalid account")
			elif t_type == 3 :
				account_num=int(input("enter account num: "))
				if account_num>=1000000000 and account_num<=9999999999:
					d_amount=int(input("enter deposit amount"))
					if d_amount>=100 and d_amount<=490000:
						print("Deposite successful: ",d_amount)
						k_n=input("enter key name: ")
						if k_n=="enter" or k_n=="ENTER":
							print("Thank you")
						else:
							print("Invalid key name")
					else:
						print("Deposite unsuccessful")
				else:
					print("Invalid account")
			elif t_type==4:
				account_num=int(input("enter account num: "))
				if account_num>=1000000000 and account_num<=9999999999:
					bill_p=int(input("enter ur bill how much you want to pay: "))
					if bill_p>=100 and bill_p<=20000:
						print("ur bill pay successful",bill_p)
						k_n=input("enter key name: ")
						if k_n=="enter" or k_n=="Enter":
							print(" Thank you: ")
						else:
							print("Invalid key")
					else:
						print("Your bill pay is unsuccessful: ")
				else:
					print(" Account invalid ")
			else:
				print("Worng choice")
		else:
			print("Worng pin number")
	else:
		print("Invalide language")
else:
	print("Please insert card properly")