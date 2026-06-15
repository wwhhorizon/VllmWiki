# vllm-project/vllm#354: Loading Models that require execution of third party code (trust_remote_code=True)

| 字段 | 值 |
| --- | --- |
| Issue | [#354](https://github.com/vllm-project/vllm/issues/354) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 15; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Loading Models that require execution of third party code (trust_remote_code=True)

### Issue 正文摘录

I am trying to load MPT using the AsyncLLMEngine: ``` engine_args = AsyncEngineArgs("mosaicml/mpt-7b-chat", engine_use_ray=True) engine = AsyncLLMEngine.from_engine_args(engine_args) ``` But I am getting this error: `ValueError: Loading mosaicml/mpt-7b-chat-local requires you to execute the configuration file in that repo on your local machine. Make sure you have read the code there to avoid malicious use, then set the option `trust_remote_code=True` to remove this error.` Is there any workaround for this or could it be possible to add the option to trust remote code to EngineArgs?

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Loading Models that require execution of third party code (trust_remote_code=True) bug I am trying to load MPT using the AsyncLLMEngine: ``` engine_args = AsyncEngineArgs("mosaicml/mpt-7b-chat", engine_use_ray=True) eng...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: your local machine. Make sure you have read the code there to avoid malicious use, then set the option `trust_remote_code=True` to remove this error.` Is there any workaround for this or could it be possible to add the...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
