# vllm-project/vllm#11130: [Bug]: SmolLM2 model not running with fp8 quantization

| 字段 | 值 |
| --- | --- |
| Issue | [#11130](https://github.com/vllm-project/vllm/issues/11130) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;model_support;quantization |
| 子分类 | install |
| Operator 关键词 | fp8;quantization |
| 症状 |  |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: SmolLM2 model not running with fp8 quantization

### Issue 正文摘录

### Your current environment Using latest VLLM docker image with NVIDIA A10 GPU 24 GB. ### Model Input Dumps [vllm_fp8_bug.txt](https://github.com/user-attachments/files/18109854/vllm_fp8_bug.txt) ### 🐛 Describe the bug I am trying to run HuggingFaceTB/SmolLM2-135M-Instruct with latest vllm docker image. I am trying to run with online quantization of fp8. As this is A10 GPU, it says it will run with marlin weight only fp8 quantization. Then the error happens. The same error doesnt happen with facebook/opt-125m model. `./vllm_docker.sh HuggingFaceTB/SmolLM2-135M-Instruct --quantization fp8` Thanks ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: 8 quantization bug;stale ### Your current environment Using latest VLLM docker image with NVIDIA A10 GPU 24 GB. ### Model Input Dumps [vllm_fp8_bug.txt](https://github.com/user-attachments/files/18109854/vllm_fp8_bug.tx...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: SmolLM2 model not running with fp8 quantization bug;stale ### Your current environment Using latest VLLM docker image with NVIDIA A10 GPU 24 GB. ### Model Input Dumps [vllm_fp8_bug.txt](https://github.com/user-at...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: SmolLM2 model not running with fp8 quantization bug;stale ### Your current environment Using latest VLLM docker image with NVIDIA A10 GPU 24 GB. ### Model Input Dumps [vllm_fp8_bug.txt](https://github.com/user-at...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: SmolLM2 model not running with fp8 quantization bug;stale ### Your current environment Using latest VLLM docker image with NVIDIA A10 GPU 24 GB. ### Model Input Dumps [vllm_fp8_bug.txt](https://github.com/user-at...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: SmolLM2 model not running with fp8 quantization bug;stale ### Your current environment Using latest VLLM docker image with NVIDIA A10 GPU 24 GB. ### Model Input Dumps [vllm_fp8_bug.txt](https://github.com/user-at...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
