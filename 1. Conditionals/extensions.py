name = input("File name: ").strip()

if (name).endswith('gif'):
    print("image/gif")
elif (name).endswith(('jpg','jpeg')):
    print("image/jpeg")
elif (name).endswith('png'):
    print("image/png")
elif (name).endswith(('PDF','pdf')):
    print("application/pdf")
elif (name).endswith('txt'):
    print("text/plain")
elif (name).endswith('zip'):
    print("application/zip")
else:
    print("application/octet-stream")

# cleanest answer v
# name = input("File name: ").strip().lower()

#if name.endswith("gif"):
#    print("image/gif")
#elif name.endswith(("jpg", "jpeg")):
#    print("image/jpeg")
#elif name.endswith("png"):
#    print("image/png")
#elif name.endswith("pdf"):
#    print("application/pdf")
#elif name.endswith("txt"):
#    print("text/plain")
#elif name.endswith("zip"):
#    print("application/zip")
#else:
#    print("application/octet-stream")