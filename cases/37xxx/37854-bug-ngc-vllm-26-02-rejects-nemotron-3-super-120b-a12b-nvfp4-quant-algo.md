# vllm-project/vllm#37854: [Bug]: NGC vLLM 26.02 rejects Nemotron-3-Super-120B-A12B-NVFP4 — quant_algo MIXED_PRECISION not in whitelist

| 字段 | 值 |
| --- | --- |
| Issue | [#37854](https://github.com/vllm-project/vllm/issues/37854) |
| 状态 | open |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;moe;quantization |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;fp8;kernel;moe;quantization |
| 症状 | build_error;crash;import_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: NGC vLLM 26.02 rejects Nemotron-3-Super-120B-A12B-NVFP4 — quant_algo MIXED_PRECISION not in whitelist

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug `nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-NVFP4` cannot be served on a DGX Spark using the current NGC vLLM container. The model's `config.json` (produced by modelopt 0.43.0) sets `quant_algo: "MIXED_PRECISION"`, which vLLM 0.15.1 rejects against a hardcoded whitelist. The FP8 variant does not fit in 128 GB unified memory (~120 GB weights alone), so the NVFP4 variant is the only viable path for single-Spark deployment. **Reproduction:** ```bash docker run --gpus all --rm --ipc=host \ -v /path/to/hf-cache:/root/.cache/huggingface \ nvcr.io/nvidia/vllm:26.02-py3 \ vllm serve nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-NVFP4 \ --dtype auto --kv-cache-dtype fp8 --tensor-parallel-size 1 \ --attention-backend TRITON_ATTN --gpu-memory-utilization 0.85 \ --enforce-eager --trust-remote-code ``` **Error:** ``` pydantic_core._pydantic_core.ValidationError: 1 validation error for VllmConfig Value error, ModelOpt currently only supports: ['FP8', 'FP8_PER_CHANNEL_PER_TOKEN', 'FP8_PB_WO', 'NVFP4'] quantizations in vLLM. Please check the `hf_quant_config.json` file for your model's quant configuration. ``` **Root cause:** The model's `quantization_...

## 现有链接修复摘要

#35047 add mixed precision support for modelopt | #36312 [Bugfix] Fixed modelopt mixed precision quant format loading

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: LLM 26.02 rejects Nemotron-3-Super-120B-A12B-NVFP4 — quant_algo MIXED_PRECISION not in whitelist ### Your current environment ### 🐛 Describe the bug `nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-NVFP4` cannot be served on a...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: [Bug]: NGC vLLM 26.02 rejects Nemotron-3-Super-120B-A12B-NVFP4 — quant_algo MIXED_PRECISION not in whitelist ### Your current environment ### 🐛 Describe the bug `nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-NVFP4` cannot be...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: side the NGC container, this replaces the pinned torch (2.11.0a0+nv26.2, CUDA 13.1) with PyPI torch 2.9.1 (CUDA 12.x), crashing with `ImportError: libcudart.so.12: cannot open shared object file`. Installing with `--no-...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: annot be served on a DGX Spark using the current NGC vLLM container. The model's `config.json` (produced by modelopt 0.43.0) sets `quant_algo: "MIXED_PRECISION"`, which vLLM 0.15.1 rejects against a hardcoded whitelist....
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ype auto --kv-cache-dtype fp8 --tensor-parallel-size 1 \ --attention-backend TRITON_ATTN --gpu-memory-utilization 0.85 \ --enforce-eager --trust-remote-code ``` **Error:** ``` pydantic_core._pydantic_core.ValidationErro...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#35047](https://github.com/vllm-project/vllm/pull/35047) | mentioned | 0.45 | add mixed precision support for modelopt | mixed precision quant format loading" (open). reports that even after #35047, `mixed_precision` still fails to parse. - #35528 — w4a8_mxfp4_fp8 also rejected by the same whitelist… |
| [#36312](https://github.com/vllm-project/vllm/pull/36312) | mentioned | 0.45 | [Bugfix] Fixed modelopt mixed precision quant format loading | 9 fp8 layers load correctly under this override. **asks:** 1. merge #36312 (or an equivalent fix) so that `mixed_precision` is recognized. 2. ship an ngc vllm container that inclu… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
