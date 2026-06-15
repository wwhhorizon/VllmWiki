# vllm-project/vllm#14205: [Bug]: Can't run offline inference (example script) in OpenVINO: TypeError: OpenVINOCausalLM.forward() missing 2 required positional arguments: 'kv_caches' and 'attn_metadata'

| 字段 | 值 |
| --- | --- |
| Issue | [#14205](https://github.com/vllm-project/vllm/issues/14205) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;operator;quantization;sampling |
| 症状 | build_error;crash;mismatch;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Can't run offline inference (example script) in OpenVINO: TypeError: OpenVINOCausalLM.forward() missing 2 required positional arguments: 'kv_caches' and 'attn_metadata'

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I'm trying to run the example script of [offline_inference](https://github.com/vllm-project/vllm/blob/main/examples/offline_inference/basic/basic.py) with OpenVINO backend. I get the error `TypeError: OpenVINOCausalLM.forward() missing 2 required positional arguments: 'kv_caches' and 'attn_metadata'`. Here are the complete logs: ``` INFO 03-04 11:45:10 [__init__.py:207] Automatically detected platform openvino. INFO 03-04 11:45:17 [config.py:569] This model supports multiple tasks: {'reward', 'embed', 'score', 'classify', 'generate'}. Defaulting to 'generate'. WARNING 03-04 11:45:17 [openvino.py:82] Only float32 dtype is supported on OpenVINO, casting from torch.float16. WARNING 03-04 11:45:17 [openvino.py:87] CUDA graph is not supported on OpenVINO backend, fallback to the eager mode. INFO 03-04 11:45:17 [openvino.py:121] OpenVINO CPU optimal block size is 32, overriding currently set 16 WARNING 03-04 11:45:17 [openvino.py:136] Environment variable VLLM_OPENVINO_KVCACHE_SPACE (GB) for OpenVINO backend is not set, using 4 by default. INFO 03-04 11:45:17 [llm_engine.py:235] Initializing a V0 LLM engine (v0.7.4.dev122+gcd711c48) wi...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: kwargs=None, pooler_config=None, compilation_config={"splitting_ops":[],"compile_sizes":[],"cudagraph_capture_sizes":[256,248,240,232,224,216,208,200,192,184,176,168,160,152,144,136,128,120,112,104,96,88,80,72,64,56,48,...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: engine (v0.7.4.dev122+gcd711c48) with config: model='facebook/opt-125m', speculative_config=None, tokenizer='facebook/opt-125m', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config=None...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: . Defaulting to 'generate'. WARNING 03-04 11:45:17 [openvino.py:82] Only float32 dtype is supported on OpenVINO, casting from torch.float16. WARNING 03-04 11:45:17 [openvino.py:87] CUDA graph is not supported on OpenVIN...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: forward() missing 2 required positional arguments: 'kv_caches' and 'attn_metadata' bug ### Your current environment ### 🐛 Describe the bug I'm trying to run the example script of [offline_inference](https://github.com/v...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: INO, casting from torch.float16. WARNING 03-04 11:45:17 [openvino.py:87] CUDA graph is not supported on OpenVINO backend, fallback to the eager mode. INFO 03-04 11:45:17 [openvino.py:121] OpenVINO CPU optimal block size...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
