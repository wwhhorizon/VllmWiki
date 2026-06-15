# vllm-project/vllm#31628: [Bug][ModelOpt]: Llama4 DP/EP FlashInfer Cutlass Is Broken

| 字段 | 值 |
| --- | --- |
| Issue | [#31628](https://github.com/vllm-project/vllm/issues/31628) |
| 状态 | closed |
| 标签 | bug;stale;nvidia |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;gemm_linear;model_support;moe;quantization |
| 子分类 | throughput |
| Operator 关键词 | cuda;fp8;moe |
| 症状 | slowdown |
| 根因提示 | dtype;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug][ModelOpt]: Llama4 DP/EP FlashInfer Cutlass Is Broken

### Issue 正文摘录

### Your current environment H100, B200, 6ef770df7c3f0d135c2f3a594c461949113aae91 ### 🐛 Describe the bug ```just MODEL_TENSOR := "nvidia/Llama-4-Scout-17B-16E-Instruct-FP8" GPUS := "2" PORT := "8000" launch_cutlass_tensor: VLLM_USE_DEEP_GEMM=0 VLLM_USE_FLASHINFER_MOE_FP8=1 VLLM_FLASHINFER_MOE_BACKEND=throughput vllm serve {{MODEL_TENSOR}} -dp {{GPUS}} --enable-expert-parallel --port {{PORT}} --max-model-len 8192 ``` I see: ```bash (EngineCore_DP0 pid=2814418) File "/home/robertgshaw2-redhat/vllm/vllm/model_executor/models/llama4.py", line 506, in load_moe_expert_weights (EngineCore_DP0 pid=2814418) new_loaded_weight = new_loaded_weight[local_expert_indices] (EngineCore_DP0 pid=2814418) ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^ (EngineCore_DP0 pid=2814418) NotImplementedError: "index_cpu" not implemented for 'Float8_e4m3fn' ``` Manually setting the loaded_weights to cuda, I see: ```bash (EngineCore_DP1 pid=2810090) File "/home/robertgshaw2-redhat/vllm/vllm/model_executor/layers/fused_moe/modular_kernel.py", line 1268, in forward (EngineCore_DP1 pid=2810090) a1q, a1q_scale, expert_tokens_meta, topk_ids, topk_weights = self._prepare( (EngineCore_DP1 pid=2810090) ^^^^^^^^^^^^^^ (EngineC...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: the bug ```just MODEL_TENSOR := "nvidia/Llama-4-Scout-17B-16E-Instruct-FP8" GPUS := "2" PORT := "8000" launch_cutlass_tensor: VLLM_USE_DEEP_GEMM=0 VLLM_USE_FLASHINFER_MOE_FP8=1 VLLM_FLASHINFER_MOE_BACKEND=throughput vll...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: shInfer Cutlass Is Broken bug;stale;nvidia ### Your current environment H100, B200, 6ef770df7c3f0d135c2f3a594c461949113aae91 ### 🐛 Describe the bug ```just MODEL_TENSOR := "nvidia/Llama-4-Scout-17B-16E-Instruct-FP8" GPU...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 4: -FP8" GPUS := "2" PORT := "8000" launch_cutlass_tensor: VLLM_USE_DEEP_GEMM=0 VLLM_USE_FLASHINFER_MOE_FP8=1 VLLM_FLASHINFER_MOE_BACKEND=throughput vllm serve {{MODEL_TENSOR}} -dp {{GPUS}} --enable-expert-parallel --port...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Bug][ModelOpt]: Llama4 DP/EP FlashInfer Cutlass Is Broken bug;stale;nvidia ### Your current environment H100, B200, 6ef770df7c3f0d135c2f3a594c461949113aae91 ### 🐛 Describe the bug ```just MODEL_TENSOR := "nvidia/Llama-...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug][ModelOpt]: Llama4 DP/EP FlashInfer Cutlass Is Broken bug;stale;nvidia ### Your current environment H100, B200, 6ef770df7c3f0d135c2f3a594c461949113aae91 ### 🐛 Describe the bug ```just MODEL_TENSOR := "nvidia/Llama-...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
