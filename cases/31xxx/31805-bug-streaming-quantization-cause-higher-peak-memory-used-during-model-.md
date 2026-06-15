# vllm-project/vllm#31805: [Bug]: streaming quantization cause higher peak memory used during model loading and post process

| 字段 | 值 |
| --- | --- |
| Issue | [#31805](https://github.com/vllm-project/vllm/issues/31805) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | memory |
| Operator 关键词 | cuda;fp8;kernel;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;oom |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: streaming quantization cause higher peak memory used during model loading and post process

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I simply print the memory allocation status during model loading w/ and w/o `patched_weight_loader` and can see the peak memory used becomes higher and eventually failed to load. Device: A100 CMD: ``` python3 examples/offline_inference/basic/generate.py --model Qwen/Qwen3-30B-A3B --enforce-eager --dtype=bfloat16 --block-size=64 --max_model_len=2048 --gpu-memory-utilization=0.8 --trust-remote-code --quantization=fp8 ``` w/ `patched_weight_loader`: ``` (EngineCore_DP0 pid=5765) Memory allocated: 1.7814621925354004 (EngineCore_DP0 pid=5765) Memory allocated: 2.9421215057373047 (EngineCore_DP0 pid=5765) Memory allocated: 4.102780818939209 (EngineCore_DP0 pid=5765) Memory allocated: 5.263440132141113 (EngineCore_DP0 pid=5765) Memory allocated: 6.424099445343018 (EngineCore_DP0 pid=5765) Memory allocated: 7.584758758544922 (EngineCore_DP0 pid=5765) Memory allocated: 8.745418071746826 (EngineCore_DP0 pid=5765) Memory allocated: 9.90607738494873 (EngineCore_DP0 pid=5765) Memory allocated: 11.066736698150635 (EngineCore_DP0 pid=5765) Memory allocated: 12.227396011352539 (EngineCore_DP0 pid=5765) Memory allocated: 13.388055324554443 (Engin...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: [Bug]: streaming quantization cause higher peak memory used during model loading and post process bug ### Your current environment ### 🐛 Describe the bug I simply print the memory allocation status during model loading...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: CUDA out of memory. Tried to allocate 384.00 MiB. GPU 0 has a total capacity of 79.25 GiB of which 157.38 MiB is free. Process 1952521 has 8.96 GiB memory in use. Process 1956684 has 70.13 GiB memory in use. Of the allo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: peak memory used becomes higher and eventually failed to load. Device: A100 CMD: ``` python3 examples/offline_inference/basic/generate.py --model Qwen/Qwen3-30B-A3B --enforce-eager --dtype=bfloat16 --block-size=64 --max...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: streaming quantization cause higher peak memory used during model loading and post process bug ### Your current environment ### 🐛 Describe the bug I simply print the memory allocation status during model loading...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: 036) INFO 01-06 03:54:13 [layer.py:366] Enabled separate cuda stream for MoE shared_experts (EngineCore_DP0 pid=6036) INFO 01-06 03:54:13 [fp8.py:168] Using Marlin backend for FP8 MoE (EngineCore_DP0 pid=6036) Memory al...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
