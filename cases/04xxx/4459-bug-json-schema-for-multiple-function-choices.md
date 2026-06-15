# vllm-project/vllm#4459: [Bug]: JSON Schema for multiple function choices

| 字段 | 值 |
| --- | --- |
| Issue | [#4459](https://github.com/vllm-project/vllm/issues/4459) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: JSON Schema for multiple function choices

### Issue 正文摘录

### Your current environment I apologize but I don't have an easy way to run this right now. I can tell you we are running v0.4.1 and that we are using lmfe for the guided decoding backend. ### 🐛 Describe the bug I believe it should be possible to define some Python functions with differing signatures and enforce a single `guided_json` schema for calling one of those functions. Here is some example Python ```python import inspect from pydantic import create_model def sums(a:int, b:int=1): "Adds a + b" return a + b def subtraction(c:int, d:int=1): "Subtract c - d" return c - d def schema(f): kw = { n: (o.annotation, ... if o.default==inspect.Parameter.empty else o.default) for n, o in inspect.signature(f).parameters.items() } s = create_model(f.__name__, **kw).model_json_schema() return s available_functions = [sums, subtraction] function_schema = { "type": "object", "properties": { "name": { "type": "string", "enum": [f.__name__ for f in available_functions] } }, "oneOf": [ { "properties": { "name": { "const": f.__name__ }, "arguments": schema(f) } } for f in available_functions ], "required": ["name", "arguments"], } ``` And here is the JSON Schema it generates ```json { "type":...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ome example Python ```python import inspect from pydantic import create_model def sums(a:int, b:int=1): "Adds a + b" return a + b def subtraction(c:int, d:int=1): "Subtract c - d" return c - d def schema(f): kw = { n: (...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: we are running v0.4.1 and that we are using lmfe for the guided decoding backend. ### 🐛 Describe the bug I believe it should be possible to define some Python functions with differing signatures and enforce a single `gu...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: calling one of those functions. Here is some example Python ```python import inspect from pydantic import create_model def sums(a:int, b:int=1): "Adds a + b" return a + b def subtraction(c:int, d:int=1): "Subtract c - d...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: = { n: (o.annotation, ... if o.default==inspect.Parameter.empty else o.default) for n, o in inspect.signature(f).parameters.items() } s = create_model(f.__name__, **kw).model_json_schema() return s available_functions =...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
