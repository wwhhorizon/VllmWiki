# vllm-project/vllm#8420: [Bug]: PyNcclCommunicator error when inferencing

| 字段 | 值 |
| --- | --- |
| Issue | [#8420](https://github.com/vllm-project/vllm/issues/8420) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cuda;operator;quantization;triton |
| 症状 | build_error;crash;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: PyNcclCommunicator error when inferencing

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When I started creating an instance from the LLM class, an error occurred. It says `AttributeError: 'PyNcclCommunicator' object has no attribute 'device'`, I don't know what to do then. The code to test it: ``` from vllm import LLM def init_model() -> LLM: llm = LLM( model="Qwen/Qwen2-7B-Instruct", tokenizer_mode="auto", trust_remote_code=True, download_dir="./.cache", tensor_parallel_size=2, # How many GPUs to use gpu_memory_utilization=0.85, pipeline_parallel_size=1, dtype="bfloat16", # max_model_len=20480, # Model context length enable_prefix_caching=True, enable_chunked_prefill=False, num_scheduler_steps=8, ) return llm if __name__ == "__main__": llm = init_model() print(llm.generate("Hello, world!")) ``` ``` INFO 09-13 00:13:27 config.py:890] Defaulting to use mp for distributed inference WARNING 09-13 00:13:27 arg_utils.py:880] Enabled BlockSpaceManagerV2 because it is required for multi-step (--num-scheduler-steps > 1) INFO 09-13 00:13:27 llm_engine.py:213] Initializing an LLM engine (v0.6.0) with config: model='Qwen/Qwen2-7B-Instruct', speculative_config=None, tokenizer='Qwen/Qwen2-7B-I...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Bug]: PyNcclCommunicator error when inferencing bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When I started creating an instance from the LLM class, an error occurred. It...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: =False, kv_cache_dtype=auto, quantization_param_path=None, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='outlines'), observability_config=ObservabilityConfig(otlp_traces_endpoint=None, coll...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: ontext length enable_prefix_caching=True, enable_chunked_prefill=False, num_scheduler_steps=8, ) return llm if __name__ == "__main__": llm = init_model() print(llm.generate("Hello, world!")) ``` ``` INFO 09-13 00:13:27...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: gpu_memory_utilization=0.85, pipeline_parallel_size=1, dtype="bfloat16", # max_model_len=20480, # Model context length enable_prefix_caching=True, enable_chunked_prefill=False, num_scheduler_steps=8, ) return llm if __n...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: unicator error when inferencing bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When I started creating an instance from the LLM class, an error occurred. It says `AttributeEr...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
