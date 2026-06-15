# vllm-project/vllm#7781: [Bug]: Can't load vision model `microsoft/Phi-3.5-vision-instruct`

| 字段 | 值 |
| --- | --- |
| Issue | [#7781](https://github.com/vllm-project/vllm/issues/7781) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;race_condition |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Can't load vision model `microsoft/Phi-3.5-vision-instruct`

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug # Reproduction ```python from vllm import LLM llm = LLM( model="microsoft/Phi-3.5-vision-instruct", trust_remote_code=True ) ``` # Bug ``` ValueError: Attempted to assign 49 x 781 = 38269 image tokens to 129997 placeholders ``` # Full Traceback ``` A new version of the following files was downloaded from https://huggingface.co/microsoft/Phi-3.5-vision-instruct: - processing_phi3_v.py . Make sure to double-check they do not contain any added malicious code. To avoid downloading new versions of the code file, you can pin a revision. /usr/local/lib/python3.10/dist-packages/transformers/models/auto/image_processing_auto.py:513: FutureWarning: The image_processor_class argument is deprecated and will be removed in v4.42. Please use `slow_image_processor_class`, or `fast_image_processor_class` instead warnings.warn( --------------------------------------------------------------------------- ValueError Traceback (most recent call last) Cell In[16], line 2 1 if 'LLM_LOADED' not in globals(): ----> 2 llm = LLM( 3 model="microsoft/Phi-3.5-vision-instruct", 4 trust_remote_code=True 5 ) 6 LLM_LOADED = True File /usr/local/lib/python3.10/dist...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: vironment ### 🐛 Describe the bug # Reproduction ```python from vllm import LLM llm = LLM( model="microsoft/Phi-3.5-vision-instruct", trust_remote_code=True ) ``` # Bug ``` ValueError: Attempted to assign 49 x 781 = 3826...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Can't load vision model `microsoft/Phi-3.5-vision-instruct` bug ### Your current environment ### 🐛 Describe the bug # Reproduction ```python from vllm import LLM llm = LLM( model="microsoft/Phi-3.5-vision-instruc...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: worker(s). 357 358 The workers will determine the number of blocks in both the GPU cache 359 and the swap CPU cache. 360 """ 361 num_gpu_blocks, num_cpu_blocks = ( --> 362 self.model_executor.determine_num_available_blo...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: 159 engine_args, usage_context=UsageContext.LLM_CLASS) 160 self.request_counter = Counter() File /usr/local/lib/python3.10/dist-packages/vllm/engine/llm_engine.py:445, in LLMEngine.from_engine_args(cls, engine_args, usa...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: izer_mode, skip_tokenizer_init, trust_remote_code, tensor_parallel_size, dtype, quantization, revision, tokenizer_revision, seed, gpu_memory_utilization, swap_space, cpu_offload_gb, enforce_eager, max_context_len_to_cap...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
