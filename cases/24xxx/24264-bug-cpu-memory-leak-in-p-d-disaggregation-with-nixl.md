# vllm-project/vllm#24264: [Bug]: CPU Memory leak in P/D disaggregation (with NIXL?)

| 字段 | 值 |
| --- | --- |
| Issue | [#24264](https://github.com/vllm-project/vllm/issues/24264) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 16; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: CPU Memory leak in P/D disaggregation (with NIXL?)

### Issue 正文摘录

### Your current environment This bug have been reproduced on top of your official docker image [v0.10.1.1](https://hub.docker.com/layers/vllm/vllm-openai/v0.10.1.1/images/sha256-d731ee65c044ae0977421eed3d93f931d4b7d79614394184c939db35b8f28fc2) on two different node with H200s. One for Prefill and one for Decode. ### 🐛 Describe the bug We noticed a big memory leak on the vLLM Decode instances with some models using fp8. So we investigated: * it doesn't leak on all models, but it definetely leak on similar model than `mistral-large-2411` or `mistral-large-2407` that uses static FP8 * this is most likely time-sensitive (ie. `--enforce-eager` or using a `mistral-large-2411` model with dynamic fp8 quantization doesn't seems to trigger the leak... it doesn't mean it's not there...) * it doesn't seem to leak on small request (maybe related to the fact it's time-sensitive?) * We think that the memory leak happen in C++ part of the code since classical Python's memory profiler like memray, guppy and other didn't helped us I managed to reproduce this bug on top of this model: https://huggingface.co/RedHatAI/Mistral-Large-Instruct-2407-FP8 But **it's not the only one** that is impacted by t...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: current environment This bug have been reproduced on top of your official docker image [v0.10.1.1](https://hub.docker.com/layers/vllm/vllm-openai/v0.10.1.1/images/sha256-d731ee65c044ae0977421eed3d93f931d4b7d79614394184c...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: 7d79614394184c939db35b8f28fc2) on two different node with H200s. One for Prefill and one for Decode. ### 🐛 Describe the bug We noticed a big memory leak on the vLLM Decode instances with some models using fp8. So we inv...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ed a big memory leak on the vLLM Decode instances with some models using fp8. So we investigated: * it doesn't leak on all models, but it definetely leak on similar model than `mistral-large-2411` or `mistral-large-2407...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: leak... it doesn't mean it's not there...) * it doesn't seem to leak on small request (maybe related to the fact it's time-sensitive?) * We think that the memory leak happen in C++ part of the code since classical Pytho...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: bug We noticed a big memory leak on the vLLM Decode instances with some models using fp8. So we investigated: * it doesn't leak on all models, but it definetely leak on similar model than `mistral-large-2411` or `mistra...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
