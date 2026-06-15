# vllm-project/vllm#35789: [Bug]: CPU OMP thread autobind fails when number of local ranks <= NUMA nodes

| 字段 | 值 |
| --- | --- |
| Issue | [#35789](https://github.com/vllm-project/vllm/issues/35789) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: CPU OMP thread autobind fails when number of local ranks <= NUMA nodes

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I'm trying to launch 4 ranks on 4 nodes, 1 rank per node. With autobind, I expect it to bind OMP threads to NUMA 0 on each node because each rank should have local rank of 0. However, it errors out due to an assertion in `_get_autobind_cpu_ids()`: ```python assert ( len(allowed_numa_nodes) >= self.parallel_config.world_size or sim_multi_numa_nodes ), ( f"Not enough allowed NUMA nodes to bind threads of " f"{self.parallel_config.world_size} CPUWorkers. " f"Allowed NUMA nodes are {allowed_numa_nodes}. " "Please try to bind threads manually." ) ``` It checks number of NUMA nodes against world size, but shouldn't it check local world size? The error can be reproduced using the following command: ```bash vllm serve meta-llama/Llama-3.1-8B-Instruct --tensor-parallel-size 4 --nnodes 4 --node-rank 0 --master-addr ``` Error message: ``` ERROR 03-02 18:40:10 [multiproc_executor.py:783] WorkerProc failed to start. ERROR 03-02 18:40:10 [multiproc_executor.py:783] Traceback (most recent call last): ERROR 03-02 18:40:10 [multiproc_executor.py:783] File "/ai_top_dir/vllm/vllm/v1/executor/multiproc_executor.py", line 754, in worker_main ERROR 03...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling build_error;crash;nan_inf...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: on assert ( len(allowed_numa_nodes) >= self.parallel_config.world_size or sim_multi_numa_nodes ), ( f"Not enough allowed NUMA nodes to bind threads of " f"{self.parallel_config.world_size} CPUWorkers. " f"Allowed NUMA
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 01 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: t world size, but shouldn't it check local world size? The error can be reproduced using the following command: ```bash vllm serve meta-llama/Llama-3.1-8B-Instruct --tensor-parallel-size 4 --nnodes 4 --node-rank 0 --mas...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ts;speculative_decoding cuda;operator;sampling build_error;crash;nan_inf dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
