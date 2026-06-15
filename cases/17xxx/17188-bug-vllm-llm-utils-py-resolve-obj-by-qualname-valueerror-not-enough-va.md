# vllm-project/vllm#17188: [Bug]: vllm LLM utils.py resolve_obj_by_qualname ValueError: not enough values to unpack (expected 2, got 1)

| 字段 | 值 |
| --- | --- |
| Issue | [#17188](https://github.com/vllm-project/vllm/issues/17188) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;quantization |
| 子分类 |  |
| Operator 关键词 | cache;cuda;kernel;quantization |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm LLM utils.py resolve_obj_by_qualname ValueError: not enough values to unpack (expected 2, got 1)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug # Sample code from vllm import LLM model_name = "mistralai/Pixtral-12B-Base-2409" llm = LLM(model=model_name, config_format="mistral", load_format="safetensors", tokenizer_mode="mistral", tensor_parallel_size=8, limit_mm_per_prompt={"image": 4},device='cpu',disable_async_output_proc=True) # Error message with full trace >>> llm = LLM(model=model_name, tokenizer_mode="mistral",device='cpu',disable_async_output_proc=True) INFO 04-25 15:09:27 [config.py:2832] Downcasting torch.float32 to torch.float16. INFO 04-25 15:09:27 [config.py:689] This model supports multiple tasks: {'reward', 'score', 'embed', 'classify', 'generate'}. Defaulting to 'generate'. WARNING 04-25 15:09:27 [arg_utils.py:1603] The model has a long context length (128000). This may causeOOM during the initial memory profiling phase, or result in low performance due to small KV cache size. Consider setting --max-model-len to a smaller value. INFO 04-25 15:09:27 [config.py:1747] Disabled the custom all-reduce kernel because it is not supported on current platform. INFO 04-25 15:09:27 [llm_engine.py:243] Initializing a V0 LLM engine (v0.8.4) with config: model='mistrala...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: current environment ### 🐛 Describe the bug # Sample code from vllm import LLM model_name = "mistralai/Pixtral-12B-Base-2409" llm = LLM(model=model_name, config_format="mistral", load_format="safetensors", tokenizer_mode...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: vironment ### 🐛 Describe the bug # Sample code from vllm import LLM model_name = "mistralai/Pixtral-12B-Base-2409" llm = LLM(model=model_name, config_format="mistral", load_format="safetensors", tokenizer_mode="mistral"...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: output_proc=True) INFO 04-25 15:09:27 [config.py:2832] Downcasting torch.float32 to torch.float16. INFO 04-25 15:09:27 [config.py:689] This model supports multiple tasks: {'reward', 'score', 'embed', 'classify', 'genera...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: qualname ValueError: not enough values to unpack (expected 2, got 1) bug;stale ### Your current environment ### 🐛 Describe the bug # Sample code from vllm import LLM model_name = "mistralai/Pixtral-12B-Base-2409" llm =...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: the initial memory profiling phase, or result in low performance due to small KV cache size. Consider setting --max-model-len to a smaller value. INFO 04-25 15:09:27 [config.py:1747] Disabled the custom all-reduce kerne...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
