# vllm-project/vllm#10913: [Bug]: Speculative decoding inconsistency for Qwen-Coder-32B

| 字段 | 值 |
| --- | --- |
| Issue | [#10913](https://github.com/vllm-project/vllm/issues/10913) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 26; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Speculative decoding inconsistency for Qwen-Coder-32B

### Issue 正文摘录

### Your current environment ### Model Input Dumps Running VLLM with docker. Speculative decoding for the Qwen-coder-32B using the 0.5B model does not work. Note that all the Qwen models described are from the official Qwen AWQ repos on Huggingface. Here is the relevant section of docker-compose.yml: command: > --model /app/models/Qwen2.5-Coder-32B-Instruct-AWQ --tensor_parallel_size 2 --max-model-len 23568 --enable-auto-tool-choice --tool-call-parser hermes --speculative_model="/app/models/Qwen2.5-Coder-0.5B-Instruct-AWQ" --num_speculative_tokens=5 However, curiously, the 7B model DOES work. command: > --model /app/models/Qwen2.5-Coder-32B-Instruct-AWQ --tensor_parallel_size 2 --max-model-len 23568 --enable-auto-tool-choice --tool-call-parser hermes --speculative_model="/app/models/Qwen2.5-Coder-**7B**-Instruct-AWQ" --num_speculative_tokens=5 A write-up on HuggingFace says that the error _could_ be due to a difference in the vocabulary size between 0.5/3B and 7/32B. The 7B model works well enough on my dual-3090 setup, but I would love to save the VRAM and get even faster performance from using the 0.5B model for speculative decoding. ### 🐛 Describe the bug Speculative decoding f...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Speculative decoding inconsistency for Qwen-Coder-32B bug;stale ### Your current environment ### Model Input Dumps Running VLLM with docker. Speculative decoding for the Qwen-coder-32B using the 0.5B model does n...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ## Your current environment ### Model Input Dumps Running VLLM with docker. Speculative decoding for the Qwen-coder-32B using the 0.5B model does not work. Note that all the Qwen models described are from the official Q...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Speculative decoding inconsistency for Qwen-Coder-32B bug;stale ### Your current environment ### Model Input Dumps Running VLLM with docker. Speculative decoding for the Qwen-coder-32B using the 0.5B model does n...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: c2f ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
