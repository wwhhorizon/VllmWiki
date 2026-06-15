# vllm-project/vllm#8010: [Doc]: nvidia ammo has been renamed

| 字段 | 值 |
| --- | --- |
| Issue | [#8010](https://github.com/vllm-project/vllm/issues/8010) |
| 状态 | closed |
| 标签 | documentation;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: nvidia ammo has been renamed

### Issue 正文摘录

### 📚 The doc issue https://docs.vllm.ai/en/latest/quantization/fp8_e4m3_kvcache.html is outdated wrt nvidia ammo From: https://github.com/NVIDIA/TensorRT-LLM/issues/1368#issuecomment-2118356237 > The AMMO toolkit has been renamed to "TensorRT model optimizer" and the documentation is available at https://nvidia.github.io/TensorRT-Model-Optimizer/ . Examples related with Model Optimizer is available at https://github.com/NVIDIA/TensorRT-Model-Optimizer?tab=readme-ov-file I'm following the breadcrumbs - will update if I can figure out the up-to-date instructions. ### Suggest a potential alternative/fix _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: documentation;stale ### 📚 The doc issue https://docs.vllm.ai/en/latest/quantization/fp8_e4m3_kvcache.html is outdated wrt nvidia ammo From: https://github.com/NVIDIA/TensorRT-LLM/issues/1368#issuecomment-2118356237 > Th...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ssuecomment-2118356237 > The AMMO toolkit has been renamed to "TensorRT model optimizer" and the documentation is available at https://nvidia.github.io/TensorRT-Model-Optimizer/ . Examples related with Model Optimizer i...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Doc]: nvidia ammo has been renamed documentation;stale ### 📚 The doc issue https://docs.vllm.ai/en/latest/quantization/fp8_e4m3_kvcache.html is outdated wrt nvidia ammo From: https://github.com/NVIDIA/TensorRT-LLM/issu...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: named documentation;stale ### 📚 The doc issue https://docs.vllm.ai/en/latest/quantization/fp8_e4m3_kvcache.html is outdated wrt nvidia ammo From: https://github.com/NVIDIA/TensorRT-LLM/issues/1368#issuecomment-211835623...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
