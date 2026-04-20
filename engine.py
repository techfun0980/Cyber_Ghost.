class GameEngine:
    def __init__(self):
        self.missions = {
            1: {
                "title": "Dehradun Node Discovery",
                "task": "Scan network for entry points.",
                "solution": "scan",
                "success": "[JINI]: Open Port found at 80. Gateway ready."
            },
            2: {
                "title": "Firewall Breach",
                "task": "Bypass gateway using 'overload' protocol.",
                "solution": "overload",
                "success": "[SUCCESS]: Firewall bypassed. System decrypted."
            }
        }
        self.current_level = 1

    def process(self, cmd):
        mission = self.missions.get(self.current_level)
        if not mission: return "MOKSHA ACHIEVED."
        
        if cmd == mission["solution"]:
            self.current_level += 1
            return f"{mission['success']}\n\n[NEXT]: {self.missions.get(self.current_level, {}).get('title', 'END')}"
        return f"[ERROR]: '{cmd}' failed. Type 'help' for mission info."
