# vllm-project/vllm#35381: [Bug]: Not able to run Qwen3-8B-NVFP4 on B200

| 字段 | 值 |
| --- | --- |
| Issue | [#35381](https://github.com/vllm-project/vllm/issues/35381) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;gemm;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Not able to run Qwen3-8B-NVFP4 on B200

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Running [Qwen3-8B-NVFP4 ](https://huggingface.co/RedHatAI/Qwen3-8B-NVFP4) on B200 gives the following error when initializing the server ``` globalStrides (2,512,32768,4194304,(EngineCore_DP0 pid=514198) (Worker_TP3 pid=514212) ERROR 02-25 23:24:46 [multiproc_executor.py:863] File "/raid/yilegu/uv_venvs/vllm-v0160/lib/python3.12/site-packages/vllm/model_executor/layers/quantization/utils/nvfp4_utils.py", line 243, in apply_nvfp4_linear 0) boxDim ((EngineCore_DP0 pid=514198) (Worker_TP3 pid=514212) ERROR 02-25 23:24:46 [multiproc_executor.py:863] out = flashinfer_scaled_fp4_mm(*mm_args, backend=backend_name) 256(EngineCore_DP0 pid=514198) (Worker_TP3 pid=514212) ERROR 02-25 23:24:46 [multiproc_executor.py:863] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ,(EngineCore_DP0 pid=514198) (Worker_TP3 pid=514212) ERROR 02-25 23:24:46 [multiproc_executor.py:863] File "/raid/yilegu/uv_venvs/vllm-v0160/lib/python3.12/site-packages/vllm/utils/flashinfer.py", line 577, in flashinfer_scaled_fp4_mm 4,(EngineCore_DP0 pid=514198) (Worker_TP3 pid=514212) ERROR 02-25 23:24:46 [multiproc_executor.py:863] return flashinfer_mm_fp4( 1(Engin...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: 3 pid=514212) ERROR 02-25 23:24:46 [multiproc_executor.py:863] out = flashinfer_scaled_fp4_mm(*mm_args, backend=backend_name) 256(EngineCore_DP0 pid=514198) (Worker_TP3 pid=514212) ERROR 02-25 23:24:46 [multiproc_execut...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: le "/raid/yilegu/uv_venvs/vllm-v0160/lib/python3.12/site-packages/torch/_compile.py", line 53, in inner 1(EngineCore_DP0 pid=514198) (Worker_TP3 pid=514212) ERROR 02-25 23:24:46 [multiproc_executor.py:863] return disabl...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: Not able to run Qwen3-8B-NVFP4 on B200 bug;stale ### Your current environment ### 🐛 Describe the bug Running [Qwen3-8B-NVFP4 ](https://huggingface.co/RedHatAI/Qwen3-8B-NVFP4) on B200 gives the following error whe...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: Not able to run Qwen3-8B-NVFP4 on B200 bug;stale ### Your current environment ### 🐛 Describe the bug Running [Qwen3-8B-NVFP4 ](https://huggingface.co/RedHatAI/Qwen3-8B-NVFP4) on B200 gives the following error whe...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Not able to run Qwen3-8B-NVFP4 on B200 bug;stale ### Your current environment ### 🐛 Describe the bug Running [Qwen3-8B-NVFP4 ](https://huggingface.co/RedHatAI/Qwen3-8B-NVFP4) on B200 gives the following error whe...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
