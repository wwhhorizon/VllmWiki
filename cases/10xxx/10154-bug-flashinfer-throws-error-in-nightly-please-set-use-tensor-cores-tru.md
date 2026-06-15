# vllm-project/vllm#10154: [Bug]: FlashInfer throws error in nightly: Please set `use_tensor_cores=True` in BatchDecodeWithPagedKVCacheWrapper for group size 3

| 字段 | 值 |
| --- | --- |
| Issue | [#10154](https://github.com/vllm-project/vllm/issues/10154) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;fp8;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: FlashInfer throws error in nightly: Please set `use_tensor_cores=True` in BatchDecodeWithPagedKVCacheWrapper for group size 3

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Error occurs in the standard `vllm/vllm-openai:latest` after manually installing the nightly version: ```vllm @ https://vllm-wheels.s3.us-west-2.amazonaws.com/nightly/vllm-1.0.0.dev-cp38-abi3-manylinux1_x86_64.whl#sha256=712e485f5ba707154b0826d79b22363f520ddb56b3ecddf5895a54611a0a53b3``` This specifically occurs with FLASHINFER enabled `export VLLM_ATTENTION_BACKEND=FLASHINFER` Reproduction: ```py from vllm import LLM model = LLM(model="neuralmagic/Llama-3.2-3B-Instruct-FP8-dynamic", max_model_len=256, tensor_parallel_size=1) ``` Error message:

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: g Error occurs in the standard `vllm/vllm-openai:latest` after manually installing the nightly version: ```vllm @ https://vllm-wheels.s3.us-west-2.amazonaws.com/nightly/vllm-1.0.0.dev-cp38-abi3-manylinux1_x86_64.whl#sha...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Bug]: FlashInfer throws error in nightly: Please set `use_tensor_cores=True` in BatchDecodeWithPagedKVCacheWrapper for group size 3 bug ### Your current environment ### 🐛 Describe the bug Error occurs in the standard `...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: om vllm import LLM model = LLM(model="neuralmagic/Llama-3.2-3B-Instruct-FP8-dynamic", max_model_len=256, tensor_parallel_size=1) ``` Error message: correctness attention_kv_cache;ci_build;distributed_parallel;frontend_a...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ATTENTION_BACKEND=FLASHINFER` Reproduction: ```py from vllm import LLM model = LLM(model="neuralmagic/Llama-3.2-3B-Instruct-FP8-dynamic", max_model_len=256, tensor_parallel_size=1) ``` Error message: correctness attenti...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: pi;hardware_porting;model_support;quantization;sampling_logits attention;cuda;fp8;operator;quantization;sampling;triton build_error;crash;nan_inf;oom dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
