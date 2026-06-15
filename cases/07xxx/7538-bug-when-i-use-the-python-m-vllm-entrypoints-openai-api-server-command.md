# vllm-project/vllm#7538: [Bug]: When I use the `python -m vllm.entrypoints.openai.api_server` command, cannot use multiple gpus

| 字段 | 值 |
| --- | --- |
| Issue | [#7538](https://github.com/vllm-project/vllm/issues/7538) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support |
| 子分类 | memory |
| Operator 关键词 | cuda |
| 症状 | build_error;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: When I use the `python -m vllm.entrypoints.openai.api_server` command, cannot use multiple gpus

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I have 4 A100s on my machine and I want to deploy the llama3.1-70B with them. I used the following command: `CUDA_VISIBLE_DEVICES=0,1,2,3 python -m vllm.entrypoints.openai.api_server --model /ldata/llms/Meta-Llama-3.1-70B-Instruct --device auto --dtype auto --api-key CPMAPI` But there is no multi-card execution, It reported an error: `torch.OutOfMemoryError: CUDA out of memory. ` what should I do？

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ch.OutOfMemoryError: CUDA out of memory. ` what should I do？ performance ci_build;frontend_api;hardware_porting;model_support cuda build_error;oom dtype;env_dependency Your current environment
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ;stale ### Your current environment ### 🐛 Describe the bug I have 4 A100s on my machine and I want to deploy the llama3.1-70B with them. I used the following command: `CUDA_VISIBLE_DEVICES=0,1,2,3 python -m vllm.entrypo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Describe the bug I have 4 A100s on my machine and I want to deploy the llama3.1-70B with them. I used the following command: `CUDA_VISIBLE_DEVICES=0,1,2,3 python -m vllm.entrypoints.openai.api_server --model /ldata/llms...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: server --model /ldata/llms/Meta-Llama-3.1-70B-Instruct --device auto --dtype auto --api-key CPMAPI` But there is no multi-card execution, It reported an error: `torch.OutOfMemoryError: CUDA out of memory. ` what should...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: ce ci_build;frontend_api;hardware_porting;model_support cuda build_error;oom dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
