toc.dat                                                                                             0000600 0004000 0002000 00000036557 14444120755 0014465 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        PGDMP       7    +                {            arms_db    15.2    15.2 -    D           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false         E           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false         F           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false         G           1262    17362    arms_db    DATABASE     �   CREATE DATABASE arms_db WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'English_Philippines.1252';
    DROP DATABASE arms_db;
                postgres    false         �            1255    17596    create_invoice()    FUNCTION       CREATE FUNCTION public.create_invoice() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
BEGIN
	IF (SELECT COUNT(*) FROM INVOICE WHERE book_id = old.book_id)<1 AND new.book_status='Finished' THEN
		INSERT INTO INVOICE (book_id) VALUES (old.book_id);
	END IF;
	RETURN NEW;
	
END;
$$;
 '   DROP FUNCTION public.create_invoice();
       public          postgres    false         �            1259    17543    book    TABLE       CREATE TABLE public.book (
    book_id integer NOT NULL,
    book_type character varying(50) NOT NULL,
    book_status character varying(20) DEFAULT 'Pending'::character varying NOT NULL,
    book_total numeric(10,2) DEFAULT 0 NOT NULL,
    book_vcl_plate character varying(20) NOT NULL,
    book_vcl_brand character varying(50) NOT NULL,
    book_vcl_model character varying(50) NOT NULL,
    date_created timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    date_updated timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    emp_id integer NOT NULL,
    cus_id integer NOT NULL,
    srv_id integer NOT NULL,
    book_start timestamp without time zone NOT NULL,
    book_end timestamp without time zone NOT NULL,
    book_details character varying(100)
);
    DROP TABLE public.book;
       public         heap    postgres    false         �            1259    17542    book_book_id_seq    SEQUENCE     �   CREATE SEQUENCE public.book_book_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.book_book_id_seq;
       public          postgres    false    223         H           0    0    book_book_id_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE public.book_book_id_seq OWNED BY public.book.book_id;
          public          postgres    false    222         �            1259    17470    customer    TABLE     [  CREATE TABLE public.customer (
    cus_id integer NOT NULL,
    cus_fname character varying(25) NOT NULL,
    cus_mname character varying(25),
    cus_lname character varying(25) NOT NULL,
    cus_mobile character varying(11) NOT NULL,
    cus_email character varying(50) NOT NULL,
    cus_sex character(6) NOT NULL,
    cus_address character varying(150) NOT NULL,
    cus_status character varying(10) DEFAULT 'Active'::character varying NOT NULL,
    date_created timestamp without time zone DEFAULT CURRENT_DATE NOT NULL,
    date_updated timestamp without time zone DEFAULT CURRENT_DATE NOT NULL
);
    DROP TABLE public.customer;
       public         heap    postgres    false         �            1259    17469    customer_cus_id_seq    SEQUENCE     �   ALTER TABLE public.customer ALTER COLUMN cus_id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.customer_cus_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);
            public          postgres    false    217         �            1259    17494    employee    TABLE     �  CREATE TABLE public.employee (
    emp_id integer NOT NULL,
    emp_fname character varying(25) NOT NULL,
    emp_mname character varying(25),
    emp_lname character varying(25) NOT NULL,
    emp_sex character(6) NOT NULL,
    emp_dob date NOT NULL,
    emp_email character varying(50) NOT NULL,
    emp_password character varying(50),
    emp_address character varying(150) NOT NULL,
    emp_mobile character varying(11) NOT NULL,
    emp_status character varying(10) DEFAULT 'Active'::character varying NOT NULL,
    emp_type character varying(20) NOT NULL,
    date_created timestamp without time zone DEFAULT CURRENT_DATE,
    date_updated timestamp without time zone DEFAULT CURRENT_DATE,
    emp_service character varying(50) NOT NULL
);
    DROP TABLE public.employee;
       public         heap    postgres    false         �            1259    17493    employee_emp_id_seq    SEQUENCE     �   ALTER TABLE public.employee ALTER COLUMN emp_id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.employee_emp_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);
            public          postgres    false    221         �            1259    17567    invoice    TABLE     �   CREATE TABLE public.invoice (
    inv_id integer NOT NULL,
    date_created timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    date_updated timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    book_id integer
);
    DROP TABLE public.invoice;
       public         heap    postgres    false         �            1259    17566    invoice_inv_id_seq    SEQUENCE     �   ALTER TABLE public.invoice ALTER COLUMN inv_id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.invoice_inv_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);
            public          postgres    false    225         �            1259    17478    service    TABLE       CREATE TABLE public.service (
    srv_id integer NOT NULL,
    srv_name character varying(50) NOT NULL,
    srv_category character varying(50) NOT NULL,
    srv_time character varying(10) NOT NULL,
    srv_fee numeric(10,2) NOT NULL,
    srv_type character varying(20) NOT NULL
);
    DROP TABLE public.service;
       public         heap    postgres    false         �            1259    17477    service_srv_id_seq    SEQUENCE     �   ALTER TABLE public.service ALTER COLUMN srv_id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.service_srv_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);
            public          postgres    false    219         �            1259    17442    shop    TABLE     �  CREATE TABLE public.shop (
    shop_id integer NOT NULL,
    shop_name character varying(100) DEFAULT 'SHOP NAME'::character varying NOT NULL,
    shop_address character varying(150) DEFAULT 'SHOP ADDRESS'::character varying NOT NULL,
    shop_email character varying(50) DEFAULT 'admin'::character varying NOT NULL,
    shop_password character varying(50) DEFAULT 'admin'::character varying NOT NULL,
    shop_owner character varying(100) DEFAULT 'SHOP OWNER'::character varying NOT NULL,
    shop_mobile character varying(11) DEFAULT 'MOBILE'::character varying NOT NULL,
    shop_telephone character varying(20) DEFAULT 'TELEPHONE'::character varying NOT NULL,
    shop_socials character varying(150) DEFAULT 'SOCIALS'::character varying NOT NULL
);
    DROP TABLE public.shop;
       public         heap    postgres    false         �            1259    17441    shop_shop_id_seq    SEQUENCE     �   CREATE SEQUENCE public.shop_shop_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.shop_shop_id_seq;
       public          postgres    false    215         I           0    0    shop_shop_id_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE public.shop_shop_id_seq OWNED BY public.shop.shop_id;
          public          postgres    false    214         �           2604    17546    book book_id    DEFAULT     l   ALTER TABLE ONLY public.book ALTER COLUMN book_id SET DEFAULT nextval('public.book_book_id_seq'::regclass);
 ;   ALTER TABLE public.book ALTER COLUMN book_id DROP DEFAULT;
       public          postgres    false    222    223    223                    2604    17445    shop shop_id    DEFAULT     l   ALTER TABLE ONLY public.shop ALTER COLUMN shop_id SET DEFAULT nextval('public.shop_shop_id_seq'::regclass);
 ;   ALTER TABLE public.shop ALTER COLUMN shop_id DROP DEFAULT;
       public          postgres    false    215    214    215         ?          0    17543    book 
   TABLE DATA           �   COPY public.book (book_id, book_type, book_status, book_total, book_vcl_plate, book_vcl_brand, book_vcl_model, date_created, date_updated, emp_id, cus_id, srv_id, book_start, book_end, book_details) FROM stdin;
    public          postgres    false    223       3391.dat 9          0    17470    customer 
   TABLE DATA           �   COPY public.customer (cus_id, cus_fname, cus_mname, cus_lname, cus_mobile, cus_email, cus_sex, cus_address, cus_status, date_created, date_updated) FROM stdin;
    public          postgres    false    217       3385.dat =          0    17494    employee 
   TABLE DATA           �   COPY public.employee (emp_id, emp_fname, emp_mname, emp_lname, emp_sex, emp_dob, emp_email, emp_password, emp_address, emp_mobile, emp_status, emp_type, date_created, date_updated, emp_service) FROM stdin;
    public          postgres    false    221       3389.dat A          0    17567    invoice 
   TABLE DATA           N   COPY public.invoice (inv_id, date_created, date_updated, book_id) FROM stdin;
    public          postgres    false    225       3393.dat ;          0    17478    service 
   TABLE DATA           ^   COPY public.service (srv_id, srv_name, srv_category, srv_time, srv_fee, srv_type) FROM stdin;
    public          postgres    false    219       3387.dat 7          0    17442    shop 
   TABLE DATA           �   COPY public.shop (shop_id, shop_name, shop_address, shop_email, shop_password, shop_owner, shop_mobile, shop_telephone, shop_socials) FROM stdin;
    public          postgres    false    215       3383.dat J           0    0    book_book_id_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public.book_book_id_seq', 11, true);
          public          postgres    false    222         K           0    0    customer_cus_id_seq    SEQUENCE SET     A   SELECT pg_catalog.setval('public.customer_cus_id_seq', 3, true);
          public          postgres    false    216         L           0    0    employee_emp_id_seq    SEQUENCE SET     B   SELECT pg_catalog.setval('public.employee_emp_id_seq', 12, true);
          public          postgres    false    220         M           0    0    invoice_inv_id_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.invoice_inv_id_seq', 2, true);
          public          postgres    false    224         N           0    0    service_srv_id_seq    SEQUENCE SET     A   SELECT pg_catalog.setval('public.service_srv_id_seq', 15, true);
          public          postgres    false    218         O           0    0    shop_shop_id_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('public.shop_shop_id_seq', 1, true);
          public          postgres    false    214         �           2606    17550    book book_pkey 
   CONSTRAINT     Q   ALTER TABLE ONLY public.book
    ADD CONSTRAINT book_pkey PRIMARY KEY (book_id);
 8   ALTER TABLE ONLY public.book DROP CONSTRAINT book_pkey;
       public            postgres    false    223         �           2606    17476    customer customer_pkey 
   CONSTRAINT     X   ALTER TABLE ONLY public.customer
    ADD CONSTRAINT customer_pkey PRIMARY KEY (cus_id);
 @   ALTER TABLE ONLY public.customer DROP CONSTRAINT customer_pkey;
       public            postgres    false    217         �           2606    17500    employee employee_pkey 
   CONSTRAINT     X   ALTER TABLE ONLY public.employee
    ADD CONSTRAINT employee_pkey PRIMARY KEY (emp_id);
 @   ALTER TABLE ONLY public.employee DROP CONSTRAINT employee_pkey;
       public            postgres    false    221         �           2606    17573    invoice invoice_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.invoice
    ADD CONSTRAINT invoice_pkey PRIMARY KEY (inv_id);
 >   ALTER TABLE ONLY public.invoice DROP CONSTRAINT invoice_pkey;
       public            postgres    false    225         �           2606    17482    service service_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.service
    ADD CONSTRAINT service_pkey PRIMARY KEY (srv_id);
 >   ALTER TABLE ONLY public.service DROP CONSTRAINT service_pkey;
       public            postgres    false    219         �           2606    17457    shop shop_pkey 
   CONSTRAINT     Q   ALTER TABLE ONLY public.shop
    ADD CONSTRAINT shop_pkey PRIMARY KEY (shop_id);
 8   ALTER TABLE ONLY public.shop DROP CONSTRAINT shop_pkey;
       public            postgres    false    215         �           2606    17601    invoice unique_book_id 
   CONSTRAINT     T   ALTER TABLE ONLY public.invoice
    ADD CONSTRAINT unique_book_id UNIQUE (book_id);
 @   ALTER TABLE ONLY public.invoice DROP CONSTRAINT unique_book_id;
       public            postgres    false    225         �           2620    17599    book trg_create_invoice    TRIGGER     u   CREATE TRIGGER trg_create_invoice AFTER UPDATE ON public.book FOR EACH ROW EXECUTE FUNCTION public.create_invoice();
 0   DROP TRIGGER trg_create_invoice ON public.book;
       public          postgres    false    226    223         �           2606    17556    book book_cus_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.book
    ADD CONSTRAINT book_cus_id_fkey FOREIGN KEY (cus_id) REFERENCES public.customer(cus_id) ON UPDATE CASCADE ON DELETE CASCADE;
 ?   ALTER TABLE ONLY public.book DROP CONSTRAINT book_cus_id_fkey;
       public          postgres    false    223    217    3224         �           2606    17551    book book_emp_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.book
    ADD CONSTRAINT book_emp_id_fkey FOREIGN KEY (emp_id) REFERENCES public.employee(emp_id) ON UPDATE CASCADE ON DELETE CASCADE;
 ?   ALTER TABLE ONLY public.book DROP CONSTRAINT book_emp_id_fkey;
       public          postgres    false    221    3228    223         �           2606    17561    book book_srv_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.book
    ADD CONSTRAINT book_srv_id_fkey FOREIGN KEY (srv_id) REFERENCES public.service(srv_id) ON UPDATE CASCADE ON DELETE CASCADE;
 ?   ALTER TABLE ONLY public.book DROP CONSTRAINT book_srv_id_fkey;
       public          postgres    false    223    3226    219         �           2606    17574    invoice invoice_book_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.invoice
    ADD CONSTRAINT invoice_book_id_fkey FOREIGN KEY (book_id) REFERENCES public.book(book_id) ON UPDATE CASCADE ON DELETE CASCADE;
 F   ALTER TABLE ONLY public.invoice DROP CONSTRAINT invoice_book_id_fkey;
       public          postgres    false    225    3230    223                                                                                                                                                         3391.dat                                                                                            0000600 0004000 0002000 00000002036 14444120755 0014260 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        6	Paid	Pending	500.00	ABC123	Honda	Civic	2023-06-17 12:56:40.092731	2023-06-17 12:56:40.092731	4	2	1	2023-06-17 00:00:00	2023-06-27 00:00:00	None
