# vllm-project/vllm#27464: [Bug]: Crashing when use PIECEWISE compilation

| 字段 | 值 |
| --- | --- |
| Issue | [#27464](https://github.com/vllm-project/vllm/issues/27464) |
| 状态 | closed |
| 标签 | bug;rocm;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization |
| 子分类 | memory |
| Operator 关键词 | cuda;gemm;kernel;moe;operator;quantization;triton |
| 症状 | build_error;crash;oom |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Crashing when use PIECEWISE compilation

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The server crashed after successfully loading weight when I ran deepseek-v3 with blockwise_int8 quantization, I already register matmul as custom op as [issue](https://github.com/vllm-project/vllm/issues/26993) mentioned. It worked on v0.10.0, but now crashed on v0.10.2. After debugging,[ this](https://github.com/vllm-project/vllm/blob/01efc7ef781391e744ed08c3292817a773d654e6/vllm/compilation/backends.py#L179) is where my code crashed on subgraph_0, the compiler is InductorStandaloneAdaptor. I wonder why it crashed? Is there any further code changing required for custom op? Here is my command: ```python VLLM_WORKER_MULTIPROC_METHOD=spawn VLLM_MLA_DISABLE=1 VLLM_USE_TRITON_FLASH_ATTN=1 vllm serve DeepSeek-V3-0324-BF16-Cast-To-Blockwise-Int8 \ --block-size 16 \ --enable-chunked-prefill \ --max-num-seqs 256 \ --max-num-batched-tokens 4096 \ --gpu-memory-utilization 0.97 \ --max-model-len 8192 \ --trust-remote-code \ -tp 8 \ -pp 4 \ --enable-expert-parallel \ --distributed-executor-backend ray ``` Here is error: ``` (EngineCore_DP0 pid=44606) (RayWorkerWrapper pid=13260, ip=192.168.23.8) INFO 10-24 07:37:55 [default_loader.py:268] Lo...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ompilation/backends.py#L179) is where my code crashed on subgraph_0, the compiler is InductorStandaloneAdaptor. I wonder why it crashed? Is there any further code changing required for custom op? Here is my command: ```...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: Crashing when use PIECEWISE compilation bug;rocm;stale ### Your current environment ### 🐛 Describe the bug The server crashed after successfully loading weight when I ran deepseek-v3 with blockwise_int8 quantizat...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: ject/vllm/blob/01efc7ef781391e744ed08c3292817a773d654e6/vllm/compilation/backends.py#L179) is where my code crashed on subgraph_0, the compiler is InductorStandaloneAdaptor. I wonder why it crashed? Is there any further...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: r successfully loading weight when I ran deepseek-v3 with blockwise_int8 quantization, I already register matmul as custom op as [issue](https://github.com/vllm-project/vllm/issues/26993) mentioned. It worked on v0.10.0...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: -max-model-len 8192 \ --trust-remote-code \ -tp 8 \ -pp 4 \ --enable-expert-parallel \ --distributed-executor-backend ray ``` Here is error: ``` (EngineCore_DP0 pid=44606) (RayWorkerWrapper pid=13260, ip=192.168.23.8) I...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
