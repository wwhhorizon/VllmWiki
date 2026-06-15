# vllm-project/vllm#35462: [Installation]: branch v0.16.0 still rely on torch 2.9.1, not 2.10

| 字段 | 值 |
| --- | --- |
| Issue | [#35462](https://github.com/vllm-project/vllm/issues/35462) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: branch v0.16.0 still rely on torch 2.9.1, not 2.10

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How you are installing vllm # Should be mirrored in pyproject.toml cmake>=3.26.1 ninja packaging>=24.2 setuptools>=77.0.3, =8 torch==2.9.1 wheel jinja2>=3.1.6 regex build protobuf >= 5.29.6, !=6.30.*, !=6.31.*, !=6.32.*, !=6.33.0.*, !=6.33.1.*, !=6.33.2.*, !=6.33.3.*, !=6.33.4.* grpcio-tools==1.78.0 # Required for grpc entrypoints ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Installation]: branch v0.16.0 still rely on torch 2.9.1, not 2.10 installation ### Your current environment ```text The output of `python collect_env.py` ``` ### How you are installing vllm # Should be mirrored in pyp
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: nts ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