5	Paid	Finished	1000.00	ABC123	Toyota	Vios	2023-06-17 12:55:18.043541	2023-06-17 12:55:18.043541	3	2	1	2023-06-17 00:00:00	2023-06-27 00:00:00	New Detail
7	Paid	Pending	2600.00	ABC123	Honda	Civic	2023-06-19 21:11:55.181341	2023-06-19 21:11:55.181341	10	3	11	2023-06-19 00:00:00	2023-06-21 00:00:00	None
9	Paid	Pending	2500.00	BCD	Toyota	Vios	2023-06-19 21:25:04.419842	2023-06-19 21:25:04.419842	11	1	1	2023-06-29 00:00:00	2023-07-09 00:00:00	asdasdasd
8	Free	Finished	2600.00	CBA321	Suzuki	Bazinga	2023-06-19 21:22:38.487328	2023-06-19 21:22:38.487328	11	1	1	2023-06-19 00:00:00	2023-06-29 00:00:00	None
10	Paid	Pending	5000.00	ABC123	Honda	Civic	2023-06-20 01:41:57.167858	2023-06-20 01:41:57.167858	5	1	3	2023-06-20 00:00:00	2023-06-30 00:00:00	None
11	Paid	Pending	5000.00	ASB321	Toyota	Corola	2023-06-20 01:47:20.041764	2023-06-20 01:47:20.041764	5	2	3	2023-06-30 00:00:00	2023-07-10 00:00:00	None
\.


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  3385.dat                                                                                            0000600 0004000 0002000 00000000562 14444120755 0014265 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        2	Zion	Vincent	Robert	09782364432	zion@gmail.com	Male  	Mandaue City	Active	2023-06-17 00:00:00	2023-06-17 00:00:00
3	Liam	Choy	Booc	09123456789	liamchoybooc@gmail.com	Male  	asdasdasdhagsds	Active	2023-06-19 00:00:00	2023-06-19 00:00:00
1	Nadine		Lustre	09234234232	nadinelustre@gmail.com	Female	Tipolo, Mandaue City	Active	2023-06-16 00:00:00	2023-06-16 00:00:00
\.


                                                                                                                                              3389.dat                                                                                            0000600 0004000 0002000 00000003731 14444120755 0014272 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        2	Oneal Ryan 	Dela Rosa	Torres	Male  	2001-09-23	torres@gmail.com	password	testing	09123456789	Active	Attendant	2023-06-16 00:00:00	2023-06-16 00:00:00	Attendant
