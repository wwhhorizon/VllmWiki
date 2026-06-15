# vllm-project/vllm#40913: [Bug]: Timeout when using LoRA with Nemotron Super (Nano is OK)

| 字段 | 值 |
| --- | --- |
| Issue | [#40913](https://github.com/vllm-project/vllm/issues/40913) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;scheduler_memory |
| 子分类 | cold_start |
| Operator 关键词 | cache;cuda;moe;operator;quantization;triton |
| 症状 | build_error;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Timeout when using LoRA with Nemotron Super (Nano is OK)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug #### Symptom When running generation with a LoRA adapter on Nemotron-3-Super, vLLM hangs indefinitely on the first inference after the LoRA is requested. After ~60 seconds, vLLM begins repeatedly logging: ``` No available shared memory broadcast block found in 60 seconds. This typically happens when some processes are hanging or doing some time-consuming work (e.g. compilation, weight/kv cache quantization). ``` vLLM eventually fails (timeout). Example with `NVIDIA-Nemotron-3-Super-120B-A12B-BF16`, TP4, B200, vLLM v0.20.0: ``` Initializing a V1 LLM engine (v0.20.0) with config ... ... (EngineCore pid=2619634) INFO 04-29 02:27:52 [shm_broadcast.py:681] No available shared memory broadcast block found in 60 seconds. This typically happens when some processes are hanging or doing some time-consuming work (e.g. compilation, weight/kv cache quantization). (EngineCore pid=2619634) INFO 04-29 02:28:52 [shm_broadcast.py:681] No available shared memory broadcast block found in 60 seconds. This typically happens when some processes are hanging or doing some time-consuming work (e.g. compilation, weight/kv cache quantization). (EngineCore p...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: P4, B200, vLLM v0.20.0: ``` Initializing a V1 LLM engine (v0.20.0) with config ... ... (EngineCore pid=2619634) INFO 04-29 02:27:52 [shm_broadcast.py:681] No available shared memory broadcast block found in 60 seconds....
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: layers) - hangs. Note: all tests done on **B200** GPUs. #### Affected versions The issue does not appear in vLLM v0.18.1, first seen with vLLM v0.19.0. And still exists in vLLM main - last tested commit is `fe57be780967...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ing or doing some time-consuming work (e.g. compilation, weight/kv cache quantization). ``` vLLM eventually fails (timeout). Example with `NVIDIA-Nemotron-3-Super-120B-A12B-BF16`, TP4, B200, vLLM v0.20.0: ``` Initializi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: (timeout). Example with `NVIDIA-Nemotron-3-Super-120B-A12B-BF16`, TP4, B200, vLLM v0.20.0: ``` Initializing a V1 LLM engine (v0.20.0) with config ... ... (EngineCore pid=2619634) INFO 04-29 02:27:52 [shm_broadcast.py:68...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: `NemotronHForCausalLM` model): * Nemotron-3-Nano-30B-A3B-BF16 (n_routed_experts=128, 23 MoE layers) - works. * Nemotron-3-Super-120B-A12B-BF16 (n_routed_experts=512, 40 MoE layers) - hangs. Note: all tests done on **B20...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
