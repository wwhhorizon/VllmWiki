# vllm-project/vllm#173: ValueError: The precision of the fractional quantity of resource

| 字段 | 值 |
| --- | --- |
| Issue | [#173](https://github.com/vllm-project/vllm/issues/173) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> ValueError: The precision of the fractional quantity of resource

### Issue 正文摘录

## Description I tried the demo code, but got an error like this: ``` File "/opt/miniconda3/lib/python3.8/site-packages/vllm/entrypoints/llm.py", line 55, in __init__ self.llm_engine = LLMEngine.from_engine_args(engine_args) File "/opt/miniconda3/lib/python3.8/site-packages/vllm/engine/llm_engine.py", line 145, in from_engine_args engine = cls(*engine_configs, distributed_init_method, devices, File "/opt/miniconda3/lib/python3.8/site-packages/vllm/engine/llm_engine.py", line 87, in __init__ worker_cls = ray.remote( File "/opt/miniconda3/lib/python3.8/site-packages/ray/_private/worker.py", line 2879, in _make_remote ray_option_utils.validate_actor_options(options, in_options=False) File "/opt/miniconda3/lib/python3.8/site-packages/ray/_private/ray_option_utils.py", line 308, in validate_actor_options actor_options[k].validate(k, v) File "/opt/miniconda3/lib/python3.8/site-packages/ray/_private/ray_option_utils.py", line 38, in validate raise ValueError(possible_error_message) ValueError: The precision of the fractional quantity of resource node:172.17.0.8 cannot go beyond 0.0001 ``` And my code is below: ``` python from vllm import LLM, SamplingParams prompts = [ "Hello, my name is...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ValueError: The precision of the fractional quantity of resource bug ## Description I tried the demo code, but got an error like this: ``` File "/opt/miniconda3/lib/python3.8/site-packages/vllm/entrypoints/llm.py", line...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: e/llm_engine.py", line 145, in from_engine_args engine = cls(*engine_configs, distributed_init_method, devices, File "/opt/miniconda3/lib/python3.8/site-packages/vllm/engine/llm_engine.py", line 87, in __init__ worker_c...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ValueError: The precision of the fractional quantity of resource bug ## Description I tried the demo code, but got an error like this: ``` File "/opt/miniconda3/lib/python3.8/site-packages/vllm/entrypoints/llm.py", line...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ValueError: The precision of the fractional quantity of resource bug ## Description I tried the demo code, but got an error like this: ``` File "/opt/miniconda3/lib/python3.8/site-packages/vllm/entrypoints/llm.py", line...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: remote ray_option_utils.validate_actor_options(options, in_options=False) File "/opt/miniconda3/lib/python3.8/site-packages/ray/_private/ray_option_utils.py", line 308, in validate_actor_options actor_options[k].validat...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
