# vllm-project/vllm#34180: [Bug]: fastsafetensors distributed loading crashes due to unsorted file list

| 字段 | 值 |
| --- | --- |
| Issue | [#34180](https://github.com/vllm-project/vllm/issues/34180) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | distributed_parallel;model_support |
| 子分类 | wrong_output |
| Operator 关键词 | cuda;kernel;moe |
| 症状 | crash;mismatch;nondeterministic |
| 根因提示 | env_dependency;race_condition |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: fastsafetensors distributed loading crashes due to unsorted file list

### Issue 正文摘录

### Your current environment vLLM version: 0.15.2rc1.dev135+g285bab475 PyTorch: with CUDA 13.1 NCCL: 2.28.9+cuda13.0 Platform: 2x NVIDIA DGX Spark (GB10, aarch64), TP=2 across nodes via InfiniBand OS: DGX OS 7.4.0, kernel 6.17.0-1008-nvidia ### 🐛 Describe the bug `fastsafetensors_weights_iterator` in `weight_utils.py` doesn't sort `hf_weights_files` before splitting the list across ranks for distributed loading. Each node constructs this file list from its local filesystem, and directory enumeration order can vary between nodes. The sub-list splitting then assigns different safetensor shards to each rank, causing mismatched NCCL broadcasts (different tensor sizes at different sequence numbers) followed by SIGABRT. This affects any multi-node tensor parallel deployment using `--load-format fastsafetensors` where the nodes have different storage hardware or filesystem state. It has been reproduced across multiple hardware configurations (NVIDIA DGX Spark, ASUS GD10, MSI Spark variants). Related: #34070 fixed a different `fastsafetensors` issue (device selection and GDS) but did not address file ordering. **How to reproduce** On a 2-node cluster where each node has one GPU: ```bash v...

## 现有链接修复摘要

#34070 [BugFix] Fix `fastsafetensors` TP all procs using all GPUs

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 5: splitting then assigns different safetensor shards to each rank, causing mismatched NCCL broadcasts (different tensor sizes at different sequence numbers) followed by SIGABRT. This affects any multi-node tensor parallel...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: g `fastsafetensors_weights_iterator` in `weight_utils.py` doesn't sort `hf_weights_files` before splitting the list across ranks for distributed loading. Each node constructs this file list from its local filesystem, an...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ent environment vLLM version: 0.15.2rc1.dev135+g285bab475 PyTorch: with CUDA 13.1 NCCL: 2.28.9+cuda13.0 Platform: 2x NVIDIA DGX Spark (GB10, aarch64), TP=2 across nodes via InfiniBand OS: DGX OS 7.4.0, kernel 6.17.0-100...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: crashes due to unsorted file list bug ### Your current environment vLLM version: 0.15.2rc1.dev135+g285bab475 PyTorch: with CUDA 13.1 NCCL: 2.28.9+cuda13.0 Platform: 2x NVIDIA DGX Spark (GB10, aarch64), TP=2 across nodes...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: DEBUG] rank=0, device=cuda:0, num_keys=95, first_5=['model.layers.11.mlp.experts.down_proj_blocks', ...] [FST DEBUG] rank=1, device=cuda:0, num_keys=76, first_5=['lm_head.weight', ...] ``` **Suggested fix** Add one line...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#34070](https://github.com/vllm-project/vllm/pull/34070) | mentioned | 0.45 | [BugFix] Fix `fastsafetensors` TP all procs using all GPUs | urations (nvidia dgx spark, asus gd10, msi spark variants). related: #34070 fixed a different `fastsafetensors` issue (device selection and gds) but did not address file ordering.… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
