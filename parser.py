def read_uploaded_file(file):
    return file.read().decode("utf-8", errors="ignore")


def parse_txt_email(text):
    sender = "Unknown"
    recipient = "Unknown"
    subject = "No Subject"
    date = "Unknown"
    body_lines = []

    for line in text.splitlines():
        if line.startswith("From:"):
            sender = line.replace("From:", "").strip()
        elif line.startswith("To:"):
            recipient = line.replace("To:", "").strip()
        elif line.startswith("Subject:"):
            subject = line.replace("Subject:", "").strip()
        elif line.startswith("Date:"):
            date = line.replace("Date:", "").strip()
        else:
            body_lines.append(line)

    body = "\n".join(body_lines).strip()

    return sender, recipient, subject, date, body