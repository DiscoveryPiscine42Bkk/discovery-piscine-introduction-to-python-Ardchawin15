#!/usr/bin/env python3
farm_tasks = []

def show_menu():
    print("\n===== เมนูจัดการงานฟาร์ม =====")
    print("1. เพิ่มงานในฟาร์ม")
    print("2. แสดงรายการงานทั้งหมด")
    print("3. ลบงาน")
    print("4. สรุปจำนวนงานในแต่ละประเภท")
    print("5. ออกจากโปรแกรม")

def add_task():
    name = input("ชื่องาน: ")
    category = input("ประเภทงาน (crops/livestock): ").lower()
    date = input("วันที่ทำงาน (เช่น 18-06-2025): ")
    farm_tasks.append({
        "name": name,
        "category": category,
        "date": date
    })
    print("✅ เพิ่มงานเรียบร้อยแล้ว")

def show_tasks():
    if not farm_tasks:
        print("ไม่มีงานในรายการ")
        return
    print("\n📋 รายการงานทั้งหมด:")
    for i, task in enumerate(farm_tasks, start=1):
        print(f"{i}. {task['name']} ({task['category']}) - วันที่: {task['date']}")

def delete_task():
    if not farm_tasks:
        print("ไม่มีงานให้ลบ")
        return

    show_tasks()
    name_to_delete = input("กรุณาใส่ 'ชื่องาน' ที่ต้องการลบ: ")

    found = False
    for i, task in enumerate(farm_tasks):
        if task["name"].lower() == name_to_delete.lower():
            removed = farm_tasks.pop(i)
            print(f"🗑 ลบงาน '{removed['name']}' แล้ว")
            found = True
            break

    if not found:
        print("❌ ไม่พบบางงานชื่อนี้ในระบบ")

def summarize_tasks():
    summary = {}
    for task in farm_tasks:
        category = task["category"]
        summary[category] = summary.get(category, 0) + 1

    print("\n📊 สรุปจำนวนงานตามประเภท:")
    if not summary:
        print("ไม่มีข้อมูล")
    else:
        for cat, count in summary.items():
            print(f"- {cat}: {count} งาน")
while True:
    show_menu()
    choice = input("กรุณาเลือกเมนู (1-5): ")
    if choice == "1":
        add_task()
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        summarize_tasks()
    elif choice == "5":
        print("👋 ออกจากโปรแกรมแล้ว")
        break
    else:
        print("❌ กรุณาเลือกเมนูให้ถูกต้อง")