# vllm-project/vllm#32172: [Bug]: DeepSeek V3.2 MTP + PD report two errors

| 字段 | 值 |
| --- | --- |
| Issue | [#32172](https://github.com/vllm-project/vllm/issues/32172) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;sampling_logits;speculative_decoding |
| 子分类 | shape_align |
| Operator 关键词 | attention;cuda;moe;operator;sampling;triton |
| 症状 | build_error;mismatch;nan_inf |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: DeepSeek V3.2 MTP + PD report two errors

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When I launch the P/D instances using the following commands: ``` # Prefill vllm serve /gpfs/rd/models/DeepSeek-V3.2 -tp=2 -dp 4 --trust-remote-code --enable-expert-parallel --all2all-backend=deepep_high_throughput --gpu_memory_utilization=0.9 --max-model-len 102400 --tokenizer-mode=deepseek_v32 --enable-eplb --eplb-config '{"window_size":"32","step_interval":"32","num_redundant_experts":"8", "async": "True"}' --kv-transfer-config '{"kv_connector":"NixlConnector","kv_role":"kv_both"}' --num-gpu-blocks-override 2000 --speculative-config.method=mtp --speculative-config.num_speculative_tokens=1 # Decode vllm serve /gpfs/rd/models/DeepSeek-V3.2 -tp=2 --trust-remote-code --enable-expert-parallel --all2all-backend=deepep_low_latency --gpu_memory_utilization=0.9 --max-model-len 102400 --tokenizer-mode=deepseek_v32 --enable-eplb --kv-transfer-config '{"kv_connector":"NixlConnector","kv_role":"kv_both"}' -dp 4 --speculative-config.method=mtp --speculative-config.num_speculative_tokens=1 --num-gpu-blocks-override 2000 # Router python /gpfs/rd/kebe/vllm/tests/v1/kv_connector/nixl_integration/toy_proxy_server.py --prefiller-hosts --decoder-h...

## 候选优化模式

- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 5: e /gpfs/rd/models/DeepSeek-V3.2 -tp=2 -dp 4 --trust-remote-code --enable-expert-parallel --all2all-backend=deepep_high_throughput --gpu_memory_utilization=0.9 --max-model-len 102400 --tokenizer-mode=deepseek_v32 --enabl...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: ug When I launch the P/D instances using the following commands: ``` # Prefill vllm serve /gpfs/rd/models/DeepSeek-V3.2 -tp=2 -dp 4 --trust-remote-code --enable-expert-parallel --all2all-backend=deepep_high_throughput -...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: trust-remote-code --enable-expert-parallel --all2all-backend=deepep_high_throughput --gpu_memory_utilization=0.9 --max-model-len 102400 --tokenizer-mode=deepseek_v32 --enable-eplb --eplb-config '{"window_size":"32","ste...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. correctness attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;sampling_logits;speculative_decoding attention;cuda;moe;...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: 44 ``` Error 2: Assertion failure in fp8_paged_mqa_logits (batch size mismatch) ``` (Worker_DP0_TP1_EP1 pid=978655) ERROR 01-09 15:49:58 [v1/executor/multiproc_executor.py:822] File " .8", line 5, in forward (Worker_DP0...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
