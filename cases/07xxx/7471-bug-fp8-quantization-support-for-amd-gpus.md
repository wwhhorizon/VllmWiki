# vllm-project/vllm#7471: [Bug]: FP8 Quantization support for AMD GPUs

| 字段 | 值 |
| --- | --- |
| Issue | [#7471](https://github.com/vllm-project/vllm/issues/7471) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | hardware_porting;quantization |
| 子分类 |  |
| Operator 关键词 | fp8;quantization |
| 症状 |  |
| 根因提示 | dtype |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: FP8 Quantization support for AMD GPUs

### Issue 正文摘录

### Your current environment I am trying out FP8 support on AMD GPUs (MI250, MI300) and the vLLM library does not seem to support AMD GPUs yet for FP8 quantization. Is there any timeline for when this will be available? ### 🐛 Describe the bug Error: "fp8 quantization is currently not supported in ROCm" while running vLLM with quantization=fp8 on AMD GPUs. I am using MI250 AMD GPUs to run the vLLM inference service.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: FP8 Quantization support for AMD GPUs bug;stale ### Your current environment I am trying out FP8 support on AMD GPUs (MI250, MI300) and the vLLM library does not seem to support AMD GPUs yet for FP8 quantization....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: our current environment I am trying out FP8 support on AMD GPUs (MI250, MI300) and the vLLM library does not seem to support AMD GPUs yet for FP8 quantization. Is there any timeline for when this will be available? ###...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: FP8 Quantization support for AMD GPUs bug;stale ### Your current environment I am trying out FP8 support on AMD GPUs (MI250, MI300) and the vLLM library does not seem to support AMD GPUs yet for FP8 quantization....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
