# vllm-project/vllm#34845: [Bug]: Qwen3-Next MTP fails when paired with chunked prefill

| 字段 | 值 |
| --- | --- |
| Issue | [#34845](https://github.com/vllm-project/vllm/issues/34845) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Qwen3-Next MTP fails when paired with chunked prefill

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Qwen3-next with MTP crashes when running with chunked prefill. To reproduce: Apply patch #34671 ``` vllm serve Qwen/Qwen3-Next-80B-A3B-Instruct \ --tokenizer-mode auto --gpu-memory-utilization 0.8 \ --speculative-config '{"method": "qwen3_next_mtp", "num_speculative_tokens": 2}' \ --tensor-parallel-size 4 --max-num-batched-tokens 64 ``` ``` lm_eval --model local-completions --model_args "base_url=http://0.0.0.0:8000/v1/completions,max_length=8192,tokenized_requests=False,tokenizer_backend=None,num_concurrent=32" --tasks gsm8k --num_fewshot 5 ``` Error: ``` (Worker_TP1 pid=22912) ERROR 02-18 22:00:01 [multiproc_executor.py:863] File "/vllm/vllm/v1/worker/worker_base.py", line 361, in execute_model (Worker_TP1 pid=22912) ERROR 02-18 22:00:01 [multiproc_executor.py:863] return self.worker.execute_model(scheduler_output) (Worker_TP1 pid=22912) ERROR 02-18 22:00:01 [multiproc_executor.py:863] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (Worker_TP1 pid=22912) ERROR 02-18 22:00:01 [multiproc_executor.py:863] File "/vllm/.venv/lib/python3.12/site-packages/torch/utils/_contextlib.py", line 124, in decorate_context (Worker_TP1 pid=22912) E...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: Qwen3-Next MTP fails when paired with chunked prefill bug ### Your current environment ### 🐛 Describe the bug Qwen3-next with MTP crashes when running with chunked prefill. To reproduce: Apply patch #34671 ``` vl...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Qwen3-Next MTP fails when paired with chunked prefill bug ### Your current environment ### 🐛 Describe the bug Qwen3-next with MTP crashes when running with chunked prefill. To reproduce: Apply patch #34671 ``` vll
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: enized_requests=False,tokenizer_backend=None,num_concurrent=32" --tasks gsm8k --num_fewshot 5 ``` Error: ``` (Worker_TP1 pid=22912) ERROR 02-18 22:00:01 [multiproc_executor.py:863] File "/vllm/vllm/v1/worker/worker_base...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: =http://0.0.0.0:8000/v1/completions,max_length=8192,tokenized_requests=False,tokenizer_backend=None,num_concurrent=32" --tasks gsm8k --num_fewshot 5 ``` Error: ``` (Worker_TP1 pid=22912) ERROR 02-18 22:00:01 [multiproc_...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: : 2}' \ --tensor-parallel-size 4 --max-num-batched-tokens 64 ``` ``` lm_eval --model local-completions --model_args "base_url=http://0.0.0.0:8000/v1/completions,max_length=8192,tokenized_requests=False,tokenizer_backend...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