3	Shane Audrey		Tagpuno	Male  	2000-01-01	tagpuno@gmail.com		in da hood	09123456789	Active	Mechanic	2023-06-16 00:00:00	2023-06-16 00:00:00	Vehicle Repair
4	Louie Jay	Landiza	Natividad	Male  	2000-01-01	louie@gmail.com		Cebu	09287364827	Active	Mechanic	2023-06-17 00:00:00	2023-06-17 00:00:00	Vehicle Maintenance
6	Sophia Marie	Reyes	 Santos	Female	1995-01-10	sophiamrsantos@gmail.com		789 Coral Street, Cebu City, Cebu, Philippines	09101234567	Active	Mechanic	2023-06-19 00:00:00	2023-06-19 00:00:00	Diagnostic Services
7	Ethan James 	Fernandez	Dela Cruz	Male  	1995-02-25	ethanjdela@gmail.com		456 Coral Avenue, Cebu City, Cebu, Philippines	09123456788	Active	Detailer	2023-06-19 00:00:00	2023-06-19 00:00:00	Tire Services
8	Liam Alexander	Cruz	Tan	Male  	1991-06-12	liamatan@gmail.com		789 Salinas Drive, Cebu City, Cebu, Philippines	09123456784	Active	Detailer	2023-06-19 00:00:00	2023-06-19 00:00:00	Auto Detailing
9	Benjamin James	Ong	Lim	Male  	1997-08-08	benjamonong@gmail.com		456 Coral Avenue, Cebu City, Cebu, Philippines	09123456782	Active	AC Technician	2023-06-19 00:00:00	2023-06-19 00:00:00	Air Conditioning Services
10	Daniel Matthew		Cruz	Male  	2000-01-01	danmcruz@gmail.com		123 Mango Street, Cebu City, Cebu, Philippines	09123456780	Active	Mechanic	2023-06-19 00:00:00	2023-06-19 00:00:00	Vehicle Repair
11	Olivia Rose	Alvarez	Yap	Male  	1993-01-07	oliviarosealvarez@gmail.com		123 Mango Street, Cebu City, Cebu, Philippines	09123456783	Active	Mechanic	2023-06-19 00:00:00	2023-06-19 00:00:00	Vehicle Repair
12	Gibe		Tirol	Male  	2000-01-01	gibetirol@gmail.com	password	test	09123456789	Active	Attendant	2023-06-19 00:00:00	2023-06-19 00:00:00	Attendant
5	John Kyle		Reponte	Male  	2001-06-27	johnkylereponte@gmail.com		asdasdasda	09123456789	Active	Painter	2023-06-19 00:00:00	2023-06-19 00:00:00	Body and Paint Services
\.


                                       3393.dat                                                                                            0000600 0004000 0002000 00000000171 14444120755 0014260 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        1	2023-06-17 19:21:06.656279	2023-06-17 19:21:06.656279	5
