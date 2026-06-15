# vllm-project/vllm#15543: [Bug]: profile deadlock when ray backend and num-scheduler-steps > 1 and max_tokens % num_scheduler_steps !=0

| 字段 | 值 |
| --- | --- |
| Issue | [#15543](https://github.com/vllm-project/vllm/issues/15543) |
| 状态 | closed |
| 标签 | bug;ray;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: profile deadlock when ray backend and num-scheduler-steps > 1 and max_tokens % num_scheduler_steps !=0

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug My script: ```python export VLLM_TORCH_PROFILER_DIR=/home/ma-user/profiler/ python -m vllm.entrypoints.openai.api_server \ --host=0.0.0.0 \ --port=9099 \ --model={deepseek_model} \ --max-num-seqs=256 \ --max-model-len=8192 \ --max-num-batched-tokens=8192 \ --num-scheduler-steps 4 \ --dtype=bfloat16 \ --block-size=128 \ --tensor-parallel-size=2 \ --served-model-name deepseek \ --trust-remote-code \ --load-format dummy \ --distributed-executor-backend=ray \ --disable-log-requests ``` I tried to change the `max_tokens` in a curl shell script like: ```shell curl -X POST "http://127.0.0.1:9099/v1/chat/completions" \ -H "Content-Type: application/json" \ -d '{ "model": "deepseek", "messages": [ { "role": "user", "content": "who are you?" } ], "max_tokens" : 5 }' ``` I found that when `max_tokens % num_scheduler_steps==0`, the warning log `WARNING 03-26 14:50:42 shm_broadcast.py:403] No available block found in 60 second` disappears, and profile start/stop method is not stuck. But when `max_tokens % num_scheduler_steps !=0`, the warning log `WARNING 03-26 14:50:42 shm_broadcast.py:403] No available block found in 60 second` still exists...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [Bug]: profile deadlock when ray backend and num-scheduler-steps > 1 and max_tokens % num_scheduler_steps !=0 bug;ray;stale ### Your current environment ### 🐛 Describe the bug My script: ```python export VLLM_TORCH_PROF...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: --max-num-batched-tokens=8192 \ --num-scheduler-steps 4 \ --dtype=bfloat16 \ --block-size=128 \ --tensor-parallel-size=2 \ --served-model-name deepseek \ --trust-remote-code \ --load-format dummy \ --distributed-executo...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: tokens=8192 \ --num-scheduler-steps 4 \ --dtype=bfloat16 \ --block-size=128 \ --tensor-parallel-size=2 \ --served-model-name deepseek \ --trust-remote-code \ --load-format dummy \ --distributed-executor-backend=ray \ --...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ypoints.openai.api_server \ --host=0.0.0.0 \ --port=9099 \ --model={deepseek_model} \ --max-num-seqs=256 \ --max-model-len=8192 \ --max-num-batched-tokens=8192 \ --num-scheduler-steps 4 \ --dtype=bfloat16 \ --block-size...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Bug]: profile deadlock when ray backend and num-scheduler-steps > 1 and max_tokens % num_scheduler_steps !=0 bug;ray;stale ### Your current environment ### 🐛 Describe the bug My script: ```python export VLLM_TORCH_PROFI

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
