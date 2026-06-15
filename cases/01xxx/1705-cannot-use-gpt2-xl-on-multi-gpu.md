# vllm-project/vllm#1705: Cannot use gpt2-xl on multi-GPU

| 字段 | 值 |
| --- | --- |
| Issue | [#1705](https://github.com/vllm-project/vllm/issues/1705) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Cannot use gpt2-xl on multi-GPU

### Issue 正文摘录

Thank you guys for the amazing effort ! I am trying to use ```gpt2-xl``` (listed in the Supported Models) with multiple GPUs. However, when I use 2 GPUs, I get ```ValueError: Total number of attention heads (25) must be divisible by tensor parallel size (2).``` And when I use 5 GPUs, I get ```File " /.local/lib/python3.10/site-packages/vllm/entrypoints/llm.py", line 89, in __init__ self.llm_engine = LLMEngine.from_engine_args(engine_args) File " /.local/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 229, in from_engine_args engine = cls(*engine_configs, File " /.local/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 106, in __init__ self._init_workers_ray(placement_group) File " /.local/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 179, in _init_workers_ray self._run_workers( File " /.local/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 696, in _run_workers all_outputs = ray.get(all_outputs) File " /.local/lib/python3.10/site-packages/ray/_private/auto_init_hook.py", line 24, in auto_init_wrapper return fn(*args, **kwargs) File " /.local/lib/python3.10/site-packages/ray/_private/client_mode_hook.py", line 103, in wrapper r...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: zing effort ! I am trying to use ```gpt2-xl``` (listed in the Supported Models) with multiple GPUs. However, when I use 2 GPUs, I get ```ValueError: Total number of attention heads (25) must be divisible by tensor paral...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Cannot use gpt2-xl on multi-GPU feature request;stale Thank you guys for the amazing effort ! I am trying to use ```gpt2-xl``` (listed in the Supported Models) with multiple GPUs. However, when I use 2 GPUs, I get ```Va...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
