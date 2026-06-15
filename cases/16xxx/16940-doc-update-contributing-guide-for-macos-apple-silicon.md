# vllm-project/vllm#16940: [Doc]: update contributing guide for macOS Apple silicon

| 字段 | 值 |
| --- | --- |
| Issue | [#16940](https://github.com/vllm-project/vllm/issues/16940) |
| 状态 | closed |
| 标签 | documentation |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: update contributing guide for macOS Apple silicon

### Issue 正文摘录

### 📚 The doc issue https://docs.vllm.ai/en/stable/contributing/overview.html doesn't work on macOS Apple silicon. https://docs.vllm.ai/en/latest/getting_started/installation/cpu.html?device=apple#build-wheel-from-source works but `requirements/dev.txt` isn't compatible. ```shell $ pip install -r requirements/dev.txt Collecting pre-commit==4.0.1 (from -r /Users/dxia/src/github.com/vllm-project/vllm/requirements/lint.txt (line 2)) Downloading pre_commit-4.0.1-py2.py3-none-any.whl.metadata (1.3 kB) Collecting absl-py==2.1.0 (from -r /Users/dxia/src/github.com/vllm-project/vllm/requirements/test.txt (line 3)) Downloading absl_py-2.1.0-py3-none-any.whl.metadata (2.3 kB) Collecting accelerate==1.0.1 (from -r /Users/dxia/src/github.com/vllm-project/vllm/requirements/test.txt (line 5)) Downloading accelerate-1.0.1-py3-none-any.whl.metadata (19 kB) Collecting aiohappyeyeballs==2.4.3 (from -r /Users/dxia/src/github.com/vllm-project/vllm/requirements/test.txt (line 9)) Downloading aiohappyeyeballs-2.4.3-py3-none-any.whl.metadata (6.1 kB) Collecting aiohttp==3.10.11 (from -r /Users/dxia/src/github.com/vllm-project/vllm/requirements/test.txt (line 11)) Downloading aiohttp-3.10.11-cp312-cp312-...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: on macOS Apple silicon. https://docs.vllm.ai/en/latest/getting_started/installation/cpu.html?device=apple#build-wheel-from-source works but `requirements/dev.txt` isn't compatible. ```shell $ pip install -r requirements...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: `pip install pre-commit==4.0.1`, running pre-commit fails because `runai-model-streamer` [doesn't have a Mac wheel](https://pypi.org/project/runai-model-streamer/#files). ```shell $ pre-commit run --all-files --show-dif...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: s/lint.txt (line 2)) Downloading pre_commit-4.0.1-py2.py3-none-any.whl.metadata (1.3 kB) Collecting absl-py==2.1.0 (from -r /Users/dxia/src/github.com/vllm-project/vllm/requirements/test.txt (line 3)) Downloading absl_p...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: local:mypy==1.11.1,types-cachetools,types-setuptools,types-PyYAML,types-requests. [INFO] Installing environment for https://github.com/google/yapf. [INFO] Once installed this environment will be reused. [INFO] This may...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
