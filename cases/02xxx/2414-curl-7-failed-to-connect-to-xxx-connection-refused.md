# vllm-project/vllm#2414: curl: (7) Failed to connect to xxx : Connection refused

| 字段 | 值 |
| --- | --- |
| Issue | [#2414](https://github.com/vllm-project/vllm/issues/2414) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> curl: (7) Failed to connect to xxx : Connection refused

### Issue 正文摘录

two GPU nodes, P100-16G and 4090-24G After i run the `vllm.entrypoints.openai.api_server`, I run `curl` command to get it web result, and return `Connection refused` error. Any guys have idea about it? ```python python -m vllm.entrypoints.openai.api_server --trust-remote-code --model /home/mqq/pre_train_models/baichuan-inc/Baichuan2-13B-Chat --gpu-memory-utilization 1 --tensor-parallel-size 2 --host 0.0.0.0 --port 8125 ``` ``` INFO 01-11 05:52:49 api_server.py:727] args: Namespace(allow_credentials=False, allowed_headers=['*'], allowed_methods=['*'], allowed_origins=['*'], block_size=16, chat_template=None, disable_log_requests=False, disable_log_stats=False, download_dir=None, dtype='auto', enforce_eager=False, engine_use_ray=False, gpu_memory_utilization=1.0, host='0.0.0.0', load_format='auto', max_context_len_to_capture=8192, max_log_len=None, max_model_len=None, max_num_batched_tokens=None, max_num_seqs=256, max_paddings=256, max_parallel_loading_workers=None, model='/home/mqq/pre_train_models/baichuan-inc/Baichuan2-13B-Chat', pipeline_parallel_size=1, port=8125, quantization=None, response_role='assistant', revision=None, seed=0, served_model_name=None, ssl_certfile=None, ssl...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: disable_log_requests=False, disable_log_stats=False, download_dir=None, dtype='auto', enforce_eager=False, engine_use_ray=False, gpu_memory_utilization=1.0, host='0.0.0.0', load_format='auto', max_context_len_to_capture...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ython python -m vllm.entrypoints.openai.api_server --trust-remote-code --model /home/mqq/pre_train_models/baichuan-inc/Baichuan2-13B-Chat --gpu-memory-utilization 1 --tensor-parallel-size 2 --host 0.0.0.0 --port 8125 ``...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: FO 01-11 05:52:49 api_server.py:727] args: Namespace(allow_credentials=False, allowed_headers=['*'], allowed_methods=['*'], allowed_origins=['*'], block_size=16, chat_template=None, disable_log_requests=False, disable_l...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ], allowed_origins=['*'], block_size=16, chat_template=None, disable_log_requests=False, disable_log_stats=False, download_dir=None, dtype='auto', enforce_eager=False, engine_use_ray=False, gpu_memory_utilization=1.0, h...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
