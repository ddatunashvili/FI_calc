

## FI_calc (financial calculator)   https://ddatunashvili.herokuapp.com/
----
**პირადი ფინანსური მენეჯმენტის პროგრამა**

----
### კომპონენტები და გამოყენება
**კომპონენტები**
* მარტივად გამოსაყენებელი დეშბორდი (ui/frontend) და მიბმული მონაცემთა ბაზა (backend)
* ხარჯებს  და შემოსავლებს აქვს პროცენტული მაჩვენებელი 
* შეგყავთ თანხის საერთო რაოდენობა ანგარიშზე (in development)
* ამატებთ ხარჯებს და შემოსავლებს (in development)
* ქმნით შესაბამის ტიპს ანიჭებთ აიქონს (in development)
* შემოსავლები იკრიბება და ემატება მთავარ ბალანს და ხარჯები აკლდება (in development)


**გამოყენების მიზანი**
* აკონროლებ ფინანსებს რამდენი გეხარჯება
* აკონტროლებ შემოსავლებს 
* აკეთებ ანალიზს რა ჯობია და რა არა
* აკეთებ ანალიზს რა რამდენი დაგიჯდება და რამდენად შეძლებ ხარჯების შემცირებას
* აკეთებ ანალიზს რისი შეძენა გინდა და რომელი შემოსავლის წყარო უფრო მომგებიანია შენი ფინანსური კეთილდღეობისთვის

----
### ინსტრუქცია

```bash
python -r requirements.txt
# გაუშვი ორივე ტერმინალით bash/unix ან cmd 
python database.py
python run.py

# გამოიყენე სერვერის ლინკი ui_ს ბრაუზერში გასახსნელად
```

### Quick fix
თუ საიტი არ ეშვება ჰოსტი და პორტი დააკონფიგურე run.py ფაილში
app.run(host='0.0.0.0',port=80,debug=True) 

