# vllm-project/vllm#1324: Transitive dependency issues causes pip install to hang

| 字段 | 值 |
| --- | --- |
| Issue | [#1324](https://github.com/vllm-project/vllm/issues/1324) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Transitive dependency issues causes pip install to hang

### Issue 正文摘录

## Problem description If you try to `pip install vllm` from a blank system or the docker image `nvcr.io/nvidia/pytorch:22.12-py3` (as recommended in the docs), it will take a very long time to install, and the command appears to hang forever. I think it might be the same issue as in https://github.com/vllm-project/vllm/issues/445. ## Quick solution In the meanwhile, if anyone else is struggling with this issue, I found that the following command fixed the install for me: ```bash pip install typing-extensions==4.5.0 transformers==4.33.1 vllm==0.2.0 ``` ## Potential reasons and fixes In `requirements.txt`, there is: ``` pydantic =4.5.0`](https://github.com/tiangolo/fastapi/blob/0.103.2/pyproject.toml#L46). I also found that `vllm.entrypoints.openai.api_server` only works with `typing-extensions==4.5.0`, otherwise you run into some error like this: ``` Traceback (most recent call last): File "/usr/lib/python3.8/runpy.py", line 194, in _run_module_as_main return _run_code(code, main_globals, None, File "/usr/lib/python3.8/runpy.py", line 87, in _run_code exec(code, run_globals) File "/usr/local/lib/python3.8/dist-packages/vllm/entrypoints/openai/api_server.py", line 21, in from vllm....

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: Transitive dependency issues causes pip install to hang installation ## Problem description If you try to `pip install vllm` from a blank system or the docker image `nvcr.io/nvidia/pytorch:22.12-py3` (as recommended in...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: roject/vllm/issues/445. ## Quick solution In the meanwhile, if anyone else is struggling with this issue, I found that the following command fixed the install for me: ```bash pip install typing-extensions==4.5.0 transfo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: enai/protocol.py", line 111, in class CompletionResponseChoice(BaseModel): File "pydantic/main.py", line 198, in pydantic.main.ModelMetaclass.__new__ File "pydantic/fields.py", line 506, in pydantic.fields.ModelField.in...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
