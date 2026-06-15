# vllm-project/vllm#2916: How to call/add a new lora module to a live server?

| 字段 | 值 |
| --- | --- |
| Issue | [#2916](https://github.com/vllm-project/vllm/issues/2916) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> How to call/add a new lora module to a live server?

### Issue 正文摘录

Hi, I was reading through the documentation for [Using Lora in VLLM](https://docs.vllm.ai/en/latest/models/lora.html). In the documentation when they start the server, it looks like they have to specify which Lora modules are available ` --lora-modules sql-lora=~/.cache/huggingface/hub/models--yard1--llama-2-7b-sql-lora-test/` Is it possible to do this in real-time instead? That is, start the server and call a recently added Lora module without having to stop and restart the server?

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: he documentation for [Using Lora in VLLM](https://docs.vllm.ai/en/latest/models/lora.html). In the documentation when they start the server, it looks like they have to specify which Lora modules are available ` --lora-m...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: documentation when they start the server, it looks like they have to specify which Lora modules are available ` --lora-modules sql-lora=~/.cache/huggingface/hub/models--yard1--llama-2-7b-sql-lora-test/` Is it possible t...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: How to call/add a new lora module to a live server? stale Hi, I was reading through the documentation for [Using Lora in VLLM](https://docs.vllm.ai/en/latest/models/lora.html). In the documentation when they start the s...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ugh the documentation for [Using Lora in VLLM](https://docs.vllm.ai/en/latest/models/lora.html). In the documentation when they start the server, it looks like they have to specify which Lora modules are available ` --l...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
