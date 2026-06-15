# vllm-project/vllm#15630: [Bug]: v1 flash_attn and triton_attn backends don't have `get_state_cls`

| 字段 | 值 |
| --- | --- |
| Issue | [#15630](https://github.com/vllm-project/vllm/issues/15630) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: v1 flash_attn and triton_attn backends don't have `get_state_cls`

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Attempting to run `self.attn_state = self.attn_backend.get_state_cls()(weakref.proxy(self))` with v1 flash_attn or triton_attn backends raises not implemented error. Specifically, from GPU model runner [here](https://github.com/vllm-project/vllm/blob/8958217ad5a6830c4d911e5f15e6eb791df337b6/vllm/worker/model_runner.py#L1071) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: v1 flash_attn or triton_attn backends raises not implemented error. Specifically, from GPU model runner [here](https://github.com/vllm-project/vllm/blob/8958217ad5a6830c4d911e5f15e6eb791df337b6/vllm/worker/model_runner....
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug]: v1 flash_attn and triton_attn backends don't have `get_state_cls` bug;stale ### Your current environment ### 🐛 Describe the bug Attempting to run `self.attn_state = self.attn_backend.get_state_cls()(weakref.proxy...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 71) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ]: v1 flash_attn and triton_attn backends don't have `get_state_cls` bug;stale ### Your current environment ### 🐛 Describe the bug Attempting to run `self.attn_state = self.attn_backend.get_state_cls()(weakref.proxy(sel...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: iton_attn backends raises not implemented error. Specifically, from GPU model runner [here](https://github.com/vllm-project/vllm/blob/8958217ad5a6830c4d911e5f15e6eb791df337b6/vllm/worker/model_runner.py#L1071) ### Befor...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
