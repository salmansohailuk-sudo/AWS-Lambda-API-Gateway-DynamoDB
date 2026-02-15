import json
import boto3
import urllib.parse
import base64
from decimal import Decimal

# DynamoDB setup
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('devdb')


def lambda_handler(event, context):
    try:
        method = event.get("httpMethod")
        query = event.get("queryStringParameters") or {}

        print("METHOD:", method)
        print("QUERY:", query)

        # ================= CORS PREFLIGHT =================
        if method == "OPTIONS":
            return response(200, {"message": "CORS OK"})

        # ================= GET =================
        if method == "GET":

            if query.get("action") == "data":
                response_data = table.scan()
                print("SCAN RESULT:", response_data)
                return response(200, response_data.get("Items", []))

            if query.get("action") == "view":
                return response(200, load_html("view.html"), "text/html")

            if query.get("action") == "edit":
                return response(200, load_html("edit.html"), "text/html")

            return response(200, load_html("index.html"), "text/html")

        # ================= INSERT =================
        if method == "POST":
            data = parse_form_data(event)

            email = data["email"].strip()

            print("INSERTING:", email)

            table.put_item(
                Item={
                    "email": email,
                    "1": Decimal(1),  # SORT KEY
                    "fname": data.get("fname", ""),
                    "lname": data.get("lname", ""),
                    "message": data.get("message", "")
                }
            )

            return response(200, load_html("success.html"), "text/html")

        # ================= DELETE =================
        if method == "DELETE":
            body = json.loads(event.get("body") or "{}")

            email = body.get("email", "").strip()

            print("DELETING:", email)

            table.delete_item(
                Key={
                    "email": email,
                    "1": Decimal(1)
                }
            )

            return response(200, {"message": "Deleted Successfully"})

        # ================= UPDATE =================
        if method == "PUT":
            body = json.loads(event.get("body") or "{}")

            email = body.get("email", "").strip()
            fname = body.get("fname", "")
            lname = body.get("lname", "")
            message = body.get("message", "")

            print("UPDATING:", email)

            # First confirm item exists
            existing = table.get_item(
                Key={
                    "email": email,
                    "1": Decimal(1)
                }
            )

            print("EXISTING ITEM:", existing)

            if "Item" not in existing:
                return response(400, {"error": "Item not found in DB"})

            # Now update
            table.update_item(
                Key={
                    "email": email,
                    "1": Decimal(1)
                },
                UpdateExpression="SET fname = :f, lname = :l, message = :m",
                ExpressionAttributeValues={
                    ":f": fname,
                    ":l": lname,
                    ":m": message
                }
            )

            print("UPDATE SUCCESS")

            return response(200, {"message": "Updated Successfully"})

        return response(405, {"message": "Method Not Allowed"})

    except Exception as e:
        print("ERROR:", str(e))
        return response(500, {"error": str(e)})


# ================= UTILITIES =================

def parse_form_data(event):
    body = event.get("body")

    if event.get("isBase64Encoded"):
        body = base64.b64decode(body).decode("utf-8")

    parsed = urllib.parse.parse_qs(body)
    return {k: v[0] for k, v in parsed.items()}


def response(status, body, content_type="application/json"):

    def decimal_default(obj):
        if isinstance(obj, Decimal):
            return int(obj)
        raise TypeError

    if isinstance(body, (dict, list)):
        body = json.dumps(body, default=decimal_default)

    return {
        "statusCode": status,
        "headers": {
            "Content-Type": content_type,
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "*",
            "Access-Control-Allow-Methods": "GET,POST,PUT,DELETE,OPTIONS"
        },
        "body": body
    }


def load_html(filename):
    with open(filename, "r") as f:
        return f.read()
