# vllm-project/vllm#24782: [Bug]: Potential Integer Overflow and Out-of-bounds in awq_gemm

| 字段 | 值 |
| --- | --- |
| Issue | [#24782](https://github.com/vllm-project/vllm/issues/24782) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | quantization |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization |
| 症状 | nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Potential Integer Overflow and Out-of-bounds in awq_gemm

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I'm performing static analysis on CUDA programs and have identified potential integer overflows and out-of-bounds in awq_gemm in awq/gemm_kernesl.cu. https://github.com/vllm-project/vllm/blob/1dc8a70b6d4e8ba4e139f1ddb86a166694f42f21/csrc/quantization/awq/gemm_kernels.cu#L57-L62 While recording the parameters of operators during invoking llm.generate, I observed that _kernel.size(1) is 1536 and _in_feats.size(1) is 4096 and _in_feats.size(0) is not fixed. So, when ```_in_feats.size(0)``` is ```524,289```, ```blockIdx.x``` is ```3,145,728```, ```threadIdx.x``` is 0, and ```threadIdx.y``` is 0, ```(((int)blockIdx_y) / j_factors1 * 16 +(((int)threadIdx.y) * row_stride_warp) + ((int)threadIdx.x) / (32 / 8)) * IC``` evaluates to ```2,147,483,648```, which overflows a 32-bit signed integer. Moreover, in the following code: ```cpp half* A_ptr = A + (((int)blockIdx_y) / j_factors1 * 16 + (((int)threadIdx.y) * row_stride_warp) + ((int)threadIdx.x) / (32 / 8)) * IC + (((int)threadIdx.x) % (32 / 8)) * 8; ``` the computed offset becomes negative, leading to an out-of-bounds access on A. https://github.com/vllm-project/vllm/blob/1dc8a70b6d4e8b...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: n, there are some integer overflows when ```_in_feats.size(0)``` is sufficiently large. https://github.com/vllm-project/vllm/blob/1dc8a70b6d4e8ba4e139f1ddb86a166694f42f21/csrc/quantization/awq/gemm_kernels.cu#L503-L504...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: nvironment ### 🐛 Describe the bug I'm performing static analysis on CUDA programs and have identified potential integer overflows and out-of-bounds in awq_gemm in awq/gemm_kernesl.cu. https://github.com/vllm-project/vll...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: (0) is not fixed. So, when ```_in_feats.size(0)``` is ```524,289```, ```blockIdx.x``` is ```3,145,728```, ```threadIdx.x``` is 0, and ```threadIdx.y``` is 0, ```(((int)blockIdx_y) / j_factors1 * 16 +(((int)threadIdx.y)...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: threadIdx.y) * row_stride_warp) + ((int)threadIdx.x) / (32 / 8)) * IC``` evaluates to ```2,147,483,648```, which overflows a 32-bit signed integer. Moreover, in the following code: ```cpp half* A_ptr = A + (((int)blockI...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: com/vllm-project/vllm/blob/1dc8a70b6d4e8ba4e139f1ddb86a166694f42f21/csrc/quantization/awq/gemm_kernels.cu#L57-L62 While recording the parameters of operators during invoking llm.generate, I observed that _kernel.size(1)...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
