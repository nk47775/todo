import os

print("📝 स्मार्ट To-Do List")
ch = input("1. काम देखें | 2. काम जोड़ें | 3. सब मिटाएं\nविकल्प चुनें (1/2/3): ")

if ch == '1':
    try:
        with open("todo.txt", "r") as f:
            tasks = f.readlines()
            if tasks:
                print("\n📌 आपके काम:")
                for i, t in enumerate(tasks, 1):
                    print(f"{i}. {t.strip()}")
            else:
                print("\n📭 लिस्ट खाली है!")
    except:
        print("\n📭 लिस्ट खाली है!")
elif ch == '2':
    task = input("\nनया काम लिखें: ")
    with open("todo.txt", "a") as f:
        f.write(f"{task}\n")
    print("✅ काम सेव हो गया!")
elif ch == '3':
    if os.path.exists("todo.txt"):
        os.remove("todo.txt")
    print("\n🗑️ सारे काम मिटा दिए गए!")
else:
    print("\n❌ गलत विकल्प!")
