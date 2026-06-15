# vllm-project/vllm#38033: [Bug]: CPUFusedMOE raises IndexError when running EP across CPU-only nodes

| 字段 | 值 |
| --- | --- |
| Issue | [#38033](https://github.com/vllm-project/vllm/issues/38033) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;moe;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;moe;operator;sampling |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: CPUFusedMOE raises IndexError when running EP across CPU-only nodes

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Launching TP=2 with EP enabled on 2 CPU-only nodes ```python vllm serve Qwen/Qwen1.5-MoE-A2.7B --tensor-parallel-size 2 --enable-expert-parallel --nnodes 2 --node-rank 0 --master-addr vllm serve Qwen/Qwen1.5-MoE-A2.7B --tensor-parallel-size 2 --enable-expert-parallel --nnodes 2 --node-rank 1 --master-addr --headless ``` It fails when warming up the model with the following error message: ```text (Worker_TP0_EP0 pid=45559) ERROR 03-24 20:08:07 [multiproc_executor.py:932] File "/root/venv/lib/python3.12/site-packages/vllm/model_executor/layers/fused_moe/cpu_fused_moe.py", line 446, in cpu_fused_moe_torch (Worker_TP0_EP0 pid=45559) ERROR 03-24 20:08:07 [multiproc_executor.py:932] gate_up = layer.gate_up_linear[i](tokens_for_this_expert) # type: ignore (Worker_TP0_EP0 pid=45559) ERROR 03-24 20:08:07 [multiproc_executor.py:932] ~~~~~~~~~~~~~~~~~~~~^^^ (Worker_TP0_EP0 pid=45559) ERROR 03-24 20:08:07 [multiproc_executor.py:932] IndexError: list index out of range ``` When EP is enabled, it should only be allowed to access experts on its local rank, and gather the outputs from other ranks if needed for following layers. ### Before submit...

## 现有链接修复摘要

#38055 [Bugfix][CPU][v1] Fix IndexError in CPUWorker for multi-node DP/EP on CPU-only nodes

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;hardware_porting;model_support;moe;sampling_logits;speculative_decoding cuda;moe;operator;sampling build_error;nan_i...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: rs. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Launching TP=2 with EP enabled on 2 CPU-only nodes ```python vllm serve Qwen/Qwen1.5-MoE-A2.7B --tensor-parallel-size 2 --enable-expert-parallel --nnodes 2 --node-rank 0 --master-addr vllm serve Qwen/Qwen1.5-MoE-A2.7B -...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [Bug]: CPUFusedMOE raises IndexError when running EP across CPU-only nodes bug ### Your current environment ### 🐛 Describe the bug Launching TP=2 with EP enabled on 2 CPU-only nodes ```python vllm serve Qwen/Qwen1.5-MoE...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: gits;speculative_decoding cuda;moe;operator;sampling build_error;nan_inf dtype;env_dependency #38055 [Bugfix][CPU][v1] Fix IndexError in CPUWorker for multi-node DP/EP on CPU-only nodes Your current environment

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#38055](https://github.com/vllm-project/vllm/pull/38055) | closes_keyword | 0.95 | [Bugfix][CPU][v1] Fix IndexError in CPUWorker for multi-node DP/EP on CPU-only nodes | Fixes #38033 **Problem:** In multi-node DP/EP scenarios, `CPUWorker.init_device()` uses global `self.rank` to index `omp_cpuids_list`, which has been sliced to local scope. Thi |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
