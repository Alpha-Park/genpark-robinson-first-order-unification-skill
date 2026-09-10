from client import FirstOrderUnifier
import json

def handle_request(req):
    unifier = FirstOrderUnifier()
    action = req.get("action")
    if action == "unify":
        t1 = req.get("t1")
        t2 = req.get("t2")
        mgu = unifier.unify(t1, t2)
        return {"status": "ok", "unifiable": mgu is not None, "mgu": mgu}
    return {"status": "error", "message": "Unknown action"}

if __name__ == "__main__":
    print(json.dumps(handle_request({"action": "unify", "t1": ["f", "?X"], "t2": ["f", "a"]})))
