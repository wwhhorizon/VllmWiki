# vllm-project/vllm#25240: [Bug]: Engine Fails when running Qwen3-Next with no traceback

| 字段 | 值 |
| --- | --- |
| Issue | [#25240](https://github.com/vllm-project/vllm/issues/25240) |
| 状态 | open |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Engine Fails when running Qwen3-Next with no traceback

### Issue 正文摘录

### 🐛 Describe the bug vLLM Server Command(v0.10.2): ``` vllm serve Qwen/Qwen3-Next-80B-A3B-Instruct --host "0.0.0.0" --port "8000" --uvicorn-log-level warning --enable-log-requests --enable-log-outputs --served-model-name qwen3-next --trust-remote-code --gpu-memory-utilization "0.9" --enable-prefix-caching --max-model-len "130000" --enable-auto-tool-choice --tool-call-parser hermes --tensor-parallel-size "4" --speculative-config '{"method":"qwen3_next_mtp","num_speculative_tokens":2}' ``` I am trying to benchmark the model using [ComplexFuncBench](https://github.com/zai-org/ComplexFuncBench): ``` python evaluation.py --model_name=qwen3-next --vllm_url=http://0.0.0.0:8000/v1 --proc_num=4 ``` Logs: ``` (APIServer pid=2358) ERROR 09-18 18:38:55 [core_client.py:564] Engine core proc EngineCore_DP0 died unexpectedly, shutting down client. (Worker_TP3 pid=2904) INFO 09-18 18:38:55 [multiproc_executor.py:546] Parent process exited, terminating worker (Worker_TP2 pid=2903) INFO 09-18 18:38:55 [multiproc_executor.py:546] Parent process exited, terminating worker (Worker_TP1 pid=2902) INFO 09-18 18:38:55 [multiproc_executor.py:546] Parent process exited, terminating worker (Worker_TP0 pid=...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Engine Fails when running Qwen3-Next with no traceback bug ### 🐛 Describe the bug vLLM Server Command(v0.10.2): ``` vllm serve Qwen/Qwen3-Next-80B-A3B-Instruct --host "0.0.0.0" --port "8000" --uvicorn-log-level w...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: ethod":"qwen3_next_mtp","num_speculative_tokens":2}' ``` I am trying to benchmark the model using [ComplexFuncBench](https://github.com/zai-org/ComplexFuncBench): ``` python evaluation.py --model_name=qwen3-next --vllm_...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: --host "0.0.0.0" --port "8000" --uvicorn-log-level warning --enable-log-requests --enable-log-outputs --served-model-name qwen3-next --trust-remote-code --gpu-memory-utilization "0.9" --enable-prefix-caching --max-model...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ng. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
