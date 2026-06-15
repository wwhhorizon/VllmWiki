# vllm-project/vllm#10898: [Performance]: Server launched with LoRA adapter but queried without is much slower than standard server

| 字段 | 值 |
| --- | --- |
| Issue | [#10898](https://github.com/vllm-project/vllm/issues/10898) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: Server launched with LoRA adapter but queried without is much slower than standard server

### Issue 正文摘录

### Report of performance regression There are several existing issues related to the performance of LoRA, but I haven't seen the problem that I encountered. When launching a server without any lora adapter via `vllm serve meta-llama/Llama-2-7b-hf --tensor_parallel_size 8 --max-model-len 4096` and querying it via `time curl http://localhost:8000/v1/completions \ -H "Content-Type: application/json" \ -d '{ "model": "meta-llama/Llama-2-7b-hf", "prompt": "Repeat the following sentence two hundred times: San Francisco is a city in California.", "max_tokens": 3000, "temperature": 0 }'`, I observe a real time of about **15 seconds** (on a machine with eight A100s with 40GB). But when I launch a server with lora adapter via `vllm serve meta-llama/Llama-2-7b-hf --tensor_parallel_size 8 --max-model-len 4096 --enable-lora --lora-modules lora=$HOME/.cache/huggingface/hub/models--yard1--llama-2-7b-sql-lora-test/... --fully-sharded-loras` and query _the base model only_ (i.e., without the lora adapter) in the very same way as above, I measure a real time of about **23 seconds**. I would like to understand where this additional running time is coming from? I observe significant additional runni...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: When launching a server without any lora adapter via `vllm serve meta-llama/Llama-2-7b-hf --tensor_parallel_size 8 --max-model-len 4096` and querying it via `time curl http://localhost:8000/v1/completions \ -H "Content-...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: slower than standard server performance;stale ### Report of performance regression There are several existing issues related to the performance of LoRA, but I haven't seen the problem that I encountered. When launching...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: "prompt": "Repeat the following sentence two hundred times: San Francisco is a city in California.", "max_tokens": 3000, "temperature": 0 }'`, I observe a real time of about **15 seconds** (on a machine with eight A100s...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: , I observe a real time of about **15 seconds** (on a machine with eight A100s with 40GB). But when I launch a server with lora adapter via `vllm serve meta-llama/Llama-2-7b-hf --tensor_parallel_size 8 --max-model-len 4...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: pter but queried without is much slower than standard server performance;stale ### Report of performance regression There are several existing issues related to the performance of LoRA, but I haven't seen the problem th...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
