# vllm-project/vllm#5803: [Misc]: vLLM logger disables other existing loggers by default

| 字段 | 值 |
| --- | --- |
| Issue | [#5803](https://github.com/vllm-project/vllm/issues/5803) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc]: vLLM logger disables other existing loggers by default

### Issue 正文摘录

### Anything you want to discuss about vllm. ## Issue The current default behavior of the logger in vLLM is to disable all other existing loggers. This can prevent logs from being outputted from other code that is defined/imported before vLLM is imported. ## Details The default logging config defined [here](https://github.com/vllm-project/vllm/blob/1744cc99ba9bdefea8f3f798cf51ed650b81a98e/vllm/logger.py#L22-L46) does not include `disable_existing_loggers=False`. When using logging.dictConfig() to configure logging, this value is set to True by default for backwards compatibility. Unless this is the intended behavior, I believe this key should be added to the configuration dictionary. Happy to add this small change if maintainers agree with this. Thank you!

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: is can prevent logs from being outputted from other code that is defined/imported before vLLM is imported. ## Details The default logging config defined [here](https://github.com/vllm-project/vllm/blob/1744cc99ba9bdefea...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: key should be added to the configuration dictionary. Happy to add this small change if maintainers agree with this. Thank you!
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: 98e/vllm/logger.py#L22-L46) does not include `disable_existing_loggers=False`. When using logging.dictConfig() to configure logging, this value is set to True by default for backwards compatibility. Unless this is the i...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: efined/imported before vLLM is imported. ## Details The default logging config defined [here](https://github.com/vllm-project/vllm/blob/1744cc99ba9bdefea8f3f798cf51ed650b81a98e/vllm/logger.py#L22-L46) does not include `...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
