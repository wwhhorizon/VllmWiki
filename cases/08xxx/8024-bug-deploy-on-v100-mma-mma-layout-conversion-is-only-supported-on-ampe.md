# vllm-project/vllm#8024: [Bug]: deploy on V100, mma -> mma layout conversion is only supported on Ampere

| 字段 | 值 |
| --- | --- |
| Issue | [#8024](https://github.com/vllm-project/vllm/issues/8024) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;gemm_linear;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda;kernel;triton |
| 症状 |  |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: deploy on V100, mma -> mma layout conversion is only supported on Ampere

### Issue 正文摘录

### Your current environment There are some related issues #2729 , #6723 ### 🐛 Describe the bug We use vLLM to startup `deepseek-ai/deepseek-coder-33b-instruct` on V100, meet Error follow as . ![image](https://github.com/user-attachments/assets/eabaa197-9659-43c2-90e0-ef29e4d1c290) The current workaround is set to `--enable-chunked-prefill=False`, but this method is unknown to most users. Does vLLM have plans to reimplement the a fwd kernel, support `enable-chunked-prefill` on V100? ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: deploy on V100, mma -> mma layout conversion is only supported on Ampere bug;stale ### Your current environment There are some related issues #2729 , #6723 ### 🐛 Describe the bug We use vLLM to startup `deepseek-...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: deploy on V100, mma -> mma layout conversion is only supported on Ampere bug;stale ### Your current environment There are some related issues #2729 , #6723 ### 🐛 Describe the bug We use vLLM to startup `deepseek-...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: [Bug]: deploy on V100, mma -> mma layout conversion is only supported on Ampere bug;stale ### Your current environment There are some related issues #2729 , #6723 ### 🐛 Describe the bug We use vLLM to startup `deepseek-...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: oy on V100, mma -> mma layout conversion is only supported on Ampere bug;stale ### Your current environment There are some related issues #2729 , #6723 ### 🐛 Describe the bug We use vLLM to startup `deepseek-ai/deepseek...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: tributed_parallel;gemm_linear;hardware_porting;model_support cuda;kernel;triton env_dependency;memory_layout Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
