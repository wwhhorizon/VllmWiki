# vllm-project/vllm#28228: [Bug]: Kimi Linear KV cache size estimation and usage not making sens

| 字段 | 值 |
| --- | --- |
| Issue | [#28228](https://github.com/vllm-project/vllm/issues/28228) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf;oom;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Kimi Linear KV cache size estimation and usage not making sens

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Running AWQ version of Kimi-Linear-48B-A3B-Instruct on 2x3090. KV cache calculations and NVRAM usage seems problematic. I can't get more than `--max_num_batched_tokens 64000` or it OOM with `--max_model_len 120000`. But I can run `--max_model_len 74000 --max_num_batched_tokens 74000` to work. The math doesn't seem right. Or am I misunderstanding the MLA+Linear KV cache calculations ? Does concurrency with Linear have any advantages that should be result in lesser KV usage and thus the calculations of the maximum number of concurrency tokens is different ? Is this accounted for ? Why would there only be 2.30GiB for KV cache while GPU NVRAM has 19GiB per card used with the rest free ? Is it per card since it's ` --tensor_parallel 2` ? ``` PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True VLLM_USE_V1=1 CUDA_VISIBLE_DEVICES=0,1 \ vllm serve cyankiwi/Kimi-Linear-48B-A3B-Instruct-AWQ-4bit \ --port 8111--gpu-memory-utilization 0.95 --max_model_len 120000 --tensor_parallel 2 --enable_prefix_caching \ --max_num_batched_tokens 64000 --max-num-seqs 8 --trust-remote-code --enable-auto-tool-choice --tool-call-parser kimi_k2 \ --served-model-na...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: Bug]: Kimi Linear KV cache size estimation and usage not making sens bug;stale ### Your current environment ### 🐛 Describe the bug Running AWQ version of Kimi-Linear-48B-A3B-Instruct on 2x3090. KV cache calculations and...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ale ### Your current environment ### 🐛 Describe the bug Running AWQ version of Kimi-Linear-48B-A3B-Instruct on 2x3090. KV cache calculations and NVRAM usage seems problematic. I can't get more than `--max_num_batched_to...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: --served-model-name Kimi-Linear-48B-A3B-Instruct --api-key local --dtype float16 ``` ```terminal ... (Worker_TP0 pid=26347) INFO 11-06 10:51:24 [gpu_model_runner.py:3012] Model loading took 14.2491 GiB and 25.774743 sec...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: --max-num-seqs 8` : ``` ... (Worker_TP0 pid=31984) INFO 11-06 11:12:22 [backends.py:281] Compiling a graph for dynamic shape takes 5.95 s (Worker_TP0 pid=31984) INFO 11-06 11:12:26 [monitor.py:34] torch.compile takes 13...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: t free ? Is it per card since it's ` --tensor_parallel 2` ? ``` PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True VLLM_USE_V1=1 CUDA_VISIBLE_DEVICES=0,1 \ vllm serve cyankiwi/Kimi-Linear-48B-A3B-Instruct-AWQ-4bit \

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
