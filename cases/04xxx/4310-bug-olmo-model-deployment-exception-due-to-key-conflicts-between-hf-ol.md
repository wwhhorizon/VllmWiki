# vllm-project/vllm#4310: [Bug]: Olmo model deployment exception due to key conflicts between hf_olmo and transformers 4.40.0

| 字段 | 值 |
| --- | --- |
| Issue | [#4310](https://github.com/vllm-project/vllm/issues/4310) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Olmo model deployment exception due to key conflicts between hf_olmo and transformers 4.40.0

### Issue 正文摘录

### 🐛 Describe the bug In Transformers 4.40.x, they introduce olmo as their default supported model and register the model config here: https://github.com/huggingface/transformers/blob/v4.40.1/src/transformers/models/auto/configuration_auto.py#L180 This is in conflict with existing olmo registration in hf_olmo module. (https://github.com/allenai/OLMo/blob/main/hf_olmo/configuration_olmo.py#L41) because they use the same key `olmo` in the config map. while vllm 0.4.x specifies transformers v4.40.x as the dependency, it is still using the `hf_olmo` module, which will cause olmo model deployment to fail. ### Your current environment ```text The output of `python collect_env.py` Collecting environment information... PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0 Clang version: Could not collect CMake version: Could not collect Libc version: glibc-2.31 Python version: 3.10.14 (main, Mar 21 2024, 16:24:04) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-5.10.192-183.736.amzn2.x86_64-x86_64-with-glibc2.31 Is CUDA available: True CUDA...

## 现有链接修复摘要

#4324 [Bugfix][Model] Refactor OLMo model to support new HF format in transformers 4.40.0

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: use they use the same key `olmo` in the config map. while vllm 0.4.x specifies transformers v4.40.x as the dependency, it is still using the `hf_olmo` module, which will cause olmo model deployment to fail. ### Your cur...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: onment information... PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Olmo model deployment exception due to key conflicts between hf_olmo and transformers 4.40.0 bug ### 🐛 Describe the bug In Transformers 4.40.x, they introduce olmo as their default supported model and register th...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: cted Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Not affected Vulnerability Retbleed: Mitigation; untrained return thunk; SMT enabled with STIBP protection Vulnerability Spec rstack overflow: Mit...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: torch==2.1.2 [pip3] torchaudio==2.2.2 [pip3] torchvision==0.17.2 [pip3] triton==2.1.0 [conda] numpy 1.23.5 pypi_0 pypi [conda] nvidia-nccl-cu12 2.18.1 pypi_0 pypi [conda] torch 2.1.2

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4324](https://github.com/vllm-project/vllm/pull/4324) | closes_keyword | 0.95 | [Bugfix][Model] Refactor OLMo model to support new HF format in transformers 4.40.0 | FIX #4310 - #4310 This PR will add support for OLMo models in HF format ([OLMo-1B-hf](https://huggingface.co/allenai/OLMo-1B-hf) and [OLMo-1.7-7B-hf](https://huggingface.co/all |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
