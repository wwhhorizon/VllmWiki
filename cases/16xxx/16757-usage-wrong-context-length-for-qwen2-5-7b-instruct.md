# vllm-project/vllm#16757: [Usage]:  Wrong context length for Qwen2.5-7B-Instruct?

| 字段 | 值 |
| --- | --- |
| Issue | [#16757](https://github.com/vllm-project/vllm/issues/16757) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | model_support |
| 子分类 |  |
| Operator 关键词 | cuda |
| 症状 | mismatch |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]:  Wrong context length for Qwen2.5-7B-Instruct?

### Issue 正文摘录

vllm 0.8.4 -------------------------------------------------- HI all, I met with the following error: The model card of qwen-2.5-7B-instruct has the context length of 128K. But the vllm max_model_len is only 32K? What's wrong? Thanks a lot! --------------------------------------------------- https://huggingface.co/Qwen/Qwen2.5-7B-Instruct [rank3]: File "/home/tom/workspace/myvenv_msswift/lib/python3.10/site-packages/vllm/engine/arg_utils.py", line 1154, in create_engine_config [rank3]: model_config = self.create_model_config() [rank3]: File "/home/tom/workspace/myvenv_msswift/lib/python3.10/site-packages/vllm/engine/arg_utils.py", line 1042, in create_model_config [rank3]: return ModelConfig( [rank3]: File "/home/tom/workspace/myvenv_msswift/lib/python3.10/site-packages/vllm/config.py", line 480, in __init__ [rank3]: self.max_model_len = _get_and_verify_max_len( [rank3]: File "/home/tom/workspace/myvenv_msswift/lib/python3.10/site-packages/vllm/config.py", line 2970, in _get_and_verify_max_len [rank3]: raise ValueError( [rank3]: ValueError: User-specified max_model_len (72000) is greater than the derived max_model_len (max_position_embeddings=32768 or model_max_length=None in mode...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Usage]: Wrong context length for Qwen2.5-7B-Instruct? usage;stale vllm 0.8.4 -------------------------------------------------- HI all, I met with the following error: The model card of qwen-2.5-7B-instruct has the con...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: one in model's config.json). This may lead to incorrect model outputs or CUDA errors. To allow overriding this maximum, set the env var VLLM_ALLOW_LONG_MAX_MODEL_LEN=1 correctness model_support cuda mismatch vllm 0.8.4
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: e env var VLLM_ALLOW_LONG_MAX_MODEL_LEN=1 correctness model_support cuda mismatch vllm 0.8.4
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: rify_max_len [rank3]: raise ValueError( [rank3]: ValueError: User-specified max_model_len (72000) is greater than the derived max_model_len (max_position_embeddings=32768 or model_max_length=None in model's config.json)...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: Wrong context length for Qwen2.5-7B-Instruct? usage;stale vllm 0.8.4 -------------------------------------------------- HI all, I met with the following error: The model card of qwen-2.5-7B-instruct has the con...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
