# vllm-project/vllm#7152: [Bug]: Unexpected Responses from Gemma-2-9b-it

| 字段 | 值 |
| --- | --- |
| Issue | [#7152](https://github.com/vllm-project/vllm/issues/7152) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Unexpected Responses from Gemma-2-9b-it

### Issue 正文摘录

### Your current environment ```text transformers==4.43.2 flashinfer == 0.1.2+cu121torch2.4 pytorch == 2.4.0 vllm == -e git+https://github.com/vllm-project/vllm.git@cc08fc7225616aeb6709a2e75e5ac47ace124985#egg=vllm vllm == 2.6.1 ``` Hardware; H100 x 1 ``` nvcc: NVIDIA (R) Cuda compiler driver Copyright (c) 2005-2023 NVIDIA Corporation Built on Mon_Apr__3_17:16:06_PDT_2023 Cuda compilation tools, release 12.1, V12.1.105 Build cuda_12.1.r12.1/compiler.32688072_0 ``` ### 🐛 Describe the bug I’m trying to use the current main branch of vllm for inference with gemma-2-9b-it, but the output I’m getting is not as expected (i.e., there is a significant discrepancy compared to the results obtained using Hugging Face, where inference results are more reasonable). Below is the bash script I used to launch the vllm OpenAI inference server. ``` VLLM_ATTENTION_BACKEND=FLASHINFER python3 -m vllm.entrypoints.openai.api_server \ --host 0.0.0.0 --port 8124 --dtype "auto" --model gemma-2-9b-it -tp 1 --gpu-memory-utilization 0.85 --max-model-len 4096 --disable-sliding-window ``` Here is the Python code I used with the OpenAI package: ``` import openai client = openai.OpenAI( base_url="http://0.0.0.0:8...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: egg=vllm vllm == 2.6.1 ``` Hardware; H100 x 1 ``` nvcc: NVIDIA (R) Cuda compiler driver Copyright (c) 2005-2023 NVIDIA Corporation Built on Mon_Apr__3_17:16:06_PDT_2023 Cuda compilation tools, release 12.1, V12.1.105 Bu...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: a-2-9b-it bug ### Your current environment ```text transformers==4.43.2 flashinfer == 0.1.2+cu121torch2.4 pytorch == 2.4.0 vllm == -e git+https://github.com/vllm-project/vllm.git@cc08fc7225616aeb6709a2e75e5ac47ace124985...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: -m vllm.entrypoints.openai.api_server \ --host 0.0.0.0 --port 8124 --dtype "auto" --model gemma-2-9b-it -tp 1 --gpu-memory-utilization 0.85 --max-model-len 4096 --disable-sliding-window ``` Here is the Python code I use...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 7225616aeb6709a2e75e5ac47ace124985#egg=vllm vllm == 2.6.1 ``` Hardware; H100 x 1 ``` nvcc: NVIDIA (R) Cuda compiler driver Copyright (c) 2005-2023 NVIDIA Corporation Built on Mon_Apr__3_17:16:06_PDT_2023 Cuda compilatio...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Unexpected Responses from Gemma-2-9b-it bug ### Your current environment ```text transformers==4.43.2 flashinfer == 0.1.2+cu121torch2.4 pytorch == 2.4.0 vllm == -e git+https://github.com/vllm-project/vllm.git@cc0...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
