# 🔐 Encrypted Tunnel using SSL/TLS in Python

This project implements a **basic encrypted communication tunnel** using Python sockets wrapped with **SSL/TLS**, simulating a secure messaging system between a client and a server. 

Though base64 encoding is currently used to simulate encryption, the infrastructure is designed to be extended to use real encryption algorithms (e.g., AES, RSA).

---

## 🧠 Project Overview

- **Protocol:** TCP (SOCK_STREAM)
- **Encryption Layer:** SSL/TLS (via Python's `ssl` module)
- **Simulated Encryption:** Base64 (placeholder for actual encryption)
- **Dual Socket Architecture:**
  - Port 9090 → Control Messages
  - Port 9091 → Data Messages

---

## 📁 File Structure

```bash
encrypted_tunnel/
├── server.py           # Secure server with dual-port SSL socket communication
├── client.py           # Client that connects to both control and data ports securely
├── ssl_cert_gen.py     # Generates SSL/TLS certificates (self-signed)
├── cert.pem            # SSL certificate (auto-generated)
├── key.pem             # SSL private key (auto-generated)
