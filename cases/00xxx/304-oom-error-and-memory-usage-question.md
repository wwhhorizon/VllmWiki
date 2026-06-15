# vllm-project/vllm#304: OOM error and memory usage question

| 字段 | 值 |
| --- | --- |
| Issue | [#304](https://github.com/vllm-project/vllm/issues/304) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | model_support |
| 子分类 | memory |
| Operator 关键词 | cuda |
| 症状 | oom |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> OOM error and memory usage question

### Issue 正文摘录

I was trying to use vLLM on a finetined LLaMA 65B model. At first the model is a complete fp32 bin file, i.e., pytorch_model.bin (more than 200GB), and I found this will cause OOM (**not cuda memory**) error even the available memory was more than 1TB. This was be fixed after I split the big file info many small shards, e.g., 00001-00100.bin. So, do we have to use the sliced version when loading super large models? Another observation is that, I execute `free -h` from time to time when loading the model, and the memory usage keeps going up and down, although the general trend is up. Is it a normal phenomenon?

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: orch_model.bin (more than 200GB), and I found this will cause OOM (**not cuda memory**) error even the available memory was more than 1TB. This was be fixed after I split the big file info many small shards, e.g., 00001...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: error and memory usage question I was trying to use vLLM on a finetined LLaMA 65B model. At first the model is a complete fp32 bin file, i.e., pytorch_model.bin (more than 200GB), and I found this will cause OOM (**not...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: y small shards, e.g., 00001-00100.bin. So, do we have to use the sliced version when loading super large models? Another observation is that, I execute `free -h` from time to time when loading the model, and the memory...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: OOM error and memory usage question I was trying to use vLLM on a finetined LLaMA 65B model. At first the model is a complete fp32 bin file, i.e., pytorch_model.bin (more than 200GB), and I found this will cause OOM (**n

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
