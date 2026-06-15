# vllm-project/vllm#484: Docker Issue

| 字段 | 值 |
| --- | --- |
| Issue | [#484](https://github.com/vllm-project/vllm/issues/484) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Docker Issue

### Issue 正文摘录

dockerfile: ``` FROM nvcr.io/nvidia/pytorch:22.12-py3 RUN pip uninstall torch -y RUN pip install vllm RUN pip install pydantic==1.10.11 RUN pip install fschat ``` The native api server was running fine -- ``` python -m vllm.entrypoints.api_server \ --model stabilityai/stablelm-tuned-alpha-7b \ --tensor-parallel-size 2 \ --host 0.0.0.0 ``` Openapi server comes with this issue -- ``` python -m vllm.entrypoints.openai.api_server \ --model stabilityai/stablelm-tuned-alpha-7b \ --tensor-parallel-size 2 \ --host 0.0.0.0 ``` transformer_engine_extensions.cpython-38-x86_64-linux-gnu.so error ^

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: Docker Issue installation dockerfile: ``` FROM nvcr.io/nvidia/pytorch:22.12-py3 RUN pip uninstall torch -y RUN pip install vllm RUN pip install pydantic==1.10.11 RUN pip install fschat ``` The native api server was runn
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: server was running fine -- ``` python -m vllm.entrypoints.api_server \ --model stabilityai/stablelm-tuned-alpha-7b \ --tensor-parallel-size 2 \ --host 0.0.0.0 ``` Openapi server comes with this issue -- ``` python -m vl...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
