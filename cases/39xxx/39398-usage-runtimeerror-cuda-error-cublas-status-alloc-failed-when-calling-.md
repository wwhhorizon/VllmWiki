# vllm-project/vllm#39398: [Usage]: RuntimeError: CUDA error: CUBLAS_STATUS_ALLOC_FAILED when calling `cublasCreate(handle)`

| 字段 | 值 |
| --- | --- |
| Issue | [#39398](https://github.com/vllm-project/vllm/issues/39398) |
| 状态 | open |
| 标签 | usage |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | model_support;quantization |
| 子分类 | runtime_err |
| Operator 关键词 | cuda;quantization |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: RuntimeError: CUDA error: CUBLAS_STATUS_ALLOC_FAILED when calling `cublasCreate(handle)`

### Issue 正文摘录

### Your current environment Colab t4 gpu ### How would you like to use vllm im trying to serve a quantized 4 bit model on a T4 gpu, i get this error ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Usage]: RuntimeError: CUDA error: CUBLAS_STATUS_ALLOC_FAILED when calling `cublasCreate(handle)` usage ### Your current environment Colab t4 gpu ### How would you like to use vllm im trying to serve a quantized 4 bit m...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: Colab t4 gpu ### How would you like to use vllm im trying to serve a quantized 4 bit model on a T4 gpu, i get this error ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ### How would you like to use vllm im trying to serve a quantized 4 bit model on a T4 gpu, i get this error ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the ch...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development model_support;quantization cuda;quantization Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
