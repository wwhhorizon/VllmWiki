# vllm-project/vllm#43811: [Bug]: Multinode no NVLink DEP8 server hangs in CUDA graph replay on MoE models during benchmarking

| 字段 | 值 |
| --- | --- |
| Issue | [#43811](https://github.com/vllm-project/vllm/issues/43811) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | cuda;moe;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Multinode no NVLink DEP8 server hangs in CUDA graph replay on MoE models during benchmarking

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Multinode no NVLink DEP8 topology hangs on `vllm bench serve` when CUDA graph is enabled. Multinode server successfully starts but fails on benchmarking. There is no hang if `--enforce-eager` flag is set. Bug was reproduced on several MoE models: `nvidia/DeepSeek-R1-0528-NVFP4`, `nvidia/Qwen3.5-397B-A17B-NVFP4`, `Qwen/Qwen3.5-35B-A3B`. Not MoE model `Qwen/Qwen3.5-0.8B` does NOT reproduce the bug. Just to highlight: **NVLink is disabled** in this run (`NCCL_MNNVL_ENABLE=0`). Likely related: #17167 (this one failed on server srart, not during benchmarking). ## Reproduce 2 nodes each 4xGB200, multinode run with topology `-tp 1 -pp 1 -dp 8 --enable-expert-parallel` ### Server — node 0 (head) ``` NCCL_MNNVL_ENABLE=0 \ vllm serve Qwen/Qwen3.5-35B-A3B \ --host 0.0.0.0 \ --port 8000 \ --tensor-parallel-size 1 \ --pipeline-parallel-size 1 \ --data-parallel-size 8 \ --data-parallel-start-rank 0 \ --data-parallel-size-local 4 \ --data-parallel-address \ --data-parallel-rpc-port 13345 \ --language-model-only \ --stream-interval 100 \ --no-async-scheduling \ --enable-expert-parallel ``` ### Server — node 1 (headless) ``` NCCL_MNNVL_ENABLE=0 \...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: Multinode no NVLink DEP8 server hangs in CUDA graph replay on MoE models during benchmarking bug ### Your current environment ### 🐛 Describe the bug Multinode no NVLink DEP8 topology hangs on `vllm bench serve` w...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: set. Bug was reproduced on several MoE models: `nvidia/DeepSeek-R1-0528-NVFP4`, `nvidia/Qwen3.5-397B-A17B-NVFP4`, `Qwen/Qwen3.5-35B-A3B`. Not MoE model `Qwen/Qwen3.5-0.8B` does NOT reproduce the bug. Just to highlight:...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Multinode no NVLink DEP8 server hangs in CUDA graph replay on MoE models during benchmarking bug ### Your current environment ### 🐛 Describe the bug Multinode no NVLink DEP8 topology hangs on `vllm bench serve` w...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: [Bug]: Multinode no NVLink DEP8 server hangs in CUDA graph replay on MoE models during benchmarking bug ### Your current environment ### 🐛 Describe the bug Multinode no NVLink DEP8 topology hangs on `vllm bench serve` w...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: (after server is `Application startup complete`) ``` vllm bench serve --backend vllm \ --model Qwen/Qwen3.5-35B-A3B \ --port 8000 --endpoint /v1/completions \ --dataset-name random --random-input 64 --random-output 128...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
