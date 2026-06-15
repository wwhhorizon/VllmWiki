# vllm-project/vllm#16581: [Bug]: value unpack mismatch in TP(0.8.3) and EP(0.8.2)

| 字段 | 值 |
| --- | --- |
| Issue | [#16581](https://github.com/vllm-project/vllm/issues/16581) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;moe;speculative_decoding |
| 子分类 | wrong_output |
| Operator 关键词 | cuda;moe;operator;triton |
| 症状 | build_error;crash;mismatch |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: value unpack mismatch in TP(0.8.3) and EP(0.8.2)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When trying to serve mistralai/Mixtral-8x7B-v0.1 on 4 A40s, there is a value unpack mismatch for EP in 0.8.2 and for TP in 0.8.3. I think they are similar problems. Loggings are too long so I only kept a part of them. To reproduce the bugs: For 0.8.2, EP crashes with ValueError: too many values to unpack (expected 12) ``` NCCL_P2P_LEVEL=NVL python -m vllm.entrypoints.openai.api_server --model mistralai/Mixtral-8x7B-v0.1 --tensor-parallel-size 4 --enable-expert-parallel ``` For 0.8.3, TP crashes with ValueError: not enough values to unpack (expected 13, got 12). ``` NCCL_P2P_LEVEL=NVL python -m vllm.entrypoints.openai.api_server --model mistralai/Mixtral-8x7B-v0.1 --tensor-parallel-size 4 ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;hardware_porting;model_support;moe;speculative_decoding cuda;moe;operator;triton build_error;crash;mismatch env_depe...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: value unpack mismatch in TP(0.8.3) and EP(0.8.2) bug ### Your current environment ### 🐛 Describe the bug When trying to serve mistralai/Mixtral-8x7B-v0.1 on 4 A40s, there is a value unpack mismatch for EP in 0.8....
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: [Bug]: value unpack mismatch in TP(0.8.3) and EP(0.8.2) bug ### Your current environment ### 🐛 Describe the bug When trying to serve mistralai/Mixtral-8x7B-v0.1 on 4 A40s, there is a value unpack mismatch for EP in 0.8....
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: er --model mistralai/Mixtral-8x7B-v0.1 --tensor-parallel-size 4 --enable-expert-parallel ``` For 0.8.3, TP crashes with ValueError: not enough values to unpack (expected 13, got 12). ``` NCCL_P2P_LEVEL=NVL python -m vll...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ardware_porting;model_support;moe;speculative_decoding cuda;moe;operator;triton build_error;crash;mismatch env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
