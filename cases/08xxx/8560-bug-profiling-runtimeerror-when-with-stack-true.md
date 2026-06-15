# vllm-project/vllm#8560: [Bug]: Profiling RuntimeError when `with_stack=True`

| 字段 | 值 |
| --- | --- |
| Issue | [#8560](https://github.com/vllm-project/vllm/issues/8560) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 |  |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Profiling RuntimeError when `with_stack=True`

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Hi there, when I tried to run examples/offline_inference_with_profiler.py, I met the following error `RuntimeError: !stack.empty() INTERNAL ASSERT FAILED at "../torch/csrc/autograd/profiler_python.cpp":969, please report a bug to PyTorch. Python replay stack is empty`. And if I set `with_stack=False` when initializing the profiler, it works fine. The only change I do to the example code is changing the facebook/opt-125m model to my local model Llama-2-7b-hf. Any help will be appreciated😊 ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: opt-125m model to my local model Llama-2-7b-hf. Any help will be appreciated😊 ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom rig...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: or when `with_stack=True` bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Hi there, when I tried to run examples/offline_inference_with_profiler.py, I met the following...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Bug]: Profiling RuntimeError when `with_stack=True` bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Hi there, when I tried to run examples/offline_inference_with_profile
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ed😊 ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Profiling RuntimeError when `with_stack=True` bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Hi there, when I tried to run examples/offline_inference_with_profil...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
