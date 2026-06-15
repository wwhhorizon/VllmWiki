# vllm-project/vllm#39664: [Bug]: Triton kernel import fails with triton 3.6.0 (`module 'triton.language' has no attribute 'constexpr_function'`), training falls back and becomes extremely slow

| 字段 | 值 |
| --- | --- |
| Issue | [#39664](https://github.com/vllm-project/vllm/issues/39664) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Triton kernel import fails with triton 3.6.0 (`module 'triton.language' has no attribute 'constexpr_function'`), training falls back and becomes extremely slow

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When running verl training with vLLM, training starts successfully, but vLLM repeatedly logs: `Failed to import Triton kernels. Please make sure your triton version is compatible. Error: module 'triton.language' has no attribute 'constexpr_function'` The job does not crash, but appears to fall back to a much slower path. In my case, a single training step takes about 4 hours, which is clearly abnormal. From local inspection, the issue seems related to vLLM Triton kernels, including: - `vllm/third_party/triton_kernels/target_info.py` - `vllm/model_executor/layers/fused_moe/gpt_oss_triton_kernels_moe.py` ### Environment 1. Set up verl training environment 2. Use: - torch 2.10.0+cu130 - triton 3.6.0 - vllm 0.19.0+cu130 3. Start training 4. Observe repeated Triton kernel import errors and extremely slow step time ### Logs ```text Failed to import Triton kernels. Please make sure your triton version is compatible. Error: module 'triton.language' has no attribute 'constexpr_function' ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Bug]: Triton kernel import fails with triton 3.6.0 (`module 'triton.language' has no attribute 'constexpr_function'`), training falls back and becomes extremely slow bug ### Your current environment ### 🐛 Describe the...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Bug]: Triton kernel import fails with triton 3.6.0 (`module 'triton.language' has no attribute 'constexpr_function'`), training falls back and becomes extremely slow bug ### Your current environment ### 🐛 Describe the...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: on' ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: s, including: - `vllm/third_party/triton_kernels/target_info.py` - `vllm/model_executor/layers/fused_moe/gpt_oss_triton_kernels_moe.py` ### Environment 1. Set up verl training environment 2. Use: - torch 2.10.0+cu130 -...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: party/triton_kernels/target_info.py` - `vllm/model_executor/layers/fused_moe/gpt_oss_triton_kernels_moe.py` ### Environment 1. Set up verl training environment 2. Use: - torch 2.10.0+cu130 - triton 3.6.0 - vllm 0.19.0+c...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
