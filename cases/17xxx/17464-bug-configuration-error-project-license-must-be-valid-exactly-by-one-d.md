# vllm-project/vllm#17464: [Bug]: configuration error: project.license must be valid exactly by one definition (2 matches found)

| 字段 | 值 |
| --- | --- |
| Issue | [#17464](https://github.com/vllm-project/vllm/issues/17464) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: configuration error: project.license must be valid exactly by one definition (2 matches found)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug `python3 setup.py develop` ``` Traceback (most recent call last): File "/app/vllmupstream/setup.py", line 688, in setup( File "/usr/local/lib/python3.10/dist-packages/setuptools/_init_.py", line 104, in setup return distutils.core.setup(**attrs) File "/usr/local/lib/python3.10/dist-packages/setuptools/_distutils/core.py", line 158, in setup dist.parse_config_files() File "/usr/local/lib/python3.10/dist-packages/setuptools/dist.py", line 631, in parse_config_files pyprojecttoml.apply_configuration(self, filename, ignore_option_errors) File "/usr/local/lib/python3.10/dist-packages/setuptools/config/pyprojecttoml.py", line 68, in apply_configuration config = read_configuration(filepath, True, ignore_option_errors, dist) File "/usr/local/lib/python3.10/dist-packages/setuptools/config/pyprojecttoml.py", line 129, in read_configuration validate(subset, filepath) File "/usr/local/lib/python3.10/dist-packages/setuptools/config/pyprojecttoml.py", line 57, in validate raise ValueError(f"{error}\n{summary}") from None ValueError: invalid pyproject.toml config: project.license. configuration error: project.license must be valid exactly by on...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ue. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Bug]: configuration error: project.license must be valid exactly by one definition (2 matches found) bug ### Your current environment ### 🐛 Describe the bug `python3 setup.py develop` ``` Traceback (most recent call la...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
