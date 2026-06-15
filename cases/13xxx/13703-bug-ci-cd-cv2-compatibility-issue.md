# vllm-project/vllm#13703: [Bug][CI/CD] cv2 compatibility issue

| 字段 | 值 |
| --- | --- |
| Issue | [#13703](https://github.com/vllm-project/vllm/issues/13703) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug][CI/CD] cv2 compatibility issue

### Issue 正文摘录

### Your current environment vLLM v0.7.2 ### 🐛 Describe the bug I think it would be better vLLM to fix the OpenCV version. ```bash ImportError while loading conftest 'conftest.py'. tests/conftest.py:26: in from vllm.assets.video import VideoAsset vllm/assets/video.py:7: in import cv2 /usr/local/lib/python3.10/dist-packages/cv2/__init__.py:181: in bootstrap() /usr/local/lib/python3.10/dist-packages/cv2/__init__.py:175: in bootstrap if __load_extra_py_code_for_module("cv2", submodule, DEBUG): /usr/local/lib/python3.10/dist-packages/cv2/__init__.py:28: in __load_extra_py_code_for_module py_module = importlib.import_module(module_name) /usr/local/lib/python3.10/dist-packages/cv2/typing/__init__.py:162: in LayerId = cv2.dnn.DictValue E AttributeError: module 'cv2.dnn' has no attribute 'DictValue' ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Bug][CI/CD] cv2 compatibility issue bug ### Your current environment vLLM v0.7.2 ### 🐛 Describe the bug I think it would be better vLLM to fix the OpenCV version. ```bash ImportError while loading conftest 'conftest.py...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: r vLLM to fix the OpenCV version. ```bash ImportError while loading conftest 'conftest.py'. tests/conftest.py:26: in from vllm.assets.video import VideoAsset vllm/assets/video.py:7: in import cv2 /usr/local/lib/python3....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
