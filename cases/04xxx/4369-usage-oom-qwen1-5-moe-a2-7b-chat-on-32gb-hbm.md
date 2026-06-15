# vllm-project/vllm#4369: [Usage]: OOM！！Qwen1.5-MoE-A2.7B-Chat on 32GB HBM

| 字段 | 值 |
| --- | --- |
| Issue | [#4369](https://github.com/vllm-project/vllm/issues/4369) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | model_support;moe |
| 子分类 | memory |
| Operator 关键词 | moe |
| 症状 | oom |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: OOM！！Qwen1.5-MoE-A2.7B-Chat on 32GB HBM

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` i have 2 * v100-16G and want to launch this model： https://huggingface.co/Qwen/Qwen1.5-MoE-A2.7B-Chat model weights took 13.3677 * 2 = 27 GB --max-model-len set to 512 then i got OOM on each gpu： allocate 372Mib but 367.12 left ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ft ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. performance model_support;moe moe oom env_dependency Your current environme...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Usage]: OOM！！Qwen1.5-MoE-A2.7B-Chat on 32GB HBM usage ### Your current environment ```text The output of `python collect_env.py` ``` i have 2 * v100-16G and want to launch this model： https://huggingface.co/Qwen/Qwen1....
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Usage]: OOM！！Qwen1.5-MoE-A2.7B-Chat on 32GB HBM usage ### Your current environment ```text The output of `python collect_env.py` ``` i have 2 * v100-16G and want to launch this model： https://huggingface.co/Qwen/Qwen1....
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Usage]: OOM！！Qwen1.5-MoE-A2.7B-Chat on 32GB HBM usage ### Your current environment ```text The output of `python collect_env.py` ``` i have 2 * v100-16G and want to launch this model： https://huggingface.co/Qwen/Qwen1....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
