# vllm-project/vllm#2386: Failed when load a merged Mistral 8x7b model

| 字段 | 值 |
| --- | --- |
| Issue | [#2386](https://github.com/vllm-project/vllm/issues/2386) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Failed when load a merged Mistral 8x7b model

### Issue 正文摘录

I merged a mistal 8x7b model with the lora adapter, and I save the .pt with torch.save(model.state_dict(), 'path_to_model.pt') However, when I use vllm to inference on the new merged model, I failed with this: ``` File "/home/zhh/miniconda3/envs/vllm/lib/python3.9/site-packages/vllm/entrypoints/llm.py", line 93, in __init__ self.llm_engine = LLMEngine.from_engine_args(engine_args) File "/home/zhh/miniconda3/envs/vllm/lib/python3.9/site-packages/vllm/engine/llm_engine.py", line 246, in from_engine_args engine = cls(*engine_configs, File "/home/zhh/miniconda3/envs/vllm/lib/python3.9/site-packages/vllm/engine/llm_engine.py", line 107, in __init__ self._init_workers_ray(placement_group) File "/home/zhh/miniconda3/envs/vllm/lib/python3.9/site-packages/vllm/engine/llm_engine.py", line 194, in _init_workers_ray self._run_workers( File "/home/zhh/miniconda3/envs/vllm/lib/python3.9/site-packages/vllm/engine/llm_engine.py", line 750, in _run_workers self._run_workers_in_batch(workers, method, *args, **kwargs)) File "/home/zhh/miniconda3/envs/vllm/lib/python3.9/site-packages/vllm/engine/llm_engine.py", line 727, in _run_workers_in_batch all_outputs = ray.get(all_outputs) File "/home/zhh/mini...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Failed when load a merged Mistral 8x7b model stale I merged a mistal 8x7b model with the lora adapter, and I save the .pt with torch.save(model.state_dict(), 'path_to_model.pt') However, when I use vllm to inference on...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Failed when load a merged Mistral 8x7b model stale I merged a mistal 8x7b model with the lora adapter, and I save the .pt with torch.save(model.state_dict(), 'path_to_model.pt') However, when I use vllm to inference on...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
