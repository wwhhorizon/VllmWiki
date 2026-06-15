# vllm-project/vllm#14443: [Bug]: External Launcher producing NaN outputs on Large Models when Collocating with Model Training

| 字段 | 值 |
| --- | --- |
| Issue | [#14443](https://github.com/vllm-project/vllm/issues/14443) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support |
| 子分类 | precision |
| Operator 关键词 | cuda;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: External Launcher producing NaN outputs on Large Models when Collocating with Model Training

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug We are observing the following when collocating a relatively large model (e.g. 72B) using external launcher with a model sharding framework (e.g., FSDP). Motivation: for RLHF, collocating is desirable, but when the model is large, we expect to shard both the vllm and model in training so that we can fit into the GPU. - for VLLM, it would be TP (or PP) - for model in training, it would be using a framework like FSDP and DeepSpeed Bug: we are observing NaN's coming from the TPed VLLM model when the model size becomes big. We have a reproduction script in this [gist](https://gist.github.com/fabianlim/66dba9138d399f4c6c70674d92503444) which demostrates the following behavior - in this script, we demonstrate two scenarios, i) the model in train is sharded with FSDP, ii) the model is unsharded. This is controlled by setting `shard_train_model=True` and `False`, respectively. - For demonstration purposes: the model in train is a very small OPT model. In actual use-cases, the model in train is usually the same as the VLLM model. But this is purposely done to make the script runnable in 4 x 80GB GPUs, and also to demonstrate this observat...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Bug]: External Launcher producing NaN outputs on Large Models when Collocating with Model Training bug;stale ### Your current environment ### 🐛 Describe the bug We are observing the following when collocating a relativ...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: respectively. - For demonstration purposes: the model in train is a very small OPT model. In actual use-cases, the model in train is usually the same as the VLLM model. But this is purposely done to make the script runn...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: External Launcher producing NaN outputs on Large Models when Collocating with Model Training bug;stale ### Your current environment ### 🐛 Describe the bug We are observing the following when collocating a relativ...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ld;distributed_parallel;frontend_api;hardware_porting;model_support cuda;triton build_error;nan_inf env_dependency Your current environment
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: unsharded. This is controlled by setting `shard_train_model=True` and `False`, respectively. - For demonstration purposes: the model in train is a very small OPT model. In actual use-cases, the model in train is usually...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
