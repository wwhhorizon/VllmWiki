# vllm-project/vllm#1178: Serving Qwen/Qwen-14B-Chat-Int4  error

| 字段 | 值 |
| --- | --- |
| Issue | [#1178](https://github.com/vllm-project/vllm/issues/1178) |
| 状态 | closed |
| 标签 |  |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Serving Qwen/Qwen-14B-Chat-Int4  error

### Issue 正文摘录

``` INFO 09-26 11:50:12 api_server.py:650] args: Namespace(host='0.0.0.0', port=8082, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], served_model_name=None, model='Qwen/Qwen-14B-Chat-Int4', tokenizer=None, tokenizer_mode='auto', trust_remote_code=True, download_dir='/home/models/qwen/Qwen-14B-Chat-Int4', load_format='auto', dtype='auto', worker_use_ray=False, pipeline_parallel_size=1, tensor_parallel_size=1, block_size=16, seed=0, swap_space=4, gpu_memory_utilization=0.9, max_num_batched_tokens=2560, max_num_seqs=256, disable_log_stats=False, engine_use_ray=False, disable_log_requests=False) INFO 09-26 11:50:13 llm_engine.py:72] Initializing an LLM engine with config: model='Qwen/Qwen-14B-Chat-Int4', tokenizer='Qwen/Qwen-14B-Chat-Int4', tokenizer_mode=auto, trust_remote_code=True, dtype=torch.float16, download_dir='/home/models/qwen/Qwen-14B-Chat-Int4', load_format=auto, tensor_parallel_size=1, seed=0) WARNING 09-26 11:50:14 tokenizer.py:64] Using a slow tokenizer. This might cause a significant slowdown. Consider using a fast tokenizer instead. INFO 09-26 11:50:14 distributed_c10d.py:442] Added key: store_based_barrier_key:1 to store...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: Serving Qwen/Qwen-14B-Chat-Int4 error ``` INFO 09-26 11:50:12 api_server.py:650] args: Namespace(host='0.0.0.0', port=8082, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], s...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: Serving Qwen/Qwen-14B-Chat-Int4 error ``` INFO 09-26 11:50:12 api_server.py:650] args: Namespace(host='0.0.0.0', port=8082, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], s...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: r.py:650] args: Namespace(host='0.0.0.0', port=8082, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], served_model_name=None, model='Qwen/Qwen-14B-Chat-Int4', tokenizer=None,...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: num_seqs=256, disable_log_stats=False, engine_use_ray=False, disable_log_requests=False) INFO 09-26 11:50:13 llm_engine.py:72] Initializing an LLM engine with config: model='Qwen/Qwen-14B-Chat-Int4', tokenizer='Qwen/Qwe...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