2	2023-06-19 21:34:37.800414	2023-06-19 21:34:37.800414	8
\.


                                                                                                                                                                                                                                                                                                                                                                                                       3387.dat                                                                                            0000600 0004000 0002000 00000001427 14444120755 0014270 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        1	Bumper Replacement	Vehicle Repair	10	500.00	4 Wheeler
2	Oil Change	Vehicle Maintenance	1	170.00	2 Wheeler
4	Engine Tune-Up	Vehicle Repair	2	1000.00	2 Wheeler
5	Brake Adjustment	Vehicle Maintenance	1	500.00	3 Wheeler
6	Check Engine Light	Diagnostic Services	1	200.00	4 Wheeler
3	Full Body Paint	Body and Paint Services	10	5000.00	4 Wheeler
8	Chain and Sprocket Replacement	Vehicle Repair	1	800.00	2 Wheeler
9	Filter Replacement	Vehicle Maintenance	1	300.00	2 Wheeler
10	Polishing	Auto Detailing	2	400.00	2 Wheeler
12	Battery Replacement	Vehicle Repair	1	400.00	3 Wheeler
7	Air Condtioning Regas	Air Conditioning Services	1	1200.00	4 Wheeler
11	Transmission Fluid Replacement	Vehicle Repair	2	2500.00	4 Wheeler
14	AC Compressor Replacement	Air Conditioning Services	1	1500.00	4 Wheeler
\.


                                                                                                                                                                                                                                         3383.dat                                                                                            0000600 0004000 0002000 00000000243 14444120755 0014257 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        1	Inday Auto Repair Shop	Mercedes Arcade, Highway Mandaue City	admin	admin	Fedilito Sombillon Aradillos	09123456789	123-4567	Facebook: Inday Auto Repair Shop
