# vllm-project/vllm#8791: [Bug]: Port binding failure when using pp > 1 after commit 7c7714d856eee6fa94aade729b67f00584f72a4c

| 字段 | 值 |
| --- | --- |
| Issue | [#8791](https://github.com/vllm-project/vllm/issues/8791) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 20; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;scheduler_memory |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Port binding failure when using pp > 1 after commit 7c7714d856eee6fa94aade729b67f00584f72a4c

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug After a binary search, I found that after commit 7c7714d856eee6fa94aade729b67f00584f72a4c, the main port binding will fail when pp> 1. But if we only set tp>1, the binding will success. For example: `vllm serve /home/ai/ai/model/Qwen2.5-3B-Instruct/ --served-model-name qwen2.5-3B -pp 2 --trust-remote-code --max-model-len 4096 --enforce-eager --port 18004 --gpu-memory-utilization 1 --preemption-mode swap ` will fail with ERROR: ERROR: [Errno 98] error while attempting to bind on address ('0.0.0.0', 18004): address already in use But `vllm serve /home/ai/ai/model/Qwen2.5-3B-Instruct/ --served-model-name qwen2.5-3B -tp 2 --trust-remote-code --max-model-len 4096 --enforce-eager --port 18004 --gpu-memory-utilization 1 --preemption-mode swap` will run successfully with: INFO: Uvicorn running on http://0.0.0.0:18004 (Press CTRL+C to quit) If we checkout to commit 9d104b5beb7bbb51c64b680e007f39169489ea86 in main branch, we can launch successfully with pp>1 ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corn...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. performance ci_build;distributed_parallel;hardware_porting;model_support;scheduler_memory cuda;operator;triton build_error env_dependency Your current environ...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: del Input Dumps _No response_ ### 🐛 Describe the bug After a binary search, I found that after commit 7c7714d856eee6fa94aade729b67f00584f72a4c, the main port binding will fail when pp> 1. But if we only set tp>1, the bi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: a94aade729b67f00584f72a4c bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug After a binary search, I found that after commit 7c7714d856eee6fa94aade729b67f00584f72a4c, the...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: n using pp > 1 after commit 7c7714d856eee6fa94aade729b67f00584f72a4c bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug After a binary search, I found that after commit 7c7...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: d_parallel;hardware_porting;model_support;scheduler_memory cuda;operator;triton build_error env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
