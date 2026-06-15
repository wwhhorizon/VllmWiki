# vllm-project/vllm#23739: [Performance]: The full cudagraph seems not work.

| 字段 | 值 |
| --- | --- |
| Issue | [#23739](https://github.com/vllm-project/vllm/issues/23739) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;fp8;operator;quantization;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: The full cudagraph seems not work.

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression command: ```shell env VLLM_FLASH_ATTN_VERSION=3 VLLM_ATTENTION_BACKEND=FLASH_ATTN CUDA_VISIBLE_DEVICES=5 vllm serve Qwen/Qwen3-Reranker-0.6B --task=score --port 12346 --data-parallel-size=1 --gpu-memory-utilization=0.6 --max-num-seqs=45 --quantization='fp8' --compilation-config '{"full_cuda_graph": true}' ``` ### Misc discussion on performance ### Your current environment (if you think it is necessary) ```shell ============================== System Info ============================== OS : CentOS Linux Server 7.2 (Paladin) (x86_64) GCC version : (GCC) 10.2.1 20200825 (Alibaba 10.2.1-3 2.17) Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.32 ============================== PyTorch Info ============================== PyTorch version : 2.7.1+cu126 Is debug build : False CUDA used to build PyTorch : 12.6 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.10.18 (main, Jun 5 2025, 13:14:17) [GCC 11.2.0] (64-bit runtime) Python platform : Linux-5.10.134-18.al8.x86_64-x86_64-with-gl...

## 现有链接修复摘要

#23942 [CI] Add `aiter` to matching list of issue auto labeller for `rocm` tag

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: Report of performance regression command: ```shell env VLLM_FLASH_ATTN_VERSION=3 VLLM_ATTENTION_BACKEND=FLASH_ATTN CUDA_VISIBLE_DEVICES=5 vllm serve Qwen/Qwen3-Reranker-0.6B --task=score --port 12346 --data-parallel-siz...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Performance]: The full cudagraph seems not work. performance;stale ### Proposal to improve performance _No response_ ### Report of performance regression command: ```shell env VLLM_FLASH_ATTN_VERSION=3 VLLM_ATTENTION_B...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: --data-parallel-size=1 --gpu-memory-utilization=0.6 --max-num-seqs=45 --quantization='fp8' --compilation-config '{"full_cuda_graph": true}' ``` ### Misc discussion on performance ### Your current environment (if you thi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: =3 VLLM_ATTENTION_BACKEND=FLASH_ATTN CUDA_VISIBLE_DEVICES=5 vllm serve Qwen/Qwen3-Reranker-0.6B --task=score --port 12346 --data-parallel-size=1 --gpu-memory-utilization=0.6 --max-num-seqs=45 --quantization='fp8' --comp...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: gression command: ```shell env VLLM_FLASH_ATTN_VERSION=3 VLLM_ATTENTION_BACKEND=FLASH_ATTN CUDA_VISIBLE_DEVICES=5 vllm serve Qwen/Qwen3-Reranker-0.6B --task=score --port 12346 --data-parallel-size=1 --gpu-memory-utiliza...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#23942](https://github.com/vllm-project/vllm/pull/23942) | mentioned | 0.6 | [CI]  Add `aiter` to matching list of issue auto labeller for `rocm` tag | el: NO (0 matches) #23744: Should have ROCm label: NO (0 matches) #23739: Should have ROCm label: NO (0 matches) #23730: Should have ROCm label: NO (0 matches) #23724: Should hav |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
