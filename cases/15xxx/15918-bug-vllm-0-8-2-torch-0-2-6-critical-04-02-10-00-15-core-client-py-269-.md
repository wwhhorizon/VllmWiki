# vllm-project/vllm#15918: [Bug]: 使用vllm 0.8.2 torch 0.2.6版本启动模型报错: CRITICAL 04-02 10:00:15 [core_client.py:269] Got fatal signal from worker processes, shutting down. See stack trace above for root cause issue.rm) 已杀死

| 字段 | 值 |
| --- | --- |
| Issue | [#15918](https://github.com/vllm-project/vllm/issues/15918) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;quantization |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;quantization |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: 使用vllm 0.8.2 torch 0.2.6版本启动模型报错: CRITICAL 04-02 10:00:15 [core_client.py:269] Got fatal signal from worker processes, shutting down. See stack trace above for root cause issue.rm) 已杀死

### Issue 正文摘录

### Your current environment PyTorch version: 2.6.0+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: CentOS Linux 7 (Core) (x86_64) GCC version: (GCC) 12.2.0 Clang version: Could not collect CMake version: Could not collect Libc version: glibc-2.17 Python version: 3.10.12 | packaged by conda-forge | (main, Jun 23 2023, 22:40:32) [GCC 12.3.0] (64-bit runtime) Python platform: Linux-3.10.0-1160.el7.x86_64-x86_64-with-glibc2.17 Is CUDA available: True CUDA runtime version: 12.2.140 ### 🐛 Describe the bug 我使用vllm 0.8.2 torch 0.2.6启动qwen2.5-32n-int4模型，启动命令为: python -m vllm.entrypoints.openai.api_server \ --served-model-name qwen2.5-32n-int4 \ --model qwen2.5-32n-int4 \ --tensor-parallel-size 2 \ --port 8019 \ --dtype float16 \ --enforce-eager \ --trust-remote-code \ --gpu-memory-utilization 0.7 \ --max-model-len 3200 报错为: (VllmWorker rank=0 pid=10003) INFO 04-02 10:00:12 [backends.py:415] Using cache directory: /root/.cache/vllm/torch_compile_cache/68e5addbf5/rank_0_0 for vLLM's torch.compile (VllmWorker rank=0 pid=10003) INFO 04-02 10:00:13 [backends.py:425] Dynamo bytecode transform time: 18.08 s (VllmWorker rank=1 pid=10014) INFO 04-02...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: e for root cause issue.rm) 已杀死 bug ### Your current environment PyTorch version: 2.6.0+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: CentOS Linux 7 (Core) (x86_64) GCC...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: 12.2.140 ### 🐛 Describe the bug 我使用vllm 0.8.2 torch 0.2.6启动qwen2.5-32n-int4模型，启动命令为: python -m vllm.entrypoints.openai.api_server \ --served-model-name qwen2.5-32n-int4 \ --model qwen2.5-32n-int4 \ --tensor-parallel-siz...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: current environment PyTorch version: 2.6.0+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: CentOS Linux 7 (Core) (x86_64) GCC version: (GCC) 12.2.0 Clang version: Could n...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: me version: 12.2.140 ### 🐛 Describe the bug 我使用vllm 0.8.2 torch 0.2.6启动qwen2.5-32n-int4模型，启动命令为: python -m vllm.entrypoints.openai.api_server \ --served-model-name qwen2.5-32n-int4 \ --model qwen2.5-32n-int4 \ --tensor-...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: ) ERROR 04-02 10:00:15 [multiproc_executor.py:379] self.model_runner.profile_run() (VllmWorker rank=0 pid=10003) ERROR 04-02 10:00:15 [multiproc_executor.py:379] File "/root/anaconda3/envs/vllm/lib/python3.10/site-packa...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
