# vllm-project/vllm#3247: Error when using nsys profile 

| 字段 | 值 |
| --- | --- |
| Issue | [#3247](https://github.com/vllm-project/vllm/issues/3247) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | memory |
| Operator 关键词 | cuda;quantization |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Error when using nsys profile 

### Issue 正文摘录

I want to use nsight system to profile vllm. Here is my code: Seems by default, Ray is not used, is that right? But my nsys profile still fails. Why is that? Thank you. ```python def initialize_engine() -> LLMEngine: """Initialize the LLMEngine.""" # max_loras: controls the number of LoRAs that can be used in the same # batch. Larger numbers will cause higher memory usage, as each LoRA # slot requires its own preallocated tensor. # max_lora_rank: controls the maximum supported rank of all LoRAs. Larger # numbers will cause higher memory usage. If you know that all LoRAs will # use the same rank, it is recommended to set this as low as possible. # max_cpu_loras: controls the size of the CPU LoRA cache. engine_args = EngineArgs(model="/data/models/vicuna-7b-v1.5/", enable_lora=True, max_loras=1, max_lora_rank=8, max_cpu_loras=2, max_num_seqs=256, enforce_eager=True ) return LLMEngine.from_engine_args(engine_args) ``` ``` root@bms-airtrunk-d-g18v3-app-10-192-82-3:/data/vllm# nsys nvprof python s-lora.py WARNING: python and any of its children processes will be profiled. INFO 03-07 03:26:52 llm_engine.py:87] Initializing an LLM engine with config: model='/data/models/vicuna-7b-v1.5/',...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: Summary page after opening the report file in GUI. **** ``` performance ci_build;distributed_parallel;frontend_api;model_support;quantization cuda;quantization build_error dtype;env_dependency;shape I want to use nsight...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: =auto, revision= None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=4096, download_dir=None, load_format=auto, tensor_parallel_size=1, disable_custom_all_reduce=False, quantization=...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: tch. Larger numbers will cause higher memory usage, as each LoRA # slot requires its own preallocated tensor. # max_lora_rank: controls the maximum supported rank of all LoRAs. Larger # numbers will cause higher memory...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: s: controls the size of the CPU LoRA cache. engine_args = EngineArgs(model="/data/models/vicuna-7b-v1.5/", enable_lora=True, max_loras=1, max_lora_rank=8, max_cpu_loras=2,
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: antization=None, enfo rce_eager=True, kv_cache_dtype=auto, device_config=cuda, seed=0) INFO 03-07 03:27:11 llm_engine.py:357] # GPU blocks: 1016, # CPU blocks: 512 Fetching 9 files: 100%|██████████| 9/9 [00:00 \nstd::ex...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
