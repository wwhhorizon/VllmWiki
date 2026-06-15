# vllm-project/vllm#34028: [Usage]: Unable to load Mistral-Small-3.2-24B-Instruct-2506-FP8 due to "Value error, Found unknown quantization", but the same configs worked for vllm v0.11.0

| 字段 | 值 |
| --- | --- |
| Issue | [#34028](https://github.com/vllm-project/vllm/issues/34028) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Unable to load Mistral-Small-3.2-24B-Instruct-2506-FP8 due to "Value error, Found unknown quantization", but the same configs worked for vllm v0.11.0

### Issue 正文摘录

### Your current environment ```text python collect_env.py --2026-02-06 23:27:52-- https://raw.githubusercontent.com/vllm-project/vllm/main/vllm/collect_env.py Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 185.199.108.133, 185.199.109.133, 185.199.110.133, ... Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|185.199.108.133|:443... connected. HTTP request sent, awaiting response... 200 OK Length: 27835 (27K) [text/plain] Saving to: ‘collect_env.py’ collect_env.py 100%[=====================================================================================================================================================>] 27.18K --.-KB/s in 0.001s 2026-02-06 23:27:52 (37.3 MB/s) - ‘collect_env.py’ saved [27835/27835] Collecting environment information... uv is set ============================== System Info ============================== OS : Rocky Linux 9.7 (Blue Onyx) (x86_64) GCC version : (GCC) 11.5.0 20240719 (Red Hat 11.5.0-11) Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.34 ============================== PyTorch Info ============================== PyTorch version : 2.9.1+cu128 Is debug build : F...

## 现有链接修复摘要

#34104 Fix Mistral config remap to accept compressed-tensors quantization #34028

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: OS : Rocky Linux 9.7 (Blue Onyx) (x86_64) GCC version : (GCC) 11.5.0 20240719 (Red Hat 11.5.0-11) Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.34 ==========
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Usage]: Unable to load Mistral-Small-3.2-24B-Instruct-2506-FP8 due to "Value error, Found unknown quantization", but the same configs worked for vllm v0.11.0 usage ### Your current environment ```text python collect_en...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: === Versions of relevant libraries ============================== [pip3] flashinfer-python==0.6.1 [pip3] numpy==2.2.6 [pip3] nvidia-cublas-cu12==12.8.4.1 [pip3] nvidia-cuda-cupti-cu12==12.8.90 [pip3] nvidia-cuda-nvrtc-c...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Usage]: Unable to load Mistral-Small-3.2-24B-Instruct-2506-FP8 due to "Value error, Found unknown quantization", but the same configs worked for vllm v0.11.0 usage ### Your current environment ```text python collect_en...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: -2506-FP8 due to "Value error, Found unknown quantization", but the same configs worked for vllm v0.11.0 usage ### Your current environment ```text python collect_env.py --2026-02-06 23:27:52-- https://raw.githubusercon...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#34104](https://github.com/vllm-project/vllm/pull/34104) | closes_keyword | 0.95 | Fix Mistral config remap to accept compressed-tensors quantization #34028 | fixed #34028 ## Test Plan ``` python -m vllm.entrypoints.openai.api_server \ --model stelterlab/Mistral-Small-3.2-24B-Instruct-2506-FP8 \ --dtype auto \ --gpu-memory-utilizat |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
