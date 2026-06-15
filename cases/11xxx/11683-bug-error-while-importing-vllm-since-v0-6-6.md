# vllm-project/vllm#11683: [Bug]: Error while importing vllm since v0.6.6

| 字段 | 值 |
| --- | --- |
| Issue | [#11683](https://github.com/vllm-project/vllm/issues/11683) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 18; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;model_support;multimodal_vlm;quantization |
| 子分类 | install |
| Operator 关键词 | cuda;quantization |
| 症状 | crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Error while importing vllm since v0.6.6

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Since v0.6.6, simply running `import vllm` results in the following error due to an issue with `cv2`. vllm was installed using `pip install vllm` inside a Docker container. ``` docker run --gpus all -it --ipc=host nvcr.io/nvidia/pytorch:23.10-py3 ``` While there may be workarounds to make it work, it would be better to ensure that `pip install vllm` works without modifications(for future versions), as it did in previous versions. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: [Bug]: Error while importing vllm since v0.6.6 bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Since v0.6.6, simply running `import vllm` results in the following error due to...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ile importing vllm since v0.6.6 bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Since v0.6.6, simply running `import vllm` results in the following error due to an issue with...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ns. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: . development ci_build;distributed_parallel;model_support;multimodal_vlm;quantization cuda;quantization crash env_dependency Your current environment
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development ci_build;distributed_parallel;model_support;multimodal_vlm;quantization c...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
