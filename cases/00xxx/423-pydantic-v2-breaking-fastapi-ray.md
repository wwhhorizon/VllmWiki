# vllm-project/vllm#423: Pydantic v2 breaking FastAPI & Ray

| 字段 | 值 |
| --- | --- |
| Issue | [#423](https://github.com/vllm-project/vllm/issues/423) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Pydantic v2 breaking FastAPI & Ray

### Issue 正文摘录

Pydantic v2 came out last week. It seems to be breaking some dependencies, including those used by VLLM. Pydantic v2 throws an error on serializing Ray results, at least pydantic.fields.ModelField. Current VLLM requirements.txt doesn't specify the version of Pydantic, so v2 can get installed. Until requirements.txt gets updated with version for Pydantic or depending libraries fix their compatibilities, you can do "pip install pydantic==1.10.11" to fix issues.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: Ray Pydantic v2 came out last week. It seems to be breaking some dependencies, including those used by VLLM. Pydantic v2 throws an error on serializing Ray results, at least pydantic.fields.ModelField. Current VLLM requ...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: v2 throws an error on serializing Ray results, at least pydantic.fields.ModelField. Current VLLM requirements.txt doesn't specify the version of Pydantic, so v2 can get installed. Until requirements.txt gets updated wit...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
