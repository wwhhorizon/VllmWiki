# vllm-project/vllm#1330: baichuan13b vllm upgrade to 0.2.0 load model error

| 字段 | 值 |
| --- | --- |
| Issue | [#1330](https://github.com/vllm-project/vllm/issues/1330) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> baichuan13b vllm upgrade to 0.2.0 load model error

### Issue 正文摘录

Traceback (most recent call last): File "/user/dddd/vllm_infer_baichuan_full.py", line 193, in vllm_model, sampling_params = __init_vllm(parser_paras) File "/user/dddd/vllm_infer_baichuan_full.py", line 148, in __init_vllm llm = LLM(model=args.state_dict_path, File "/user/dpoenv/lib/python3.9/site-packages/vllm/entrypoints/llm.py", line 89, in __init__ self.llm_engine = LLMEngine.from_engine_args(engine_args) File "/user/dpoenv/lib/python3.9/site-packages/vllm/engine/llm_engine.py", line 229, in from_engine_args engine = cls(*engine_configs, File "/user/dpoenv/lib/python3.9/site-packages/vllm/engine/llm_engine.py", line 106, in __init__ self._init_workers_ray(placement_group) File "/user/dpoenv/lib/python3.9/site-packages/vllm/engine/llm_engine.py", line 179, in _init_workers_ray self._run_workers( File "/user/dpoenv/lib/python3.9/site-packages/vllm/engine/llm_engine.py", line 696, in _run_workers all_outputs = ray.get(all_outputs) File "/user/dpoenv/lib/python3.9/site-packages/ray/_private/auto_init_hook.py", line 24, in auto_init_wrapper return fn(*args, **kwargs) File "/user/dpoenv/lib/python3.9/site-packages/ray/_private/client_mode_hook.py", line 103, in wrapper return func(*...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: baichuan13b vllm upgrade to 0.2.0 load model error Traceback (most recent call last): File "/user/dddd/vllm_infer_baichuan_full.py", line 193, in vllm_model, sampling_params = __init_vllm(parser_paras) File "/user/dddd/...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
