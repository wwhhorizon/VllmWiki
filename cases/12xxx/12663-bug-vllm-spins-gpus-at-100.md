# vllm-project/vllm#12663: [Bug]: vllm spins gpus at 100%

| 字段 | 值 |
| --- | --- |
| Issue | [#12663](https://github.com/vllm-project/vllm/issues/12663) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm spins gpus at 100%

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Fresh pip install of vllm 7.1 in a new venv on ubuntu 24.04 I'm running: vllm serve /home/bruce/Downloads/models/Qwen2.5-32B-Instruct --tensor-parallel-size 2 --max-model-len 12288 --enforce-eager --port 5000 If I ^C out of vllm and then restart it (first killing any processes still hanging on to gpu vram, there is usually one on gpu 1), first query just spins both gpu's at 100% and never returns. tried prefixing the above with NCCL_P2P_DISABLE=1: vllm serve /home/bruce/Downloads/models/Qwen2.5-32B-Instruct --tensor-parallel-size 2 --max-model-len 12288 --enforce-eager --port 5000 no difference. behavior persists till reboot. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ### Model Input Dumps _No response_ ### 🐛 Describe the bug Fresh pip install of vllm 7.1 in a new venv on ubuntu 24.04 I'm running: vllm serve /home/bruce/Downloads/models/Qwen2.5-32B-Instruct --tensor-parallel-size 2 -...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ot. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: vllm spins gpus at 100% bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Fresh pip install of vllm 7.1 in a new venv on ubuntu 24.04 I'm running: vllm serve /home/bruce/...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ted_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
