# vllm-project/vllm#29983: [Bug]: v0.12.0 Dockerfile.cpu fails to build on ARM server

| 字段 | 值 |
| --- | --- |
| Issue | [#29983](https://github.com/vllm-project/vllm/issues/29983) |
| 状态 | closed |
| 标签 | bug;stale;cpu |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: v0.12.0 Dockerfile.cpu fails to build on ARM server

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug v0.12.0 Dockerfile.cpu fails to build image on ARM server running RHEL 9.6 ``COMMAND SEQUENCE sut# cat /etc/os-release "Red Hat Enterprise Linux 9.6 (Plow)" sut# uname -r 5.14.0-570.12.1.el9_6.aarch64 sut# lscpu | grep Model Ampere-1a BIOS Model name: AmpereOne (R) sut# git clone https://github.com/vllm-project/vllm; cd vllm **sut# podman build --platform=linux/arm64 -f docker/Dockerfile.cpu .** [1/9] STEP 19/21: RUN --mount=type=cache,target=/root/.cache/uv --mount=type=bind,src=requirements/common.txt,target=requirements/common.txt --mount=type=bind,src=requirements/cpu.txt,target=requirements/cpu.txt uv pip install --upgrade pip && uv pip install -r requirements/cpu.txt Using Python 3.12.12 environment at: /opt/venv Resolved 1 package in 145ms Audited 1 package in 0.02ms error: File not found: `requirements/cpu.txt` Error: building at STEP "RUN --mount=type=cache,target=/root/.cache/uv --mount=type=bind,src=requirements/common.txt,target=requirements/common.txt --mount=type=bind,src=requirements/cpu.txt,target=requirements/cpu.txt uv pip install --upgrade pip && uv pip install -r requirements/cpu.txt": while running runtime: e...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Bug]: v0.12.0 Dockerfile.cpu fails to build on ARM server bug;stale;cpu ### Your current environment ### 🐛 Describe the bug v0.12.0 Dockerfile.cpu fails to build image on ARM server running RHEL 9.6 ``COMMAND SEQUENCE...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: Hat Enterprise Linux 9.6 (Plow)" sut# uname -r 5.14.0-570.12.1.el9_6.aarch64 sut# lscpu | grep Model Ampere-1a BIOS Model name: AmpereOne (R) sut# git clone https://github.com/vllm-project/vllm; cd vllm **sut# podman bu...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: (Plow)" sut# uname -r 5.14.0-570.12.1.el9_6.aarch64 sut# lscpu | grep Model Ampere-1a BIOS Model name: AmpereOne (R) sut# git clone https://github.com/vllm-project/vllm; cd vllm **sut# podman build --platform=linux/arm6...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: v0.12.0 Dockerfile.cpu fails to build on ARM server bug;stale;cpu ### Your current environment ### 🐛 Describe the bug v0.12.0 Dockerfile.cpu fails to build image on ARM server running RHEL 9.6 ``COMMAND SEQUENCE...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
