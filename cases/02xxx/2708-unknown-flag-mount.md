# vllm-project/vllm#2708:  Unknown flag: mount

| 字段 | 值 |
| --- | --- |
| Issue | [#2708](https://github.com/vllm-project/vllm/issues/2708) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;frontend_api;model_support |
| 子分类 |  |
| Operator 关键词 | kernel |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

>  Unknown flag: mount

### Issue 正文摘录

code tag: v0.2.7 sudo docker build . --ssh default --target vllm-openai --tag vllm/vllm-openai:1.0 Sending build context to Docker daemon 7.181MB Error response from daemon: Dockerfile parse error line 10: Unknown flag: mount docker info: Client: Context: default Debug Mode: false Plugins: app: Docker App (Docker Inc., v0.9.1-beta3) buildx: Docker Buildx (Docker Inc., v0.9.1-docker) scan: Docker Scan (Docker Inc., v0.17.0) Server: Containers: 42 Running: 2 Paused: 0 Stopped: 40 Images: 28 Server Version: 19.03.15 Storage Driver: overlay2 Backing Filesystem: extfs Supports d_type: true Native Overlay Diff: true Logging Driver: json-file Cgroup Driver: cgroupfs Plugins: Volume: local Network: bridge host ipvlan macvlan null overlay Log: awslogs fluentd gcplogs gelf journald json-file local logentries splunk syslog Swarm: inactive Runtimes: nvidia runc Default Runtime: runc Init Binary: docker-init containerd version: 9cd3357b7fd7218e4aec3eae239db1f68a5a6ec6 runc version: v1.1.4-0-g5fd4c4d init version: fec3683 Security Options: apparmor seccomp Profile: default Kernel Version: 5.4.0-169-generic Operating System: Ubuntu 20.04.6 LTS OSType: linux Architecture: x86_64 CPUs: 32 Total Me...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: Unknown flag: mount code tag: v0.2.7 sudo docker build . --ssh default --target vllm-openai --tag vllm/vllm-openai:1.0 Sending build context to Docker daemon 7.181MB Error response from daemon: Dockerfile parse error li...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 5.4.0-169-generic Operating System: Ubuntu 20.04.6 LTS OSType: linux Architecture: x86_64 CPUs: 32 Total Memory: 251.6GiB Name: ai-gpu-trainer-02 ID: IMMV:UKQG:BJSV:BSM6:MYW3:FZFM:LW3W:AFII:IANI:7DC2:WUIK:5BK5 Docker Ro...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: wn flag: mount docker info: Client: Context: default Debug Mode: false Plugins: app: Docker App (Docker Inc., v0.9.1-beta3) buildx: Docker Buildx (Docker Inc., v0.9.1-docker) scan: Docker Scan (Docker Inc., v0.17.0) Ser...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: false WARNING: No swap limit support performance ci_build;frontend_api;model_support kernel build_error env_dependency code tag: v0.2.7
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: fd4c4d init version: fec3683 Security Options: apparmor seccomp Profile: default Kernel Version: 5.4.0-169-generic Operating System: Ubuntu 20.04.6 LTS OSType: linux Architecture: x86_64 CPUs: 32 Total Memory: 251.6GiB...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
