# vllm-project/vllm#5578: [Bug]: chunked prefill scheudler uses up swap on many n>=2 requests

| 字段 | 值 |
| --- | --- |
| Issue | [#5578](https://github.com/vllm-project/vllm/issues/5578) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;frontend_api;model_support;quantization;scheduler_memory |
| 子分类 | throughput |
| Operator 关键词 | cache;cuda;quantization |
| 症状 | crash;oom;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: chunked prefill scheudler uses up swap on many n>=2 requests

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug Sending many `n>=2` (or `best_of>=2`) requests fills up CPU KV cache, more often if chunked prefill is enabled. `_schedule_chunked_prefill` schedules prefills even if there are swapped seq groups https://github.com/vllm-project/vllm/blob/v0.5.0.post1/vllm/core/scheduler.py#L871-L873 while `_schedule_default` does not https://github.com/vllm-project/vllm/blob/v0.5.0.post1/vllm/core/scheduler.py#L763-L766 To reproduce, ```python import vllm print(vllm.__version__) from vllm import LLM, SamplingParams long_text = open(vllm.core.scheduler.__file__).read() prompts = [f"```python\n" + long_text[i:i+1000] for i in range(10000)] llm = LLM( model="facebook/opt-125m", enable_chunked_prefill=True, disable_log_stats=False, max_num_batched_tokens=4096, num_gpu_blocks_override=8192, ) sampling_params = SamplingParams(max_tokens=1000, n=8) llm.generate(prompts, sampling_params) ``` consumes CPU KV cache (`Running: 39 reqs, Swapped: 129 reqs` in the end) output ``` 0.5.0.post1 /home/kataoka/venv1/lib/python3.10/site-packages/huggingface_hub/file_download.py:1132: FutureWarning: `resume_download`...

## 现有链接修复摘要

#5633 [Bugfix] [Core] don't schedule prefill if freeing kv cache | #13539 fix(chunked prefill): don't schedule prefill if freeing kv cache

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: chunked prefill scheudler uses up swap on many n>=2 requests bug;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug Sending many `n>=2` (or `best_of>=2`) r...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: b/v0.5.0.post1/vllm/core/scheduler.py#L763-L766 To reproduce, ```python import vllm print(vllm.__version__) from vllm import LLM, SamplingParams long_text = open(vllm.core.scheduler.__file__).read() prompts = [f"```pyth...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ``python\n" + long_text[i:i+1000] for i in range(10000)] llm = LLM( model="facebook/opt-125m", enable_chunked_prefill=True, disable_log_stats=False, max_num_batched_tokens=4096, num_gpu_blocks_override=8192, ) sampling_...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: None, rope_theta=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=2048, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=1, disable_custom_all_reduce=False, qu...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: book/opt-125m", enable_chunked_prefill=True, disable_log_stats=False, max_num_batched_tokens=4096, num_gpu_blocks_override=8192, ) sampling_params = SamplingParams(max_tokens=1000, n=8) llm.generate(prompts, sampling_pa...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#5633](https://github.com/vllm-project/vllm/pull/5633) | closes_keyword | 0.95 | [Bugfix] [Core] don't schedule prefill if freeing kv cache | FIX #5578 This PR makes the priority "running > swapped > waiting" strict. The previous code has chance to schedule new prefills even if preemption/swap happens or there's a swa |
| [#13539](https://github.com/vllm-project/vllm/pull/13539) | closes_keyword | 0.95 | fix(chunked prefill): don't schedule prefill if freeing kv cache | FIX #5578 This PR makes the priority "running > swapped > waiting" strict. The previous code has chance to schedule new prefills even if preemption/swap happens or there's a swapp |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
