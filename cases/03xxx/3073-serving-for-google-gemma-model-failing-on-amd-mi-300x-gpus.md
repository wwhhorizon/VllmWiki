# vllm-project/vllm#3073: Serving for Google Gemma model failing on AMD MI 300X GPUs

| 字段 | 值 |
| --- | --- |
| Issue | [#3073](https://github.com/vllm-project/vllm/issues/3073) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;hardware_porting;model_support |
| 子分类 | install |
| Operator 关键词 | attention;operator |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Serving for Google Gemma model failing on AMD MI 300X GPUs

### Issue 正文摘录

The vLLM serving for the Google Gemma models is failing on AMD MI 300X GPUs with the latest version of the vLLM (0.3.2) and ROCm 6.0.2 version. Reproducing steps: 1. Clone the vllm repo and switch to [tag v0.3.2](https://github.com/vllm-project/vllm/tree/v0.3.2) 2. Build the Dockerfile.rocm dockerfile with instructions from [Option 3: Build from source with docker -Installation with ROCm](https://docs.vllm.ai/en/latest/getting_started/amd-installation.html#build-from-source-docker-rocm) build command: ```sh docker build -f Dockerfile.rocm -t vllm-rocm:latest . ``` 3. The vLLM serving command used: ```sh python3 -m vllm.entrypoints.openai.api_server --model google/gemma-7b --dtype bfloat16 ``` The error below: ```sh File "/opt/conda/envs/py_3.9/lib/python3.9/site-packages/vllm-0.3.2+rocm603-py3.9-linux-x86_64.egg/vllm/model_executor/models/gemma.py", line 160, in forward attn_output = self.attn(q, k, v, k_cache, v_cache, input_metadata) File "/opt/conda/envs/py_3.9/lib/python3.9/site-packages/torch/nn/modules/module.py", line 1518, in _wrapped_call_impl return self._call_impl(*args, **kwargs) File "/opt/conda/envs/py_3.9/lib/python3.9/site-packages/torch/nn/modules/module.py", line...

## 现有链接修复摘要

#3972 [Model][AMD] ROCm support for 256 head dims for Gemma

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: the Google Gemma models is failing on AMD MI 300X GPUs with the latest version of the vLLM (0.3.2) and ROCm 6.0.2 version. Reproducing steps: 1. Clone the vllm repo and switch to [tag v0.3.2](https://github.com/vllm-pro...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: python3 -m vllm.entrypoints.openai.api_server --model google/gemma-7b --dtype bfloat16 ``` The error below: ```sh File "/opt/conda/envs/py_3.9/lib/python3.9/site-packages/vllm-0.3.2+rocm603-py3.9-linux-x86_64.egg/vllm/m...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: in forward attn_output = self.attn(q, k, v, k_cache, v_cache, input_metadata) File "/opt/conda/envs/py_3.9/lib/python3.9/site-packages/torch/nn/modules/module.py", line 1518, in _wrapped_call_impl return self._call_impl...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Serving for Google Gemma model failing on AMD MI 300X GPUs The vLLM serving for the Google Gemma models is failing on AMD MI 300X GPUs with the latest version of the vLLM (0.3.2) and ROCm 6.0.2 version. Reproducing step...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: packages/xformers/ops/fmha/flash.py", line 130, in _flash_fwd ) = _C_flashattention.varlen_fwd( RuntimeError: FlashAttention forward only supports head dimension at most 128 ``` **Issues:** 1. This issue is for serving...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#3972](https://github.com/vllm-project/vllm/pull/3972) | closes_keyword | 0.95 | [Model][AMD] ROCm support for 256 head dims for Gemma | FIX #3073 (*link existing issues this PR will resolve*) **BEFORE SUBMITTING, PLEASE READ THE CHECKLIST BELOW AND FILL IN THE DESCRIPTION ABOVE** --- <details> <!-- inside |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
