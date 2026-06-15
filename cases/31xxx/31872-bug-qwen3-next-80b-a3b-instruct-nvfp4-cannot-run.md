# vllm-project/vllm#31872: [Bug]: Qwen3-Next-80B-A3B-Instruct-NVFP4 cannot run

| 字段 | 值 |
| --- | --- |
| Issue | [#31872](https://github.com/vllm-project/vllm/issues/31872) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;gemm;moe;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3-Next-80B-A3B-Instruct-NVFP4 cannot run

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug (EngineCore_DP0 pid=273616) INFO 01-07 13:43:10 [parallel_state.py:1203] world_size=1 rank=0 local_rank=0 distributed_init_method=tcp://192.168.50.83:44989 backend=nccl (EngineCore_DP0 pid=273616) INFO 01-07 13:43:10 [parallel_state.py:1411] rank 0 in world size 1 is assigned as DP rank 0, PP rank 0, PCP rank 0, TP rank 0, EP rank 0 (EngineCore_DP0 pid=273616) INFO 01-07 13:43:10 [gpu_model_runner.py:3551] Starting to load model /home/oliver/.xinference/cache/v2/Qwen3-Next-Instruct-fp4-80b-fp4... (EngineCore_DP0 pid=273616) INFO 01-07 13:43:10 [modelopt.py:916] Using flashinfer-cutlass for NVFP4 GEMM (EngineCore_DP0 pid=273616) INFO 01-07 13:43:10 [layer.py:372] Enabled separate cuda stream for MoE shared_experts (EngineCore_DP0 pid=273616) INFO 01-07 13:43:10 [modelopt.py:1132] Using Cutlass for ModelOptNvFp4FusedMoE. (EngineCore_DP0 pid=273616) INFO 01-07 13:43:10 [cuda.py:412] Using FLASH_ATTN attention backend out of potential backends: ['FLASH_ATTN', 'FLASHINFER', 'TRITON_ATTN', 'FLEX_ATTENTION'] Loading safetensors checkpoint shards: 0% Completed | 0/10 [00:00<?, ?it/s] (EngineCore_DP0 pid=273616) ERROR 01-07 13:43:31 [core...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: [Bug]: Qwen3-Next-80B-A3B-Instruct-NVFP4 cannot run bug;stale ### Your current environment ### 🐛 Describe the bug (EngineCore_DP0 pid=273616) INFO 01-07 13:43:10 [parallel_state.py:1203] world_size=1 rank=0 local_rank=0...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: =1 rank=0 local_rank=0 distributed_init_method=tcp://192.168.50.83:44989 backend=nccl (EngineCore_DP0 pid=273616) INFO 01-07 13:43:10 [parallel_state.py:1411] rank 0 in world size 1 is assigned as DP rank 0, PP rank 0,...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. correctness attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding attent...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Qwen3-Next-80B-A3B-Instruct-NVFP4 cannot run bug;stale ### Your current environment ### 🐛 Describe the bug (EngineCore_DP0 pid=273616) INFO 01-07 13:43:10 [parallel_state.py:1203] world_size=1 rank=0 local_rank=0...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: INFO 01-07 13:43:10 [modelopt.py:916] Using flashinfer-cutlass for NVFP4 GEMM (EngineCore_DP0 pid=273616) INFO 01-07 13:43:10 [layer.py:372] Enabled separate cuda stream for MoE shared_experts (EngineCore_DP0 pid=273616...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
