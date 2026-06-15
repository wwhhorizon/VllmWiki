# vllm-project/vllm#28650: [Bug][XPU]: Error spam "Unsupported gpu_arch of paged_attention_vllm!!"

| 字段 | 值 |
| --- | --- |
| Issue | [#28650](https://github.com/vllm-project/vllm/issues/28650) |
| 状态 | closed |
| 标签 | bug;intel-gpu;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug][XPU]: Error spam "Unsupported gpu_arch of paged_attention_vllm!!"

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Upon trying to serve model with the following command: `vllm serve Qwen/Qwen3-4B --dtype half --max-model-len 12K --gpu-memory-utilization 0.8 --enforce-eager --enable-auto-tool-choice --tool-call-parser hermes --reasoning-parser deepseek_r1`, I get a ton of error spam after trying to generate any response with a model: I tried with `Intel/Qwen3-8B-int4-AutoRound` model as well, no difference, also tried with `docker.io/intel/vllm:0.10.2-xpu` container as provided by Intel, same issue. GPU is Intel Arc A770 LE. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: /Qwen3-8B-int4-AutoRound` model as well, no difference, also tried with `docker.io/intel/vllm:0.10.2-xpu` container as provided by Intel, same issue. GPU is Intel Arc A770 LE. ### Before submitting a new issue... - [x]...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: g to serve model with the following command: `vllm serve Qwen/Qwen3-4B --dtype half --max-model-len 12K --gpu-memory-utilization 0.8 --enforce-eager --enable-auto-tool-choice --tool-call-parser hermes --reasoning-parser...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug][XPU]: Error spam "Unsupported gpu_arch of paged_attention_vllm!!" bug;intel-gpu;stale ### Your current environment ### 🐛 Describe the bug Upon trying to serve model with the following command: `vllm serve Qwen/Qwe...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: our current environment ### 🐛 Describe the bug Upon trying to serve model with the following command: `vllm serve Qwen/Qwen3-4B --dtype half --max-model-len 12K --gpu-memory-utilization 0.8 --enforce-eager --enable-auto...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: rror spam "Unsupported gpu_arch of paged_attention_vllm!!" bug;intel-gpu;stale ### Your current environment ### 🐛 Describe the bug Upon trying to serve model with the following command: `vllm serve Qwen/Qwen3-4B --dtype...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
