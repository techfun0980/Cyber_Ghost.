def process_input(self, cmd):
        cmd = cmd.lower().strip() # Normalize input
        mission = self.missions.get(self.current_level)
        
        if not mission:
            return "DIGITAL MOKSHA ACHIEVED. ALL LEVELS CLEARED."

        # System Commands (Always Active)
        if cmd == "help":
            return f"--- MISSION PROTOCOL ---\nOBJECTIVE: {mission['task']}\nHINT: {mission['hint']}\nLEVEL: {self.current_level}"
        
        if cmd == "clear":
            return "CLEAR_SCREEN"

        # Mission Progress Logic
        if cmd == mission["solution"]:
            self.current_level += 1
            next_m = self.missions.get(self.current_level, {"title": "Final Frontier"})
            return f"{mission['success']}\n\n[NEW MISSION]: {next_m['title']}"
        else:
            return f"[ERROR]: Command '{cmd}' failed. Access Denied."
# engine.py update
self.missions[3] = {
    "title": "The Subnet Stalker",
    "task": "Intercept the encrypted handshake between Node A and Node B.",
    "hint": "Use 'sniff --packet' to capture the data stream.",
    "solution": "sniff --packet",
    "success": "[JINI]: Packet Captured! Decrypting password... Key found: 'Dharma_2026'."
}
