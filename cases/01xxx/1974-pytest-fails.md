# vllm-project/vllm#1974: pytest fails

| 字段 | 值 |
| --- | --- |
| Issue | [#1974](https://github.com/vllm-project/vllm/issues/1974) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api |
| 子分类 | install |
| Operator 关键词 | cuda |
| 症状 | import_error |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> pytest fails

### Issue 正文摘录

Following https://github.com/vllm-project/vllm/blob/main/CONTRIBUTING.md#testing, I am running ```shell pip install -e . pip install -r requirements-dev.txt pytest tests/ ``` It prints an error: ``` ImportError while loading conftest '/home/wyi/w/vllm/tests/conftest.py'. File "/home/wyi/w/vllm/tests/conftest.py", line 23 def example_prompts() -> List[str]: ^ SyntaxError: invalid syntax ``` I work on a CUDA server. I can start `api_server.py` and the CURL command returns a reasonable result.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: oject/vllm/blob/main/CONTRIBUTING.md#testing, I am running ```shell pip install -e . pip install -r requirements-dev.txt pytest tests/ ``` It prints an error: ``` ImportError while loading conftest '/home/wyi/w/vllm/tes...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ^ SyntaxError: invalid syntax ``` I work on a CUDA server. I can start `api_server.py` and the CURL command returns a reasonable result. development ci_build;frontend_api cuda import_error Following https://github.com/v...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: pytest fails Following https://github.com/vllm-project/vllm/blob/main/CONTRIBUTING.md#testing, I am running ```shell pip install -e . pip install -r requirements-dev.txt pytest tests/ ``` It prints an error: ``` ImportE

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
