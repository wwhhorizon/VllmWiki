# vllm-project/vllm#36141: [Bug]: Vllm models crashes when using runai_streamer & --api-server-count > 1

| 字段 | 值 |
| --- | --- |
| Issue | [#36141](https://github.com/vllm-project/vllm/issues/36141) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Vllm models crashes when using runai_streamer & --api-server-count > 1

### Issue 正文摘录

### Your current environment - vLLM: 0.15.1 - load format: runai_streamer - model source: S3 - --api-server-count: 2 ### 🐛 Describe the bug When running vLLM with --api-server-count > 1 and --load-format runai_streamer, the second API server process crashes during startup. Both API processes attempt to initialize the RunAI model streamer cache directory simultaneously. One process removes the directory while the other is still accessing it, resulting in a FileNotFoundError. Reproduction: ``` vllm serve s3://bucket/model \ --load-format runai_streamer \ --api-server-count 2 ``` The second API server process fails with: ``` FileNotFoundError: [Errno 2] No such file or directory: /root/.cache/vllm/assets/model_streamer/ ``` Models loaded from a local path (e.g., from a PVC) without runai_streamer work correctly with multiple API servers (--api-server-count > 1). The issue only occurs when using --load-format runai_streamer with S3. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked q...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Vllm models crashes when using runai_streamer & --api-server-count > 1 bug ### Your current environment - vLLM: 0.15.1 - load format: runai_streamer - model source: S3 - --api-server-count: 2 ### 🐛 Describe the b...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: S3. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