\.


                                                                                                                                                                                                                                                                                                                                                             restore.sql                                                                                         0000600 0004000 0002000 00000033361 14444120755 0015400 0                                                                                                    ustar 00postgres                        postgres                        0000000 0000000                                                                                                                                                                        --
-- NOTE:
--
-- File paths need to be edited. Search for $$PATH$$ and
-- replace it with the path to the directory containing
-- the extracted data files.
--
--
-- PostgreSQL database dump
--

-- Dumped from database version 15.2
-- Dumped by pg_dump version 15.2

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

DROP DATABASE arms_db;
--
-- Name: arms_db; Type: DATABASE; Schema: -; Owner: postgres
--

CREATE DATABASE arms_db WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'English_Philippines.1252';


ALTER DATABASE arms_db OWNER TO postgres;

\connect arms_db

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: create_invoice(); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION public.create_invoice() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
BEGIN
	IF (SELECT COUNT(*) FROM INVOICE WHERE book_id = old.book_id)<1 AND new.book_status='Finished' THEN
		INSERT INTO INVOICE (book_id) VALUES (old.book_id);
	END IF;
	RETURN NEW;
	
END;
$$;


ALTER FUNCTION public.create_invoice() OWNER TO postgres;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: book; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.book (
    book_id integer NOT NULL,
    book_type character varying(50) NOT NULL,
    book_status character varying(20) DEFAULT 'Pending'::character varying NOT NULL,
    book_total numeric(10,2) DEFAULT 0 NOT NULL,
    book_vcl_plate character varying(20) NOT NULL,
    book_vcl_brand character varying(50) NOT NULL,
    book_vcl_model character varying(50) NOT NULL,
    date_created timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    date_updated timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    emp_id integer NOT NULL,
    cus_id integer NOT NULL,
    srv_id integer NOT NULL,
    book_start timestamp without time zone NOT NULL,
    book_end timestamp without time zone NOT NULL,
    book_details character varying(100)
);


