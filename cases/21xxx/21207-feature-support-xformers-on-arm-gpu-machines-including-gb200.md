# vllm-project/vllm#21207: [Feature]: Support xformers on ARM GPU machines including GB200.

| 字段 | 值 |
| --- | --- |
| Issue | [#21207](https://github.com/vllm-project/vllm/issues/21207) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;quantization |
| 子分类 | install |
| Operator 关键词 | cuda;fp8 |
| 症状 | build_error |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Support xformers on ARM GPU machines including GB200.

### Issue 正文摘录

### 🚀 The feature, motivation and pitch The official [Dockerfile](https://github.com/vllm-project/vllm/blob/main/docker/Dockerfile) and [requirements file](https://github.com/vllm-project/vllm/blob/main/requirements/cuda.txt) don't include building `xformers` for ARM GPU machines such as GB200 machines. Would it be possible to support `xformers`? This dependency is needed for many models, including meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8. Thank you! ### Alternatives There are existing issues discussing building `xformers` for GH200s: - https://github.com/vllm-project/vllm/issues/15803 - https://github.com/vllm-project/vllm/issues/10459 - https://github.com/vllm-project/vllm/issues/2021 These solutions haven't been incorporated into the official build files. ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: . feature request;stale ### 🚀 The feature, motivation and pitch The official [Dockerfile](https://github.com/vllm-project/vllm/blob/main/docker/Dockerfile) and [requirements file](https://github.com/vllm-project/vllm/bl...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: for many models, including meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8. Thank you! ### Alternatives There are existing issues discussing building `xformers` for GH200s: - https://github.com/vllm-project/vllm/issue...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Feature]: Support xformers on ARM GPU machines including GB200. feature request;stale ### 🚀 The feature, motivation and pitch The official [Dockerfile](https://github.com/vllm-project/vllm/blob/main/docker/Dockerfile)...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: it be possible to support `xformers`? This dependency is needed for many models, including meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8. Thank you! ### Alternatives There are existing issues discussing building `xf...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Support xformers on ARM GPU machines including GB200. feature request;stale ### 🚀 The feature, motivation and pitch The official [Dockerfile](https://github.com/vllm-project/vllm/blob/main/docker/Dockerfile)...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
