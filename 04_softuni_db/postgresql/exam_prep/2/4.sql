DELETE
FROM clients
WHERE id in
      (SELECT clients.id
       FROM clients
                LEFT JOIN courses ON clients.id = courses.client_id
       WHERE courses.id IS NULL);