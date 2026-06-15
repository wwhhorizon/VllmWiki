# vllm-project/vllm#27655: [Bug]: 'FlashInferAllToAllManager' object has no attribute 'prepare_workspace'

| 字段 | 值 |
| --- | --- |
| Issue | [#27655](https://github.com/vllm-project/vllm/issues/27655) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;moe;operator;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: 'FlashInferAllToAllManager' object has no attribute 'prepare_workspace'

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug vLLM throws an error when using the `flashinfer_all2allv` all2all backend: `AttributeError: 'FlashInferAllToAllManager' object has no attribute 'prepare_workspace'` And my output: ``` [1;36m(EngineCore_DP7 pid=3825627)[0;0m File "/root/workspace/vllm_nvfp4/vllm/model_executor/layers/fused_moe/flashinfer_cutlass_prepare_finalize.py", line 238, in flashinfer_alltoall_dispatch [1;36m(EngineCore_DP7 pid=3825627)[0;0m all2all_manager.prepare_workspace, [1;36m(EngineCore_DP7 pid=3825627)[0;0m ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ [1;36m(EngineCore_DP7 pid=3825627)[0;0m AttributeError: 'FlashInferAllToAllManager' object has no attribute 'prepare_workspace' ``` [server_dbg.log](https://github.com/user-attachments/files/23188258/server_dbg.log) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 现有链接修复摘要

#27862 [BugFix] Fixed 'FlashInferAllToAllManager' object has no attribute 'prepare_workspace'

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: [Bug]: 'FlashInferAllToAllManager' object has no attribute 'prepare_workspace' bug ### Your current environment ### 🐛 Describe the bug vLLM throws an error when using the `flashinfer_all2allv` all2all backend: `Attribut...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: ` [1;36m(EngineCore_DP7 pid=3825627)[0;0m File "/root/workspace/vllm_nvfp4/vllm/model_executor/layers/fused_moe/flashinfer_cutlass_prepare_finalize.py", line 238, in flashinfer_alltoall_dispatch [1;36m(EngineCore_DP7...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: equently asked questions. correctness activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;scheduler_memory;speculative_decoding cuda;...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: og) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: 0;0m File "/root/workspace/vllm_nvfp4/vllm/model_executor/layers/fused_moe/flashinfer_cutlass_prepare_finalize.py", line 238, in flashinfer_alltoall_dispatch [1;36m(EngineCore_DP7 pid=3825627)[0;0m all2all_manager.pre...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#27862](https://github.com/vllm-project/vllm/pull/27862) | closes_keyword | 0.95 | [BugFix] Fixed 'FlashInferAllToAllManager' object has no attribute 'prepare_workspace' | fixes the bug reported in issue #27655 . There are two main changes: 1. Fix AttributeError with `flashinfer_all2allv` backend: When using the `flashinfer_all2allv` backend, an Att |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
