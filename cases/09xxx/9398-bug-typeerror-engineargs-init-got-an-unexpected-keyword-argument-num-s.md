# vllm-project/vllm#9398: [Bug]: TypeError: EngineArgs.__init__() got an unexpected keyword argument 'num_scheduler_steps'

| 字段 | 值 |
| --- | --- |
| Issue | [#9398](https://github.com/vllm-project/vllm/issues/9398) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: TypeError: EngineArgs.__init__() got an unexpected keyword argument 'num_scheduler_steps'

### Issue 正文摘录

### Your current environment vllm==0.6.3 ### Model Input Dumps _No response_ ### 🐛 Describe the bug ``` model = LLM( model=checkpoint, trust_remote_code=True, gpu_memory_utilization=0.3, dtype="bfloat16", enforce_eager=True, num_scheduler_steps=8, ) ``` File "/root/anaconda3/envs/Qwen_vllm_0.6.3/lib/python3.10/site-packages/vllm/entrypoints/llm.py", line 129, in __init__ engine_args = EngineArgs( TypeError: EngineArgs.__init__() got an unexpected keyword argument 'num_scheduler_steps' ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: trust_remote_code=True, gpu_memory_utilization=0.3, dtype="bfloat16", enforce_eager=True, num_scheduler_steps=8, ) ``` File "/root/anaconda3/envs/Qwen_vllm_0.6.3/lib/python3.10/site-packages/vllm/entrypoints/llm.py", li...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: 'num_scheduler_steps' bug ### Your current environment vllm==0.6.3 ### Model Input Dumps _No response_ ### 🐛 Describe the bug ``` model = LLM( model=checkpoint, trust_remote_code=True, gpu_memory_utilization=0.3, dtype=...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ps' ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: TypeError: EngineArgs.__init__() got an unexpected keyword argument 'num_scheduler_steps' bug ### Your current environment vllm==0.6.3 ### Model Input Dumps _No response_ ### 🐛 Describe the bug ``` model = LLM( model=ch...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
