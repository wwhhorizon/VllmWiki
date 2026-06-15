# vllm-project/vllm#29042: [Feature]: Add option to tolerate self-signed certificates to vllm bench serve

| 字段 | 值 |
| --- | --- |
| Issue | [#29042](https://github.com/vllm-project/vllm/issues/29042) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Add option to tolerate self-signed certificates to vllm bench serve

### Issue 正文摘录

### 🚀 The feature, motivation and pitch It now seems to be impossible to run `vllm bench serve` against an existing vLLM deployment that is exposed with self-signed certificates (a common occurrence in test/lab environments). Since `benchmark_serving.py` is now gone, it's also not possible to doctor the code and let `requests` tolerate self-signed. Can an `--no-ssl-verify` option be added to the CLI? ### Alternatives Tried different things such as importing the self-signed to the system keychain, adding `export REQUESTS_CA_BUNDLE=my_ca.crt`... nothing seems to help. ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: option to tolerate self-signed certificates to vllm bench serve feature request;stale ### 🚀 The feature, motivation and pitch It now seems to be impossible to run `vllm bench serve` against an existing vLLM deployment t...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: nt that is exposed with self-signed certificates (a common occurrence in test/lab environments). Since `benchmark_serving.py` is now gone, it's also not possible to doctor the code and let `requests` tolerate self-signe...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: be added to the CLI? ### Alternatives Tried different things such as importing the self-signed to the system keychain, adding `export REQUESTS_CA_BUNDLE=my_ca.crt`... nothing seems to help. ### Additional context _No re...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
