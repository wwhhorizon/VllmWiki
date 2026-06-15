# vllm-project/vllm#21109: [Bug]: RuntimeError: Failed to apply Qwen2_5_VLProcessor on data={'text': '<|image_pad|>', 'images': [<PIL.Image.Image image mode=RGB size=332x27 at 0x7FA449949720>]} with kwargs={}

| 字段 | 值 |
| --- | --- |
| Issue | [#21109](https://github.com/vllm-project/vllm/issues/21109) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;model_support |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda |
| 症状 | crash |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: RuntimeError: Failed to apply Qwen2_5_VLProcessor on data={'text': '<\|image_pad\|>', 'images': [<PIL.Image.Image image mode=RGB size=332x27 at 0x7FA449949720>]} with kwargs={}

### Issue 正文摘录

### Your current environment Ubuntu Server 22.04 LTS vllm-v0.8.5 cuda 12.2 ### 🐛 Describe the bug ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ;stale ### Your current environment Ubuntu Server 22.04 LTS vllm-v0.8.5 cuda 12.2 ### 🐛 Describe the bug ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatb...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: RuntimeError: Failed to apply Qwen2_5_VLProcessor on data={'text': '<|image_pad|>', 'images': [<PIL.Image.Image image mode=RGB size=332x27 at 0x7FA449949720>]} with kwargs={} bug;stale ### Your current environmen...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: . performance distributed_parallel;frontend_api;model_support cuda crash dtype Your current environment
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Image image mode=RGB size=332x27 at 0x7FA449949720>]} with kwargs={} bug;stale ### Your current environment Ubuntu Server 22.04 LTS vllm-v0.8.5 cuda 12.2 ### 🐛 Describe the bug ### Before submitting a new issue... - [x]...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. performance distributed_parallel;frontend_api;model_support cuda crash dtype Your cur...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
