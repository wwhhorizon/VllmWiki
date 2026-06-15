# vllm-project/vllm#22090: [Feature]: supporting full `torch.compile` mode (`enforce_eager=False`) for `vllm serve --data-parallel-size` on a single-node

| 字段 | 值 |
| --- | --- |
| Issue | [#22090](https://github.com/vllm-project/vllm/issues/22090) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api |
| 子分类 |  |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: supporting full `torch.compile` mode (`enforce_eager=False`) for `vllm serve --data-parallel-size` on a single-node

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Since just python multiprocessing is used and the engines are fully independent, why can't they use the `torch.compile` mode? Also, any Inductor cached artifacts could be shared via file-system (or MEGA cache), right? ``` INFO 08-01 12:18:31 [config.py:1869] Defaulting to use mp for distributed inference INFO 08-01 12:18:31 [config.py:2112] Chunked prefill is enabled with max_num_batched_tokens=8192. INFO 08-01 12:18:31 [cuda.py:156] Data Parallel: Forcing enforce eager to be True since DP is currently not supported with CUDA Graphs. ``` Forced RunLLM's responses are not too helpful https://discuss.vllm.ai/t/vllm-serve-to-use-all-gpus-of-a-single-node-multi-use/1264 :( would prefer to be able to chat with humans... Also its linked issues seem completely unrelated to this question. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Feature]: supporting full `torch.compile` mode (`enforce_eager=False`) for `vllm serve --data-parallel-size` on a single-node feature request ### 🚀 The feature, motivation and pitch Since just python multiprocessing is...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: refill is enabled with max_num_batched_tokens=8192. INFO 08-01 12:18:31 [cuda.py:156] Data Parallel: Forcing enforce eager to be True since DP is currently not supported with CUDA Graphs. ``` Forced RunLLM's responses a...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: r=False`) for `vllm serve --data-parallel-size` on a single-node feature request ### 🚀 The feature, motivation and pitch Since just python multiprocessing is used and the engines are fully independent, why can't they us...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: [Feature]: supporting full `torch.compile` mode (`enforce_eager=False`) for `vllm serve --data-parallel-size` on a single-node feature request ### 🚀 The feature, motivation and pitch Since just python multiprocessing is...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: shared via file-system (or MEGA cache), right? ``` INFO 08-01 12:18:31 [config.py:1869] Defaulting to use mp for distributed inference INFO 08-01 12:18:31 [config.py:2112] Chunked prefill is enabled with max_num_batched...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
