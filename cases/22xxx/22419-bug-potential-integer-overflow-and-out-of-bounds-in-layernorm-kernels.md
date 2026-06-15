# vllm-project/vllm#22419: [Bug]: Potential Integer Overflow and Out-of-bounds in layernorm_kernels

| 字段 | 值 |
| --- | --- |
| Issue | [#22419](https://github.com/vllm-project/vllm/issues/22419) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;model_support |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator |
| 症状 | nan_inf |
| 根因提示 | shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Potential Integer Overflow and Out-of-bounds in layernorm_kernels

### Issue 正文摘录

### 🐛 Describe the bug I'm performing static analysis on CUDA programs and have identified potential integer overflows and out-of-bounds in layernorm_kernels.cu. https://github.com/vllm-project/vllm/blob/1dc8a70b6d4e8ba4e139f1ddb86a166694f42f21/csrc/layernorm_kernels.cu#L17-L41 While recording the parameters of operators during invoking llm.generate, I observed that the input tensor typically has the shape [batch_size*seq_len, 4096], where 4096 is the hidden_size—a common configuration in many models. In this case, input_stride is equal to hidden_size. The kernel is launched with ```dim3 grid(num_tokens)```. So max(blockIdx.x)=num_tokens-1. If ```batch_size*seq_len = 524,289``` and hidden_size = 4096, then ```blockIdx.x * input_stride``` equals 2^31, causing an integer overflow. Furthermore, the expression ```blockIdx.x * input_stride + idx``` can become negative, resulting in an out-of-bounds access in ```input[blockIdx.x * input_stride + idx]```. A similar issue exists in fused_add_rms_norm_kernel for the computation ```blockIdx.x * vec_hidden_size``` and access to ```residual_v[id]```. https://github.com/vllm-project/vllm/blob/1dc8a70b6d4e8ba4e139f1ddb86a166694f42f21/csrc/layer...

## 现有链接修复摘要

#34842 [Bugfix][Kernel] Fix integer overflow in layernorm kernel index computations

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: e hidden_size—a common configuration in many models. In this case, input_stride is equal to hidden_size. The kernel is launched with ```dim3 grid(num_tokens)```. So max(blockIdx.x)=num_tokens-1. If ```batch_size*seq_len...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: nels bug;stale ### 🐛 Describe the bug I'm performing static analysis on CUDA programs and have identified potential integer overflows and out-of-bounds in layernorm_kernels.cu. https://github.com/vllm-project/vllm/blob/...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: shape [batch_size*seq_len, 4096], where 4096 is the hidden_size—a common configuration in many models. In this case, input_stride is equal to hidden_size. The kernel is launched with ```dim3 grid(num_tokens)```. So max(...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ng them here for completeness and to ensure future safety as model sizes scale. in ```rms_norm``` and ```fused_add_rms_norm``` in layernorm_kernels.cu: ```cuda int num_tokens = input.numel() / hidden_size; ``` ```input....
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ]: Potential Integer Overflow and Out-of-bounds in layernorm_kernels bug;stale ### 🐛 Describe the bug I'm performing static analysis on CUDA programs and have identified potential integer overflows and out-of-bounds in...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#34842](https://github.com/vllm-project/vllm/pull/34842) | closes_keyword | 0.95 | [Bugfix][Kernel] Fix integer overflow in layernorm kernel index computations | Fixes #22419 <!-- markdownlint-disable --> ## Purpose ## Test Plan ## Test Result --- <details> <summary> Essential Elements of an Effective PR Description Checklist </summary |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
