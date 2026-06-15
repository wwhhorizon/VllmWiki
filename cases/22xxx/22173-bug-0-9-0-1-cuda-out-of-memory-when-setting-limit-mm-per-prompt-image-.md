# vllm-project/vllm#22173: [Bug]: 0.9.0.1:CUDA out of memory when setting limit_mm_per_prompt={"image":10,"video":1} with Qwen2.5-VL-72B-GPTQ-Int4

| 字段 | 值 |
| --- | --- |
| Issue | [#22173](https://github.com/vllm-project/vllm/issues/22173) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;moe;multimodal_vlm;quantization;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;fp8;operator;quantization |
| 症状 | crash;oom;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: 0.9.0.1:CUDA out of memory when setting limit_mm_per_prompt={"image":10,"video":1} with Qwen2.5-VL-72B-GPTQ-Int4

### Issue 正文摘录

### 🐛 Describe the bug - vLLM版本: 0.9.0.1 - 硬件配置: 4x NVIDIA V100 32GB llm = LLM( model=MODEL_PATH, tokenizer=MODEL_PATH, limit_mm_per_prompt={"image": 10, "video": 1}, dtype="float16", gpu_memory_utilization=0.9, quantization="gptq", # awq, gptq tensor_parallel_size=4, max_model_len=4096*2, #4096*2 kv_cache_dtype="fp8_e5m2", # max_num_batched_tokens=8192, # 扩大序列池 # enforce_eager=True, # V100需禁用算子融合 trust_remote_code=True ) ##报错 INFO 08-04 16:53:29 [__init__.py:31] Available plugins for group vllm.general_plugins: INFO 08-04 16:53:29 [__init__.py:33] - lora_filesystem_resolver -> vllm.plugins.lora_resolvers.filesystem_resolver:register_filesystem_resolver INFO 08-04 16:53:29 [__init__.py:36] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load. WARNING 08-04 16:53:29 [config.py:3135] Casting torch.bfloat16 to torch.float16. INFO 08-04 16:53:47 [config.py:793] This model supports multiple tasks: {'generate', 'score', 'reward', 'embed', 'classify'}. Defaulting to 'generate'. WARNING 08-04 16:53:49 [config.py:907] gptq quantization is not fully optimized yet. The speed can be slower than non-quantized models. WARNING 08-04 16:53:49 [arg_utils.py...

## 现有链接修复摘要

#4096 [Frontend] Entrypoint for hosting local Kobold Lite chat interface

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: ting limit_mm_per_prompt={"image":10,"video":1} with Qwen2.5-VL-72B-GPTQ-Int4 bug;stale ### 🐛 Describe the bug - vLLM版本: 0.9.0.1 - 硬件配置: 4x NVIDIA V100 32GB llm = LLM( model=MODEL_PATH, tokenizer=MODEL_PATH, limit_mm_pe...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: t of memory when setting limit_mm_per_prompt={"image":10,"video":1} with Qwen2.5-VL-72B-GPTQ-Int4 bug;stale ### 🐛 Describe the bug - vLLM版本: 0.9.0.1 - 硬件配置: 4x NVIDIA V100 32GB llm = LLM( model=MODEL_PATH, tokenizer=MOD...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: t_mm_per_prompt={"image":10,"video":1} with Qwen2.5-VL-72B-GPTQ-Int4 bug;stale ### 🐛 Describe the bug - vLLM版本: 0.9.0.1 - 硬件配置: 4x NVIDIA V100 32GB llm = LLM( model=MODEL_PATH, tokenizer=MODEL_PATH, limit_mm_per_prompt=...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: 0.9.0.1:CUDA out of memory when setting limit_mm_per_prompt={"image":10,"video":1} with Qwen2.5-VL-72B-GPTQ-Int4 bug;stale ### 🐛 Describe the bug - vLLM版本: 0.9.0.1 - 硬件配置: 4x NVIDIA V100 32GB llm = LLM( model=MOD...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: llmWorkerProcess pid=42876) INFO 08-04 16:54:12 [cuda.py:240] Cannot use FlashAttention-2 backend for Volta and Turing GPUs. (VllmWorkerProcess pid=42876) INFO 08-04 16:54:12 [cuda.py:289] Using XFormers backend. (VllmW...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4096](https://github.com/vllm-project/vllm/pull/4096) | mentioned | 0.45 | [Frontend] Entrypoint for hosting local Kobold Lite chat interface | , gptq tensor_parallel_size=4, max_model_len=4096*2, #4096*2 kv_cache_dtype="fp8_e5m2", # max_num_batched_tokens=8192, # 扩大序列池 # enforce_eager= |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
