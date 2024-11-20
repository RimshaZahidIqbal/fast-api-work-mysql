CREATE TABLE invoices (
   invoice_id     INT AUTO_INCREMENT PRIMARY KEY,
   invoice_date   DATE NOT NULL,
   invoice_number VARCHAR(50) NOT NULL,
   total          DECIMAL(10, 2) NOT NULL
);


insert into invoices (
   invoice_date,
   invoice_number,
   total
) values ( '2024-01-01',
           'INV001',
           300.00 ),( '2024-02-15',
                      'INV002',
                      150.00 ),( '2024-03-20',
                                 'INV003',
                                 500.00 );

DELIMITER $$

CREATE PROCEDURE get_all_invoices ()
BEGIN
   SELECT invoice_date, 
          invoice_number, 
          total
   FROM invoices
   ORDER BY invoice_date;
END$$

DELIMITER ;