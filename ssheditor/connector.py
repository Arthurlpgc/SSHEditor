from paramiko import SSHClient, AutoAddPolicy
class Connection:
    def __init__(self, host="sshserver", port=22):
        self.client = SSHClient()
        self.client.set_missing_host_key_policy(AutoAddPolicy)
        self.client.connect(hostname = host, username = "root", password = "root")
        self.bashIn, self.bashOut, self.bashErr = self.client.exec_command("bash")
    def get_file_structure(self, path):
        cin, cout, cerr = self.client.exec_command("ls -la " + path)
        output = cout.read().decode('ascii')
        lines = output.split('\n')
        ret = {}
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


        
