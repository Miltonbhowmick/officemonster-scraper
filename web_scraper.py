from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.window import WindowTypes
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import logging
from datetime import datetime
import random
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
import threading
import socket
import io
from PIL import Image

SCRAPER_SETUP = 1

EXPRESS_VPN_LIST = [
    "Canada",
    "Denmark",
    "France",
    "Finland",
    "Germany",
    "Hungary",
    "Norway",
    "Sweden",
    "Switzerland",
    "United Kingdom",
    "United States",
]

CYBER_GHOST_VPN_LIST = [
    "Canada",
    "Denmark",
    "France",
    "Finland",
    "Germany",
    "Hungary",
    "Norway",
    "Russia",
    "Sweden",
    "Switzerland",
    "United Arab Emirates",
    "United Kingdom",
    "United States",
]

PROTON_VPN_LIST = [
    "AR#17",
    "AR#18",
    "AR#19",
    "AR#20",
    "AR#21",
    "AR#22",
    "AR#23",
    "AR#24",
    "AR#25",
    "AR#26",
    "AR#27",
    "AR#28",
    "AR#29",
    "AR#30",
    "AR#31",
    "AR#32",
    "AU#29",
    "AU#30",
    "AU#31",
    "AU#32",
    "AU#33",
    "AU#34",
    "AU#35",
    "AU#36",
    "AU#45",
    "AU#46",
    "AU#47",
    "AU#48",
    "AU#49",
    "AU#50",
    "AU#51",
    "AU#52",
    "AU#53",
    "AU#54",
    "AU#55",
    "AU#56",
    "AU#57",
    "AU#58",
    "AU#59",
    "AU#60",
    "AU#61",
    "AU#62",
    "AU#63",
    "AU#64",
    "AU#65",
    "AU#66",
    "AU#67",
    "AU#68",
    "AU#69",
    "AU#70",
    "AU#71",
    "AU#72",
    "AU#73",
    "AU#74",
    "AU#75",
    "AU#76",
    "AU#77",
    "AU#78",
    "AU#79",
    "AU#80",
    "AU#81",
    "AU#82",
    "AU#83",
    "AU#84",
    "AU#85",
    "AU#86",
    "AU#87",
    "AU#88",
    "AU#89",
    "AU#90",
    "AU#91",
    "AU#92",
    "AU#101",
    "AU#102",
    "AU#103",
    "AU#104",
    "AU#105",
    "AU#106",
    "AU#107",
    "AU#108",
    "AU#109",
    "AU#110",
    "AU#111",
    "AU#112",
    "AU#113",
    "AU#114",
    "AU#115",
    "AU#116",
    "AU#117",
    "AU#118",
    "AU#119",
    "AU#120",
    "AU#121",
    "AU#122",
    "AU#123",
    "AU#124",
    "AU#125",
    "AU#126",
    "AU#127",
    "AU#128",
    "AU#129",
    "AU#130",
    "AU#131",
    "US-AZ#9",
    "US-AZ#10",
    "US-AZ#11",
    "US-AZ#12",
    "US-AZ#13",
    "US-AZ#14",
    "US-AZ#15",
    "US-AZ#16",
    "US-AZ#17",
    "US-AZ#18",
    "US-AZ#19",
    "US-AZ#20",
    "US-AZ#21",
    "US-AZ#22",
    "US-AZ#23",
    "US-AZ#24",
    "US-AZ#25",
    "US-AZ#26",
    "US-AZ#27",
    "US-AZ#28",
    "US-AZ#29",
    "US-AZ#30",
    "US-AZ#31",
    "US-AZ#32",
    "US-CA#17",
    "US-CA#18",
    "US-CA#19",
    "US-CA#20",
    "US-CA#21",
    "US-CA#22",
    "US-CA#23",
    "US-CA#24",
    "US-CA#25",
    "US-CA#26",
    "US-CA#27",
    "US-CA#28",
    "US-CA#29",
    "US-CA#30",
    "US-CA#31",
    "US-CA#32",
    "US-CA#33",
    "US-CA#34",
    "US-CA#35",
    "US-CA#36",
    "US-CA#37",
    "US-CA#38",
    "US-CA#39",
    "US-CA#40",
    "US-CA#41",
    "US-CA#42",
    "US-CA#43",
    "US-CA#44",
    "US-CA#45",
    "US-CA#46",
    "US-CA#47",
    "US-CA#48",
    "US-CA#49",
    "US-CA#50",
    "US-CA#51",
    "US-CA#52",
    "US-CA#53",
    "US-CA#54",
    "US-CA#55",
    "US-CA#56",
    "US-CA#57",
    "US-CA#58",
    "US-CA#59",
    "US-CA#60",
    "US-CA#61",
    "US-CA#62",
    "US-CA#63",
    "US-CA#64",
    "US-CA#65",
    "US-CA#66",
    "US-CA#67",
    "US-CA#68",
    "US-CA#69",
    "US-CA#70",
    "US-CA#71",
    "US-CA#72",
    "US-CA#77",
    "US-CA#78",
    "US-CA#79",
    "US-CA#80",
    "US-CA#81",
    "US-CA#82",
    "US-CA#83",
    "US-CA#84",
    "US-CA#85",
    "US-CA#86",
    "US-CA#87",
    "US-CA#88",
    "US-CA#89",
    "US-CA#90",
    "US-CA#91",
    "US-CA#92",
    "US-CA#93",
    "US-CA#94",
    "US-CA#95",
    "US-CA#96",
    "US-CA#97",
    "US-CA#98",
    "US-CA#99",
    "US-CA#100",
    "UK#53",
    "UK#54",
    "UK#55",
    "UK#56",
    "UK#57",
    "UK#58",
    "UK#59",
    "UK#60",
    "UK#61",
    "UK#62",
    "UK#63",
    "UK#64",
    "UK#65",
    "UK#66",
    "UK#67",
    "UK#68",
    "UK#69",
    "UK#70",
    "UK#71",
    "UK#72",
    "UK#73",
    "UK#74",
    "UK#75",
    "UK#76",
    "UK#77",
    "UK#78",
    "UK#79",
    "UK#80",
    "UK#81",
    "UK#82",
    "UK#83",
    "UK#84",
    "UK#85",
    "UK#86",
    "UK#87",
    "UK#88",
    "UK#89",
    "UK#90",
    "UK#91",
    "UK#92",
    "UK#93",
    "UK#94",
    "UK#95",
    "UK#96",
    "UK#97",
    "UK#98",
    "UK#99",
    "UK#100",
    "UK#101",
    "UK#102",
    "UK#103",
    "UK#104",
    "UK#105",
    "UK#106",
    "UK#107",
    "UK#108",
    "UK#109",
    "UK#110",
    "UK#111",
    "UK#112",
    "UK#113",
    "UK#114",
    "UK#115",
    "UK#116",
    "UK#117",
    "UK#118",
    "UK#119",
    "UK#120",
    "UK#121",
    "UK#122",
    "UK#123",
    "UK#124",
    "UK#125",
    "UK#126",
    "UK#127",
    "UK#128",
    "UK#129",
    "UK#130",
    "UK#131",
    "UK#132",
    "UK#133",
    "UK#134",
    "UK#135",
    "UK#136",
    "UK#137",
    "UK#138",
    "UK#139",
    "UK#140",
    "UK#141",
    "UK#142",
    "UK#143",
    "UK#144",
    "UK#145",
    "UK#146",
    "UK#147",
    "UK#148",
    "UK#149",
    "UK#150",
    "UK#151",
    "UK#152",
    "UK#153",
    "UK#154",
    "UK#155",
    "UK#156",
    "UK#157",
    "UK#158",
    "UK#159",
    "UK#160",
    "UK#161",
    "UK#162",
    "UK#163",
    "UK#164",
    "UK#165",
    "UK#166",
    "UK#167",
    "UK#168",
    "UK#169",
    "UK#170",
    "UK#171",
    "UK#172",
    "UK#173",
    "UK#174",
    "UK#175",
    "UK#176",
    "UK#177",
    "UK#178",
    "AE#9",
    "AE#10",
    "AE#11",
    "AE#12",
    "AE#13",
    "AE#14",
    "AE#15",
    "AE#16",
    "AE#21",
    "AE#22",
    "AE#23",
    "AE#24",
    "AE#25",
    "AE#26",
    "AE#27",
    "AE#28",
    "DE#1",
    "DE#2",
    "DE#3",
    "DE#4",
    "DE#5",
    "DE#6",
    "DE#7",
    "DE#8",
    "DE#9",
    "DE#10",
    "DE#11",
    "DE#12",
    "DE#13",
    "DE#14",
    "DE#15",
    "DE#16",
    "DE#17",
    "DE#18",
    "DE#19",
    "DE#20",
    "DE#33",
    "DE#34",
    "DE#35",
    "DE#36",
    "DE#90",
    "DE#91",
    "DE#92",
    "DE#93",
    "DE#94",
    "DE#95",
    "DE#96",
    "DE#97",
    "DE#98",
    "DE#99",
    "DE#100",
    "DE#101",
    "DE#54",
    "DE#55",
    "DE#56",
    "DE#57",
    "DE#58",
    "DE#59",
    "DE#60",
    "DE#61",
    "DE#62",
    "DE#63",
    "DE#64",
    "DE#65",
    "DE#66",
    "DE#67",
    "DE#68",
    "DE#69",
    "DE#70",
    "DE#71",
    "DE#72",
    "DE#73",
    "DE#74",
    "DE#75",
    "DE#76",
    "DE#77",
    "DE#78",
    "DE#79",
    "DE#80",
    "DE#81",
    "DE#82",
    "DE#83",
    "DE#84",
    "DE#85",
    "DE#86",
    "DE#87",
    "DE#88",
    "DE#89",
    "DE#102",
    "DE#103",
    "DE#104",
    "DE#105",
    "DE#106",
    "DE#107",
    "DE#108",
    "DE#109",
    "DE#110",
    "DE#111",
    "DE#112",
    "DE#113",
    "DE#114",
    "DE#115",
    "DE#116",
    "DE#117",
    "DE#118",
    "DE#119",
    "DE#120",
    "DE#121",
    "DE#122",
    "DE#123",
    "DE#124",
    "DE#125",
    "DE#126",
    "DE#127",
    "DE#128",
    "DE#129",
    "DE#130",
    "DE#131",
    "DE#132",
    "DE#133",
    "DE#134",
    "DE#135",
    "DE#136",
    "DE#137",
    "FR#37",
    "FR#38",
    "FR#39",
    "FR#40",
    "FR#61",
    "FR#62",
    "FR#63",
    "FR#64",
    "FR#65",
    "FR#66",
    "FR#67",
    "FR#68",
    "FR#69",
    "FR#70",
    "FR#71",
    "FR#72",
    "FR#73",
    "FR#74",
    "FR#75",
    "FR#76",
    "FR#77",
    "FR#78",
    "FR#79",
    "FR#80",
    "FR#81",
    "FR#82",
    "FR#83",
    "FR#84",
    "FR#85",
    "FR#86",
    "FR#87",
    "FR#88",
    "FR#89",
    "FR#90",
    "FR#91",
    "FR#92",
    "FR#93",
    "FR#94",
    "FR#95",
    "FR#96",
    "FR#109",
    "FR#110",
    "FR#111",
    "FR#112",
    "FR#113",
    "FR#114",
    "FR#115",
    "FR#116",
    "FR#117",
    "FR#118",
    "FR#119",
    "FR#120",
    "FR#121",
    "FR#122",
    "FR#123",
    "FR#124",
    "FR#125",
    "FR#126",
    "FR#127",
    "FR#128",
    "FR#129",
    "FR#130",
    "FR#131",
    "FR#132",
    "FR#133",
    "FR#134",
    "FR#135",
    "FR#136",
    "FR#137",
    "FR#138",
    "FR#139",
    "FR#140",
    "FR#141",
    "FR#142",
    "FR#143",
    "FR#144",
    "FR#146",
    "FR#147",
    "FR#148",
    "FR#149",
    "FR#150",
    "FR#151",
    "FR#152",
    "FR#153",
    "FR#154",
    "FR#155",
    "FR#156",
    "FR#157",
    "FR#158",
    "FR#159",
    "FR#160",
    "FR#161",
    "FR#162",
    "FR#163",
    "FR#164",
    "FR#165",
    "FR#166",
    "FR#167",
    "FR#168",
    "FR#169",
    "FR#170",
    "FR#171",
    "FR#172",
    "FR#173",
    "FR#174",
    "FR#175",
    "FR#176",
    "FR#177",
    "FR#178",
    "FR#179",
    "FR#180",
    "FR#181",
    "FL#1",
    "FL#2",
    "FL#3",
    "FL#4",
    "FL#5",
    "FL#6",
    "FL#7",
    "FL#8",
    "FL#9",
    "FL#10",
    "FL#11",
    "FL#12",
    "HU#13",
    "HU#14",
    "HU#15",
    "HU#16",
    "HU#17",
    "HU#18",
    "HU#19",
    "HU#20",
    "HU#21",
    "HU#22",
    "HU#23",
    "HU#24",
    "HU#25",
    "HU#26",
    "HU#27",
    "HU#28",
    "HU#29",
    "HU#30",
    "HU#31",
    "HU#32",
    "HU#33",
    "HU#34",
    "HU#35",
    "HU#36",
    "RU#1",
    "RU#2",
    "RU#3",
    "RU#4",
    "RU#5",
    "RU#6",
    "RU#7",
    "RU#8",
    "RU#9",
    "RU#10",
    "RU#11",
    "RU#12",
    "RU#13",
    "RU#14",
    "RU#15",
    "RU#16",
]


