# vllm-project/vllm#37223: [Feature]: Add LoRA support for Qwen3ASRForConditionalGeneration

| 字段 | 值 |
| --- | --- |
| Issue | [#37223](https://github.com/vllm-project/vllm/issues/37223) |
| 状态 | closed |
| 标签 | good first issue;feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Add LoRA support for Qwen3ASRForConditionalGeneration

### Issue 正文摘录

### 🚀 The feature, motivation and pitch When attempting to serve Qwen/Qwen3-ASR-0.6B with LoRA enabled using the following command: ``` vllm serve Qwen/Qwen3-ASR-0.6B \ --enable-lora \ --lora-modules my-adapter=./my-lora-adapter/ \ --max-lora-rank 256 \ --gpu-memory-utilization 0.5 ``` The server fails at model load time with the following error: ``` File ".../vllm/v1/worker/gpu_model_runner.py", line 4301, in load_model self.model = self.load_lora_model( File ".../vllm/v1/worker/lora_model_runner_mixin.py", line 38, in load_lora_model raise ValueError(f"{model.__class__.__name__} does not support LoRA yet.") ValueError: Qwen3ASRForConditionalGeneration does not support LoRA yet. ``` It would be great to get LoRA support for `Qwen3ASRForConditionalGeneration` in `vllm/model_executor/models/` (similar to how other conditional generation models have been wired up), so that --enable-lora works end-to-end for this architecture. ### Alternatives - ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/la...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Feature]: Add LoRA support for Qwen3ASRForConditionalGeneration good first issue;feature request ### 🚀 The feature, motivation and pitch When attempting to serve Qwen/Qwen3-ASR-0.6B with LoRA enabled using the followin...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: els have been wired up), so that --enable-lora works end-to-end for this architecture. ### Alternatives - ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched fo...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: RA support for Qwen3ASRForConditionalGeneration good first issue;feature request ### 🚀 The feature, motivation and pitch When attempting to serve Qwen/Qwen3-ASR-0.6B with LoRA enabled using the following command: ``` vl...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
