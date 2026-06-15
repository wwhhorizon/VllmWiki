# vllm-project/vllm#29747: [Bug]: --scheduling-policy=priority & n>1 crashes engine

| 字段 | 值 |
| --- | --- |
| Issue | [#29747](https://github.com/vllm-project/vllm/issues/29747) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: --scheduling-policy=priority & n>1 crashes engine

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When running with priority scheduling, e.g.: ```bash vllm serve Qwen/Qwen3-0.6B --scheduling-policy=priority ``` and using `n` > 1 in the request, like: ```python from openai import OpenAI client = OpenAI(base_url="http://localhost:8000/v1", api_key="dummy") res = client.chat.completions.create( model=client.models.list().data[0].id, messages=[{"role": "user", "content": "What is the meaning of life?"}], n=2 ) print(res) ``` vllm crashes with: ```python (EngineCore_DP0 pid=207394) ERROR 11-30 15:14:29 [core.py:844] EngineCore encountered a fatal error. (EngineCore_DP0 pid=207394) ERROR 11-30 15:14:29 [core.py:844] Traceback (most recent call last): (EngineCore_DP0 pid=207394) ERROR 11-30 15:14:29 [core.py:844] File "/home/user/code/debug/.venv/lib/python3.10/site-packages/vllm/v1/engine/core.py", line 835, in run_engine_core (EngineCore_DP0 pid=207394) ERROR 11-30 15:14:29 [core.py:844] engine_core.run_busy_loop() (EngineCore_DP0 pid=207394) ERROR 11-30 15:14:29 [core.py:844] File "/home/user/code/debug/.venv/lib/python3.10/site-packages/vllm/v1/engine/core.py", line 860, in run_busy_loop (EngineCore_DP0 pid=207394) ERROR 11-30 1...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: en/Qwen3-0.6B --scheduling-policy=priority ``` and using `n` > 1 in the request, like: ```python from openai import OpenAI client = OpenAI(base_url="http://localhost:8000/v1", api_key="dummy") res = client.chat.completi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: the bug When running with priority scheduling, e.g.: ```bash vllm serve Qwen/Qwen3-0.6B --scheduling-policy=priority ``` and using `n` > 1 in the request, like: ```python from openai import OpenAI client = OpenAI(base_u...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ority ``` and using `n` > 1 in the request, like: ```python from openai import OpenAI client = OpenAI(base_url="http://localhost:8000/v1", api_key="dummy") res = client.chat.completions.create( model=client.models.list(...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: .2) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
