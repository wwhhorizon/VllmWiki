# vllm-project/vllm#30076: [Installation]: 'podman run vllm-cpu-release-repo:v0.12.0’ fails on aarch64

| 字段 | 值 |
| --- | --- |
| Issue | [#30076](https://github.com/vllm-project/vllm/issues/30076) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: 'podman run vllm-cpu-release-repo:v0.12.0’ fails on aarch64

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How you are installing vllm ``` sut# podman run --name vllm-cpu --rm --privileged=true public.ecr.aws/q9t5s3a7/vllm-cpu-release-repo:v0.12.0 ``` **WARNING:** image platform (linux/amd64) does not match the expected platform (linux/arm64) {"msg":"exec container process `/opt/venv/bin/vllm`: Exec format error","level":"error","time":"2025-12-04T15:15:35.826445Z"} ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Installation]: 'podman run vllm-cpu-release-repo:v0.12.0’ fails on aarch64 installation;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How you are installing vllm ``` sut# pod
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [Installation]: 'podman run vllm-cpu-release-repo:v0.12.0’ fails on aarch64 installation;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How you are installing vllm ``` sut# podm...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: (linux/arm64) {"msg":"exec container process `/opt/venv/bin/vllm`: Exec format error","level":"error","time":"2025-12-04T15:15:35.826445Z"} ### Before submitting a new issue... - [x] Make sure you already searched for r...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: 'podman run vllm-cpu-release-repo:v0.12.0’ fails on aarch64 installation;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How you are installing vllm ``` sut# podman run --name vl...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
