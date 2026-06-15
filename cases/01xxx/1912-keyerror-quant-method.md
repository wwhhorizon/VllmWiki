# vllm-project/vllm#1912: KeyError: 'quant_method'

| 字段 | 值 |
| --- | --- |
| Issue | [#1912](https://github.com/vllm-project/vllm/issues/1912) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> KeyError: 'quant_method'

### Issue 正文摘录

I was running the following command to start an api server using predownloaded Baichuan model: python3 -m vllm.entrypoints.openai.api_server --model ./baichuan-inc/Baichuan2-13B-Chat-4bits --trust-remote-code However ,this error occurred: INFO 12-04 01:53:01 api_server.py:638] args: Namespace(allow_credentials=False, allowed_headers=['*'], allowed_methods=['*'], allowed_origins=['*'], block_size=16, disable_log_requests=False, disable_log_stats=False, download_dir=None, dtype='auto', engine_use_ray=False, gpu_memory_utilization=0.9, host=None, load_format='auto', max_log_len=None, max_model_len=None, max_num_batched_tokens=None, max_num_seqs=256, max_paddings=256, model='./baichuan-inc/Baichuan2-13B-Chat-4bits', pipeline_parallel_size=1, port=8000, quantization=None, revision=None, seed=0, served_model_name=None, swap_space=4, tensor_parallel_size=1, tokenizer=None, tokenizer_mode='auto', tokenizer_revision=None, trust_remote_code=True, worker_use_ray=False) Traceback (most recent call last): File "/usr/lib/python3.8/runpy.py", line 194, in _run_module_as_main return _run_code(code, main_globals, None, File "/usr/lib/python3.8/runpy.py", line 87, in _run_code exec(code, run_global...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: he following command to start an api server using predownloaded Baichuan model: python3 -m vllm.entrypoints.openai.api_server --model ./baichuan-inc/Baichuan2-13B-Chat-4bits --trust-remote-code However ,this error occur...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: KeyError: 'quant_method' I was running the following command to start an api server using predownloaded Baichuan model: python3 -m vllm.entrypoints.openai.api_server --model ./baichuan-inc/Baichuan2-13B-Chat-4bits --tru...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: FO 12-04 01:53:01 api_server.py:638] args: Namespace(allow_credentials=False, allowed_headers=['*'], allowed_methods=['*'], allowed_origins=['*'], block_size=16, disable_log_requests=False, disable_log_stats=False, down...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: allowed_methods=['*'], allowed_origins=['*'], block_size=16, disable_log_requests=False, disable_log_stats=False, download_dir=None, dtype='auto', engine_use_ray=False, gpu_memory_utilization=0.9, host=None, load_format...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
