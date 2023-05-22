from ansible_runner import run

def run_playbook(playbook_path):
    result= run(playbook=playbook_path)
    return result
    