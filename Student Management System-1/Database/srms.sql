-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 24, 2021 at 05:21 AM
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
-- Table structure for table `certificate_table`
--

CREATE TABLE `certificate_table` (
  `batch` text NOT NULL,
  `name` text NOT NULL,
  `course` text NOT NULL,
  `certificateno` text NOT NULL,
  `certificateissue` text NOT NULL,
  `cissuedate` text NOT NULL,
  `marksheetissue` text NOT NULL,
  `missuedate` text NOT NULL,
  `remark` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `course`
--

CREATE TABLE `course` (
  `cid` int(10) NOT NULL,
  `name` varchar(50) NOT NULL,
  `duration` int(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `course`
--

INSERT INTO `course` (`cid`, `name`, `duration`) VALUES
(1, '', 0),
(2, 'a', 4),
(3, 'python', 3);

-- --------------------------------------------------------

--
-- Table structure for table `employee`
--

CREATE TABLE `employee` (
  `f_name` varchar(20) NOT NULL,
  `l_name` varchar(20) NOT NULL,
  `contact` bigint(10) NOT NULL,
  `email` varchar(30) NOT NULL,
  `question` varchar(50) NOT NULL,
  `answer` varchar(20) NOT NULL,
  `password` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `employee`
--

INSERT INTO `employee` (`f_name`, `l_name`, `contact`, `email`, `question`, `answer`, `password`) VALUES
('Amit', 'Chawarekar', 9503016634, 'amit@gmail.com', 'Your Birth Place', 'bhadgaon', 'amit5'),
('prabhat', 'jaiswar', 9819703749, 'prabhat01@gmail.com', 'Your Birth Place', 'mumbai', 'prabhat123'),
('Neha', 'Patil', 1234, 'neha@gmail.com', 'Your Birth Place', 'mumbai', 'neha123');

-- --------------------------------------------------------

--
-- Table structure for table `enquiry_student`
--

CREATE TABLE `enquiry_student` (
  `date` text NOT NULL,
  `name` text NOT NULL,
  `course` text NOT NULL,
  `coursefees` text NOT NULL,
  `contact1` bigint(10) NOT NULL,
  `contact2` bigint(10) NOT NULL,
  `followup` text NOT NULL,
  `email` text NOT NULL,
  `address` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `enquiry_student`
--

INSERT INTO `enquiry_student` (`date`, `name`, `course`, `coursefees`, `contact1`, `contact2`, `followup`, `email`, `address`) VALUES
('7/12/21', 'a', 'Select Course', '', 0, 0, '', '', '\n');

-- --------------------------------------------------------

--
-- Table structure for table `register_student`
--

CREATE TABLE `register_student` (
  `regid` int(3) UNSIGNED ZEROFILL NOT NULL,
  `date` text NOT NULL,
  `batch` text NOT NULL,
  `name` text NOT NULL,
  `gender` text NOT NULL,
  `contact1` bigint(10) NOT NULL,
  `contact2` bigint(20) NOT NULL,
  `email` text NOT NULL,
  `dob` text NOT NULL,
  `course` text NOT NULL,
  `coursefees` text NOT NULL,
  `amountpaid` text NOT NULL,
  `date_ap` text NOT NULL,
  `balance` text NOT NULL,
  `address` text NOT NULL,
  `applicationform` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `register_student`
--

INSERT INTO `register_student` (`regid`, `date`, `batch`, `name`, `gender`, `contact1`, `contact2`, `email`, `dob`, `course`, `coursefees`, `amountpaid`, `date_ap`, `balance`, `address`, `applicationform`) VALUES
(001, '5/4/21', 'Select', 'a', 'Select', 1234567890, 1234567890, 'bhadgaon', '444422', 'Select Course', '5000', '3000', '424', '2000.0', 'Pune\n', 'a.txt'),
(002, '2424', 'March', 'amit', 'Female', 1234567890, 1234567890, 'bhadgaon', '114', 'a', '5', '3', '324', '2.0', 'rat\n', 'amit.txt'),
(003, '1313', 'Select', 'aaa', 'Select', 1234567890, 1234567890, 'bhadgaon', '3133', 'a', '5000', '400', '1113', '4600.0', 'pune\n', 'aaa.txt'),
(004, '1313', 'Select', 'aaaa', 'Select', 1234567890, 1234567890, 'bhadgaon', '3133', 'a', '5000', '400', '1113', '4600.0', 'pune\n', 'aaaa.txt'),
(005, '13', 'Select', 'sdawdawd', 'Select', 1234567890, 1234567890, 'dfwf', 'dad', 'Select ', 'das', 'dsa', 'asd', 'sda', 'sad\n', 'sdawdawd.txt'),
(006, '7/12/21', 'March', 'aaaaa', 'Male', 1234567890, 1234567890, '13', '7/12/21', 'a', '4', '3', '7/12/21', '1.0', '1d\n', 'aaaaa.txt'),
(007, '7/12/21', 'Select', 'ccccc', 'Select', 1234567890, 1234567890, 'asdd', '7/12/21', 'Select ', '5', '3', '7/12/21', '2.0', 'asdd\n', 'ccccc.txt'),
(008, '7/12/21', 'February', 'amitc', 'Male', 1234567880, 1234567880, 'amit4.chawarekar@gmail.com', '7/12/21', 'a', '5000', '3000', '7/12/21', '2000.0', 'Mumbai\n\n', 'amitc.txt'),
(009, '7/12/21', 'February', 'prabhat', 'Male', 1234567880, 1234567880, 'prabhatjaiswar01@gmail.com', '7/12/21', 'a', '5000', '3000', '7/12/21', '2000.0', 'Mumbai\n\n', 'prabhat.txt'),
(010, '7/12/21', 'July', 'Durvesh', 'Male', 1234567880, 1234567890, 'durveshvpatil01@gmail.com', '7/15/14', 'python', '5000', '3000', '7/13/21', '2000.0', 'Mumbai\n\n', 'Durvesh.txt');

-- --------------------------------------------------------

--
-- Table structure for table `result`
--

CREATE TABLE `result` (
  `rid` int(10) NOT NULL,
  `name` text NOT NULL,
  `course` text NOT NULL,
  `obj` text NOT NULL,
  `practical` text NOT NULL,
  `total` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `result`
--

INSERT INTO `result` (`rid`, `name`, `course`, `obj`, `practical`, `total`) VALUES
(2, 'mitali', 'Select Course', '70', '100', '70'),
(3, 'Amit Chawarekar', '', '30', '40', '70.0'),
(4, 'Mitali Chawarekar', 'MS-CIT', '35', '50', '85.0'),
(5, 'Sanika', 'Python', '30', '30', '60.0'),
(6, 'Durvesh', 'python', '50', '30', '80.0');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `course`
--
ALTER TABLE `course`
  ADD PRIMARY KEY (`cid`);

--
-- Indexes for table `register_student`
--
ALTER TABLE `register_student`
  ADD PRIMARY KEY (`regid`);

--
-- Indexes for table `result`
--
ALTER TABLE `result`
  ADD PRIMARY KEY (`rid`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `course`
--
ALTER TABLE `course`
  MODIFY `cid` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `register_student`
--
ALTER TABLE `register_student`
  MODIFY `regid` int(3) UNSIGNED ZEROFILL NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `result`
--
ALTER TABLE `result`
  MODIFY `rid` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
