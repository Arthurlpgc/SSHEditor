from paramiko import SSHClient, AutoAddPolicy
class Connection:
    def __init__(self, hostname="sshserver", username="root", password="root"):
        self.hostname = hostname
        self.username = username
        self.password = password
        self.client = SSHClient()
        self.client.set_missing_host_key_policy(AutoAddPolicy)
        self.client.connect(hostname = hostname, username = username, password = password)
        self.bashIn, self.bashOut, self.bashErr = self.client.exec_command("bash")
    def get_file_structure(self, path, reconnects = 2):
        cin, cout, cerr = self.client.exec_command("ls -la " + path)
        output = cout.read().decode('ascii')
        lines = output.split('\n')
        ret = {}
        if len(lines) < 2:
            if reconnects > 0:
                self.client.connect(hostname = self.hostname, username = self.username, password = self.password)
                return self.get_file_structure(path, reconnects - 1)
            else:
                return "ERROR"
        lnt = len(lines[1]) -1
        for line in lines[3:]:
            if line != '':
                file = line[lnt:]
                tp = line[0]
                if tp == '-':
                    ret[file] = '-'
                else:
                    ret[file] = self.get_file_structure(path + '/' + file)
        return ret


        
