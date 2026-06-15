# vllm-project/vllm#18535: [Bug]: Error when run qwen3-235b-a22b-Q4

| 字段 | 值 |
| --- | --- |
| Issue | [#18535](https://github.com/vllm-project/vllm/issues/18535) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;kernel;quantization;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Error when run qwen3-235b-a22b-Q4

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When i run following code, some error occured. ``` from vllm import LLM llm = LLM(model="qwen3-235b-a22b", tensor_parallel_size=2) ``` ``` INFO 05-22 14:12:17 [__init__.py:239] Automatically detected platform cuda. INFO 05-22 14:12:30 [config.py:717] This model supports multiple tasks: {'classify', 'score', 'generate', 'reward', 'embed'}. Defaulting to 'generate'. INFO 05-22 14:12:31 [gptq_marlin.py:143] The model is convertible to gptq_marlin during runtime. Using gptq_marlin kernel. INFO 05-22 14:12:32 [config.py:1770] Defaulting to use mp for distributed inference INFO 05-22 14:12:32 [config.py:2003] Chunked prefill is enabled with max_num_batched_tokens=16384. INFO 05-22 14:12:33 [core.py:58] Initializing a V1 LLM engine (v0.8.5.post1) with config: model='/home/my/data1/qwen3-235b-a22b', speculative_config=None, tokenizer='/home/my/data1/qwen3-235b-a22b', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=40960, download_dir=None, load_format=auto, tensor_parallel_size=2, pipeline_parallel_size=1, disabl...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: be the bug When i run following code, some error occured. ``` from vllm import LLM llm = LLM(model="qwen3-235b-a22b", tensor_parallel_size=2) ``` ``` INFO 05-22 14:12:17 [__init__.py:239] Automatically detected platform...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: Error when run qwen3-235b-a22b-Q4 bug;stale ### Your current environment ### 🐛 Describe the bug When i run following code, some error occured. ``` from vllm import LLM llm = LLM(model="qwen3-235b-a22b", tensor_pa...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: uto, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='auto', reasoning_backend=None), observability_config=ObservabilityConfig(show_hidden_metrics=False, otlp_traces_endpoint=None, collect_mod...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: `` INFO 05-22 14:12:17 [__init__.py:239] Automatically detected platform cuda. INFO 05-22 14:12:30 [config.py:717] This model supports multiple tasks: {'classify', 'score', 'generate', 'reward', 'embed'}. Defaulting to...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Error when run qwen3-235b-a22b-Q4 bug;stale ### Your current environment ### 🐛 Describe the bug When i run following code, some error occured. ``` from vllm import LLM llm = LLM(model="qwen3-235b-a22b", tensor_pa...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
