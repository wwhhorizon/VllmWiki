# vllm-project/vllm#16004: [Bug] [Misc]: test_sharded_state_loader run failed

| 字段 | 值 |
| --- | --- |
| Issue | [#16004](https://github.com/vllm-project/vllm/issues/16004) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug] [Misc]: test_sharded_state_loader run failed

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When I run test command `VLLM_USE_V1=0 VLLM_WORKER_MULTIPROC_METHOD=spawn pytest -s -v test_sharded_state_loader.py::test_sharded_state_loader`, it failed. The actual reason is the problem of metadata file copying, and I think it is unreasonable to repeatedly download the model in the temporary directory. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits cuda;operator;quantization;sampling;triton...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ry. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: support;quantization;sampling_logits cuda;operator;quantization;sampling;triton build_error;nan_inf env_dependency Your current environment
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: i_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits cuda;operator;quantization;sampling;triton build_error;nan_inf env_dependency Your current environment
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: st_sharded_state_loader`, it failed. The actual reason is the problem of metadata file copying, and I think it is unreasonable to repeatedly download the model in the temporary directory. ### Before submitting a new iss...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