USER_AGENTS_LIST = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.56 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4564.140 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/82.0.4084.110 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-A515F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.62 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4896.52 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-N970U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.60 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-G781U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4564.47 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; LM-G900N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.39 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Pixel 3a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.69 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Redmi K20 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-G986U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.38 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; LG-G820) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.59 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-J600F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.82 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-N960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-G930U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.93 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Pixel 2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-G970U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-A705F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.81 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-A515F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-G980U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; LG-Q730) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/82.0.4084.89 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; LM-G710) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.117 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:130.0) Gecko/20100101 Firefox/130.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:129.0) Gecko/20100101 Firefox/129.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0) Gecko/20100101 Firefox/128.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) Gecko/20100101 Firefox/126.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:119.0) Gecko/20100101 Firefox/119.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:118.0) Gecko/20100101 Firefox/118.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:117.0) Gecko/20100101 Firefox/117.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:116.0) Gecko/20100101 Firefox/116.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:115.0) Gecko/20100101 Firefox/115.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:114.0) Gecko/20100101 Firefox/114.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:113.0) Gecko/20100101 Firefox/113.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:112.0) Gecko/20100101 Firefox/112.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:111.0) Gecko/20100101 Firefox/111.0",
    "Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-G991U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.58 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-G991U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4896.60 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-G991U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4896.65 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-G991U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4896.65 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-G991U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4896.69 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-G991U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4896.70 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-G991U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4896.71 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-G991U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4896.72 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-G991U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4896.74 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-G991U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4896.75 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-G991U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4896.76 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-G991U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4896.77 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-G991U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4896.78 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-G991U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4896.79 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-G991U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4896.80 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-G991U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4896.81 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-G991U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4896.82 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-G991U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4896.83 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-G991U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/82.0.4896.85 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-G991U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4896.86 Mobile Safari/537.36",
]

