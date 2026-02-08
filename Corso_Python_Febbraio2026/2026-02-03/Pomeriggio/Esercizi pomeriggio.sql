/*3-2-2026 Pomeriggio*/
/*Mostra i 10 film più lunghi presenti nel database, ordinandoli dal più lungo al più corto*/
select *
from film
order by length desc
limit 10;

/*Qual è il prezzo medio di noleggio (rental_rate) di tutti i film? 
Rinomina il risultato come "Prezzo_Medio_Noleggio"*/
select avg(rental_rate) as Prezzo_Medio_Noleggio
from film;

/*Nella tabella film, conta quanti film ci sono per ogni durata di noleggio (rental_duration)*/
select rental_duration as Durata_noleggio, count(*) as Numero_film
from film
group by rental_duration;

/*Vai nella tabella payment e conta quanti pagamenti ha registrato ogni staff_id*/
select staff_id, count(*) as Pagamenti
from payment
group by staff_id;

/*Per ogni customer_id nella tabella payment, mostra il pagamento più alto (MAX) 
e quello più basso (MIN) che abbiano mai effettuato*/
select customer_id, MAX(amount) as Pagamento_massimo, MIN(amount) as Pagamento_minimo
from payment
group by customer_id;