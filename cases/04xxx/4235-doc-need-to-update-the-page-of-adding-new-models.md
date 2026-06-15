# vllm-project/vllm#4235: [Doc]: Need to update the page of adding new models

| 字段 | 值 |
| --- | --- |
| Issue | [#4235](https://github.com/vllm-project/vllm/issues/4235) |
| 状态 | closed |
| 标签 | documentation |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: Need to update the page of adding new models

### Issue 正文摘录

### 📚 The doc issue https://docs.vllm.ai/en/latest/models/adding_model.html#register-your-model The `_MODEL_REGISTRY ` in [vllm/model_executor/model_loader.py](https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/model_loader.py) was removed, and documentation of registering models needs to update about . Although @esmeetu in https://github.com/vllm-project/vllm/issues/3075#issuecomment-1970071404_ mentioned it will update later but for now it can not accommodate this change yet. ### Suggest a potential alternative/fix Finally, include your `*ForCausalLM` class in [vllm/model_executor/models/\_\_init__.py](https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/models/__init__.py) and register it to the `_MODELS` in [vllm/model_executor/models/\_\_init__.py](https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/models/__init__.py).

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: documentation of registering models needs to update about . Although @esmeetu in https://github.com/vllm-project/vllm/issues/3075#issuecomment-1970071404_ mentioned it will update later but for now it can not accommodat...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Doc]: Need to update the page of adding new models documentation ### 📚 The doc issue https://docs.vllm.ai/en/latest/models/adding_model.html#register-your-model The `_MODEL_REGISTRY ` in [vllm/model_executor/model_load...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: new models documentation ### 📚 The doc issue https://docs.vllm.ai/en/latest/models/adding_model.html#register-your-model The `_MODEL_REGISTRY ` in [vllm/model_executor/model_loader.py](https://github.com/vllm-project/vl...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
