# vllm-project/vllm#31273: [Bug]:OOM during weight loading on H20 (141GB) in v0.13.0, but works in v0.12.0 (Qwen2.5-72B FP8)

| 字段 | 值 |
| --- | --- |
| Issue | [#31273](https://github.com/vllm-project/vllm/issues/31273) |
| 状态 | open |
| 标签 | bug;unstale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | attention;cuda;fp8;operator;quantization;triton |
| 症状 | build_error;crash;oom |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:OOM during weight loading on H20 (141GB) in v0.13.0, but works in v0.12.0 (Qwen2.5-72B FP8)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug After upgrading from vLLM v0.12.0 to v0.13.0, I encountered a torch.OutOfMemoryError during the model weight loading phase. The same configuration and environment work perfectly fine in v0.12.0. The error occurs when loading Qwen2.5-72B-Instruct with FP8 quantization on an H20 (141GB) GPU. It seems the memory management or the weight loading logic in the new version is consuming more memory than before, causing the OOM. command ``` vllm serve qwen-qwen2.5-72b-instruct \ --port 8080 \ --served-model-name model \ --max-num-seqs 64 \ --enable-lora \ --enable-auto-tool-choice \ --tool-call-parser hermes \ --enable-prompt-tokens-details \ --quantization fp8 ``` logs ``` (EngineCore_DP0 pid=556790) INFO 12-24 08:50:24 [parallel_state.py:1411] rank 0 in world size 1 is assigned as DP rank 0, PP rank 0, PCP rank 0, TP rank 0, EP rank 0 (EngineCore_DP0 pid=556790) INFO 12-24 08:50:26 [gpu_model_runner.py:3562] Starting to load model qwen-qwen2.5-72b-instruct... (EngineCore_DP0 pid=556790) INFO 12-24 08:50:27 [cuda.py:351] Using FLASH_ATTN attention backend out of potential backends: ('FLASH_ATTN', 'FLASHINFER', 'TRITON_ATTN', 'FLEX_ATTENT...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: pid=556790) INFO 12-24 08:50:27 [cuda.py:351] Using FLASH_ATTN attention backend out of potential backends: ('FLASH_ATTN', 'FLASHINFER', 'TRITON_ATTN', 'FLEX_ATTENTION') Loading safetensors checkpoint shards: 0% Complet...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: U. It seems the memory management or the weight loading logic in the new version is consuming more memory than before, causing the OOM. command ``` vllm serve qwen-qwen2.5-72b-instruct \ --port 8080 \ --served-model-nam...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ght loading on H20 (141GB) in v0.13.0, but works in v0.12.0 (Qwen2.5-72B FP8) bug;unstale ### Your current environment ### 🐛 Describe the bug After upgrading from vLLM v0.12.0 to v0.13.0, I encountered a torch.OutOfMemo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: M during weight loading on H20 (141GB) in v0.13.0, but works in v0.12.0 (Qwen2.5-72B FP8) bug;unstale ### Your current environment ### 🐛 Describe the bug After upgrading from vLLM v0.12.0 to v0.13.0, I encountered a tor...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: wen2.5-72b-instruct... (EngineCore_DP0 pid=556790) INFO 12-24 08:50:27 [cuda.py:351] Using FLASH_ATTN attention backend out of potential backends: ('FLASH_ATTN', 'FLASHINFER', 'TRITON_ATTN', 'FLEX_ATTENTION') Loading sa...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
