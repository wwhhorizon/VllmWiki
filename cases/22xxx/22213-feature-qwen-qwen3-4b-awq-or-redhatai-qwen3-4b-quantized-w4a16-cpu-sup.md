# vllm-project/vllm#22213: [Feature]: Qwen/Qwen3-4B-AWQ or RedHatAI/Qwen3-4B-quantized.w4a16 CPU support

| 字段 | 值 |
| --- | --- |
| Issue | [#22213](https://github.com/vllm-project/vllm/issues/22213) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Qwen/Qwen3-4B-AWQ or RedHatAI/Qwen3-4B-quantized.w4a16 CPU support

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Testing things with small models on CPU is a nice to have, and then switch to GPU, possibly with bigger models, when things are ready, etc. Also CPUs and regular RAM are getting faster each day so it's tarting to not be so crazy to just use them for some things. ### Alternatives Don't use AWQ or use another inference engine. ### Additional context Tested on v0.10.0 without AVX512 [Qwen3-4B-AWQ.txt](https://github.com/user-attachments/files/21583977/Qwen3-4B-AWQ.txt) [Qwen3-4B-quantized.w4a16.txt](https://github.com/user-attachments/files/21583976/Qwen3-4B-quantized.w4a16.txt) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: quest;stale ### 🚀 The feature, motivation and pitch Testing things with small models on CPU is a nice to have, and then switch to GPU, possibly with bigger models, when things are ready, etc. Also CPUs and regular RAM a...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Feature]: Qwen/Qwen3-4B-AWQ or RedHatAI/Qwen3-4B-quantized.w4a16 CPU support feature request;stale ### 🚀 The feature, motivation and pitch Testing things with small models on CPU is a nice to have, and then switch to G...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: en/Qwen3-4B-AWQ or RedHatAI/Qwen3-4B-quantized.w4a16 CPU support feature request;stale ### 🚀 The feature, motivation and pitch Testing things with small models on CPU is a nice to have, and then switch to GPU, possibly...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [Feature]: Qwen/Qwen3-4B-AWQ or RedHatAI/Qwen3-4B-quantized.w4a16 CPU support feature request;stale ### 🚀 The feature, motivation and pitch Testing things with small models on CPU is a nice to have, and then switch to G...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: U support feature request;stale ### 🚀 The feature, motivation and pitch Testing things with small models on CPU is a nice to have, and then switch to GPU, possibly with bigger models, when things are ready, etc. Also CP...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
