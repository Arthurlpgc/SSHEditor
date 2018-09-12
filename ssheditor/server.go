package main

import (
    "fmt"
    "log"
	"net/http"
	"golang.org/x/crypto/ssh"
)

func handler(w http.ResponseWriter, r *http.Request) {
	if (r.URL.Path[1:8] == "connect") {
		sshConfig := &ssh.ClientConfig{
			User: "root",
			Auth: []ssh.AuthMethod{ssh.Password("root")},
		}
		sshConfig.HostKeyCallback = ssh.InsecureIgnoreHostKey()
		client, _ := ssh.Dial("tcp", "sshserver:22", sshConfig)
		session, _ := client.NewSession()
		fmt.Fprintf(w, "Hi there, I love %s!", err)
	} else {
		fmt.Fprintf(w, r.URL.Path[1:7])
	}
}

func main() {
    http.HandleFunc("/", handler)
    log.Fatal(http.ListenAndServe(":5000", nil))
}