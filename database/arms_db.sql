PGDMP          5                {            arms_db    15.2    15.2 ,    B           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            C           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            D           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            E           1262    17362    arms_db    DATABASE     �   CREATE DATABASE arms_db WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'English_Philippines.1252';
    DROP DATABASE arms_db;
                postgres    false            �            1255    17596    create_invoice()    FUNCTION       CREATE FUNCTION public.create_invoice() RETURNS trigger
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
       public          postgres    false            �            1259    17543    book    TABLE       CREATE TABLE public.book (
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
       public         heap    postgres    false            �            1259    17542    book_book_id_seq    SEQUENCE     �   CREATE SEQUENCE public.book_book_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.book_book_id_seq;
       public          postgres    false    223            F           0    0    book_book_id_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE public.book_book_id_seq OWNED BY public.book.book_id;
          public          postgres    false    222            �            1259    17470    customer    TABLE     [  CREATE TABLE public.customer (
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
       public         heap    postgres    false            �            1259    17469    customer_cus_id_seq    SEQUENCE     �   ALTER TABLE public.customer ALTER COLUMN cus_id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.customer_cus_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);
            public          postgres    false    217            �            1259    17494    employee    TABLE     �  CREATE TABLE public.employee (
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
       public         heap    postgres    false            �            1259    17493    employee_emp_id_seq    SEQUENCE     �   ALTER TABLE public.employee ALTER COLUMN emp_id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.employee_emp_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);
            public          postgres    false    221            �            1259    17567    invoice    TABLE     �   CREATE TABLE public.invoice (
    inv_id integer NOT NULL,
    date_created timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    date_updated timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    book_id integer
);
    DROP TABLE public.invoice;
       public         heap    postgres    false            �            1259    17566    invoice_inv_id_seq    SEQUENCE     �   ALTER TABLE public.invoice ALTER COLUMN inv_id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.invoice_inv_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);
            public          postgres    false    225            �            1259    17478    service    TABLE       CREATE TABLE public.service (
    srv_id integer NOT NULL,
    srv_name character varying(50) NOT NULL,
    srv_category character varying(50) NOT NULL,
    srv_time character varying(10) NOT NULL,
    srv_fee numeric(10,2) NOT NULL,
    srv_type character varying(20) NOT NULL
);
    DROP TABLE public.service;
       public         heap    postgres    false            �            1259    17477    service_srv_id_seq    SEQUENCE     �   ALTER TABLE public.service ALTER COLUMN srv_id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.service_srv_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);
            public          postgres    false    219            �            1259    17442    shop    TABLE     �  CREATE TABLE public.shop (
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
       public         heap    postgres    false            �            1259    17441    shop_shop_id_seq    SEQUENCE     �   CREATE SEQUENCE public.shop_shop_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.shop_shop_id_seq;
       public          postgres    false    215            G           0    0    shop_shop_id_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE public.shop_shop_id_seq OWNED BY public.shop.shop_id;
          public          postgres    false    214            �           2604    17546    book book_id    DEFAULT     l   ALTER TABLE ONLY public.book ALTER COLUMN book_id SET DEFAULT nextval('public.book_book_id_seq'::regclass);
 ;   ALTER TABLE public.book ALTER COLUMN book_id DROP DEFAULT;
       public          postgres    false    223    222    223                       2604    17445    shop shop_id    DEFAULT     l   ALTER TABLE ONLY public.shop ALTER COLUMN shop_id SET DEFAULT nextval('public.shop_shop_id_seq'::regclass);
 ;   ALTER TABLE public.shop ALTER COLUMN shop_id DROP DEFAULT;
       public          postgres    false    215    214    215            =          0    17543    book 
   TABLE DATA           �   COPY public.book (book_id, book_type, book_status, book_total, book_vcl_plate, book_vcl_brand, book_vcl_model, date_created, date_updated, emp_id, cus_id, srv_id, book_start, book_end, book_details) FROM stdin;
    public          postgres    false    223   �<       7          0    17470    customer 
   TABLE DATA           �   COPY public.customer (cus_id, cus_fname, cus_mname, cus_lname, cus_mobile, cus_email, cus_sex, cus_address, cus_status, date_created, date_updated) FROM stdin;
    public          postgres    false    217   j=       ;          0    17494    employee 
   TABLE DATA           �   COPY public.employee (emp_id, emp_fname, emp_mname, emp_lname, emp_sex, emp_dob, emp_email, emp_password, emp_address, emp_mobile, emp_status, emp_type, date_created, date_updated, emp_service) FROM stdin;
    public          postgres    false    221   >       ?          0    17567    invoice 
   TABLE DATA           N   COPY public.invoice (inv_id, date_created, date_updated, book_id) FROM stdin;
    public          postgres    false    225   ?       9          0    17478    service 
   TABLE DATA           ^   COPY public.service (srv_id, srv_name, srv_category, srv_time, srv_fee, srv_type) FROM stdin;
    public          postgres    false    219   W?       5          0    17442    shop 
   TABLE DATA           �   COPY public.shop (shop_id, shop_name, shop_address, shop_email, shop_password, shop_owner, shop_mobile, shop_telephone, shop_socials) FROM stdin;
    public          postgres    false    215   �?       H           0    0    book_book_id_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('public.book_book_id_seq', 6, true);
          public          postgres    false    222            I           0    0    customer_cus_id_seq    SEQUENCE SET     A   SELECT pg_catalog.setval('public.customer_cus_id_seq', 2, true);
          public          postgres    false    216            J           0    0    employee_emp_id_seq    SEQUENCE SET     A   SELECT pg_catalog.setval('public.employee_emp_id_seq', 4, true);
          public          postgres    false    220            K           0    0    invoice_inv_id_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.invoice_inv_id_seq', 1, true);
          public          postgres    false    224            L           0    0    service_srv_id_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.service_srv_id_seq', 3, true);
          public          postgres    false    218            M           0    0    shop_shop_id_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('public.shop_shop_id_seq', 1, true);
          public          postgres    false    214            �           2606    17550    book book_pkey 
   CONSTRAINT     Q   ALTER TABLE ONLY public.book
    ADD CONSTRAINT book_pkey PRIMARY KEY (book_id);
 8   ALTER TABLE ONLY public.book DROP CONSTRAINT book_pkey;
       public            postgres    false    223            �           2606    17476    customer customer_pkey 
   CONSTRAINT     X   ALTER TABLE ONLY public.customer
    ADD CONSTRAINT customer_pkey PRIMARY KEY (cus_id);
 @   ALTER TABLE ONLY public.customer DROP CONSTRAINT customer_pkey;
       public            postgres    false    217            �           2606    17500    employee employee_pkey 
   CONSTRAINT     X   ALTER TABLE ONLY public.employee
    ADD CONSTRAINT employee_pkey PRIMARY KEY (emp_id);
 @   ALTER TABLE ONLY public.employee DROP CONSTRAINT employee_pkey;
       public            postgres    false    221            �           2606    17573    invoice invoice_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.invoice
    ADD CONSTRAINT invoice_pkey PRIMARY KEY (inv_id);
 >   ALTER TABLE ONLY public.invoice DROP CONSTRAINT invoice_pkey;
       public            postgres    false    225            �           2606    17482    service service_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.service
    ADD CONSTRAINT service_pkey PRIMARY KEY (srv_id);
 >   ALTER TABLE ONLY public.service DROP CONSTRAINT service_pkey;
       public            postgres    false    219            �           2606    17457    shop shop_pkey 
   CONSTRAINT     Q   ALTER TABLE ONLY public.shop
    ADD CONSTRAINT shop_pkey PRIMARY KEY (shop_id);
 8   ALTER TABLE ONLY public.shop DROP CONSTRAINT shop_pkey;
       public            postgres    false    215            �           2620    17599    book trg_create_invoice    TRIGGER     u   CREATE TRIGGER trg_create_invoice AFTER UPDATE ON public.book FOR EACH ROW EXECUTE FUNCTION public.create_invoice();
 0   DROP TRIGGER trg_create_invoice ON public.book;
       public          postgres    false    226    223            �           2606    17556    book book_cus_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.book
    ADD CONSTRAINT book_cus_id_fkey FOREIGN KEY (cus_id) REFERENCES public.customer(cus_id) ON UPDATE CASCADE ON DELETE CASCADE;
 ?   ALTER TABLE ONLY public.book DROP CONSTRAINT book_cus_id_fkey;
       public          postgres    false    223    3224    217            �           2606    17551    book book_emp_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.book
    ADD CONSTRAINT book_emp_id_fkey FOREIGN KEY (emp_id) REFERENCES public.employee(emp_id) ON UPDATE CASCADE ON DELETE CASCADE;
 ?   ALTER TABLE ONLY public.book DROP CONSTRAINT book_emp_id_fkey;
       public          postgres    false    221    3228    223            �           2606    17561    book book_srv_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.book
    ADD CONSTRAINT book_srv_id_fkey FOREIGN KEY (srv_id) REFERENCES public.service(srv_id) ON UPDATE CASCADE ON DELETE CASCADE;
 ?   ALTER TABLE ONLY public.book DROP CONSTRAINT book_srv_id_fkey;
       public          postgres    false    223    3226    219            �           2606    17574    invoice invoice_book_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.invoice
    ADD CONSTRAINT invoice_book_id_fkey FOREIGN KEY (book_id) REFERENCES public.book(book_id) ON UPDATE CASCADE ON DELETE CASCADE;
 F   ALTER TABLE ONLY public.invoice DROP CONSTRAINT invoice_book_id_fkey;
       public          postgres    false    225    223    3230            =   �   x����
�0Dϛ��4l6I��iE<I��K0�.HrhQ�{EAZA��̃y���1NXD��e�H�&�����t�U��B���3rN�V�& �=��h�ms�¾�֜�?� 
'N�|˃�=����:5�h�5_N�I����*��� �w!qA|      7   �   x�}��
�0E痯�ؒ��V;)��:�8�Kl� M���~�!�E8p�� ��;8�k�8�+Ԣ����R#��_�z�6o};cI�8�3#�5����OT�3UeE-�jS�(`o:v�a��C]&\R6�����#߽�3�7_M俟��B�%�C+      ;   �   x����J�0���)�YҤ�ÓEO��PO^f��d�ҦJ}z�+H]�4��)x����3zO��aD8�a��sPR&B�Bi���C{F�vM8C�����h}�L�Nﲼ(�j��$�b$o��%Ii!3�d\��km��.���=�j2� Gl�ɇM��.��;Y��zn�w!�-ց�%�6�V�Sg��mM=ځ���%��3������K�5h6��=�iZ`��u�*��7`�M�ǎ1��<�)      ?   -   x�3�4202�50�54W0��22�20�33532��'e����� z\�      9   �   x�]��
�0ϛ��/(IT��7A�xYӇ	�����K���u�aկn@��,t�b
�T�Y�X[YKk�F �O�����,�^��P� r�s�fE�>N��;�}�a����(��$?������X�3�      5   �   x�3���KI�Tp,-�WJ-H�,R��/��M-JNMI-Vp,JNLI�Q��L�(��Mj(MUp�,��LL��̃�n�)�9�@c��s�2sr��zS@�bNKC#cS3sKN K��tKLNM��϶R���=... r54Z     