-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 14-Jun-2021 às 13:03
-- Versão do servidor: 10.4.19-MariaDB
-- versão do PHP: 8.0.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `dbescola`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `tbadministrador`
--

CREATE TABLE `tbadministrador` (
  `id` int(11) NOT NULL,
  `user` varchar(20) DEFAULT NULL,
  `senha` varchar(30) DEFAULT NULL,
  `nome` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `tbadministrador`
--

INSERT INTO `tbadministrador` (`id`, `user`, `senha`, `nome`) VALUES
(1, 'Gabriel', '123', 'Gabriel Cabral'),
(2, 'Gabriel', '123', 'Gab');

-- --------------------------------------------------------

--
-- Estrutura da tabela `tbarquivo`
--

CREATE TABLE `tbarquivo` (
  `id` int(11) NOT NULL,
  `nome` varchar(30) DEFAULT NULL,
  `fk_tbmodulos_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `tbarquivo`
--

INSERT INTO `tbarquivo` (`id`, `nome`, `fk_tbmodulos_id`) VALUES
(3, 'dasda', 1);

-- --------------------------------------------------------

--
-- Estrutura da tabela `tbatividades`
--

CREATE TABLE `tbatividades` (
  `id` int(11) NOT NULL,
  `questao` varchar(100) DEFAULT NULL,
  `idmodulo` int(11) DEFAULT NULL,
  `um` varchar(50) DEFAULT NULL,
  `dois` varchar(50) DEFAULT NULL,
  `tres` varchar(50) DEFAULT NULL,
  `quatro` varchar(50) DEFAULT NULL,
  `resposta` int(11) DEFAULT NULL,
  `numero` varchar(30) DEFAULT NULL,
  `fk_tbmodulos_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `tbatividades`
--

INSERT INTO `tbatividades` (`id`, `questao`, `idmodulo`, `um`, `dois`, `tres`, `quatro`, `resposta`, `numero`, `fk_tbmodulos_id`) VALUES
(1, 'dasda', 1, 'das', 'dasd', 'das', 'das', 1, 'ssdas', 1);

-- --------------------------------------------------------

--
-- Estrutura da tabela `tbcategoria`
--

CREATE TABLE `tbcategoria` (
  `id` int(11) NOT NULL,
  `categoriacurso` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `tbcategoria`
--

INSERT INTO `tbcategoria` (`id`, `categoriacurso`) VALUES
(1, 'aula');

-- --------------------------------------------------------

--
-- Estrutura da tabela `tbcliente`
--

CREATE TABLE `tbcliente` (
  `id` int(11) NOT NULL,
  `nome` varchar(45) DEFAULT NULL,
  `telefone` varchar(15) DEFAULT NULL,
  `email` varchar(35) DEFAULT NULL,
  `cpf` varchar(14) DEFAULT NULL,
  `senha` varchar(30) DEFAULT NULL,
  `autorizado` tinyint(1) DEFAULT NULL,
  `tipo` enum('adm','nu') DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `tbcliente`
--

INSERT INTO `tbcliente` (`id`, `nome`, `telefone`, `email`, `cpf`, `senha`, `autorizado`, `tipo`) VALUES
(10, 'Gabriel', '40028922', 'biel@biel', NULL, NULL, NULL, 'adm'),
(16, 'João', '123', 'teste', NULL, NULL, NULL, NULL),
(18, 'Luis', '1212121', 'oloco', NULL, NULL, NULL, NULL),
(19, 'rONALDO', '1212121', 'OLOCO', NULL, NULL, NULL, NULL),
(20, '12', '12', '12', NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Estrutura da tabela `tbcurso`
--

CREATE TABLE `tbcurso` (
  `id` int(11) NOT NULL,
  `titulo` varchar(30) DEFAULT NULL,
  `descricao` varchar(50) DEFAULT NULL,
  `palavrachave` varchar(30) DEFAULT NULL,
  `duracao` int(11) DEFAULT NULL,
  `caminhoIMG` varchar(50) DEFAULT NULL,
  `fk_tbcategoria_id` int(11) DEFAULT NULL,
  `fk_tbinstrutor_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `tbcurso`
--

INSERT INTO `tbcurso` (`id`, `titulo`, `descricao`, `palavrachave`, `duracao`, `caminhoIMG`, `fk_tbcategoria_id`, `fk_tbinstrutor_id`) VALUES
(1, 'Historia', 'Aula', 'veio', 12, 'asdasdas', 1, 1);

-- --------------------------------------------------------

--
-- Estrutura da tabela `tbdetalhemat`
--

CREATE TABLE `tbdetalhemat` (
  `id` int(11) NOT NULL,
  `nome` varchar(30) DEFAULT NULL,
  `video` int(11) DEFAULT NULL,
  `tempo` int(11) DEFAULT NULL,
  `modulo` varchar(30) DEFAULT NULL,
  `fk_tbmodulos_id` int(11) DEFAULT NULL,
  `fk_tbmatricula_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estrutura da tabela `tbinstrutor`
--

CREATE TABLE `tbinstrutor` (
  `id` int(11) NOT NULL,
  `nome` varchar(50) DEFAULT NULL,
  `login` varchar(20) DEFAULT NULL,
  `senha` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `tbinstrutor`
--

INSERT INTO `tbinstrutor` (`id`, `nome`, `login`, `senha`) VALUES
(1, 'Luis', 'luis', '123');

-- --------------------------------------------------------

--
-- Estrutura da tabela `tbmatricula`
--

CREATE TABLE `tbmatricula` (
  `id` int(11) NOT NULL,
  `situacao` enum('m','nm') DEFAULT NULL,
  `andamento` int(11) DEFAULT NULL,
  `data` date DEFAULT NULL,
  `fk_tbcurso_id` int(11) DEFAULT NULL,
  `fk_tbcliente_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `tbmatricula`
--

INSERT INTO `tbmatricula` (`id`, `situacao`, `andamento`, `data`, `fk_tbcurso_id`, `fk_tbcliente_id`) VALUES
(1, 'm', 231, '2021-06-09', 1, 10);

-- --------------------------------------------------------

--
-- Estrutura da tabela `tbmodulos`
--

CREATE TABLE `tbmodulos` (
  `id` int(11) NOT NULL,
  `nome` varchar(30) DEFAULT NULL,
  `sigla` varchar(10) DEFAULT NULL,
  `palavrachave` varchar(30) DEFAULT NULL,
  `fk_tbcurso_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `tbmodulos`
--

INSERT INTO `tbmodulos` (`id`, `nome`, `sigla`, `palavrachave`, `fk_tbcurso_id`) VALUES
(1, 'Historia', 'HIST', 'veio', 1);

-- --------------------------------------------------------

--
-- Estrutura da tabela `tbnotas`
--

CREATE TABLE `tbnotas` (
  `id` int(11) NOT NULL,
  `escolha` int(11) DEFAULT NULL,
  `resposta` int(11) DEFAULT NULL,
  `nota` int(11) DEFAULT NULL,
  `fk_tbatividades_id` int(11) DEFAULT NULL,
  `fk_tbmodulos_id` int(11) DEFAULT NULL,
  `fk_tbmatricula_id` int(11) DEFAULT NULL,
  `fk_tbmatricula_idcurso` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `tbadministrador`
--
ALTER TABLE `tbadministrador`
  ADD PRIMARY KEY (`id`);

--
-- Índices para tabela `tbarquivo`
--
ALTER TABLE `tbarquivo`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_tbmodulos_id` (`fk_tbmodulos_id`);

--
-- Índices para tabela `tbatividades`
--
ALTER TABLE `tbatividades`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_tbmodulos_id` (`fk_tbmodulos_id`);

--
-- Índices para tabela `tbcategoria`
--
ALTER TABLE `tbcategoria`
  ADD PRIMARY KEY (`id`);

--
-- Índices para tabela `tbcliente`
--
ALTER TABLE `tbcliente`
  ADD PRIMARY KEY (`id`);

--
-- Índices para tabela `tbcurso`
--
ALTER TABLE `tbcurso`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_tbcategoria_id` (`fk_tbcategoria_id`),
  ADD KEY `fk_tbinstrutor_id` (`fk_tbinstrutor_id`);

--
-- Índices para tabela `tbdetalhemat`
--
ALTER TABLE `tbdetalhemat`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_tbmodulos_id` (`fk_tbmodulos_id`),
  ADD KEY `fk_tbmatricula_id` (`fk_tbmatricula_id`);

--
-- Índices para tabela `tbinstrutor`
--
ALTER TABLE `tbinstrutor`
  ADD PRIMARY KEY (`id`);

--
-- Índices para tabela `tbmatricula`
--
ALTER TABLE `tbmatricula`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_tbcurso_id` (`fk_tbcurso_id`),
  ADD KEY `fk_tbcliente_id` (`fk_tbcliente_id`);

--
-- Índices para tabela `tbmodulos`
--
ALTER TABLE `tbmodulos`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_tbcurso_id` (`fk_tbcurso_id`);

--
-- Índices para tabela `tbnotas`
--
ALTER TABLE `tbnotas`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_tbatividades_id` (`fk_tbatividades_id`),
  ADD KEY `fk_tbmodulos_id` (`fk_tbmodulos_id`),
  ADD KEY `fk_tbmatricula_id` (`fk_tbmatricula_id`),
  ADD KEY `fk_tbmatricula_idcurso` (`fk_tbmatricula_idcurso`);

--
-- AUTO_INCREMENT de tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `tbadministrador`
--
ALTER TABLE `tbadministrador`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de tabela `tbarquivo`
--
ALTER TABLE `tbarquivo`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de tabela `tbatividades`
--
ALTER TABLE `tbatividades`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de tabela `tbcategoria`
--
ALTER TABLE `tbcategoria`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de tabela `tbcliente`
--
ALTER TABLE `tbcliente`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT de tabela `tbcurso`
--
ALTER TABLE `tbcurso`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de tabela `tbdetalhemat`
--
ALTER TABLE `tbdetalhemat`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `tbinstrutor`
--
ALTER TABLE `tbinstrutor`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de tabela `tbmatricula`
--
ALTER TABLE `tbmatricula`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de tabela `tbmodulos`
--
ALTER TABLE `tbmodulos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de tabela `tbnotas`
--
ALTER TABLE `tbnotas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Restrições para despejos de tabelas
--

--
-- Limitadores para a tabela `tbarquivo`
--
ALTER TABLE `tbarquivo`
  ADD CONSTRAINT `tbarquivo_ibfk_1` FOREIGN KEY (`fk_tbmodulos_id`) REFERENCES `tbmodulos` (`id`);

--
-- Limitadores para a tabela `tbatividades`
--
ALTER TABLE `tbatividades`
  ADD CONSTRAINT `tbatividades_ibfk_1` FOREIGN KEY (`fk_tbmodulos_id`) REFERENCES `tbmodulos` (`id`);

--
-- Limitadores para a tabela `tbcurso`
--
ALTER TABLE `tbcurso`
  ADD CONSTRAINT `tbcurso_ibfk_1` FOREIGN KEY (`fk_tbcategoria_id`) REFERENCES `tbcategoria` (`id`),
  ADD CONSTRAINT `tbcurso_ibfk_2` FOREIGN KEY (`fk_tbinstrutor_id`) REFERENCES `tbinstrutor` (`id`);

--
-- Limitadores para a tabela `tbdetalhemat`
--
ALTER TABLE `tbdetalhemat`
  ADD CONSTRAINT `tbdetalhemat_ibfk_1` FOREIGN KEY (`fk_tbmodulos_id`) REFERENCES `tbmodulos` (`id`),
  ADD CONSTRAINT `tbdetalhemat_ibfk_2` FOREIGN KEY (`fk_tbmatricula_id`) REFERENCES `tbmatricula` (`id`);

--
-- Limitadores para a tabela `tbmatricula`
--
ALTER TABLE `tbmatricula`
  ADD CONSTRAINT `tbmatricula_ibfk_1` FOREIGN KEY (`fk_tbcurso_id`) REFERENCES `tbcurso` (`id`),
  ADD CONSTRAINT `tbmatricula_ibfk_2` FOREIGN KEY (`fk_tbcliente_id`) REFERENCES `tbcliente` (`id`);

--
-- Limitadores para a tabela `tbmodulos`
--
ALTER TABLE `tbmodulos`
  ADD CONSTRAINT `tbmodulos_ibfk_1` FOREIGN KEY (`fk_tbcurso_id`) REFERENCES `tbcurso` (`id`);

--
-- Limitadores para a tabela `tbnotas`
--
ALTER TABLE `tbnotas`
  ADD CONSTRAINT `tbnotas_ibfk_1` FOREIGN KEY (`fk_tbatividades_id`) REFERENCES `tbatividades` (`id`),
  ADD CONSTRAINT `tbnotas_ibfk_2` FOREIGN KEY (`fk_tbmodulos_id`) REFERENCES `tbmodulos` (`id`),
  ADD CONSTRAINT `tbnotas_ibfk_3` FOREIGN KEY (`fk_tbmatricula_id`) REFERENCES `tbmatricula` (`id`),
  ADD CONSTRAINT `tbnotas_ibfk_4` FOREIGN KEY (`fk_tbmatricula_idcurso`) REFERENCES `tbmatricula` (`fk_tbcurso_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
