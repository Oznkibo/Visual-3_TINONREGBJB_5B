import pymysql


def get_connection():
    """Mengembalikan koneksi ke database."""
    try:
        return pymysql.connect(
            host="localhost",
            user="root",
            password="",  # Ganti dengan password MySQL Anda
            database="db_sekolah",  # Ganti dengan nama database Anda
            charset="utf8mb4"
        )
    except pymysql.MySQLError as e:
        raise Exception(f"Gagal terhubung ke database: {str(e)}")
