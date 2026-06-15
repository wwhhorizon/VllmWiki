# vllm-project/vllm#20617: [Bug]: ValueError: There is no module or parameter named 'view_seperator' in DeepseekVLV2ForCausalLM

| 字段 | 值 |
| --- | --- |
| Issue | [#20617](https://github.com/vllm-project/vllm/issues/20617) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;mismatch;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: ValueError: There is no module or parameter named 'view_seperator' in DeepseekVLV2ForCausalLM

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Using the Deepseek VL2 models results in the below error. ```text vllm_server | ERROR 07-08 00:46:53 [core.py:586] ValueError: There is no module or parameter named 'view_seperator' in DeepseekVLV2ForCausalLM ``` This is due to a problem introduced by the spellchecker change last month in commit 2f1c19b2456d4fb15f3475c9db5b077777feab76 Specifically, although obviously Deepseek should have spelled their variable 'view_separator', they did not, they used 'view_seperator'; the typo is in their repo, not VLLM, so the original incorrect spelling needs to be restored for the model to work. I'm about to submit a pull request that reverts the variable name in deepseek_vl2.py. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: change last month in commit 2f1c19b2456d4fb15f3475c9db5b077777feab76 Specifically, although obviously Deepseek should have spelled their variable 'view_separator', they did not, they used 'view_seperator'; the typo is i...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: py. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: needs to be restored for the model to work. I'm about to submit a pull request that reverts the variable name in deepseek_vl2.py. ### Before submitting a new issue... - [x] Make sure you already searched for relevant is...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;mismatch;nan_inf env_dependency Your current environment
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ng_logits;speculative_decoding cuda;operator;sampling;triton build_error;mismatch;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
