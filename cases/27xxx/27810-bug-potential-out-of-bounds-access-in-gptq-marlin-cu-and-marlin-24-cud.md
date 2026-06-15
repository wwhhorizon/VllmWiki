# vllm-project/vllm#27810: [Bug]: Potential Out-of-Bounds Access in gptq_marlin.cu and marlin_24_cuda_kernel.cu

| 字段 | 值 |
| --- | --- |
| Issue | [#27810](https://github.com/vllm-project/vllm/issues/27810) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | quantization |
| 子分类 |  |
| Operator 关键词 | cuda;kernel;quantization |
| 症状 |  |
| 根因提示 | env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Potential Out-of-Bounds Access in gptq_marlin.cu and marlin_24_cuda_kernel.cu

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug While performing static analysis on CUDA kernels, I identified potential out-of-bounds memory accesses in the gptq_marlin_gemm and gptq_marlin_24_gemm functions. **1. gptq_marlin_gemm** https://github.com/vllm-project/vllm/blob/4464723f220a74785cd1971cf62a04e3961c2846/csrc/quantization/gptq_marlin/marlin_template.h#L779-L788 ```A[a_gl_rd_delta_i * i + a_gl_rd + a_gl_rd_delta_o * a_off]``` may access out of bounds. The shape of A: ```[batch_size * seq_len, 2560]```. For the first iteration (i.e., i=0 and a_off=0), the index is ```((blockIdx.x * 8) % 20) * 16 + threadIdx.x % 16 + (threadIdx.x / 16) * 320``` when ```thread_k_blocks = 8, thread_n_blocks=8, thread_k=128, thread_n= 128, num_thread=256, prob_k=2560, prob_n=4096, sms=80```. Example Scenario: ``` blockIdx.x: 59 threadIdx.x: 128 batch_size*seq_len: 1 ``` In this case, the computed index exceeds A.size, causing an out-of-bounds access. **2. gptq_marlin_24_gemm** https://github.com/vllm-project/vllm/blob/1994de99ea0bf8dd84257a19800f4f62526a7edf/csrc/quantization/marlin/sparse/marlin_24_cuda_kernel.cu#L379-L388 ```A[a_gl_rd_delta_i * i + a_gl_rd + a_gl_rd_delta_o * a_off]```...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Potential Out-of-Bounds Access in gptq_marlin.cu and marlin_24_cuda_kernel.cu bug;stale ### Your current environment ### 🐛 Describe the bug While performing static analysis on CUDA kernels, I identified potential...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: y asked questions. performance quantization cuda;kernel;quantization env_dependency;shape Your current environment
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: com/vllm-project/vllm/blob/4464723f220a74785cd1971cf62a04e3961c2846/csrc/quantization/gptq_marlin/marlin_template.h#L779-L788 ```A[a_gl_rd_delta_i * i + a_gl_rd + a_gl_rd_delta_o * a_off]``` may access out of bounds. Th...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ]```. For the first iteration (i.e., i=0 and a_off=0), the index is ```((blockIdx.x * 8) % 20) * 16 + threadIdx.x % 16 + (threadIdx.x / 16) * 320``` when ```thread_k_blocks = 8, thread_n_blocks=8, thread_k=128, thread_n...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: I identified potential out-of-bounds memory accesses in the gptq_marlin_gemm and gptq_marlin_24_gemm functions. **1. gptq_marlin_gemm** https://github.com/vllm-project/vllm/blob/4464723f220a74785cd1971cf62a04e3961c2846/...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
