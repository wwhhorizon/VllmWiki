# vllm-project/vllm#734: LLM init baichuan 13B get error "trust_remote_code"

| 字段 | 值 |
| --- | --- |
| Issue | [#734](https://github.com/vllm-project/vllm/issues/734) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> LLM init baichuan 13B get error "trust_remote_code"

### Issue 正文摘录

Tot an unexpected keyword argument 'trust_remote_code', while init model . │ 20 │ if is_vllm: │ │ 21 │ │ # lora_weights = torch.load(os.path.join(lora_weights, 'adapte │ │ 22 │ │ │ │ ❱ 23 │ │ model = LLM(model_dir, dtype='float16',**trust_remote_code=True**) │ │ 24 │ │ │ │ 25 │ │ # lora_merge_unmerge_state_dict(model, lora_weights) │ │ 26 │ │ return tokenizer, model │ │ │ │ /usr/share/python3/lib/python3.9/site-packages/vllm/entrypoints/llm.py:53 in │ │ __init__ │ │ │ │ 50 │ ) -> None: │ │ 51 │ │ if "disable_log_stats" not in kwargs: │ │ 52 │ │ │ kwargs["disable_log_stats"] = True │ │ ❱ 53 │ │ engine_args = EngineArgs( │ │ 54 │ │ │ model=model, │ │ 55 │ │ │ tokenizer=tokenizer, │ │ 56 │ │ │ tokenizer_mode=tokenizer_mode, │ ╰──────────────────────────────────────────────────────────────────────────────╯ **TypeError: __init__() got an unexpected keyword argument 'trust_remote_code'**

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: │ │ ❱ 23 │ │ model = LLM(model_dir, dtype='float16',**trust_remote_code=True**) │ │ 24 │ │ │ │ 25 │ │ # lora_merge_unmerge_state_dict(model, lora_weights) │ │ 26 │
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: code" Tot an unexpected keyword argument 'trust_remote_code', while init model . │ 20 │ if is_vllm: │ │ 21 │ │ # lora_weights = torch.load(os.path.join(lora_weights, 'adapte │ │ 22 │ │

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
