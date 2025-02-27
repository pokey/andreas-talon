from talon import actions, Module, actions, app, scope
from typing import Any
from pathlib import Path
import json
import time

mod = Module()
dir_path = None
hostname = None
os = None


@mod.action_class
class Actions:
    def persist_append(name: str, payload: Any):
        """Append payload to persisted storage"""
        date = actions.user.date_today()
        file = dir_path / f"{name}_{date}.jsonl"
        full_payload = {
            "time": time.time(),
            "hostname": hostname,
            "os": os,
            **payload,
        }
        with open(file, "a") as f:
            f.writelines([json.dumps(full_payload), "\n"])


def on_ready():
    global dir_path, hostname, os
    dir_path = Path(actions.path.user_home()) / "Documents" / "Talon persisted files"
    dir_path.mkdir(exist_ok=True)
    hostname = scope.get("main.hostname")
    os = scope.get("main.os")


app.register("ready", on_ready)
