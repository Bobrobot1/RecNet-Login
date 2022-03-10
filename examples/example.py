from recnetlogin import RecNetLogin

# Insert your Rec Room account credentials
USERNAME: str = ""
PASSWORD: str = ""

def main() -> None:
    rnl = RecNetLogin(username=USERNAME, password=PASSWORD)

    token = rnl.get_token(include_bearer=True)
    decoded_token = rnl.get_decoded_token()

    print(f"{token=}\n{decoded_token=}")

if __name__ == "__main__":
    main()