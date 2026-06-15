# vllm-project/vllm#30569: [Feature]: Add --ssl-ciphers to CLI arguments

| 字段 | 值 |
| --- | --- |
| Issue | [#30569](https://github.com/vllm-project/vllm/issues/30569) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Add --ssl-ciphers to CLI arguments

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Add support for an --ssl-ciphers CLI argument. This flag would be passed directly to uvicorn's --ssl-ciphers kwargs inside the existing serve_http command, parallel to how --ssl-certfile and --ssl-keyfile flags are handled Motivation: vLLM already exposes several uvicorn SSL-related parameters, enabling users to run the vLLM server with managed TLS. However, currently there is no way to specify the allowed SSL/TLS cipher suites. Adding this CLI option provides users with finer control over TLS requirements. ### Alternatives _No response_ ### Additional context Related uvicorn documentation: [https://uvicorn.dev/settings/#HTTP](https://uvicorn.dev/settings/#HTTP) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Feature]: Add --ssl-ciphers to CLI arguments feature request ### 🚀 The feature, motivation and pitch Add support for an --ssl-ciphers CLI argument. This flag would be passed directly to uvicorn's --ssl-ciphers kwargs i...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: TP) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Add --ssl-ciphers to CLI arguments feature request ### 🚀 The feature, motivation and pitch Add support for an --ssl-ciphers CLI argument. This flag would be passed directly to uvicorn's --ssl-ciphers kwargs i...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
