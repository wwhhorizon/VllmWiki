# vllm-project/vllm#6562: [Bug]: Failed to import from vllm._C with ImportError("/lib64/libc.so.6: version `GLIBC_2.32' not found

| 字段 | 值 |
| --- | --- |
| Issue | [#6562](https://github.com/vllm-project/vllm/issues/6562) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization |
| 子分类 | env_compat |
| Operator 关键词 | activation;attention;cuda;operator;quantization;triton |
| 症状 | build_error;crash;import_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Failed to import from vllm._C with ImportError("/lib64/libc.so.6: version `GLIBC_2.32' not found

### Issue 正文摘录

### Your current environment ```text (vllm311) [root@instance-bg8ds9yc pengfei]# python vllm/collect_env.py Collecting environment information... WARNING 07-19 14:45:53 _custom_ops.py:14] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'") PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: CentOS Linux release 7.9.2009 (Core) (x86_64) GCC version: (GCC) 4.8.5 20150623 (Red Hat 4.8.5-44) Clang version: Could not collect CMake version: version 3.30.0 Libc version: glibc-2.17 Python version: 3.11.9 (main, Apr 19 2024, 16:48:06) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-3.10.0-1160.102.1.el7.x86_64-x86_64-with-glibc2.17 Is CUDA available: True CUDA runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: Tesla V100-SXM2-32GB GPU 1: Tesla V100-SXM2-32GB Nvidia driver version: 530.30.02 cuDNN version: /root/miniconda3/envs/wizardcoder34/lib/python3.10/site-packages/nvidia/cudnn/lib/libcudnn.so.8 HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: [Bug]: Failed to import from vllm._C with ImportError("/lib64/libc.so.6: version `GLIBC_2.32' not found bug ### Your current environment ```text (vllm311) [root@instance-bg8ds9yc pengfei]# python vllm/collect_env.py Col...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: ule named 'vllm._C'") PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: CentOS Linux release 7.9.2009 (Core) (x86_64) GCC version: (GCC) 4.8.5 201506...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: e-bg8ds9yc pengfei]# python vllm/collect_env.py Collecting environment information... WARNING 07-19 14:45:53 _custom_ops.py:14] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'") PyTorch...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: False, max_prompt_adapters=1, max_prompt_adapter_token=0, device='auto', scheduler_delay_factor=0.0, enable_chunked_prefill=False, speculative_model=None, num_speculative_tokens=None, speculative_draft_tensor_parallel_s...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: n -m vllm.entrypoints.openai.api_server --model Qwen/Qwen2-7B-Instruct --dtype half `` I got this: ```text WARNING 07-19 14:50:28 _custom_ops.py:14] Failed to import from vllm._C with ImportError("/lib64/libc.so.6: vers...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
