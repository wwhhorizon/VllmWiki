# vllm-project/vllm#37191: [Bug]: Benchmark tuning MoE kernel config fails due to triton 3.6

| 字段 | 值 |
| --- | --- |
| Issue | [#37191](https://github.com/vllm-project/vllm/issues/37191) |
| 状态 | open |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;gemm;kernel;moe;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Benchmark tuning MoE kernel config fails due to triton 3.6

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug To reproduce: ``` docker run --gpus all --ipc=host \ --entrypoint /bin/bash \ -it vllm/vllm-openai:v0.20.2-aarch64 ``` Then, from inside the container in /vllm-workspace/benchmarks/kernels : `python3 benchmark_moe.py -tp 1 --tune --model "Qwen/Qwen3.6-35B-A3B" ` Results in: ``` INFO 05-12 18:50:00 [nixl_utils.py:20] Setting UCX_RCACHE_MAX_UNRELEASED to '1024' to avoid a rare memory leak in UCX when using NIXL. INFO 05-12 18:50:00 [nixl_utils.py:32] NIXL is available Namespace(model='Qwen/Qwen3.6-35B-A3B', tp_size=1, enable_expert_parallel=False, dtype='auto', use_deep_gemm=False, save_dir='/mnt/fused_moe_configs/', seed=0, batch_size=None, tune=True, trust_remote_code=False, model_prefix=None) Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads. 2026-05-12 18:50:04,471 INFO worker.py:2012 -- Started a local Ray instance. /usr/local/lib/python3.12/site-packages/ray/_private/worker.py:2051: FutureWarning: Tip: In future versions of Ray, Ray will no longer override accelerator visible devices env var if num_gpus=0 or num_gpus=None (default). To enab...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: Your current environment ### 🐛 Describe the bug To reproduce: ``` docker run --gpus all --ipc=host \ --entrypoint /bin/bash \ -it vllm/vllm-openai:v0.20.2-aarch64 ``` Then, from inside the container in /vllm-workspace/b...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: --ipc=host \ --entrypoint /bin/bash \ -it vllm/vllm-openai:v0.20.2-aarch64 ``` Then, from inside the container in /vllm-workspace/benchmarks/kernels : `python3 benchmark_moe.py -tp 1 --tune --model "Qwen/Qwen3.6-35B-A3B...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Benchmark tuning MoE kernel config fails due to triton 3.6 bug ### Your current environment ### 🐛 Describe the bug To reproduce: ``` docker run --gpus all --ipc=host \ --entrypoint /bin/bash \ -it vllm/vllm-opena...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Bug]: Benchmark tuning MoE kernel config fails due to triton 3.6 bug ### Your current environment ### 🐛 Describe the bug To reproduce: ``` docker run --gpus all --ipc=host \ --entrypoint /bin/bash \ -it vllm/vllm-opena...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: espace(model='Qwen/Qwen3.6-35B-A3B', tp_size=1, enable_expert_parallel=False, dtype='auto', use_deep_gemm=False, save_dir='/mnt/fused_moe_configs/', seed=0, batch_size=None, tune=True, trust_remote_code=False, model_pre...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
