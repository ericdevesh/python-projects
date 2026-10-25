# PRT — CI/CD Automation with Docker and Kubernetes

This project is stored under `prt-cicd-devops/` in the public GitHub repository [ericdevesh/python-projects](https://github.com/ericdevesh/python-projects).

## Three-machine architecture
- `ci-master`: Ubuntu, Jenkins + Java + Ansible
- `ci-agent`: Ubuntu, Jenkins SSH agent + Java + Docker
- `k8s-node`: Terraform-provisioned Ubuntu VM with a single-node Kubernetes cluster

## Project files
- `Dockerfile` and `app/index.html`
- `Jenkinsfile`
- `ansible/site.yml` and `ansible/kubernetes.yml`
- `terraform/*.tf`
- `k8s/deployment.yaml` and `k8s/service.yaml`

This is a starter kit, **not proof that the cloud deployment has already run**. Replace placeholders, run each stage, and attach your own genuine screenshots to the report.

## Clone
```bash
git clone https://github.com/ericdevesh/python-projects.git
cd python-projects/prt-cicd-devops
```

## Terraform
Use an authorized AWS account with a default VPC and an existing EC2 key pair. Install Terraform and AWS CLI; configure credentials using your own IAM identity. From this folder:
```bash
cd terraform
cp terraform.tfvars.example terraform.tfvars
# Edit terraform.tfvars with the exact EC2 key pair name
terraform init
terraform validate
terraform apply
```
Record the `k8s_node_public_ip` output. The example security group exposes SSH (22) and app NodePort (30080) for a short lab; restrict the SSH CIDR and remove resources after grading.

## Ansible
On `ci-master`, install Ansible, put your lab private key at `/home/ubuntu/.ssh/lab.pem` with mode 600, and edit `ansible/inventory.ini` with your real agent and k8s-node public IP addresses.
```bash
sudo apt update && sudo apt install -y ansible git
chmod 600 ~/.ssh/lab.pem
cd ~/python-projects/prt-cicd-devops/ansible
ansible all -i inventory.ini -m ping
ansible-playbook -i inventory.ini site.yml
ansible-playbook -i inventory.ini kubernetes.yml
```

## Jenkins setup
Finish Jenkins setup at `http://CI_MASTER_PUBLIC_IP:8080`; install suggested plugins plus **SSH Build Agents**. Add permanent agent `ci-agent`, remote root `/home/ubuntu/jenkins`, launch via SSH, label `docker`, and use your lab key.

Create a **public Docker Hub repository** named `prt-cicd`. In Jenkins add credentials:
- username/password ID `dockerhub-creds`: Docker Hub username + access token
- SSH private-key ID `k8s-ssh`: username `ubuntu` + lab key

Replace `REPLACE_WITH_K8S_NODE_PUBLIC_IP` in `Jenkinsfile` with Terraform's output and commit the change. Create a Jenkins Pipeline job configured as:
- SCM URL: `https://github.com/ericdevesh/python-projects.git`
- Branch: `*/main`
- Script path: `prt-cicd-devops/Jenkinsfile`

Click **Build Now**. The agent must be Online and its Ubuntu user must be able to run Docker.

## Verify and take screenshots
```bash
kubectl get nodes -o wide
kubectl get pods -A
kubectl get svc
```
Open `http://K8S_NODE_PUBLIC_IP:30080`. The page should show **PRT – CI/CD Completed Successfully**.

Take real screenshots of the GitHub files, Ansible PLAY RECAP, Jenkins agent Online, Terraform apply output, successful Jenkins stages, Kubernetes node/pod/service state, and browser output. Do not fake or claim results before running them. Never commit PEM files, AWS credentials, or tokens. Terminate the lab instances and run `terraform destroy` after evaluation to avoid charges.
