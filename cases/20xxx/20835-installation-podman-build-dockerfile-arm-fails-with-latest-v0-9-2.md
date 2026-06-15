# vllm-project/vllm#20835: [Installation]: podman build Dockerfile.arm fails with 'latest/v0.9.2'

| 字段 | 值 |
| --- | --- |
| Issue | [#20835](https://github.com/vllm-project/vllm/issues/20835) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: podman build Dockerfile.arm fails with 'latest/v0.9.2'

### Issue 正文摘录

### Your current environment With a current 'git clone' (v0.9.2) I am no longer able to build vLLM-cpu for ARM. This command runs successfully when I 'git clone' previous release (eg. vllm-0.9.1.dev47+gb169d5f7b.cpu) Here is some info about the Host System ``` root# cat /etc/os-release NAME="Red Hat Enterprise Linux" VERSION="9.4 (Plow)" root# podman --version podman version 4.9.4-rhel root# lscpu | grep -i model Model name: Neoverse-N1 BIOS Model name: Ampere(R) Altra(R) Max Processor ``` Here is the podman build command being issued: ``` root# podman build -f docker/Dockerfile.arm --tag vllm-cpu-env --target build . ``` And here is the resulting error w/v0.9.2: ``` [233/235] Building CXX object /workspace/vllm/.deps/onednn-build/src/cpu/CMakeFiles/dnnl_cpu.dir/reorder/cpu_reorder_comp_f32_s8.cpp.o ninja: build stopped: subcommand failed. Traceback (most recent call last): File "/workspace/vllm/setup.py", line 685, in setup( File "/usr/local/lib/python3.10/dist-packages/setuptools/__init__.py", line 117, in setup return distutils.core.setup(**attrs) File "/usr/local/lib/python3.10/dist-packages/setuptools/_distutils/core.py", line 186, in setup return run_commands(dist) File "/us...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Installation]: podman build Dockerfile.arm fails with 'latest/v0.9.2' installation;stale ### Your current environment With a current 'git clone' (v0.9.2) I am no longer able to build vLLM-cpu for ARM. This command runs
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: Neoverse-N1 BIOS Model name: Ampere(R) Altra(R) Max Processor ``` Here is the podman build command being issued: ``` root# podman build -f docker/Dockerfile.arm --tag vllm-cpu-env --target build . ``` And here is the re...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: root# podman --version podman version 4.9.4-rhel root# lscpu | grep -i model Model name: Neoverse-N1 BIOS Model name: Ampere(R) Altra(R) Max Processor ``` Here is the podman build command being issued: ``` root# podman...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: on]: podman build Dockerfile.arm fails with 'latest/v0.9.2' installation;stale ### Your current environment With a current 'git clone' (v0.9.2) I am no longer able to build vLLM-cpu for ARM. This command runs successful...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [Installation]: podman build Dockerfile.arm fails with 'latest/v0.9.2' installation;stale ### Your current environment With a current 'git clone' (v0.9.2) I am no longer able to build vLLM-cpu for ARM. This command runs...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
