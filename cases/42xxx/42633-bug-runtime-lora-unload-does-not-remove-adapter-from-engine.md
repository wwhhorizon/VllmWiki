# vllm-project/vllm#42633: [Bug]:  Runtime LoRA unload does not remove adapter from engine

| 字段 | 值 |
| --- | --- |
| Issue | [#42633](https://github.com/vllm-project/vllm/issues/42633) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]:  Runtime LoRA unload does not remove adapter from engine

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## Bug Runtime LoRA unload does not fully remove the adapter from the engine. ## Description When using `/v1/load_lora_adapter`, the adapter is registered in the OpenAI serving layer and also preloaded into the engine via `add_lora`. However, `/v1/unload_lora_adapter` currently only removes the adapter from the OpenAI serving-side registry. It does not call the engine-side `remove_lora`, so the engine-side LoRA manager may still retain the adapter after the API reports that it has been unloaded. ## Expected behavior Calling `/v1/unload_lora_adapter` should remove the LoRA adapter from both: - the OpenAI serving-side registry - the engine-side LoRA manager ## Related discussion Originally noticed while looking into #42207. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 07. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
