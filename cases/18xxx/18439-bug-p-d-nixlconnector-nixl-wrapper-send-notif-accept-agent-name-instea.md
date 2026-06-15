# vllm-project/vllm#18439: [Bug]: P/D NixlConnector nixl_wrapper send_notif() accept agent_name instead of engine_id

| 字段 | 值 |
| --- | --- |
| Issue | [#18439](https://github.com/vllm-project/vllm/issues/18439) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: P/D NixlConnector nixl_wrapper send_notif() accept agent_name instead of engine_id

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug [`send_notif()`](https://github.com/ai-dynamo/nixl/blob/9f00c7c01a939f6b0e7451299748cfa4af3f17fd/src/api/python/_api.py#L571) of nixl_wrapper should accept the dst agent's name instead of `dst_engine_id`. Current code will lead to the following error: ``` ... File "/home/xxx/vllm/vllm/distributed/kv_transfer/kv_connector/v1/nixl_connector.py", line 965, in _read_blocks self.nixl_wrapper.send_notif(dst_engine_id, File "/home/xxx/anaconda3/envs/nixl/lib/python3.10/site-packages/nixl/_api.py", line 558, in send_notif self.agent.genNotif(remote_agent_name, notif_msg) nixl._bindings.nixlNotFoundError: NIXL_ERR_NOT_FOUND ``` I am using nixl 0.1.1, but it seems the latest nixl (`send_notif()`) has the same interface. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;sampling;triton build_error;na...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ce. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: porting;model_support;sampling_logits;speculative_decoding cuda;sampling;triton build_error;nan_inf env_dependency Your current environment
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: buted/kv_transfer/kv_connector/v1/nixl_connector.py", line 965, in _read_blocks self.nixl_wrapper.send_notif(dst_engine_id, File "/home/xxx/anaconda3/envs/nixl/lib/python3.10/site-packages/nixl/_api.py", line 558, in se...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
