# vllm-project/vllm#12476: [Bug]: Computation cache has already been initialized error on TPUs

| 字段 | 值 |
| --- | --- |
| Issue | [#12476](https://github.com/vllm-project/vllm/issues/12476) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;operator;quantization;sampling |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Computation cache has already been initialized error on TPUs

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug The error occurs when we try to initialize an `LLM` twice on the same node after originally using it to do some calculations. It complains that the computation cache has already been initialized. Full Stack Trace: ``` (test_llm_call pid=846, ip=10.202.1.109) DEBUG 01-27 09:43:32 __init__.py:26] No plugins for group vllm.platform_plugins found. (test_llm_call pid=846, ip=10.202.1.109) INFO 01-27 09:43:32 __init__.py:183] Automatically detected platform tpu. (test_llm_call pid=846, ip=10.202.1.109) DEBUG 01-27 09:43:32 __init__.py:26] No plugins for group vllm.general_plugins found. (test_llm_call pid=846, ip=10.202.1.109) INFO 01-27 09:43:38 config.py:520] This model supports multiple tasks: {'embed', 'classify', 'reward', 'generate', 'score'}. Defaulting to 'generate'. (test_llm_call pid=846, ip=10.202.1.109) INFO 01-27 09:43:38 llm_engine.py:232] Initializing an LLM engine (v0.6.6.post2.dev371+gab5bbf5a) with config: model='/opt/gcsfuse_mount/models/meta-llama--Llama-3-1-8B-Instruct', speculative_config=None, tokenizer='/opt/gcsfuse_mount/models/meta-llama--Llama-3-1-8B-Instruct', skip_tokeniz...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: e, compilation_config={"level":2,"backend":"openxla","splitting_ops":[],"compile_sizes":[],"cudagraph_capture_sizes":[],"max_capture_size":0}, use_cached_outputs=False, (test_llm_call pid=846, ip=10.202.1.109) WARNING:r...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: de_neuron_config=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=8192, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, disable_custom_all_...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: initialized error on TPUs bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug The error occurs when we try to initialize an `LLM` twice on the same node after originally usi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: Computation cache has already been initialized error on TPUs bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug The error occurs when we try to initialize an `LLM` t...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ig={"level":2,"backend":"openxla","splitting_ops":[],"compile_sizes":[],"cudagraph_capture_sizes":[],"max_capture_size":0}, use_cached_outputs=False, (test_llm_call pid=846, ip=10.202.1.109) WARNING:root:libtpu.so and T...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