ALTER TABLE public.book OWNER TO postgres;

--
-- Name: book_book_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.book_book_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.book_book_id_seq OWNER TO postgres;

--
-- Name: book_book_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.book_book_id_seq OWNED BY public.book.book_id;


--
-- Name: customer; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.customer (
    cus_id integer NOT NULL,
    cus_fname character varying(25) NOT NULL,
    cus_mname character varying(25),
    cus_lname character varying(25) NOT NULL,
    cus_mobile character varying(11) NOT NULL,
    cus_email character varying(50) NOT NULL,
    cus_sex character(6) NOT NULL,
    cus_address character varying(150) NOT NULL,
    cus_status character varying(10) DEFAULT 'Active'::character varying NOT NULL,
    date_created timestamp without time zone DEFAULT CURRENT_DATE NOT NULL,
    date_updated timestamp without time zone DEFAULT CURRENT_DATE NOT NULL
);


ALTER TABLE public.customer OWNER TO postgres;

--
-- Name: customer_cus_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.customer ALTER COLUMN cus_id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.customer_cus_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: employee; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.employee (
    emp_id integer NOT NULL,
    emp_fname character varying(25) NOT NULL,
    emp_mname character varying(25),
    emp_lname character varying(25) NOT NULL,
    emp_sex character(6) NOT NULL,
    emp_dob date NOT NULL,
    emp_email character varying(50) NOT NULL,
    emp_password character varying(50),
    emp_address character varying(150) NOT NULL,
    emp_mobile character varying(11) NOT NULL,
    emp_status character varying(10) DEFAULT 'Active'::character varying NOT NULL,
    emp_type character varying(20) NOT NULL,
    date_created timestamp without time zone DEFAULT CURRENT_DATE,
    date_updated timestamp without time zone DEFAULT CURRENT_DATE,
    emp_service character varying(50) NOT NULL
);


