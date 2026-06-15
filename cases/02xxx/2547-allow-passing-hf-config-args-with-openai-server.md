# vllm-project/vllm#2547: Allow passing hf config args with openai server

| 字段 | 值 |
| --- | --- |
| Issue | [#2547](https://github.com/vllm-project/vllm/issues/2547) |
| 状态 | closed |
| 标签 | good first issue;feature request;unstale |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Allow passing hf config args with openai server

### Issue 正文摘录

Hi, Is there a specific reason for why can't we allow passing of args from the openai server to the HF config class, there are very reasonable use cases where i would want to override the existing args in a config while running the model dynamically though the server. [reference line](https://github.com/vllm-project/vllm/blob/18bfcdd05c657e6997b132488e6f4e74307d6cee/vllm/transformers_utils/config.py#L23) simply allowing `*args` in the openai server that are passed to this while loading the model, i believe there are internal checks for failing if anything configured is wrong anyway. supported documentation in the transformers library: ``` >>> # Change some config attributes when loading a pretrained config. >>> config = AutoConfig.from_pretrained("bert-base-uncased", output_attentions=True, foo=False) >>> config.output_attentions True ```

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: Allow passing hf config args with openai server good first issue;feature request;unstale Hi, Is there a specific reason for why can't we allow passing of args from the openai server to the HF config class, there are ver...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Allow passing hf config args with openai server good first issue;feature request;unstale Hi, Is there a specific reason for why can't we allow passing of args from the openai server to the HF config class, there are ver...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: penai server good first issue;feature request;unstale Hi, Is there a specific reason for why can't we allow passing of args from the openai server to the HF config class, there are very reasonable use cases where i woul...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: onfig.from_pretrained("bert-base-uncased", output_attentions=True, foo=False) >>> config.output_attentions True ```

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
