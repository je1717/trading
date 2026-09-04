Enterimport asyncio
from metaapi_cloud_sdk import MetaApi

# البيانات الخاصة بحسابك
API_TOKEN = "eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiIzMzFhYmZhODFhMmJmZjMzMTgzNzhhMjk3ZjRkYzE1OCIsImFjY2Vzc1J1bGVzIjpbeyJpZCI6InRyYWRpbmctYWNjb3VudC1tYW5hZ2VtZW50LWFwaSIsIm1ldGhvZHMiOlsidHJhZGluZy1hY2NvdW50LW1hbmFnZW1lbnQtYXBpOnJlc3Q6cHVibGljOio6KiJdLCJyb2xlcyI6WyJyZWFkZXIiXSwicmVzb3VyY2VzIjpbImFjY2Vzc1J1bGVzIjpbImFjY291bnQ6JFVTRVJfSUQkOmE5MTE0MDQ5LTMwZGUtNDdmZS1hZWU1LTYyZTQwYjQ1MDZkNCJdfSx7ImlkIjoibWV0YWFwaS1yZXN0LWFwaSIsIm1ldGhvZHMiOlsibWV0YWFwaS1hcGk6cmVzdDpwdWJsaWM6KjoqIl0sInJvbGVzIjpbInJlYWRlciIsIndyaXRlciJdLCJyZXNvdXJjZXMiOlsiYWNjb3VudDokVVNFUl9JRCQ6YTkxMTQwNDktMzBkZS00N2ZlLWFlZTUtNjJlNDBiNDUwNmQ0Il19LHsiaWQiOiJtZXRhYXBpLXJwYy1hcGkiLCJtZXRob2RzIjpbIm1ldGFhcGktYXBpOndzOnB1YmxpYzoqOioiXSwicm9sZXMiOlsicmVhZGVyIiwid3JpdGVyIl0sInJlc291cmNlcyI6WyJhY2NvdW50OiRVU0VSX0lEJDphOTExNDA0OS0zMGRlLTQ3ZmUtYWVlNS02MmU0MGI0NTA2ZDQiXX0seyJpZCI6Im1ldGFhcGktcmVhbC10aW1lLXN0cmVhbWluZy1hcGkiLCJtZXRob2RzIjpbIm1ldGFhcGktYXBpOndzOnB1YmxpYzoqOioiXSwicm9sZXMiOlsicmVhZGVyIiwid3JpdGVyIl0sInJlc291cmNlcyI6WyJhY2NvdW50OiRVU0VSX0lEJDphOTExNDA0OS0zMGRlLTQ3ZmUtYWVlNS02MmU0MGI0NTA2ZDQiXX0seyJpZCI6Im1ldGFzdGF0cy1hcGkiLCJtZXRob2RzIjpbIm1ldGFzdGF0cy1hcGk6cmVzdDpwdWJsaWM6KjoqIl0sInJvbGVzIjpbInJlYWRlciJdLCJyZXNvdXJjZXMiOlsiYWNjb3VudDokVVNFUl9JRCQ6YTkxMTQwNDktMzBkZS00N2ZlLWFlZTUtNjJlNDBiNDUwNmQ0Il19LHsiaWQiOiJyaXNrLW1hbmFnZW1lbnQtYXBpIiwibWV0aG9kcyI6WyJyaXNrLW1hbmFnZW1lbnQtYXBpOnJlc3Q6cHVibGljOio6KiJdLCJyb2xlcyI6WyJyZWFkZXIiXSwicmVzb3VyY2VzIjpbImFjY291bnQ6JFVTRVJfSUQkOmE5MTE0MDQ5LTMwZGUtNDdmZS1hZWU1LTYyZTQwYjQ1MDZkNCJdfV0sImlnbm9yZVJhdGVMaW1pdHMiOmZhbHNlLCJ0b2tlbklkIjoiMjAyMTAyMTMiLCJpbXBlcnNvbmF0ZWQiOmZhbHNlLCJyZWFsVXNlcklkIjoiMzMxYWJmYTgxYTJiZmYzMzE4Mzc4YTI5N2Y0ZGMxNTgiLCJpYXQiOjE3ODg1NDk2MDIsImV4cCI6MTc5NjMyNTYwMn0.BPkbvYOO5xBp4Y6P-duhFP9Xe1GNuR-iUaFvpjKlZmVzOsxUY6R4tVjwRwiPbheHJLf7pB9N1nHNbnKgeNSh3Okuf2fUqPYRMMnNTBFuWa0feiOPJrnBdvDuXtsYKdGCbhWNVQRBmGOfb_p0WU1UOkbszqUqiyO2Hqh5wEOOHSLXIXJAR50RxsdEdymtwlobxExcdCstVlKX2DSEYu0yjmEeUgTK7FFwioLHZ4uGRa3_Guvloz6cRn5Ca9LYgiCxBzD2O-2jrJOLlXgaC_IVn1eH-KUMDkY7V-Ct8GQabbIcbUnoRWlllzpuHsRz22pn_ksqd9NX1FG6_-qBHJwqdJdbuUJztaKWiBBv7SZSm27H_bNK7m_PZUMPvimx55N8l9ys7Vu7hCGqlMTQumXvCcgJnyun_dPjC16lAU59FVISVw8V916Xv7nJOIQ2BjGWgevqYQhTEj-veZPH7Mv9QuCPyxqGSuKwObWxw7BPGunxHlg5lPNtRNsNjQXNs-QYBsadTyue9MP1Hs-LkFUYeFTCpEWRds5QFY51yVZ9sq-MIwTBRmT-co10Nb93mVDOTSqh51kDI462Q1RjznUUf85KRzPMtodi1dID0gQx5zKujfj1PqCV7HBAzUI5Sqgxid1l0iRHSocqtBo2nTkbxCbwDB_cqGyK7b7m4NxyZ7w"
ACCOUNT_ID = "a9114049-30de-47fe-aee5-62e40b4506d4"

async def run_bot():
    print("جاري الاتصال بـ MetaApi...")
    api = MetaApi(API_TOKEN)
    account = await api.metatrader_account_api.get_account(ACCOUNT_ID)
    
    # تفعيل الحساب والانتظار للاتصال
    await account.deploy()
    await account.wait_connected()
    
    connection = account.get_rpc_connection()
    await connection.connect()
    await connection.wait_synchronized()
    print("تم الاتصال بنجاح بالحساب التجريبي!")

    # التداول على الذهب
    symbol = 'XAUUSD'
    lot_size = 0.01  # حجم العقد التجريبي
    
    # جلب السعر الحالي للذهب
    price = await connection.get_symbol_price(symbol)
    ask_price = price['ask']
    print(f"السعر الحالي للذهب ({symbol}) هو: {ask_price}")

    # تحديد الهدف ووقف الخسارة للذهب (مثال: فارق 5 دولار)
    stop_loss = ask_price - 5.0
    take_profit = ask_price + 5.0

    print("جاري تنفيذ صفقة شراء تجريبية على الذهب...")
    result = await connection.create_market_buy_order(
        symbol=symbol,
        volume=lot_size,
        stop_loss=stop_loss,
        take_profit=take_profit
    )
    
    print(f"تم فتح صفقة الذهب بنجاح! رقم الصفقة: {result['orderId']}")

# تشغيل البوت
asyncio.run(run_bot())
