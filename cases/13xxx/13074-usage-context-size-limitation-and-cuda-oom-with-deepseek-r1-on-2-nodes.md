# vllm-project/vllm#13074: [Usage]: Context Size Limitation and CUDA OOM with DeepSeek R1 on 2 Nodes (TP8 PP2, 16 GPUs with 141GB VRAM Each)

| 字段 | 值 |
| --- | --- |
| Issue | [#13074](https://github.com/vllm-project/vllm/issues/13074) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 15; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf;oom |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Context Size Limitation and CUDA OOM with DeepSeek R1 on 2 Nodes (TP8 PP2, 16 GPUs with 141GB VRAM Each)

### Issue 正文摘录

### Your current environment When using 2 nodes with 16 GPUs (TP8 PP2), the context size is the same as when using a single node with 8 GPUs (TP8). Setting the context size to 64K in both cases results in a CUDA out of memory error. What could be the reason for this? According to the vLLM documentation, when a single node cannot fit the model, PP (pipeline parallelism) allows deploying the model across multiple nodes. After limiting the number of GPUs per node to 4 using Docker and configuring TP4 PP2, I was indeed able to deploy the R1 model. So, why can't the context length be increased when using TP8 PP2? Theoretically, the available memory should be sufficient to accommodate even two R1 models, so GPU memory shouldn't be the bottleneck limiting the context to 32K. ```bash python3 -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port 9997 --model /mnt/models/DeepSeek-R1-671B --tensor-parallel-size 8 --max-model-len 32768 --trust-remote-code --gpu-memory-utilization 1 --max-num-seqs 1 --served-model-name DeepSeek-R1 python3 -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port 9997 --model /mnt/models/DeepSeek-R1-671B --tensor-parallel-size 8 --pipeline-parallel-size...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: ss multiple nodes. After limiting the number of GPUs per node to 4 using Docker and configuring TP4 PP2, I was indeed able to deploy the R1 model. So, why can't the context length be increased when using TP8 PP2? Theore...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Usage]: Context Size Limitation and CUDA OOM with DeepSeek R1 on 2 Nodes (TP8 PP2, 16 GPUs with 141GB VRAM Each) usage ### Your current environment When using 2 nodes with 16 GPUs (TP8 PP2), the context size is the sam...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: According to the vLLM documentation, when a single node cannot fit the model, PP (pipeline parallelism) allows deploying the model across multiple nodes. After limiting the number of GPUs per node to 4 using Docker and...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: max-num-seqs 1 --served-model-name DeepSeek-R1 ``` ```bash ======== Autoscaler status: 2025-02-10 19:23:38.872862 ======== Node status --------------------------------------------------------------- Active: 1 node_06e3d...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: [Usage]: Context Size Limitation and CUDA OOM with DeepSeek R1 on 2 Nodes (TP8 PP2, 16 GPUs with 141GB VRAM Each) usage ### Your current environment When using 2 nodes with 16 GPUs (TP8 PP2), the context size is the sam...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
