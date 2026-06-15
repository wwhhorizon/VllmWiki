# vllm-project/vllm#7272: [Bug]: OpenGVLab/InternVL2-26B AsyncEngineDeadError: Task finished unexpectedly - value error in merge_vision_embeddings

| 字段 | 值 |
| --- | --- |
| Issue | [#7272](https://github.com/vllm-project/vllm/issues/7272) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;multimodal_vlm |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: OpenGVLab/InternVL2-26B AsyncEngineDeadError: Task finished unexpectedly - value error in merge_vision_embeddings

### Issue 正文摘录

### Your current environment ``` PyTorch version: N/A Is debug build: N/A CUDA used to build PyTorch: N/A ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.22.1 Libc version: glibc-2.35 Python version: 3.11.5 (main, Sep 11 2023, 13:54:46) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-5.15.0-1042-azure-x86_64-with-glibc2.35 Is CUDA available: N/A CUDA runtime version: 12.2.140 CUDA_MODULE_LOADING set to: N/A GPU models and configuration: GPU 0: NVIDIA A100 80GB PCIe GPU 1: NVIDIA A100 80GB PCIe Nvidia driver version: 535.54.03 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: N/A CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 48 bits physical, 48 bits virtual Byte Order: Little Endian CPU(s): 48 On-line CPU(s) list: 0-47 Vendor ID: AuthenticAMD Model name: AMD EPYC 7V13 64-Core Processor CPU family: 25 Model: 1 Thread(s) per core: 1 Core(s) per socket: 48 Socket(s): 1 Stepping: 1 BogoMIPS: 4890.89 Flags: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse...

## 现有链接修复摘要

#7164 [Bugfix] Fix input processor for InternVL2 model | #42056 Bump the minor-update group across 1 directory with 142 updates | #42717 Bump the minor-update group across 1 directory with 143 updates | #43505 Bump the minor-update group across 1 directory with 145 updates | #43993 Bump the minor-update group across 1 directory with 147 updates

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: in merge_vision_embeddings bug ### Your current environment ``` PyTorch version: N/A Is debug build: N/A CUDA used to build PyTorch: N/A ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubun...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: [Bug]: OpenGVLab/InternVL2-26B AsyncEngineDeadError: Task finished unexpectedly - value error in merge_vision_embeddings bug ### Your current environment ``` PyTorch version: N/A Is debug build: N/A CUDA used to build P...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: # Your current environment ``` PyTorch version: N/A Is debug build: N/A CUDA used to build PyTorch: N/A ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ffected Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Not affected Vulnerability Retbleed: Not affected Vulnerability Spec store bypass: Vulnerable Vulnerability Spectre v1: Mitigation; usercopy/sw...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: nd: NIC0: mlx5_an0 ``` ``` ### 🐛 Describe the bug Tried to host and test `OpenGVLab/InternVL2-26B` model using vllm image [v0.5.4](https://hub.docker.com/layers/vllm/vllm-openai/v0.5.4/images/sha256-7ab0cf7b287876cec657...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#7164](https://github.com/vllm-project/vllm/pull/7164) | closes_keyword | 0.95 | [Bugfix] Fix input processor for InternVL2 model | FIX #7272 - This PR also aims to make some small refactor to fix some hidden issues. ~~So I marked it as a draft.~~ - Since most of process args can be obtained from config, th |
| [#42056](https://github.com/vllm-project/vllm/pull/42056) | mentioned | 0.6 | Bump the minor-update group across 1 directory with 142 updates | ease. (<a href="https://redirect.github.com/psf/requests/issues/7272">#7272</a>)</p> </li> </ul> <p><strong>Improvements</strong></p> <ul> <li>Digest Auth hashing algorithms have… |
| [#42717](https://github.com/vllm-project/vllm/pull/42717) | mentioned | 0.6 | Bump the minor-update group across 1 directory with 143 updates | ease. (<a href="https://redirect.github.com/psf/requests/issues/7272">#7272</a>)</p> </li> </ul> <p><strong>Improvements</strong></p> <ul> <li>Digest Auth hashing algorithms have… |
| [#43505](https://github.com/vllm-project/vllm/pull/43505) | mentioned | 0.6 | Bump the minor-update group across 1 directory with 145 updates | ease. (<a href="https://redirect.github.com/psf/requests/issues/7272">#7272</a>)</p> </li> </ul> <p><strong>Improvements</strong></p> <ul> <li>Digest Auth hashing algorithms have… |
| [#43993](https://github.com/vllm-project/vllm/pull/43993) | mentioned | 0.6 | Bump the minor-update group across 1 directory with 147 updates | ease. (<a href="https://redirect.github.com/psf/requests/issues/7272">#7272</a>)</p> </li> </ul> <p><strong>Improvements</strong></p> <ul> <li>Digest Auth hashing algorithms have… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
