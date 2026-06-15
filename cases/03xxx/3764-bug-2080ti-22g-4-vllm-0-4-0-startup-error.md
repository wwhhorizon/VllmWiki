# vllm-project/vllm#3764: [Bug]: 2080ti 22G * 4, vllm=0.4.0 startup error

| 字段 | 值 |
| --- | --- |
| Issue | [#3764](https://github.com/vllm-project/vllm/issues/3764) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 28; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf;oom |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: 2080ti 22G * 4, vllm=0.4.0 startup error

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` # For security purposes, please feel free to check the contents of collect_env.py before running it. python collect_env.py --2024-04-01 08:16:40-- https://raw.githubusercontent.com/vllm-project/vllm/main/collect_env.py 正在解析主机 raw.githubusercontent.com (raw.githubusercontent.com)... 2606:50c0:8003::154, 2606:50c0:8002::154, 2606:50c0:8001::154, ... 正在连接 raw.githubusercontent.com (raw.githubusercontent.com)|2606:50c0:8003::154|:443... 已连接。 已发出 HTTP 请求，正在等待回应... 200 OK 长度： 24853 (24K) [text/plain] 正在保存至: ‘collect_env.py’ collect_env.py 100%[===============================================================>] 24.27K 110KB/s 用时 0.2s 2024-04-01 08:16:41 (110 KB/s) - 已保存 ‘collect_env.py’ [24853/24853]) Collecting environment information... PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.29.0 Libc version: glibc-2.35 Python version: 3.9.19 (main, Mar 21 2024, 17:11:28) [GCC 11.2.0] (64-bit runtime) Python platfor...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ct_env.py’ [24853/24853]) Collecting environment information... PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC ver...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: onment information... PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: 10 KB/s) - 已保存 ‘collect_env.py’ [24853/24853]) Collecting environment information... PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: nvironment information... PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 1...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: e Vulnerability Meltdown: Mitigation; PTI Vulnerability Mmio stale data: Mitigation; Clear CPU buffers; SMT vulnerable Vulnerability Retbleed: Not affected Vulnerability Spec rstack overflow: Not affected Vulnerability...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