ALTER TABLE public.employee OWNER TO postgres;

--
-- Name: employee_emp_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.employee ALTER COLUMN emp_id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.employee_emp_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: invoice; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.invoice (
    inv_id integer NOT NULL,
    date_created timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    date_updated timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    book_id integer
);


ALTER TABLE public.invoice OWNER TO postgres;

--
-- Name: invoice_inv_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.invoice ALTER COLUMN inv_id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.invoice_inv_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: service; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.service (
    srv_id integer NOT NULL,
    srv_name character varying(50) NOT NULL,
    srv_category character varying(50) NOT NULL,
    srv_time character varying(10) NOT NULL,
    srv_fee numeric(10,2) NOT NULL,
    srv_type character varying(20) NOT NULL
);


ALTER TABLE public.service OWNER TO postgres;

--
-- Name: service_srv_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.service ALTER COLUMN srv_id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.service_srv_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: shop; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.shop (
    shop_id integer NOT NULL,
    shop_name character varying(100) DEFAULT 'SHOP NAME'::character varying NOT NULL,
    shop_address character varying(150) DEFAULT 'SHOP ADDRESS'::character varying NOT NULL,
    shop_email character varying(50) DEFAULT 'admin'::character varying NOT NULL,
    shop_password character varying(50) DEFAULT 'admin'::character varying NOT NULL,
    shop_owner character varying(100) DEFAULT 'SHOP OWNER'::character varying NOT NULL,
    shop_mobile character varying(11) DEFAULT 'MOBILE'::character varying NOT NULL,
    shop_telephone character varying(20) DEFAULT 'TELEPHONE'::character varying NOT NULL,
    shop_socials character varying(150) DEFAULT 'SOCIALS'::character varying NOT NULL
);


ALTER TABLE public.shop OWNER TO postgres;

--
-- Name: shop_shop_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.shop_shop_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.shop_shop_id_seq OWNER TO postgres;

--
-- Name: shop_shop_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.shop_shop_id_seq OWNED BY public.shop.shop_id;


--
-- Name: book book_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.book ALTER COLUMN book_id SET DEFAULT nextval('public.book_book_id_seq'::regclass);


--
-- Name: shop shop_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.shop ALTER COLUMN shop_id SET DEFAULT nextval('public.shop_shop_id_seq'::regclass);


--
-- Data for Name: book; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.book (book_id, book_type, book_status, book_total, book_vcl_plate, book_vcl_brand, book_vcl_model, date_created, date_updated, emp_id, cus_id, srv_id, book_start, book_end, book_details) FROM stdin;
\.
COPY public.book (book_id, book_type, book_status, book_total, book_vcl_plate, book_vcl_brand, book_vcl_model, date_created, date_updated, emp_id, cus_id, srv_id, book_start, book_end, book_details) FROM '$$PATH$$/3391.dat';

--
-- Data for Name: customer; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.customer (cus_id, cus_fname, cus_mname, cus_lname, cus_mobile, cus_email, cus_sex, cus_address, cus_status, date_created, date_updated) FROM stdin;
\.
COPY public.customer (cus_id, cus_fname, cus_mname, cus_lname, cus_mobile, cus_email, cus_sex, cus_address, cus_status, date_created, date_updated) FROM '$$PATH$$/3385.dat';

