# vllm-project/vllm#19077: [Bug]: CUDA error: unknown error when running vllm serve on WSL2 Ubuntu22.04

| 字段 | 值 |
| --- | --- |
| Issue | [#19077](https://github.com/vllm-project/vllm/issues/19077) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;kernel;operator;quantization;triton |
| 症状 | build_error;crash;mismatch;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: CUDA error: unknown error when running vllm serve on WSL2 Ubuntu22.04

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I installed Ubuntu22.04 for WSL2 on Windows10 21H2(19044.3086) and followed the steps in the NVIDA documentation to install the driver. Then I executed 'vllm serve' (Refer to the output information below for parameters) in python==3.11 version of the conda environment after `pip install vllm==0.7.0` (Tsinghua source) . Then, "CUDA error: unknown error" is thrown before loading module. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: .04 bug;stale ### Your current environment ### 🐛 Describe the bug I installed Ubuntu22.04 for WSL2 on Windows10 21H2(19044.3086) and followed the steps in the NVIDA documentation to install the driver. Then I executed '...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: CUDA error: unknown error when running vllm serve on WSL2 Ubuntu22.04 bug;stale ### Your current environment ### 🐛 Describe the bug I installed Ubuntu22.04 for WSL2 on Windows10 21H2(19044.3086) and followed the...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;speculative_decoding attention;cuda;kernel;operator;quantization;triton build_error;crash;mismatch;slowdown dtype;env_dependency;memo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: install the driver. Then I executed 'vllm serve' (Refer to the output information below for parameters) in python==3.11 version of the conda environment after `pip install vllm==0.7.0` (Tsinghua source) . Then, "CUDA er...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: UDA error: unknown error when running vllm serve on WSL2 Ubuntu22.04 bug;stale ### Your current environment ### 🐛 Describe the bug I installed Ubuntu22.04 for WSL2 on Windows10 21H2(19044.3086) and followed the steps in...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
