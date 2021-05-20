CREATE TABLE `taxas` (
  `id` int(200) NOT NULL,
  `date_created` date NOT NULL,
  `chave` varchar(20) NOT NULL,
  `valor` varchar(20) NOT NULL
);

ALTER TABLE `taxas`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `key_id` (`chave`);

ALTER TABLE `taxas`
  MODIFY `id` int(200) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;