--
-- Data for Name: employee; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.employee (emp_id, emp_fname, emp_mname, emp_lname, emp_sex, emp_dob, emp_email, emp_password, emp_address, emp_mobile, emp_status, emp_type, date_created, date_updated, emp_service) FROM stdin;
\.
COPY public.employee (emp_id, emp_fname, emp_mname, emp_lname, emp_sex, emp_dob, emp_email, emp_password, emp_address, emp_mobile, emp_status, emp_type, date_created, date_updated, emp_service) FROM '$$PATH$$/3389.dat';

--
-- Data for Name: invoice; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.invoice (inv_id, date_created, date_updated, book_id) FROM stdin;
\.
COPY public.invoice (inv_id, date_created, date_updated, book_id) FROM '$$PATH$$/3393.dat';

--
-- Data for Name: service; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.service (srv_id, srv_name, srv_category, srv_time, srv_fee, srv_type) FROM stdin;
\.
COPY public.service (srv_id, srv_name, srv_category, srv_time, srv_fee, srv_type) FROM '$$PATH$$/3387.dat';

--
-- Data for Name: shop; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.shop (shop_id, shop_name, shop_address, shop_email, shop_password, shop_owner, shop_mobile, shop_telephone, shop_socials) FROM stdin;
\.
COPY public.shop (shop_id, shop_name, shop_address, shop_email, shop_password, shop_owner, shop_mobile, shop_telephone, shop_socials) FROM '$$PATH$$/3383.dat';

--
-- Name: book_book_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.book_book_id_seq', 11, true);


--
-- Name: customer_cus_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.customer_cus_id_seq', 3, true);


--
-- Name: employee_emp_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.employee_emp_id_seq', 12, true);


--
-- Name: invoice_inv_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.invoice_inv_id_seq', 2, true);


--
-- Name: service_srv_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.service_srv_id_seq', 15, true);


--
-- Name: shop_shop_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.shop_shop_id_seq', 1, true);


--
-- Name: book book_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.book
    ADD CONSTRAINT book_pkey PRIMARY KEY (book_id);


--
-- Name: customer customer_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.customer
    ADD CONSTRAINT customer_pkey PRIMARY KEY (cus_id);


--
-- Name: employee employee_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.employee
    ADD CONSTRAINT employee_pkey PRIMARY KEY (emp_id);


--
-- Name: invoice invoice_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.invoice
    ADD CONSTRAINT invoice_pkey PRIMARY KEY (inv_id);


--
-- Name: service service_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.service
    ADD CONSTRAINT service_pkey PRIMARY KEY (srv_id);


--
-- Name: shop shop_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.shop
    ADD CONSTRAINT shop_pkey PRIMARY KEY (shop_id);


--
-- Name: invoice unique_book_id; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.invoice
    ADD CONSTRAINT unique_book_id UNIQUE (book_id);


--
-- Name: book trg_create_invoice; Type: TRIGGER; Schema: public; Owner: postgres
--

CREATE TRIGGER trg_create_invoice AFTER UPDATE ON public.book FOR EACH ROW EXECUTE FUNCTION public.create_invoice();


--
-- Name: book book_cus_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.book
    ADD CONSTRAINT book_cus_id_fkey FOREIGN KEY (cus_id) REFERENCES public.customer(cus_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: book book_emp_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.book
    ADD CONSTRAINT book_emp_id_fkey FOREIGN KEY (emp_id) REFERENCES public.employee(emp_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: book book_srv_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.book
    ADD CONSTRAINT book_srv_id_fkey FOREIGN KEY (srv_id) REFERENCES public.service(srv_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: invoice invoice_book_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.invoice
    ADD CONSTRAINT invoice_book_id_fkey FOREIGN KEY (book_id) REFERENCES public.book(book_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- PostgreSQL database dump complete
--

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               