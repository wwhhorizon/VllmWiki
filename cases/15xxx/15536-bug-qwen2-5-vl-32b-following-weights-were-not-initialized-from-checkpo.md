# vllm-project/vllm#15536: [Bug]: Qwen2.5-VL-32B, Following weights were not initialized from checkpoint

| 字段 | 值 |
| --- | --- |
| Issue | [#15536](https://github.com/vllm-project/vllm/issues/15536) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Qwen2.5-VL-32B, Following weights were not initialized from checkpoint

### Issue 正文摘录

### Your current environment vllm==0.7.3 ### 🐛 Describe the bug vllm serve Qwen/Qwen2.5-32B-Instruct \ --max-model-len=32768 \ --limit-mm-per-prompt image=10 \ --gpu-memory-utilization 0.6 \ --port 23333 \ -tp 8 --trust-remote-code ``` ERROR 03-26 17:12:18 engine.py:400] engine = MQLLMEngine.from_engine_args(engine_args=engine_args, ERROR 03-26 17:12:18 engine.py:400] File "/usr/local/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 124, in from_engin e_args ERROR 03-26 17:12:18 engine.py:400] return cls(ipc_path=ipc_path, ERROR 03-26 17:12:18 engine.py:400] File "/usr/local/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 76, in __init__ ERROR 03-26 17:12:18 engine.py:400] self.engine = LLMEngine(*args, **kwargs) ERROR 03-26 17:12:18 engine.py:400] File "/usr/local/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 273, in __init__ ERROR 03-26 17:12:18 engine.py:400] self.model_executor = executor_class(vllm_config=vllm_config, ) ERROR 03-26 17:12:18 engine.py:400] File "/usr/local/lib/python3.10/site-packages/vllm/executor/executor_base.py", line 271, in __init__ ERROR 03-26 17:12:18 engine.py:400] super().__init__(*ar...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Qwen2.5-VL-32B, Following weights were not initialized from checkpoint bug;stale ### Your current environment vllm==0.7.3 ### 🐛 Describe the bug vllm serve Qwen/Qwen2.5-32B-Instruct \ --max-model-len=32768 \ --
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: en2.5-VL-32B, Following weights were not initialized from checkpoint bug;stale ### Your current environment vllm==0.7.3 ### 🐛 Describe the bug vllm serve Qwen/Qwen2.5-32B-Instruct \ --max-model-len=32768 \ --limit-mm-pe...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
