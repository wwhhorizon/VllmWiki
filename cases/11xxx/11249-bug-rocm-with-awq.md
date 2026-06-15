# vllm-project/vllm#11249: [Bug]: ROCM with AWQ

| 字段 | 值 |
| --- | --- |
| Issue | [#11249](https://github.com/vllm-project/vllm/issues/11249) |
| 状态 | closed |
| 标签 | bug;rocm |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;gemm;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: ROCM with AWQ

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Using the latest vllm from git, I've created a vllm-rocm image based off the Dockerfile.rocm. I proceeded to try to run an AWQ model like so: ``` vllm serve --model casperhansen/llama-3.3-70b-instruct-awq --served-model-name Llama-3.3-70B-Instruct --enforce-eager --quantization awq --max_model_len 8192 --gpu-memory-utilization 0.95 --tensor-parallel-size 2 ``` but getting this error: Tried searching but couldn't find anything related to this. I tried installing autoawq inside the container with: ``` pip install autoawq ``` but this didn't get me anywhere. I read the docs and https://rocm.docs.amd.com/en/latest/how-to/tuning-guides/mi300x/workload.html#awq-quantization seems to suggest AWQ should work out of the box but I havent had any success. I do have this working on the CUDA version using `docker.io/vllm/vllm-openai:latest` but trying to get a rocm version going. Any ideas what im doing wrong?

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: g the latest vllm from git, I've created a vllm-rocm image based off the Dockerfile.rocm. I proceeded to try to run an AWQ model like so: ``` vllm serve --model casperhansen/llama-3.3-70b-instruct-awq --served-model-nam...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: ROCM with AWQ bug;rocm ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Using the latest vllm from git, I've created a vllm-rocm image based off the Dockerfile.rocm. I proce
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: ROCM with AWQ bug;rocm ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Using the latest vllm from git, I've created a vllm-rocm image based off the Dockerfile.rocm. I proce...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ing_logits;speculative_decoding cuda;gemm;operator;quantization;sampling;triton build_error;crash;nan_inf env_dependency Your current environment
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: nstruct-awq --served-model-name Llama-3.3-70B-Instruct --enforce-eager --quantization awq --max_model_len 8192 --gpu-memory-utilization 0.95 --tensor-parallel-size 2 ``` but getting this error: Tried searching but could...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
