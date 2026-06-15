# vllm-project/vllm#2814: Support for Qwen 1.5 on vLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#2814](https://github.com/vllm-project/vllm/issues/2814) |
| 状态 | closed |
| 标签 |  |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Support for Qwen 1.5 on vLLM

### Issue 正文摘录

Currently, this gives this error: ``` 2024-02-08T06:28:20.354023087-08:00 OSError: Can't load the configuration of 'Qwen/Qwen1.5-72B-Chat-AWQ'. If you were trying to load it from 'https://huggingface.co/models', make sure you don't have a local directory with the same name. Otherwise, make sure 'Qwen/Qwen1.5-72B-Chat-AWQ' is the correct path to a directory containing a config.json file ``` Reference implementation: [here](https://runpod.io/gsc?template=ju7oo9mf5w&ref=jmfkcdio)

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: Support for Qwen 1.5 on vLLM Currently, this gives this error: ``` 2024-02-08T06:28:20.354023087-08:00 OSError: Can't load the configuration of 'Qwen/Qwen1.5-72B-Chat-AWQ'. If you were trying to load it from 'https://hu...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
