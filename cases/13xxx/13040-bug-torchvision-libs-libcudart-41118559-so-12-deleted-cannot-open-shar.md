# vllm-project/vllm#13040: [Bug]: torchvision.libs/libcudart.41118559.so.12 (deleted): cannot open shared object file: No such file or directory

| 字段 | 值 |
| --- | --- |
| Issue | [#13040](https://github.com/vllm-project/vllm/issues/13040) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;quantization;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: torchvision.libs/libcudart.41118559.so.12 (deleted): cannot open shared object file: No such file or directory

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ```python from vllm import LLM llm = LLM(model='/ceph/home/tong01/wyf/model/Qwen2.5-Coder-0.5B') ``` The error message: ``` INFO 02-10 22:19:29 config.py:542] This model supports multiple tasks: {'score', 'embed', 'classify', 'generate', 'reward'}. Defaulting to 'generate'. INFO 02-10 22:19:29 llm_engine.py:234] Initializing a V0 LLM engine (v0.7.2) with config: model='/ceph/home/tong01/wyf/model/Qwen2.5-Coder-0.5B', speculative_config=None, tokenizer='/ceph/home/tong01/wyf/model/Qwen2.5-Coder-0.5B', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=32768, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=1, pipeline_parallel_size=1, disable_custom_all_reduce=False, quantization=None, enforce_eager=False, kv_cache_dtype=auto, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='xgrammar'), observability_config=ObservabilityConfig(otlp_traces_endpoint=None, collect_model_forward_time=False, collect_model_execute_time=False), seed=0, served_model_name=/ceph/home/tong...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: Your current environment ### 🐛 Describe the bug ```python from vllm import LLM llm = LLM(model='/ceph/home/tong01/wyf/model/Qwen2.5-Coder-0.5B') ``` The error message: ``` INFO 02-10 22:19:29 config.py:542] This model s...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: de_neuron_config=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=32768, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=1, pipeline_parallel_size=1, disable...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ent ### 🐛 Describe the bug ```python from vllm import LLM llm = LLM(model='/ceph/home/tong01/wyf/model/Qwen2.5-Coder-0.5B') ``` The error message: ``` INFO 02-10 22:19:29 config.py:542] This model supports multiple task...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: (deleted): cannot open shared object file: No such file or directory bug;stale ### Your current environment ### 🐛 Describe the bug ```python from vllm import LLM llm = LLM(model='/ceph/home/tong01/wyf/model/Qwen2.5-Code...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: uto, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='xgrammar'), observability_config=ObservabilityConfig(otlp_traces_endpoint=None, collect_model_forward_time=False, collect_model_execute_ti...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
