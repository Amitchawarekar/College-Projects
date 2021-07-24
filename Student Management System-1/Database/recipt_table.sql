-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 24, 2021 at 06:00 AM
-- Server version: 10.4.18-MariaDB
-- PHP Version: 8.0.5

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `srms`
--

-- --------------------------------------------------------

--
-- Table structure for table `recipt_table`
--

CREATE TABLE `recipt_table` (
  `date` text NOT NULL,
  `instno` int(11) NOT NULL,
  `instreciptno` int(11) NOT NULL,
  `name` text NOT NULL,
  `sofruppes` bigint(20) NOT NULL,
  `course` text NOT NULL,
  `coursefees` bigint(20) NOT NULL,
  `amountpaid` bigint(20) NOT NULL,
  `paidby` bigint(20) NOT NULL,
  `balance` bigint(20) NOT NULL,
  `recipt` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `recipt_table`
--

INSERT INTO `recipt_table` (`date`, `instno`, `instreciptno`, `name`, `sofruppes`, `course`, `coursefees`, `amountpaid`, `paidby`, `balance`, `recipt`) VALUES
('MM-DD-YYYY', 0, 1, 'Amit', 0, 'Select ', 0, 0, 0, 0, 'Amit.txt');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `recipt_table`
--
ALTER TABLE `recipt_table`
  ADD PRIMARY KEY (`instreciptno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `recipt_table`
--
ALTER TABLE `recipt_table`
  MODIFY `instreciptno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
