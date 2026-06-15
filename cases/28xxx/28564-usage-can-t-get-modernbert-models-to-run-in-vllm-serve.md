# vllm-project/vllm#28564: [Usage]: Can't get ModernBert models to run in vllm serve

| 字段 | 值 |
| --- | --- |
| Issue | [#28564](https://github.com/vllm-project/vllm/issues/28564) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Can't get ModernBert models to run in vllm serve

### Issue 正文摘录

### Your current environment I am trying to download and use ModernBertModel with the vllm serve feature. At first I thought it was an issue with the model so I switched from trying to use BertEmbed with Alibaba-NLP/gte-modernbert-base since it appears in the docs as a model that supports embedding. Source: https://docs.vllm.ai/en/latest/models/supported_models/#pooling-models I download and run it like this. Download: `huggingface-cli download Alibaba-NLP/gte-modernbert-base --local-dir models/bert --local-dir-use-symlinks False` Serve (example, I have used many iterations): `vllm serve models/bert2 --host 0.0.0.0 --port 8003 --task embed --trust-remote-code --gpu-memory-utilization 0.3` No matter what I get this: Assertion failed, The model should be a generative or pooling model when task is set to 'embedding'. [type=assertion_error, input_value=ArgsKwargs((), {'model': ...rocessor_plugin': None}), input_type=ArgsKwargs] I tried setting runner but that didn't do a thing. I really have no clue why it says this model is supported in the docs. I have searched through other issues and documentation to try out a bunch of solutions but obviously none have worked so far. Been trying t...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Usage]: Can't get ModernBert models to run in vllm serve usage;stale ### Your current environment I am trying to download and use ModernBertModel with the vllm serve feature. At first I thought it was an issue with the...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ibaba-NLP/gte-modernbert-base --local-dir models/bert --local-dir-use-symlinks False` Serve (example, I have used many iterations): `vllm serve models/bert2 --host 0.0.0.0 --port 8003 --task embed --trust-remote-code --...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: have no clue why it says this model is supported in the docs. I have searched through other issues and documentation to try out a bunch of solutions but obviously none have worked so far. Been trying to figure this out...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: P/gte-modernbert-base --local-dir models/bert --local-dir-use-symlinks False` Serve (example, I have used many iterations): `vllm serve models/bert2 --host 0.0.0.0 --port 8003 --task embed --trust-remote-code --gpu-memo...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: Can't get ModernBert models to run in vllm serve usage;stale ### Your current environment I am trying to download and use ModernBertModel with the vllm serve feature. At first I thought it was an issue with the...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
