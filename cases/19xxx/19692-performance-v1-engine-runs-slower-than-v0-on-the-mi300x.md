# vllm-project/vllm#19692: [Performance]: V1 engine runs slower than V0 on the MI300X

| 字段 | 值 |
| --- | --- |
| Issue | [#19692](https://github.com/vllm-project/vllm/issues/19692) |
| 状态 | closed |
| 标签 | performance;rocm;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;hardware_porting |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;kernel;triton |
| 症状 | build_error;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: V1 engine runs slower than V0 on the MI300X

### Issue 正文摘录

### Proposal to improve performance I run a Llama3 8B inference benchmark on the MI300X with both V0 and V1 engines. I noticed that V1 is quite slower at decoding compared to V0. Normally, V1 is much faster than V0 on Nvidia. One thing I noticed though is that, with V1, it doesn't print the Triton autotune output of the flash attn kernel, could be related to the attn implementation with V1. ### Report of performance regression ![Image](https://github.com/user-attachments/assets/84bdebe9-ff9d-486e-b60c-79c38588aa3e) ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text ============================== PyTorch Info ============================== PyTorch version : 2.8.0.dev20250615+rocm6.4 Is debug build : False CUDA used to build PyTorch : N/A ROCM used to build PyTorch : 6.4.43482-0f2d60242 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : Could not collect CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : AMD Instinct MI300X (gfx942:sramecc+:xnack-) Nvidia driver version : Could not collect cuDNN version : Could not collect HIP run...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [Performance]: V1 engine runs slower than V0 on the MI300X performance;rocm;stale ### Proposal to improve performance I run a Llama3 8B inference benchmark on the MI300X with both V0 and V1 engines. I noticed that V1 is...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: =========== PyTorch Info ============================== PyTorch version : 2.8.0.dev20250615+rocm6.4 Is debug build : False CUDA used to build PyTorch : N/A ROCM used to build PyTorch : 6.4.43482-0f2d60242 ==============...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: 300X performance;rocm;stale ### Proposal to improve performance I run a Llama3 8B inference benchmark on the MI300X with both V0 and V1 engines. I noticed that V1 is quite slower at decoding compared to V0. Normally, V1...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: m;stale ### Proposal to improve performance I run a Llama3 8B inference benchmark on the MI300X with both V0 and V1 engines. I noticed that V1 is quite slower at decoding compared to V0. Normally, V1 is much faster than...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: dia. One thing I noticed though is that, with V1, it doesn't print the Triton autotune output of the flash attn kernel, could be related to the attn implementation with V1. ### Report of performance regression ![Image](...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
