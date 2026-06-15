# vllm-project/vllm#17960: [Bug]: With Pytorch 2.7 in case of POWER getting, NotImplementedError: Could not run '_C_cache_ops::reshape_and_cache' with arguments from the 'CPU' backend

| 字段 | 值 |
| --- | --- |
| Issue | [#17960](https://github.com/vllm-project/vllm/issues/17960) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: With Pytorch 2.7 in case of POWER getting, NotImplementedError: Could not run '_C_cache_ops::reshape_and_cache' with arguments from the 'CPU' backend

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Trying to run ``` examples/offline_inference/basic/basic.py ``` and I am seeing the following error. It was running fine till v0.8.5 ``` INFO 05-11 07:51:38 [__init__.py:239] Automatically detected platform cpu. INFO 05-11 07:51:41 [config.py:2902] For POWERPC, we cast models to bfloat16 instead of using float16 by default. Float16 is not currently supported for POWERPC. WARNING 05-11 07:51:41 [config.py:2951] Casting torch.float16 to torch.bfloat16. INFO 05-11 07:51:49 [config.py:713] This model supports multiple tasks: {'reward', 'score', 'embed', 'classify', 'generate'}. Defaulting to 'generate'. WARNING 05-11 07:51:49 [arg_utils.py:1684] device type=cpu is not supported by the V1 Engine. Falling back to V0. INFO 05-11 07:51:49 [config.py:1794] Disabled the custom all-reduce kernel because it is not supported on current platform. WARNING 05-11 07:51:49 [cpu.py:106] Environment variable VLLM_CPU_KVCACHE_SPACE (GiB) for CPU backend is not set, using 4 by default. WARNING 05-11 07:51:49 [cpu.py:119] uni is not supported on CPU, fallback to mp distributed executor backend. INFO 05-11 07:51:49 [llm_engine.py:243] Initializing a V0...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: not run '_C_cache_ops::reshape_and_cache' with arguments from the 'CPU' backend bug ### Your current environment ### 🐛 Describe the bug Trying to run ``` examples/offline_inference/basic/basic.py ``` and I am seeing the...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: kwargs=None, pooler_config=None, compilation_config={"splitting_ops":[],"compile_sizes":[],"cudagraph_capture_sizes":[256,248,240,232,224,216,208,200,192,184,176,168,160,152,144,136,128,120,112,104,96,88,80,72,64,56,48,...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: cpu. INFO 05-11 07:51:41 [config.py:2902] For POWERPC, we cast models to bfloat16 instead of using float16 by default. Float16 is not currently supported for POWERPC. WARNING 05-11 07:51:41 [config.py:2951] Casting torc...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: v0.1.dev5926+g6d7febe.d20250429) with config: model='facebook/opt-125m', speculative_config=None, tokenizer='facebook/opt-125m', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config=None...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: init__.py:239] Automatically detected platform cpu. INFO 05-11 07:51:41 [config.py:2902] For POWERPC, we cast models to bfloat16 instead of using float16 by default. Float16 is not currently supported for POWERPC. WARNI...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
