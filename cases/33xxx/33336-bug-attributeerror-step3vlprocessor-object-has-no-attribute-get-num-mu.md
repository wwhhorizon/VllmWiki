# vllm-project/vllm#33336: [Bug]: AttributeError: 'Step3VLProcessor' object has no attribute '_get_num_multimodal_tokens'

| 字段 | 值 |
| --- | --- |
| Issue | [#33336](https://github.com/vllm-project/vllm/issues/33336) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: AttributeError: 'Step3VLProcessor' object has no attribute '_get_num_multimodal_tokens'

### Issue 正文摘录

### Your current environment **Hf link:** https://huggingface.co/stepfun-ai/Step3-VL-10B **Issues:** AttributeError: 'Step3VLProcessor' object has no attribute '_get_num_multimodal_tokens' ### 🐛 Describe the bug **Discussions:** https://huggingface.co/stepfun-ai/Step3-VL-10B/discussions/4 Same issue even nightly. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: g]: AttributeError: 'Step3VLProcessor' object has no attribute '_get_num_multimodal_tokens' bug;stale ### Your current environment **Hf link:** https://huggingface.co/stepfun-ai/Step3-VL-10B **Issues:** AttributeError:...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: _get_num_multimodal_tokens' bug;stale ### Your current environment **Hf link:** https://huggingface.co/stepfun-ai/Step3-VL-10B **Issues:** AttributeError: 'Step3VLProcessor' object has no attribute '_get_num_multimodal_...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ly. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ep3VLProcessor' object has no attribute '_get_num_multimodal_tokens' bug;stale ### Your current environment **Hf link:** https://huggingface.co/stepfun-ai/Step3-VL-10B **Issues:** AttributeError: 'Step3VLProcessor' obje...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
