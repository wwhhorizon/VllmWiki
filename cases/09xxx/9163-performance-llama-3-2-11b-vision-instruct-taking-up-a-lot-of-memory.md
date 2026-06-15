# vllm-project/vllm#9163: [Performance]: Llama-3.2-11B-Vision-Instruct taking up a lot of memory

| 字段 | 值 |
| --- | --- |
| Issue | [#9163](https://github.com/vllm-project/vllm/issues/9163) |
| 状态 | closed |
| 标签 | performance |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;frontend_api;model_support;quantization;sampling_logits;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cache;cuda;quantization |
| 症状 | crash;oom |
| 根因提示 | dtype;env_dependency;race_condition;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: Llama-3.2-11B-Vision-Instruct taking up a lot of memory

### Issue 正文摘录

### Proposal to improve performance Currently when I load the generic huggingface model it takes a max of `22637MiB` at inference time on BF16. When I load it with vLLM: ```python llm = LLM(model="meta-llama/Llama-3.2-11B-Vision-Instruct", dtype="bfloat16") ``` it OOMs: ``` INFO 10-08 17:37:09 weight_utils.py:242] Using model weights format ['*.safetensors'] Loading safetensors checkpoint shards: 0% Completed | 0[/5](http://98.84.183.65:8888/5) [00:00 1 llm = LLM(model="meta-llama[/Llama-3.2-11B-Vision-Instruct](http://98.84.183.65:8888/Llama-3.2-11B-Vision-Instruct)", dtype="bfloat16") File [/opt/conda/lib/python3.12/site-packages/vllm/entrypoints/llm.py:214](http://98.84.183.65:8888/opt/conda/lib/python3.12/site-packages/vllm/entrypoints/llm.py#line=213), in LLM.__init__(self, model, tokenizer, tokenizer_mode, skip_tokenizer_init, trust_remote_code, tensor_parallel_size, dtype, quantization, revision, tokenizer_revision, seed, gpu_memory_utilization, swap_space, cpu_offload_gb, enforce_eager, max_context_len_to_capture, max_seq_len_to_capture, disable_custom_all_reduce, disable_async_output_proc, mm_processor_kwargs, **kwargs) 189 raise TypeError( 190 "There is no need to pass v...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Performance]: Llama-3.2-11B-Vision-Instruct taking up a lot of memory performance ### Proposal to improve performance Currently when I load the generic huggingface model it takes a max of `22637MiB` at inference time o...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: eric huggingface model it takes a max of `22637MiB` at inference time on BF16. When I load it with vLLM: ```python llm = LLM(model="meta-llama/Llama-3.2-11B-Vision-Instruct", dtype="bfloat16") ``` it OOMs: ``` INFO 10-0...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: odule._wrapped_call_impl(self, *args, **kwargs) 1551 return self._compiled_call_impl(*args, **kwargs) # type: ignore[misc] 1552 else: -> 1553 return self._call_impl(*args, **kwargs) File [/opt/conda/lib/python3.12/site-...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: 215 engine_args, usage_context=UsageContext.LLM_CLASS) 216 self.request_counter = Counter() File [/opt/conda/lib/python3.12/site-packages/vllm/engine/llm_engine.py:564](http://98.84.183.65:8888/opt/conda/lib/python3.12/...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: el="meta-llama/Llama-3.2-11B-Vision-Instruct", dtype="bfloat16") ``` it OOMs: ``` INFO 10-08 17:37:09 weight_utils.py:242] Using model weights format ['*.safetensors'] Loading safetensors checkpoint shards: 0% Completed...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
