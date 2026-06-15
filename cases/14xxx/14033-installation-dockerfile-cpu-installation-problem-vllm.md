# vllm-project/vllm#14033: [Installation]: Dockerfile.cpu installation problem vLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#14033](https://github.com/vllm-project/vllm/issues/14033) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: Dockerfile.cpu installation problem vLLM

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` Dockerfile.cpu installation I can't complete the build somehow, I want to use vLLM over CPU since I don't have a graphics card on my own server, but the installation gives an error as follows. OS= rockylinux 9.4 ram 16gb vCPU=> 24 Hypervisor= proxmox 8.2.7 docker version => Docker version 28.0.1, build 068a01e errors messages; docker build -f Dockerfile.cpu -t vllm-cpu-env --shm-size=4g . Dockerfile.cpu:54 -------------------- 53 | 54 | >>> RUN --mount=type=cache,target=/root/.cache/pip \ 55 | >>> --mount=type=cache,target=/root/.cache/ccache \ 56 | >>> --mount=type=bind,source=.git,target=.git \ 57 | >>> VLLM_TARGET_DEVICE=cpu python3 setup.py bdist_wheel && \ 58 | >>> pip install dist/*.whl && \ 59 | >>> rm -rf dist 60 | -------------------- ERROR: failed to solve: process "/bin/sh -c VLLM_TARGET_DEVICE=cpu python3 setup.py bdist_wheel && pip install dist/*.whl && rm -rf dist" did not complete successfully: exit code: 1 ### How you are installing vllm docker build -f Dockerfile.cpu -t vllm-cpu-env --shm-size=4g . ### Before submitting a new issue... - [x] Make sure you already searched for relevant is...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Installation]: Dockerfile.cpu installation problem vLLM installation;stale ### Your current environment ```text The output of `python collect_env.py` ``` Dockerfile.cpu installation I can't complete the build somehow, I
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: g . ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Installation]: Dockerfile.cpu installation problem vLLM installation;stale ### Your current environment ```text The output of `python collect_env.py` ``` Dockerfile.cpu installation I can't complete the build somehow,...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
