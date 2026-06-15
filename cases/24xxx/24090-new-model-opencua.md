# vllm-project/vllm#24090: [New Model]: OpenCUA

| 字段 | 值 |
| --- | --- |
| Issue | [#24090](https://github.com/vllm-project/vllm/issues/24090) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: OpenCUA

### Issue 正文摘录

### The model to consider. https://huggingface.co/xlangai/OpenCUA-32B ### The closest model vllm already supports. They are based on the weights of Qwen2.5-VL-7B-Instruction and Qwen2.5-VL-32B-Instruction, which are already supported by vLLM. ### What's your difficulty of supporting the model you want? According to the OpenC-UA project, vLLM support is already in progress. I just wanted to ask if there is a timeline or roadmap for when this support might become available. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [New Model]: OpenCUA stale ### The model to consider. https://huggingface.co/xlangai/OpenCUA-32B ### The closest model vllm already supports. They are based on the weights of Qwen2.5-VL-7B-Instruction and Qwen2.5-VL-32B...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: le. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [New Model]: OpenCUA stale ### The model to consider. https://huggingface.co/xlangai/OpenCUA-32B ### The closest model vllm already supports. They are based on the weights of Qwen2.5-VL-7B-Instruction and Qwen2.5-VL-32B...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
