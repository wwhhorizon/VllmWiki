# vllm-project/vllm#28626: [Bug]:Qwen3-VL-32B-AWQ model memory usage: 8k context limit with 40GB VRAM?

| 字段 | 值 |
| --- | --- |
| Issue | [#28626](https://github.com/vllm-project/vllm/issues/28626) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]:Qwen3-VL-32B-AWQ model memory usage: 8k context limit with 40GB VRAM?

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Running models on the latest stable vLLM release: https://huggingface.co/QuantTrio/Qwen3-VL-32B-Instruct-AWQ The model size is 20GB, and my GPU has 40GB VRAM total. Using parameter: --gpu-memory-utilization 0.9 Why am I only getting around 8k max context length? Do VL models really hog that much VRAM? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]:Qwen3-VL-32B-AWQ model memory usage: 8k context limit with 40GB VRAM? bug;stale ### Your current environment ### 🐛 Describe the bug Running models on the latest stable vLLM release: https://huggingface.co/QuantTri...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: Running models on the latest stable vLLM release: https://huggingface.co/QuantTrio/Qwen3-VL-32B-Instruct-AWQ The model size is 20GB, and my GPU has 40GB VRAM total. Using parameter: --gpu-memory-utilization 0.9 Why am I...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: AM? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: wen3-VL-32B-AWQ model memory usage: 8k context limit with 40GB VRAM? bug;stale ### Your current environment ### 🐛 Describe the bug Running models on the latest stable vLLM release: https://huggingface.co/QuantTrio/Qwen3...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: current environment ### 🐛 Describe the bug Running models on the latest stable vLLM release: https://huggingface.co/QuantTrio/Qwen3-VL-32B-Instruct-AWQ The model size is 20GB, and my GPU has 40GB VRAM total. Using param...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
