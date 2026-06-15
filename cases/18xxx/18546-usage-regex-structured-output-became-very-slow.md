# vllm-project/vllm#18546: [Usage]: Regex Structured Output Became Very Slow

| 字段 | 值 |
| --- | --- |
| Issue | [#18546](https://github.com/vllm-project/vllm/issues/18546) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Regex Structured Output Became Very Slow

### Issue 正文摘录

### Your current environment On my machine, adding a regular expression constraint is dozens of times slower than not adding it. I debugged into the vllm python pack. Found Line 1423 of the vllm/entrypoints/llm.py file ```python step_outputs = self.llm_engine.step() ``` always returns an empty list, causing me to keep looping in this area if I add a regex constraint, which is much slower. I think that this step() method should be to generate something, maybe by logits+bitmask. So, it should definitely be able to sample the generated tokens after softmax. Why does it keep returning empty lists? My LLM config is down here: > EngineArgs(model='/home/xxx.cache/modelscope/hub/models/Qwen/Qwen3-1.7B', served_model_name=None, tokenizer='/home/lianshixi1/.cache/modelscope/hub/models/Qwen/Qwen3-1.7B', hf_config_path=None, task='auto', skip_tokenizer_init=False, tokenizer_mode='auto', trust_remote_code=False, allowed_local_media_path='', download_dir=None, load_format='auto', config_format= , dtype='auto', kv_cache_dtype='auto', seed=0, max_model_len=1024, distributed_executor_backend='external_launcher', pipeline_parallel_size=1, tensor_parallel_size=1, data_parallel_size=1, enable_expert_...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ve_config=None, qlora_adapter_name_or_path=None, show_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_detailed_traces=None, disable_async_output_proc=False, scheduling_policy='fcfs', scheduler_cls='v...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: version : 2.6.0+cu124 Is debug build : False CUDA used to build PyTorch : 12.4 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.10.16 (...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: d tokens after softmax. Why does it keep returning empty lists? My LLM config is down here: > EngineArgs(model='/home/xxx.cache/modelscope/hub/models/Qwen/Qwen3-1.7B', served_model_name=None, tokenizer='/home/lianshixi1...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: l_media_path='', download_dir=None, load_format='auto', config_format= , dtype='auto', kv_cache_dtype='auto', seed=0, max_model_len=1024, distributed_executor_backend='external_launcher', pipeline_parallel_size=1, tenso...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Usage]: Regex Structured Output Became Very Slow usage;stale ### Your current environment On my machine, adding a regular expression constraint is dozens of times slower than not adding it. I debugged into the vllm pyt...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
