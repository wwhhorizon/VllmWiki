# vllm-project/vllm#3582: [Bug]: ImportError: cannot import name 'model_validator' from 'pydantic' (/usr/local/lib/python3.10/dist-packages/pydantic/__init__.cpython-310-x86_64-linux-gnu.so)

| 字段 | 值 |
| --- | --- |
| Issue | [#3582](https://github.com/vllm-project/vllm/issues/3582) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: ImportError: cannot import name 'model_validator' from 'pydantic' (/usr/local/lib/python3.10/dist-packages/pydantic/__init__.cpython-310-x86_64-linux-gnu.so)

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug ![微信截图_20240323021712](https://github.com/vllm-project/vllm/assets/16223129/749c18ca-4ad9-45cd-a3e0-91738d75c4c9) `ImportError: cannot import name 'model_validator' from 'pydantic' (/usr/local/lib/python3.10/dist-packages/pydantic/__init__.cpython-310-x86_64-linux-gnu.so)` When I try to start the large language model with vllm, I encounter this error, but I couldn't find any relevant information or resources online. My environment is Docker with Python 3.10.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Bug]: ImportError: cannot import name 'model_validator' from 'pydantic' (/usr/local/lib/python3.10/dist-packages/pydantic/__init__.cpython-310-x86_64-linux-gnu.so) bug ### Your current environment ```text The output of...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: ImportError: cannot import name 'model_validator' from 'pydantic' (/usr/local/lib/python3.10/dist-packages/pydantic/__init__.cpython-310-x86_64-linux-gnu.so) bug ### Your current environment ```text The output of...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
