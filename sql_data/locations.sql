--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = off;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET escape_string_warning = off;

SET search_path = public, pg_catalog;

--
-- Name: location_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('location_id_seq', 73, true);


--
-- Data for Name: location; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY location (id, location, facilityname, address, suite, city, state, zipcode, phone) FROM stdin;
1	Atlanta Training Center 	Jack Morton at ATG	5600 Roswell Rd NE	Suite 009	Atlanta	GA	30342	800-462-0102
2	Austin IBM Training Center	IBM in Austin	11501 Burnet Road		Austin	TX	78758	800-462-0102
3	Austin Training Location	Jack Morton at St. Edwards	9420 Research Blvd	Echelon III - Suite 200	Austin	TX	78759	800-462-0102
4	Blue Ash Training Center	IBM at Arden	4675 Cornell Road	Suite 175	Blue Ash	OH	45241	800-462-0102
5	Boston Training Center	Jack Morton at Compuworks	263 Summer Street	3rd Floor	Boston	MA	2110	800-462-0102
6	Broomfield Avnet Training Center	Avnet in Broomfield	360 Interlocken Blvd	#200	Broomfield	CO	80021	800-426-0102
7	Chicago Training Center	Jack Morton at CTS	420 N Wabash Ave	Suite 203	Chicago	IL	60611	800-462-0102
8	Chicago Training Center	Jack Morton at New Horizons	200 West Monroe Street	Suite 900 - 9th Floor	Chicago	IL	60606	800-462-0102
9	Chicago Training Center II	Jack Morton at PCCTI	216 West Jackson Boulevard	Suite 900	Chicago	IL	60606	800-4620102
10	Columbia Training Center	Jack Morton at Training, Etc	7150 Riverwood Drive		Columbia	MD	21046	800-426-0102
11	Columbus Training Center	Jack Morton at Computer Workshop	5131 Post Road	Suite 102	Dublin	OH	43017	614-798-9505
12	Costa Mesa IBM Training Center	IBM at Citent	600 Anton Blvd		Costa Mesa	CA	92626	800-462-0102
13	Costa Mesa MUX Training Center	MUX at Citent	611 Anton Blvd	Suite 950	Costa Mesa	CA	92626	800-462-0102
14	Costa Mesa Training Center	Jack Morton at Citent	611 Anton Blvd	Suite 950	Costa Mesa	CA	92626	800-462-0102
15	Dallas CTREC Training Center	Jack Morton at CTREC	1605 LBJ Freeway	Suite 100	Dallas	TX	75234	800-462-0102
16	Dallas IBM Training Center	IBM in Dallas	1000 Belleview Street		Dallas	TX	75215	800-462-0102
17	Dallas Training Center	Jack Morton at Improving Enterprises	16633 Dallas Parkway	Suite 110	Addison	TX	75001	800-462-0102
18	Durham Training Center	Jack Morton at New Horizons	5400 South Miami Blvd	Suite 140	Durham	NC	27703	800-462-0102
19	East Lansing Training Center	MDC at East Lansing	600 E Crescent Road		East Lansing	MI	48824	800-462-0102
20	Elk Grove MUX Training Center	MUX at Executive Training Solutions	9245 Laguna Springs Drive	Suite 325	Elk Grove	CA	95758	800-462-0102
21	Englewood Training Center	Integro in Englewood	88 Inverness Circle East	Suite N106	Englewood	CO	801112	800-462-0102
22	Herndon Training Center	Jack Morton at Nextec	205 Van Buren	Suite 140	Herndon	VA	20170	800-462-0102
23	Houston Festus Training Center	Festus in Houston	20333 State Highway 249	Suite 200	Houston	TX	77070	800-462-0102
24	Irvine CA Training Center	Jack Morton at ExecuTrain	5 Corporate Park	Suite 280	Irvine	CA	92606	800-462-0102
25	Irvine MUX Training Center	MUX at Circle Software	17310 Red Hill Ave	Suite 135	Irvine	CA	92614	800-462-0102
26	Kennesaw Training Center	MSA at Homewood Suites	905 Cobb Place Blvd NW		Kennesaw	GA	30144	800-462-0102
27	Live Virtual Classroom		1		1	1	1	1
28	Markham Training Center	Jack Morton in Markham	3600 Steeles Ave East		Markham	ON	L3R 9Z7	800-462-0102
29	Minneapolis Training Center	Jack Morton at Evolving Solutions	Elm Creek Business Park	3989 County Road 116	Hamel	MN	55340	800-462-0102
30	Morrisville Training Center	Jack Morton at CST	1 Copley Parkway	Suite 400	Morrisville	NC	24560	800-462-0102
31	New York IBM Training Center	IBM in New York City	33 Maiden Lane		New York	NY	10038	800-462-0102
32	New York NetLan Training Center	NetLan in New York	39 West 37th Street	11th Floor	New York	NY	10018	800-462-0102
33	New York Training Center	Jack Morton at WWBC	575 Madison Avenue (56th Street)	8th Floor	New York	NY	10022	800-462-0102
34	Ottawa Training Center	Jack Morton at ExitCertified	220 Laurier Ave West	Suite 1000	Ottawa	ON	K1P 5Z9	800-462-0102
35	Parsippany Training Center	Jack Morton at New Horizons	1639 State Rt 10		Parsippany	NJ	7054	800-462-0102
36	Phoenix MUX Training Center	MUX at Executive Training Solutions	4926 E McDowell Road	Suite 102	Phoenix	AZ	85008	800-462-0102
37	Phoenix Training Center	Jack Morton at ExitCertified	101 N 1st Ave	Suite 1875	Phoenix	AZ	85003	800-462-0102
38	Pittsburgh Training Center	ContePointe in Pittsburgh	1000 Omega Drive	Suite 1110	Pittsburgh	PA	15205	800-426-0102
39	Raleigh Training Center	Jack Morton at Knowledge Source	3100 Smoketree Court	Suite 200	Raleigh	NC	27604	800-462-0102
40	Sacramento Training Center	Jack Morton at ExitCertified	8950 Cal Center Drive	Suite 110, Bldg 1	Sacramento	CA	95826	800-462-0102
41	San Francisco Training Center	Jack Morton at ExitCertified	450 Sansome Street	Suite 600	San Francisco	CA	94111	800-462-0102
42	Shaumburg IBM Training Center	IBM at Schaumburg	10 N Martingale Road		Schaumburg	IL	60173	800-462-0102
43	Tallahassee Training Center	IBM in Tallahassee	2009 Apalachee Parkway	Suite 105	Tallahassee	FL	32301	800-462-0102
44	Toronto Training Center	Jack Morton at ExitCertfied	40 Eglinton Ave E	Suite 305	Toronto	ON	M4P 1A1	800-462-0102
45	Towson Fillmore Training Center	Fillmore Group in Towson	8501 LaSalle Road	Suite31B	Towson	MD	21286	800-462-0102
46	Waltham Training Center	Charles River Public in Waltham	154 Moody Street		Waltham	MA	2453	800-462-0102
47	Washington DC Training Center	Jack Morton at Gestalt Partners	1325 G Street NW	Suite 1020	Washington	DC	20005	800-462-0102
48	Washington DC Training Center II	Jack Morton at Knowlogy	818 Connecticut Ave, N.W.	4th Floor	Washington	DC	20006	800-462-0102
49	Washington DC Training Center III	Jack Morton at Regus	1776 I Street, NW	Republic Building - 9th Floor	Washington	DC	20006	800-462-0102
50	Wayne Training Center	IBM in Wayne	65 Willowbrook Blvd		Wayne	NJ	7470	800-462-0102
51	Woburn Training Center	Jack Morton at CompuWorks	600 W Cummings Park	Suite 2550A	Woburn	MA	1801	800-462-0102
65	Revelstoke	The Rev	2950 N Halsted	Unit 2	Chicago	IL	60657	7082997663
69	Mexico	Barcelo	Carretera Chetumal-Puerto Juárez	Km 266.3	Riviera Maya	QR	77750	
73	edit location	Dallas Training Center	Carretera Chetumal-Puerto Juárez	Km 266.3	Riviera Maya	27	77750	7082997663
\.


--
-- PostgreSQL database dump complete
--

