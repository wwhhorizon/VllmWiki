# vllm-project/vllm#613: Run openai server error

| 字段 | 值 |
| --- | --- |
| Issue | [#613](https://github.com/vllm-project/vllm/issues/613) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Run openai server error

### Issue 正文摘录

When I install vllm in the docker environment you provided, the normal server opens fine, but when I try to run the openai server, I get the following error. ``` vllm# python -m vllm.entrypoints.openai.api_server \ > --model facebook/opt-125m Traceback (most recent call last): File "/usr/lib/python3.8/runpy.py", line 194, in _run_module_as_main return _run_code(code, main_globals, None, File "/usr/lib/python3.8/runpy.py", line 87, in _run_code exec(code, run_globals) File "/home/****/origin_vllm/vllm/vllm/entrypoints/openai/api_server.py", line 20, in from vllm.entrypoints.openai.protocol import ( File "/home/****/origin_vllm/vllm/vllm/entrypoints/openai/protocol.py", line 106, in class CompletionResponseChoice(BaseModel): File "pydantic/main.py", line 198, in pydantic.main.ModelMetaclass.__new__ File "pydantic/fields.py", line 506, in pydantic.fields.ModelField.infer File "pydantic/fields.py", line 436, in pydantic.fields.ModelField.__init__ File "pydantic/fields.py", line 552, in pydantic.fields.ModelField.prepare File "pydantic/fields.py", line 661, in pydantic.fields.ModelField._type_analysis File "pydantic/fields.py", line 668, in pydantic.fields.ModelField._type_analysis Fil...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: Run openai server error When I install vllm in the docker environment you provided, the normal server opens fine, but when I try to run the openai server, I get the following error. ``` vllm# python -m vllm.entrypoints....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ing error. ``` vllm# python -m vllm.entrypoints.openai.api_server \ > --model facebook/opt-125m Traceback (most recent call last): File "/usr/lib/python3.8/runpy.py", line 194, in _run_module_as_main return _run_code(co...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
