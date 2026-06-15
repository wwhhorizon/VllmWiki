# vllm-project/vllm#3069: NCCL cannot be captured in a graph

| 字段 | 值 |
| --- | --- |
| Issue | [#3069](https://github.com/vllm-project/vllm/issues/3069) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | distributed_parallel;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> NCCL cannot be captured in a graph

### Issue 正文摘录

用一张卡跑7b模型不会报错，用两张卡时报NCCL错误。vllm版本v0.3.2。 command： python -m vllm.entrypoints.openai.api_server --model models/Qwen-14B-Chat --trust-remote-code --port 8509 --served-model-name qwen-14b-chat --dtype float16 --tensor-parallel-size 2 NCCL：NCCL version 2.19.3+cuda11.0 CUDA：11.6 error： NCCL WARN NCCL cannot be captured in a graph if either it wasn't built with CUDA runtime >= 11.3 or if the installed CUDA driver < R465. 看了nvidia官网上nccl的版本，只有三个： ![image](https://github.com/vllm-project/vllm/assets/137265386/df3372bc-8b9c-456d-a6ab-460cd1ca7bb4)

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: l-name qwen-14b-chat --dtype float16 --tensor-parallel-size 2 NCCL：NCCL version 2.19.3+cuda11.0 CUDA：11.6 error： NCCL WARN NCCL cannot be captured in a graph if either it wasn't built with CUDA runtime >= 11.3 or if the...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: Chat --trust-remote-code --port 8509 --served-model-name qwen-14b-chat --dtype float16 --tensor-parallel-size 2 NCCL：NCCL version 2.19.3+cuda11.0 CUDA：11.6 error： NCCL WARN NCCL cannot be captured in a graph if either i...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: 误。vllm版本v0.3.2。 command： python -m vllm.entrypoints.openai.api_server --model models/Qwen-14B-Chat --trust-remote-code --port 8509 --served-model-name qwen-14b-chat --dtype float16 --tensor-parallel-size 2 NCCL：NCCL ver...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: -chat --dtype float16 --tensor-parallel-size 2 NCCL：NCCL version 2.19.3+cuda11.0 CUDA：11.6 error： NCCL WARN NCCL cannot be captured in a graph if either it wasn't built with CUDA runtime >= 11.3 or if the installed CUDA...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
