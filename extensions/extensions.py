name = input("Filename: ").lower().strip()
suffix = name.split('.')[-1]

match suffix:
    case "gif" | "png":
        print(f"image/{suffix}")
    case "jpeg" | "jpg":
        print(f"image/jpeg")
    case "pdf" | "zip":
        print(f"application/{suffix}")
    case "txt":
        print(f"text/plain")
    case _:
        print("application/octet-stream")