CHROME_DRIVER_PATH = "./chromedriver.exe"

TARGET_WEBSITE_URL = "https://www.officemonster.co.uk/"


class ScraperLogger:
    """
    This class creates loggs of all movements for scraper.

    Attributes:
    _filename contains a string name of the file where loggs are stored.
    _filemode contains a string value indicated the above file's accessibility
    _format contains concatenated string of time, seconds, name, level and message for every actions
    _dateformat contains string of date format for tracks loggs of each actions
    """

    def __init__(self):
        self._logger_name = "puresounds"
        self._filename = "web_traffic_logging.log"
        self._filemode = "a"
        self._format = "%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s"
        self._dateformat = "%d-%b-%y %H:%M:%S"
        self.setup_logfile()

    def setup_logfile(self):
        """
        Initialize logging config
        """
        logging.basicConfig(
            filename=self._filename,
            filemode=self._filemode,
            format=self._format,
            datefmt=self._dateformat,
            level=logging.INFO,
        )


class WebTraffic:
    def __init__(self) -> None:
        self.browser_options = ChromeOptions()
        self.browser_options.headless = True
        self.browser_options.add_argument("--log-level=1")
        self.service = Service(executable_path=CHROME_DRIVER_PATH)
        self.driver = None
        self.run_driver()
        self.is_messenger_logged_in = False

    def run_driver(self, user_agent=None) -> None:
        """
        A method which initialize the selenium driver.
        """
        if user_agent:
            self.browser_options.add_argument(f"user-agent={user_agent}")
        self.driver = Chrome(service=self.service, options=self.browser_options)
        self.driver.maximize_window()

    def wait_till_locator(
        self, by_what, by_value, load_time=180, soup_driver=None
    ) -> None:
        """
        A method which helps to check a specific web element of page
        is existed or not within a load duration time.
        """
        try:
            element = EC.presence_of_element_located((by_what, by_value))
            if soup_driver:
                WebDriverWait(soup_driver, load_time).until(element)
            else:
                WebDriverWait(self.driver, load_time).until(element)
            logging.info("Locator loading is found properly")
            return True
        except TimeoutException:
            logging.debug("Locator loading is not found properly")
            return False

    def accept_cokkies(self) -> None:
        """
        A method which accepts puresounds cookies.
        """
        if self.wait_till_locator(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]'):
            logging.info("Finding accept cokkies button")
            accept_button = self.driver.find_element(
                By.XPATH, '//*[@id="onetrust-accept-btn-handler"]'
            )
            logging.info("click on accept cokkies")
            accept_button.click()
        else:
            logging.warning("accept_all_cookies not loaded")

    def get_custom_user_agent(self) -> str:
        """
        Returns a random user agent string.
        """
        return random.choice(USER_AGENTS_LIST)

    def go_next_tab(self) -> None:
        """
        A method whichs move current tab to immediate next tab
        """
        total_tabs = len(self.driver.window_handles)
        if total_tabs > 1:
            self.driver.switch_to.window(self.driver.window_handles[total_tabs - 1])
        else:
            print("There are less than 1 tabs!")

    def single_frame_element_operation(self, element_no) -> None:
        if self.wait_till_locator(
            By.XPATH,
            f"/html/body/div[3]/section[2]/div/div/div[2]/div[1]/div[2]/div/div[3]/div/form/div/div[5]/div/div[{element_no}]",
        ):
            print(f"{element_no} frame element is found!")
            frame_element = self.driver.find_element(
                By.XPATH,
                f"/html/body/div[3]/section[2]/div/div/div[2]/div[1]/div[2]/div/div[3]/div/form/div/div[5]/div/div[{element_no}]",
            )
            frame_element.click()
        else:
            print(f"{element_no} frame element is not found!")

    def get_all_frame_color_elements(self) -> list:
        if self.wait_till_locator(
            By.XPATH,
            "/html/body/div[3]/section[2]/div/div/div[2]/div[1]/div[2]/div/div[3]/div/form/div/div[5]/div",
        ):
            print("All frame colored list of elements is found!")
            frame_elements = self.driver.find_elements(
                By.XPATH,
                "/html/body/div[3]/section[2]/div/div/div[2]/div[1]/div[2]/div/div[3]/div/form/div/div[5]/div/div",
            )
            frame_elements[0].click()
            print("Total frame colored list: ", len(frame_elements))
            return frame_elements
        else:
            print("All frame colored list of elements is not found!")
            return []

    def single_color_element_operation(self, element_no) -> None:
        if self.wait_till_locator(
            By.XPATH,
            f"/html/body/div[3]/section[2]/div/div/div[2]/div[1]/div[2]/div/div[3]/div/form/div/div[4]/div/div[{element_no}]",
        ):
            print(f"{element_no} color element is found!")
            color_element = self.driver.find_element(
                By.XPATH,
                f"/html/body/div[3]/section[2]/div/div/div[2]/div[1]/div[2]/div/div[3]/div/form/div/div[4]/div/div[{element_no}]",
            )
            color_element.click()
        else:
            print(f"{element_no} color element is not found!")

    def get_all_color_elements(self) -> list:
        if self.wait_till_locator(
            By.XPATH,
            "/html/body/div[3]/section[2]/div/div/div[2]/div[1]/div[2]/div/div[3]/div/form/div/div[4]/div",
        ):
            print("All colored list of elements is found!")
            color_elements = self.driver.find_elements(
                By.XPATH,
                "/html/body/div[3]/section[2]/div/div/div[2]/div[1]/div[2]/div/div[3]/div/form/div/div[4]/div/div",
            )
            print("Total colored list: ", len(color_elements))
            return color_elements
        else:
            print("All colored list of elements is not found!")
            return []

    def mouseover_product_image(self):
        if self.wait_till_locator(
            By.XPATH, "/html/body/div[3]/section[2]/div/div/div[2]/div[1]/div[1]/div[1]"
        ):
            print("Product image for mouseover is found!")
            image_div_element = self.driver.find_element(
                By.XPATH,
                "/html/body/div[3]/section[2]/div/div/div[2]/div[1]/div[1]/div[1]",
            )
            ActionChains(self.driver).move_to_element(image_div_element).perform()
            time.sleep(2)
        else:
            print("Product image for mouseover is not found!")

    def get_product_image(self):
        if self.wait_till_locator(By.CLASS_NAME, "magnify"):
            print("Product image is found!")
            product_image_element = self.driver.find_element(
                By.CLASS_NAME, "magnify"
            ).find_element(By.TAG_NAME, "img")
            image_src = product_image_element.get_attribute("src")
            print("Product image src: ", image_src)
            self.driver.switch_to.new_window(WindowTypes.TAB)
            self.driver.get(image_src)
            time.sleep(3)

            image_element = self.driver.find_element(By.XPATH, "/html/body/img")
            image_binary = image_element.screenshot_as_png
            img = Image.open(io.BytesIO(image_binary))
            image_path = "E:/project/BEM Group/officemonster-scraper/product-images"
            img.save(f"{image_path}/image.png")
            print("New image is saved!")
        else:
            print("Product image is not found!")

    def image_collection(self):
        total_color_elements = len(self.get_all_color_elements())
        total_frame_elements = len(self.get_all_frame_color_elements())

        for element_idx in range(1, total_color_elements + 1):
            self.driver.implicitly_wait(10)
            self.single_color_element_operation(element_no=element_idx)
            time.sleep(3)
            for frame_idx in range(1, total_frame_elements + 1):
                self.single_frame_element_operation(element_no=frame_idx)
                time.sleep(3)
                self.mouseover_product_image()
                time.sleep(3)
                self.get_product_image()
                time.sleep(1)
                self.driver.close()
                self.driver.switch_to.window(self.driver.window_handles[-1])
                time.sleep(1)

    def run(self) -> None:
        starttime = datetime.now()

        self.driver.get(
            "https://www.officemonster.co.uk/corner-desks--1/maestro-25-cantilever-ergonomic-corner-desk"
        )
        time.sleep(5)
        self.image_collection()

        endtime = datetime.now()
        logging.info(f"Start time: {starttime}")
        logging.info(f"End time: {endtime}")
        logging.info(f"Total Duration: {endtime - starttime}")
        custom_user_agent = self.get_custom_user_agent()
        self.run_driver(user_agent=custom_user_agent)
        user_agent = self.driver.execute_script("return navigator.userAgent;")
        logging.info(user_agent)
        time.sleep(10)


def run_scraper():
    web_traffic = WebTraffic()
    web_traffic.run()


def is_internet_connected():
    try:
        s = socket.create_connection(("1.1.1.1", 80))
        print("Internet connection is available!")
        return True
    except OSError:
        print("There is no internet connection!")
    return False


if __name__ == "__main__":
    scraper_logger = ScraperLogger()
    run_scraper()
