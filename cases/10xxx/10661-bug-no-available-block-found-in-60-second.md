# vllm-project/vllm#10661: [Bug]: No available block found in 60 second. 

| 字段 | 值 |
| --- | --- |
| Issue | [#10661](https://github.com/vllm-project/vllm/issues/10661) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits |
| 子分类 | memory |
| Operator 关键词 | attention;cache;cuda;operator;quantization;triton |
| 症状 | build_error;oom |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: No available block found in 60 second. 

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When I set `task="embedding"` to use the vLLM serving [Llama-3.1-Nemotron-70B-Reward-HF](https://huggingface.co/nvidia/Llama-3.1-Nemotron-70B-Reward-HF) model, the following error occurred. However, no error occurs when `task="embedding"` is not set. Additionally, when task="embedding" is set, no error occurs when using `python -u -m vllm.entrypoints.openai.api_server --task embedding --pipeline-parallel-size 8`. ```python from vllm import LLM from vllm.config import PoolerConfig llm = LLM( model="./Llama-3.1-Nemotron-70B-Reward-HF", task="embedding", tensor_parallel_size=8, pipeline_parallel_size=1, trust_remote_code=True, dtype='bfloat16', enable_chunked_prefill=False, enable_prefix_caching=True, disable_custom_all_reduce=True ) prompt = "What is 1+1?" output = llm.encode(prompt) ``` ``` INFO 11-26 12:54:37 config.py:1854] Downcasting torch.float32 to torch.bfloat16. INFO 11-26 12:54:44 config.py:1025] Defaulting to use mp for distributed inference WARNING 11-26 12:54:44 arg_utils.py:1030] The model has a long context length (131072). This may cause OOM errors during the initial memory profil...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: erver --task embedding --pipeline-parallel-size 8`. ```python from vllm import LLM from vllm.config import PoolerConfig llm = LLM( model="./Llama-3.1-Nemotron-70B-Reward-HF", task="embedding", tensor_parallel_size=8, pi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: lock found in 60 second. bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When I set `task="embedding"` to use the vLLM serving [Llama-3.1-Nemotron-70B-Reward-HF](https:/...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [Bug]: No available block found in 60 second. bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When I set `task="embedding"` to use the vLLM serving [Llama-3.1-Nemotron-7...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: pipeline_parallel_size=1, trust_remote_code=True, dtype='bfloat16', enable_chunked_prefill=False, enable_prefix_caching=True, disable_custom_all_reduce=True ) prompt = "What is 1+1?" output = llm.encode(prompt) ``` ```...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: None, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='outlines'), observability_config=ObservabilityConfig(otlp_traces_endpoint=None, collect_model_forward_time=False, collect_model_execute_t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
