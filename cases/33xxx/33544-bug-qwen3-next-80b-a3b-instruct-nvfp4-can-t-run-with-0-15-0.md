# vllm-project/vllm#33544: [Bug]: Qwen3-Next-80B-A3B-Instruct-NVFP4 can't run with 0.15.0

| 字段 | 值 |
| --- | --- |
| Issue | [#33544](https://github.com/vllm-project/vllm/issues/33544) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Qwen3-Next-80B-A3B-Instruct-NVFP4 can't run with 0.15.0

### Issue 正文摘录

### Your current environment GPU: NNVIDIA GB10 vllm: 0.15.0 model: RedHatAI/Qwen3-Next-80B-A3B-Instruct-NVFP4 command: vllm serve --model RedHatAI/Qwen3-Next-80B-A3B-Instruct-NVFP4 --gpu-memory-utilization 0.85 --port 8000 --enable-chunked-prefill ### 🐛 Describe the bug ### Using VLLM version 0.14.0, Qwen3-Next-80B-A3B-Instruct-NVFP4 can be run, but when VLLM is updated to 0.15.0, the following error is reported： (EngineCore_DP0 pid=280053) INFO 02-02 14:41:46 [gpu_model_runner.py:4118] Model loading took 44.31 GiB memory and 350.335601 seconds (EngineCore_DP0 pid=280053) INFO 02-02 14:41:51 [backends.py:805] Using cache directory: /home/smc02/.cache/vllm/torch_compile_cache/64c6351b11/rank_0_0/backbone for vLLM's torch.compile (EngineCore_DP0 pid=280053) INFO 02-02 14:41:51 [backends.py:865] Dynamo bytecode transform time: 4.28 s (EngineCore_DP0 pid=280053) [rank0]:W0202 14:41:53.781083 280053 site-packages/torch/_inductor/utils.py:1613] Not enough SMs to use max_autotune_gemm mode (EngineCore_DP0 pid=280053) INFO 02-02 14:41:54 [backends.py:302] Cache the graph of compile range (1, 2048) for later use (EngineCore_DP0 pid=280053) ERROR 02-02 14:41:58 [core.py:946] EngineCore fail...

## 候选优化模式

- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 4: ckages/torch/_inductor/utils.py:1613] Not enough SMs to use max_autotune_gemm mode (EngineCore_DP0 pid=280053) INFO 02-02 14:41:54 [backends.py:302] Cache the graph of compile range (1, 2048) for later use (EngineCore_D...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: Qwen3-Next-80B-A3B-Instruct-NVFP4 can't run with 0.15.0 bug;stale ### Your current environment GPU: NNVIDIA GB10 vllm: 0.15.0 model: RedHatAI/Qwen3-Next-80B-A3B-Instruct-NVFP4 command: vllm serve --model RedHatAI...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: 0053) INFO 02-02 14:41:51 [backends.py:805] Using cache directory: /home/smc02/.cache/vllm/torch_compile_cache/64c6351b11/rank_0_0/backbone for vLLM's torch.compile (EngineCore_DP0 pid=280053) INFO 02-02 14:41:51 [backe...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Qwen3-Next-80B-A3B-Instruct-NVFP4 can't run with 0.15.0 bug;stale ### Your current environment GPU: NNVIDIA GB10 vllm: 0.15.0 model: RedHatAI/Qwen3-Next-80B-A3B-Instruct-NVFP4 command: vllm serve --model RedHatAI...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: DP0 pid=280053) ERROR 02-02 14:41:58 [core.py:946] self.model_runner.profile_run() (EngineCore_DP0 pid=280053) ERROR 02-02 14:41:58 [core.py:946] File "/home/smc02/miniconda3/envs/vLLM15_pt310/lib/python3.10/site-packag...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
