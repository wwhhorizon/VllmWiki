# vllm-project/vllm#2204: Feature request: add json formating via opanai entrypoint

| 字段 | 值 |
| --- | --- |
| Issue | [#2204](https://github.com/vllm-project/vllm/issues/2204) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Feature request: add json formating via opanai entrypoint

### Issue 正文摘录

Add option to https://github.com/vllm-project/vllm/blob/de60a3fb93957dce6b242299b5d163f02ef7f383/vllm/entrypoints/openai/protocol.py#L82 ` json_format: Union[Boolean, string, None] = None` which False or None says do not force json format, True says format to some json, and string should describe specific json (usind pydantic.schema()) using [lm-format-enforcer](https://github.com/noamgat/lm-format-enforcer)

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: son format, True says format to some json, and string should describe specific json (usind pydantic.schema()) using [lm-format-enforcer](https://github.com/noamgat/lm-format-enforcer)
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: col.py#L82 ` json_format: Union[Boolean, string, None] = None` which False or None says do not force json format, True says format to some json, and string should describe specific json (usind pydantic.schema()) using [...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Feature request: add json formating via opanai entrypoint Add option to https://github.com/vllm-project/vllm/blob/de60a3fb93957dce6b242299b5d163f02ef7f383/vllm/entrypoints/openai/protocol.py#L82 ` json_format: Union[Boo...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Feature request: add json formating via opanai entrypoint Add option to https://github.com/vllm-project/vllm/blob/de60a3fb93957dce6b242299b5d163f02ef7f383/vllm/entrypoints/openai/protocol.py#L82 ` json_format: Union[Boo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
