# vllm-project/vllm#19048: [Bug]: System Memory OOM after upgrading to v0.9.0.1

| 字段 | 值 |
| --- | --- |
| Issue | [#19048](https://github.com/vllm-project/vllm/issues/19048) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: System Memory OOM after upgrading to v0.9.0.1

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I use command `vllm serve ~/work/ai/models/Qwen2.5-Coder-32B-Instruct-Q6_K_L.gguf --max-model-len 20480 --swap-space 2 --tensor-parallel-size 2 --gpu-memory-utilization 0.9 --port 2200 --api-key "Lyoko5438!" --enable-sleep-mode --calculate-kv-scales --served-model-name "Qwen2.5-Coder" --dtype=half --fully-sharded-loras` to serve model to my frontend. As having only 16GB of **System Memory**, I use `swap_space=2` to prevent OOM during loading model file stage. This works fine until v0.8.5.post1. But after upgrading to v0.9.0.1 the **same** command I run to serve model result in a complete OOM during the early stage of loading model. It seems the `--swap_space` parameter not having any effect as I tried to change it from 2 to 1 and the problem still exists. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: .9 --port 2200 --api-key "Lyoko5438!" --enable-sleep-mode --calculate-kv-scales --served-model-name "Qwen2.5-Coder" --dtype=half --fully-sharded-loras` to serve model to my frontend. As having only 16GB of **System Memo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ts. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ironment ### 🐛 Describe the bug I use command `vllm serve ~/work/ai/models/Qwen2.5-Coder-32B-Instruct-Q6_K_L.gguf --max-model-len 20480 --swap-space 2 --tensor-parallel-size 2 --gpu-memory-utilization 0.9 --port 2200 --...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: System Memory OOM after upgrading to v0.9.0.1 bug;stale ### Your current environment ### 🐛 Describe the bug I use command `vllm serve ~/work/ai/models/Qwen2.5-Coder-32B-Instruct-Q6_K_L.gguf --max-model-len 20480...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
