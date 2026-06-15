# vllm-project/vllm#25494: [Bug]: AssertionError: Do not capture num_reqs > max_num_reqs for uniform batch

| 字段 | 值 |
| --- | --- |
| Issue | [#25494](https://github.com/vllm-project/vllm/issues/25494) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: AssertionError: Do not capture num_reqs > max_num_reqs for uniform batch

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug `vllm serve --model="deepseek-ai/DeepSeek-R1" --max-num-seqs 512 --data-parallel-size 8 --enable-expert-parallel --gpu-memory-utilization 0.9 --port 9256` `vllm bench serve --model deepseek-ai/DeepSeek-R1 --dataset-name random --host 127.0.0.1 --port 9256 --random-input-len 130000 --random-output-len 1 --request-rate inf --num-prompts 1` Will meet an error: ```bash (EngineCore_DP7 pid=3747941) File "/usr/lib/python3.12/multiprocessing/process.py", line 314, in _bootstrap (EngineCore_DP7 pid=3747941) self.run() (EngineCore_DP7 pid=3747941) File "/usr/lib/python3.12/multiprocessing/process.py", line 108, in run (EngineCore_DP7 pid=3747941) self._target(*self._args, **self._kwargs) (EngineCore_DP7 pid=3747941) File "/home/wentao/vllm-source/vllm/v1/engine/core.py", line 712, in run_engine_core (EngineCore_DP7 pid=3747941) raise e (EngineCore_DP7 pid=3747941) File "/home/wentao/vllm-source/vllm/v1/engine/core.py", line 701, in run_engine_core (EngineCore_DP7 pid=3747941) engine_core.run_busy_loop() (EngineCore_DP7 pid=3747941) File "/home/wentao/vllm-source/vllm/v1/engine/core.py", line 1056, in run_busy_loop (EngineCore_DP7 pid=3747...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: 127.0.0.1 --port 9256 --random-input-len 130000 --random-output-len 1 --request-rate inf --num-prompts 1` Will meet an error: ```bash (EngineCore_DP7 pid=3747941) File "/usr/lib/python3.12/multiprocessing/process.py", l...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: g ### Your current environment ### 🐛 Describe the bug `vllm serve --model="deepseek-ai/DeepSeek-R1" --max-num-seqs 512 --data-parallel-size 8 --enable-expert-parallel --gpu-memory-utilization 0.9 --port 9256` `vllm benc...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: pseek-ai/DeepSeek-R1" --max-num-seqs 512 --data-parallel-size 8 --enable-expert-parallel --gpu-memory-utilization 0.9 --port 9256` `vllm bench serve --model deepseek-ai/DeepSeek-R1 --dataset-name random --host 127.0.0.1...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
