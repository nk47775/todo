print("📝 To-Do List")
ch = input("1. टास्क देखें | 2. नया टास्क जोड़ें\nविकल्प चुनें (1/2): ")

if ch == '1':
    try:
        print("\n📌 आपके काम:")
        with open("todo.txt", "r") as f:
            print(f.read())
    except:
        print("\n❌ अभी कोई काम सेव नहीं है!")
elif ch == '2':
    task = input("\nनया काम लिखें: ")
    with open("todo.txt", "a") as f:
        f.write(f"👉 {task}\n")
    print("\n✅ काम सेव हो गया!")
  
