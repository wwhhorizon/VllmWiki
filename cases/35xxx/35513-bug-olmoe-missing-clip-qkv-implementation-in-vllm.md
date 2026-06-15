# vllm-project/vllm#35513: [Bug]: OLMoE missing clip_qkv implementation in vLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#35513](https://github.com/vllm-project/vllm/issues/35513) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: OLMoE missing clip_qkv implementation in vLLM

### Issue 正文摘录

### Your current environment None ### 🐛 Describe the bug In vllm/olmoe.py, the Q/K/V clipping (clip_qkv) is completely missing while [config](https://huggingface.co/allenai/OLMoE-1B-7B-0924-Instruct/blob/main/config.json) still includes the `clip_qkv` option. By contrast, vllm/olmo.py already implements clip_qkv: ``` if self.clip_qkv is not None: qkv.clamp_(min=-self.clip_qkv, max=self.clip_qkv) ``` Expected behavior vllm/olmoe.py should implement clip_qkv in the same way as vllm/olmo.py: ``` if self.clip_qkv is not None: query_states.clamp_(min=-self.clip_qkv, max=self.clip_qkv) key_states.clamp_(min=-self.clip_qkv, max=self.clip_qkv) value_states.clamp_(min=-self.clip_qkv, max=self.clip_qkv) ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: llm/olmoe.py, the Q/K/V clipping (clip_qkv) is completely missing while [config](https://huggingface.co/allenai/OLMoE-1B-7B-0924-Instruct/blob/main/config.json) still includes the `clip_qkv` option. By contrast, vllm/ol...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Bug]: OLMoE missing clip_qkv implementation in vLLM bug;stale ### Your current environment None ### 🐛 Describe the bug In vllm/olmoe.py, the Q/K/V clipping (clip_qkv) is completely missing while [config](https://huggin...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: OLMoE missing clip_qkv implementation in vLLM bug;stale ### Your current environment None ### 🐛 Describe the bug In vllm/olmoe.py, the Q/K/V clipping (clip_qkv) is completely missing while [config](https://huggin...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
