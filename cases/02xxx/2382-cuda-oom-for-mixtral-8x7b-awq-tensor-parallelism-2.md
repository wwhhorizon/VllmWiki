# vllm-project/vllm#2382: CUDA OOM for Mixtral 8x7B AWQ Tensor Parallelism 2

| 字段 | 值 |
| --- | --- |
| Issue | [#2382](https://github.com/vllm-project/vllm/issues/2382) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;model_support;quantization |
| 子分类 | race_cond |
| Operator 关键词 | cuda;quantization |
| 症状 | mismatch;oom |
| 根因提示 | dtype;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> CUDA OOM for Mixtral 8x7B AWQ Tensor Parallelism 2

### Issue 正文摘录

I am trying to run TheBloke/Mixtral-8x7B-Instruct-v0.1-AWQ with 2 x A10 GPUs ``` docker run --shm-size 10gb -it --rm --gpus all -v /data/:/data/ vllm/vllm-openai:v0.2.7 --model TheBloke/Mixtral-8x7B-Instruct-v0.1-AWQ --quantization awq --dtype auto --enforce-eager --disable-log-requests --tensor-parallel-size 2 --download-dir /data/ ``` and while theoretically, it should fit it runs into CUDA OOM I already looked at this: https://github.com/vllm-project/vllm/issues/2312 Interestingly, if I try it on 2 x A100 80GB but with `--gpu-memory-utilization 0.5`, it fits fine and settles to ``` # GPU blocks: 6487, # CPU blocks: 4096 ``` ``` +-----------------------------------------------------------------------------+ | Processes: | | GPU GI CI PID Type Process name GPU Memory | | ID ID Usage | |=============================================================================| | 0 N/A N/A 86918 C python3 20238MiB | | 1 N/A N/A 89935 C ray::RayWorkerVllm 20238MiB | +-----------------------------------------------------------------------------+ ``` It should be able to run fine with 2 x A10 GB too. But even on 2 x A100 80 GB it cannot load with `--gpu-memory-utilization 0.3` or `--gpu-memory-uti...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ng to run TheBloke/Mixtral-8x7B-Instruct-v0.1-AWQ with 2 x A10 GPUs ``` docker run --shm-size 10gb -it --rm --gpus all -v /data/:/data/ vllm/vllm-openai:v0.2.7 --model TheBloke/Mixtral-8x7B-Instruct-v0.1-AWQ --quantizat...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: CUDA OOM for Mixtral 8x7B AWQ Tensor Parallelism 2 I am trying to run TheBloke/Mixtral-8x7B-Instruct-v0.1-AWQ with 2 x A10 GPUs ``` docker run --shm-size 10gb -it --rm --gpus all -v /data/:/data/ vllm/vllm-openai:v0.2.7
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: CUDA OOM for Mixtral 8x7B AWQ Tensor Parallelism 2 I am trying to run TheBloke/Mixtral-8x7B-Instruct-v0.1-AWQ with 2 x A10 GPUs ``` docker run --shm-size 10gb -it --rm --gpus all -v /data/:/data/ vllm/vllm-openai:v0.2.7...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: lm/vllm-openai:v0.2.7 --model TheBloke/Mixtral-8x7B-Instruct-v0.1-AWQ --quantization awq --dtype auto --enforce-eager --disable-log-requests --tensor-parallel-size 2 --download-dir /data/ ``` and while theoretically, it...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: h `--gpu-memory-utilization 0.5`, it fits fine and settles to ``` # GPU blocks: 6487, # CPU blocks: 4096 ``` ``` +-----------------------------------------------------------------------------+ | Processes: | | GPU GI CI

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
