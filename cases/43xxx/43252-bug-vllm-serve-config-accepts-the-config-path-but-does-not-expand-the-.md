# vllm-project/vllm#43252: [Bug]: `vllm serve --config=...` accepts the config path but does not expand the YAML

| 字段 | 值 |
| --- | --- |
| Issue | [#43252](https://github.com/vllm-project/vllm/issues/43252) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: `vllm serve --config=...` accepts the config path but does not expand the YAML

### Issue 正文摘录

### Your current environment ## Environment Reproduced against the latest official CPU release wheel: `vllm==0.21.0+cpu`. ``` Collecting environment information... uv is set ============================== System Info ============================== OS : Ubuntu 24.04.4 LTS (x86_64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0 Clang version : 18.1.3 (1ubuntu1) CMake version : Could not collect Libc version : glibc-2.39 ============================== PyTorch Info ============================== PyTorch version : 2.11.0+cpu Is debug build : False CUDA used to build PyTorch : None ROCM used to build PyTorch : N/A XPU used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.3 (main, Mar 23 2026, 19:04:32) [GCC 13.3.0] (64-bit runtime) Python platform : Linux-6.8.0-111-generic-x86_64-with-glibc2.39 ============================== CPU Info ============================== Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 48 bits physical, 48 bits virtual Byte Order: Little Endian CPU(s): 6 On-line CPU(s) list: 0-5 Vendor ID: AuthenticAMD Model name: AMD EPYC Processor (with IBPB) CPU family: 23...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 10: r current environment ## Environment Reproduced against the latest official CPU release wheel: `vllm==0.21.0+cpu`. ``` Collecting environment information... uv is set ============================== System Info =========...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: h version : 2.11.0+cpu Is debug build : False CUDA used to build PyTorch : None ROCM used to build PyTorch : N/A XPU used to build PyTorch : N/A ============================== Python Environment ========================...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: `vllm serve --config=...` accepts the config path but does not expand the YAML bug ### Your current environment ## Environment Reproduced against the latest official CPU release wheel: `vllm==0.21.0+cpu`. ``` Col...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Not affected Vulnerability Reg file data sampling: Not affected Vulnerability Retbleed: Mitigation; untrained return thunk; SMT disabled Vulnerability...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: pyzmq==27.1.0 [pip3] torch==2.11.0+cpu [pip3] transformers==5.9.0 [pip3] triton==3.7.0 [conda] Could not collect ============================== vLLM Info ============================== ROCM Version : Could not collect v...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
