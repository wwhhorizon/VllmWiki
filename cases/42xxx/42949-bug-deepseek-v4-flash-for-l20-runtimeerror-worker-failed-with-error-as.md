# vllm-project/vllm#42949: [Bug]: DeepSeek-V4-Flash for L20,RuntimeError: Worker failed with error 'AssertionError: auto_functionalized was not removed', please check the stack trace above for the root cause

| 字段 | 值 |
| --- | --- |
| Issue | [#42949](https://github.com/vllm-project/vllm/issues/42949) |
| 状态 | open |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;moe;quantization |
| 子分类 | memory |
| Operator 关键词 | cuda;fp8;moe;operator |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: DeepSeek-V4-Flash for L20,RuntimeError: Worker failed with error 'AssertionError: auto_functionalized was not removed', please check the stack trace above for the root cause

### Issue 正文摘录

### Your current environment root@node37:/disk1/DeepSeek-V4-Flash# nvidia-smi Mon May 18 16:25:07 2026 +-----------------------------------------------------------------------------------------+ | NVIDIA-SMI 550.54.15 Driver Version: 550.54.15 CUDA Version: 12.4 | |-----------------------------------------+------------------------+----------------------+ | GPU Name Persistence-M | Bus-Id Disp.A | Volatile Uncorr. ECC | | Fan Temp Perf Pwr:Usage/Cap | Memory-Usage | GPU-Util Compute M. | | | | MIG M. | |=========================================+========================+======================| | 0 NVIDIA L20 Off | 00000000:02:00.0 Off | 0 | | N/A 29C P0 75W / 350W | 0MiB / 46068MiB | 0% Default | | | | N/A | +-----------------------------------------+------------------------+----------------------+ | 1 NVIDIA L20 Off | 00000000:03:00.0 Off | 0 | | N/A 28C P0 77W / 350W | 0MiB / 46068MiB | 0% Default | | | | N/A | +-----------------------------------------+------------------------+----------------------+ | 2 NVIDIA L20 Off | 00000000:82:00.0 Off | 0 | | N/A 27C P0 73W / 350W | 0MiB / 46068MiB | 2% Default | | | | N/A | +-----------------------------------------+----------------------...

## 现有链接修复摘要

#43058 [Fix] Handle auto_functionalized for DeepSeek-V4 MLA fused kernel

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: ----------------------------+ | NVIDIA-SMI 550.54.15 Driver Version: 550.54.15 CUDA Version: 12.4 | |-----------------------------------------+------------------------+----------------------+ | GPU Name Persistence-M |...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: del /models/DeepSeek-V4-Flash --trust-remote-code --kv-cache-dtype fp8 --max-model-len 262144 --tensor-parallel-size 4 --gpu-memory-utilization 0.9 --block-size 256 --enable-expert-parallel --compilation-config '{"cudag...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: # Your current environment root@node37:/disk1/DeepSeek-V4-Flash# nvidia-smi Mon May 18 16:25:07 2026 +-----------------------------------------------------------------------------------------+ | NVIDIA-SMI 550.54.15 Dri...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: --tensor-parallel-size 4 --gpu-memory-utilization 0.9 --block-size 256 --enable-expert-parallel --compilation-config '{"cudagraph_mode":"FULL_AND_PIECEWISE", "custom_ops":["all"]}' --tokenizer-mode deepseek_v4 --reasoni...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: or.py:962] File "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/eval_frame.py", line 873, in aot_compile (Worker_TP0_EP0 pid=279) ERROR 05-18 08:21:14 [multiproc_executor.py:962] return aot_compile_fullgraph( (Wo...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#43058](https://github.com/vllm-project/vllm/pull/43058) | closes_keyword | 0.95 | [Fix] Handle auto_functionalized for DeepSeek-V4 MLA fused kernel | Fixes #42949 ## Root Cause The `fused_deepseek_v4_qnorm_rope_kv_rope_quant_insert` kernel (DeepSeek-V4 MLA attention) mutates `q` and `k_cache` tensors in-place. During `torch.co |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
