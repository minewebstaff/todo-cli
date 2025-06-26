import argparse

def main():
    parser = argparse.ArgumentParser(description="ToDo CLI ツール")
    subparsers = parser.add_subparsers(dest="command", required=True, help="Command to execute")

    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("task", nargs="?", help="Task description")

    list_parser = subparsers.add_parser("list", help="List all tasks")
    # list_parser.add_argument("--all", action="store_true", help="Show all tasks")
    
    args = parser.parse_args()

    if args.command == "add":
        print(f"タスク追加: {args.task}")
    elif args.command == "list":
        print("タスク一覧（未実装）")
        
        
if __name__ == "__main__":
    main()
