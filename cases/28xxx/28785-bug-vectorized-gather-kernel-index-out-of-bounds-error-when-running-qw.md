# vllm-project/vllm#28785: [Bug]: "vectorized gather kernel index out of bounds" error when running qwen3-vl-moe + nvfp4

| 字段 | 值 |
| --- | --- |
| Issue | [#28785](https://github.com/vllm-project/vllm/issues/28785) |
| 状态 | closed |
| 标签 | bug;nvidia |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: "vectorized gather kernel index out of bounds" error when running qwen3-vl-moe + nvfp4

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Hi! I'm trying to run the nvfp4 quantized model `Qwen3-VL-235B-A22B-Instruct-NVFP4` on a single B200 GPU, but encountered the following error: ``` /pytorch/aten/src/ATen/native/cuda/IndexKernelUtils.cu:16: vectorized_gather_kernel: block: [569,1,0], thread: [192,0,0] Assertion `ind >=0 && ind < ind_dim_size && "vectorized gather kernel index out of bounds"` failed. ``` Server launching command: ``` vllm serve RedHatAI/Qwen3-VL-235B-A22B-Instruct-NVFP4 --host 0.0.0.0 --port 54323 --async-scheduling --max-model-len 32768 --max-num-seqs 1024 ``` Benchmark command: ``` vllm bench serve --backend openai-chat --base-url http://0.0.0.0:54323 --endpoint /v1/chat/completions --model RedHatAI/Qwen3-VL-235B-A22B-Instruct-NVFP4 --dataset-name random --random-input-len 300 --random-output-len 200 ``` The backtrace (with CUDA_LAUNCH_BLOCKING=1) is like: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory cuda;kerne...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: zed gather kernel index out of bounds" error when running qwen3-vl-moe + nvfp4 bug;nvidia ### Your current environment ### 🐛 Describe the bug Hi! I'm trying to run the nvfp4 quantized model `Qwen3-VL-235B-A22B-Instruct-...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: he nvfp4 quantized model `Qwen3-VL-235B-A22B-Instruct-NVFP4` on a single B200 GPU, but encountered the following error: ``` /pytorch/aten/src/ATen/native/cuda/IndexKernelUtils.cu:16: vectorized_gather_kernel: block: [56...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: 32768 --max-num-seqs 1024 ``` Benchmark command: ``` vllm bench serve --backend openai-chat --base-url http://0.0.0.0:54323 --endpoint /v1/chat/completions --model RedHatAI/Qwen3-VL-235B-A22B-Instruct-NVFP4 --dataset-na...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: n/src/ATen/native/cuda/IndexKernelUtils.cu:16: vectorized_gather_kernel: block: [569,1,0], thread: [192,0,0] Assertion `ind >=0 && ind < ind_dim_size && "vectorized gather kernel index out of bounds"` failed. ``` Server...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
