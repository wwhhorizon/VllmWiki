# vllm-project/vllm#7614: [Bug]: CUDA error: an illegal memory access was encountered when running autofp8

| 字段 | 值 |
| --- | --- |
| Issue | [#7614](https://github.com/vllm-project/vllm/issues/7614) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: CUDA error: an illegal memory access was encountered when running autofp8

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The error happens when running [llama3.1-405b-instruct](https://huggingface.co/meta-llama/Meta-Llama-3.1-405B-Instruct) 1. Quantize the model using https://github.com/neuralmagic/AutoFP8; 2. Serving the model using vllm; Full error is here: https://gist.github.com/sfc-gh-zhwang/0fe366245fed0a450df2ae5b652c8a77

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: st.github.com/sfc-gh-zhwang/0fe366245fed0a450df2ae5b652c8a77 correctness ci_build;distributed_parallel;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding cuda;operator;quantization;sampling...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: environment ### 🐛 Describe the bug The error happens when running [llama3.1-405b-instruct](https://huggingface.co/meta-llama/Meta-Llama-3.1-405B-Instruct) 1. Quantize the model using https://github.com/neuralmagic/AutoF...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ]: CUDA error: an illegal memory access was encountered when running autofp8 bug ### Your current environment ### 🐛 Describe the bug The error happens when running [llama3.1-405b-instruct](https://huggingface.co/meta-ll...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: sampling_logits;speculative_decoding cuda;operator;quantization;sampling;triton build_error;nan_inf env_dependency Your current environment
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [Bug]: CUDA error: an illegal memory access was encountered when running autofp8 bug ### Your current environment ### 🐛 Describe the bug The error happens when running [llama3.1-405b-instruct](https://huggingface.co/met...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
