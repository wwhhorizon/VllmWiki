# vllm-project/vllm#1975: Need httpx when running tests

| 字段 | 值 |
| --- | --- |
| Issue | [#1975](https://github.com/vllm-project/vllm/issues/1975) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Need httpx when running tests

### Issue 正文摘录

`python -m pytest tests/` gave me the following error ``` _______________________________________________ ERROR collecting tests/async_engine/test_openai_server.py ________________________________________________ ImportError while importing test module '/home/wyi/w/vllm/tests/async_engine/test_openai_server.py'. Hint: make sure your test modules/packages have valid Python names. Traceback: ../../miniconda3/envs/vllm/lib/python3.9/importlib/__init__.py:127: in import_module return _bootstrap._gcd_import(name[level:], package, level) tests/async_engine/test_openai_server.py:5: in from fastapi.testclient import TestClient ../../miniconda3/envs/vllm/lib/python3.9/site-packages/fastapi/testclient.py:1: in from starlette.testclient import TestClient as TestClient # noqa ../../miniconda3/envs/vllm/lib/python3.9/site-packages/starlette/testclient.py:16: in import httpx E ModuleNotFoundError: No module named 'httpx' ```

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: e/test_openai_server.py ________________________________________________ ImportError while importing test module '/home/wyi/w/vllm/tests/async_engine/test_openai_server.py'. Hint: make sure your test modules/packages ha...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: Need httpx when running tests `python -m pytest tests/` gave me the following error ``` _______________________________________________ ERROR collecting tests/async_engine/test_openai_server.py _________________________...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
